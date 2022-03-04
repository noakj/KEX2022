import sys
import json

def format_artifact(module):
    
    path, version = module.split('@')
    path_split = path.split('/')
    name = path_split.pop()
    # provider = path_split.pop() if len(path_split) else name

    return {
            'name': name,
            'version': version,
            'gav': module
            }


if __name__ == "__main__":

    modules = sys.stdin
    artifacts = {}
    root = format_artifact(modules.readline())
    
    for mod in modules.read().splitlines():

        artifact = format_artifact(mod)
        gav = artifact['gav']
        artifacts[gav] = artifact

    print(artifacts)
    with open(root['name'] + '_artifacts.json', 'w') as file:
        json.dump(artifacts, file)
