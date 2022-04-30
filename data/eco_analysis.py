import sys
import json
from collections import Counter

def get_project_tree(project_name):

    path = project_name + '/' + project_name
    artifacts = {}
    dependencies = {}
    
    with open(path + '_artifacts.json', 'r') as art_file:
        artifacts = json.load(art_file)

    with open(path + '_dependencies.json', 'r') as deps_file:
        dependencies = json.load(deps_file)

    return {
            'artifacts': artifacts,
            'dependencies': dependencies
            }
    
def get_project_artifacts(project_name):

    path = project_name + '/' + project_name

    with open(path + '_artifacts.json', 'r') as art_file:
        artifacts = json.load(art_file)
    
    libraries = []

    for artifact in artifacts.values():
        artifactId = artifact.get('artifactId')
        groupId = artifact.get('groupId', '')
        print(artifactId)
        print(groupId)

        libraries.append(groupId + '@' + artifactId)
    
    return libraries
    
    
if __name__ == "__main__":

    project_paths = sys.argv[1:]
    projects = {}
    
    for project_name in project_paths:
        projects[project_name] = get_project_tree(project_name)
    
    artifact_sets = []
    for project_name in project_paths:
        project_artifacts = get_project_artifacts(project_name)
        artifact_sets.append(set(project_artifacts))

    #get ecosystem intersection
    intersection = set.intersection(*artifact_sets)

    #get monoculture suppliers
    intersection_suppliers = []
    
    dummy_project = projects[list(projects.keys())[0]] #use any project as all contain intersection
    dummy_artifacts = dummy_project.get('artifacts')
    
    for library in intersection:
        supplier, _ = library.split('@')
        intersection_suppliers.append(supplier)

    supplier_counter = Counter(intersection_suppliers)

    with open(''.join(project_paths) + '.txt', 'w') as outfile:
        outfile.write('Intersection count: ' + str(len(intersection_suppliers)) + '\n')
        outfile.write(str(supplier_counter))
