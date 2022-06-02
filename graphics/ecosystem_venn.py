import matplotlib.pyplot as plt
from matplotlib_venn import venn2 as venn
import sys
import json

def get_project_artifacts(project_name):

    path = project_name + '/' + project_name

    with open(path + '_artifacts.json', 'r') as art_file:
        artifacts = json.load(art_file)

    libraries = []

    for artifact in artifacts.values():
        artifactId = artifact.get('artifactId')
        groupId = artifact.get('groupId', '')

        libraries.append(groupId + '@' + artifactId)

    return libraries

if __name__ == "__main__":

    projects = sys.argv[1:]
    
    artifact_sets = []

    for p in projects:
        artifacts_list = get_project_artifacts(p)
        artifact_sets.append(set(artifacts_list))
    
    venn(artifact_sets, set(projects))
    plt.show()
