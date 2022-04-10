import sys
import json
import re

def format_artifact(data):
    
    split_data = data.split(':')
    group = split_data.pop(0)
    artifact = split_data.pop(0)
    version = split_data.pop()

    return {
            'group': group,
            'artifact': artifact,
            'version': version,
            'gav': group + artifact + '@' + str(version),
            }

if __name__ == "__main__":

    tree = sys.stdin

    artifacts = {}
    dependencies = {}
    versions = {}

    re_depth = re.compile('[^\w.]')

    parents = []

    for line in tree.read().splitlines():

        data = [data for data in line.split(' ') if data]
        depth = len([x for x in data if re_depth.match(x)])
        print(data)
        artifact_data = data[depth]

        artifact = format_artifact(artifact_data)
        gav = artifact['gav']
        artifacts[gav] = artifact
       
        parent = parents[depth-1]
        parents.insert(depth, gav)

        temp = dependencies.get(parent, [])
        temp.append(gav)
        dependencies[parent] = temp

    with open('_artifacts.json', 'w') as file:
        json.dump(artifacts, file)

    with open('_dependencies.json', 'w') as file:
        json.dump(dependencies, file)
