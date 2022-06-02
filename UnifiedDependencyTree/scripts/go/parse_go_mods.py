import sys
import json

def format_artifact(module):
    
    path, version = module.split('@')
    path_split = path.split('/')
    name = path_split.pop()
    version = version[:6]
    # provider = path_split.pop() if len(path_split) else name
    if len(path_split):
        group = path_split.pop()
    else:
        group = name

    return {
            'artifactId': name,
            'groupdId': group,
            'version': version,
            'gav': module
            }


if __name__ == "__main__":

    modules = sys.stdin
    artifacts = {}
    project = format_artifact(modules.readline().rstrip('\n'))

    artifacts[project.get('gav')] = project
    
    for mod in modules.read().splitlines():

        artifact = format_artifact(mod)
        gav = artifact['gav']
        artifacts[gav] = artifact

    with open(project['artifactId'] + '_artifacts.json', 'w') as file:
        json.dump(artifacts, file)
