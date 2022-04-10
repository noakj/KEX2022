import sys
import json
import re

def check_scope(line):
    scopes = ['build', 'dev']
    return line in scopes

def format_artifact(data):

    version = data.pop()
    name = data.pop()
    path = data.pop() if data else name
    group = path.split('/')[-1] 

    return {
            'name': name,
            'version': version,
            'group': group,
            'gav': group + name + '@' + version
            }

    
if __name__ == "__main__":

    tree = sys.stdin

    artifacts = {}
    dependencies = {}
    versions = {}
    project = tree.readline()
    
    re_depth = re.compile('[^\w.]')

    parents = [project]

    for line in tree.read().splitlines():

        data = [data for data in line.split(' ') if data]
        depth = len([x for x in data if re_depth.match(x)])
        artifact_data = data[depth:]

        if check_scope(artifact_data[0]):
            scopes.insert(depth, artifact_data[0])
            scopes = scopes[:depth]
        else:

            artifact = format_artifact(artifact_data)
            gav = artifact['gav']
            artifacts[gav] = artifact

            parent = parents[depth-1]
            parents.insert(depth, gav)

            temp = dependencies.get(parent, [])
            temp.append(gav)
            dependencies[parent] = temp

    project = project.replace(' ', '')
    with open(project + '_artifacts.json', 'w') as file:
        json.dump(artifacts, file)

    with open(project + '_dependencies.json', 'w') as file:
        json.dump(dependencies, file)
