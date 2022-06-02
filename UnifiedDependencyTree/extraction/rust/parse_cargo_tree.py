import sys
import json
import re




def format_artifact(data):

    version = data.pop()
    name = data.pop()
    path = data.pop() if data else name
    path_split = path.split('/')
    group = path_split[-2] if len(path_split) > 1 else path_split[-1]

    return {
            'artifactId': name,
            'groupId': group,
            'version': version,
            'gav': group + name + '@' + version
            }


def check_scope(line):
    scopes = ['build', 'dev']
    return line in scopes

    
if __name__ == "__main__":

    tree = sys.stdin

    artifacts = {}
    dependencies = {}
    project = tree.readline()
    
    re_depth = re.compile('[^\w.]')

    parents = [project]

    for line in tree.read().splitlines():

        data = [data for data in line.split(' ') if data]
        depth = len([x for x in data if re_depth.match(x)]) #get number of indentations
        artifact_data = data[depth:]

        if not check_scope(artifact_data[0]):
            #scope not saved due to unability to properly assign scopes from deeply nested transitive dependencies

            artifact = format_artifact(artifact_data)
            gav = artifact['gav']
            artifacts[gav] = artifact

            parent = parents[depth-1] #get last added artifact which is one level higher
            parents.insert(depth, gav) #add current artifact as latest parent at depth


            #update or initialize dependencies dictionary for parent of current
            temp = dependencies.get(parent, [])
            temp.append(gav)
            dependencies[parent] = temp

    project = project.replace(' ', '')

    udt = {
            'project': project,
            'artifacts': artifacts,
            'dependencies': dependencies,
            'language': 'rust'
            }

    with open(project + '_udt.json') as outfile:
        json.dump(udt, outfile)
