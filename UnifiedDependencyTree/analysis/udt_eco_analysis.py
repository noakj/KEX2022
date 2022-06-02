import sys
import json
from collections import Counter

def get_udt(project_name):
    
    with open(path + '_udt.json', 'r') as udt_file:
        udt = json.load(udt_file)

    return udt

if __name__ == "__main__":

    project_paths = sys.argv[1:]
    projects = {}
    
    for project_name in project_paths:
        projects[project_name] = get_udt(project_name)
    
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
