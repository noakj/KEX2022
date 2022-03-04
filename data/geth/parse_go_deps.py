import sys
import json

if __name__ == "__main__":

    graph = sys.stdin
    dependencies = {}       # source_gav: [target_gav, ...]
    versions = {}           # artifactId: [gav, ...]

    root, target =  graph.readline().split(' ')
    root_name = root.split('/')[-1]

    with open(root_name + '_artifacts.json', 'r') as art_file:
        artifacts = json.load(art_file)
        for dep in graph.read().splitlines():

            source, target = dep.split(' ') 
            if source in artifacts:
                if target in artifacts:
                    temp = dependencies.get(source, [])
                    temp.append(target)
                    dependencies[source] = temp

    with open(root_name + '_dependencies.json', 'w') as deps_file:
        json.dump(dependencies, deps_file)

    with open(root_name + '_versions.json', 'w') as vers_file:
        json.dumps(versions, vers_file)
