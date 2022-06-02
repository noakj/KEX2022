import sys
import json

def format_go_artifacts(module):

    path, version = module.split('@')
    path_split = path.split('/')
    name = path_split.pop()
    if len(path_split):
        group = path_split.pop()
    else:
        group = name

    return {
            'artifactId': name,
            'groupId': group,
            'version': version,
            'gav': module
            }

def get_artifacts(modules):

    artifacts = {}
    
    for mod in modules:
        artifact = format_go_artifact(mod)
        gav = artifact.get('gav')
        artifacts[gav] = artifact

    return artifacts

def get_dependencies(dep_pairs, artifacts):

    dependencies = {}

    for dep in dep_pairs:
        source_gav, target_gav = dep.split(' ')
        if source_gav in artifacts:
            if target_gav in artifacts:
                temp = dependencies.get(source, [])
                temp.append(target_gav)
                dependencies[source_gav] = target_gav

    return dependencies

if __name__ == "__main__":

    stdin = sys.stdin
    stdin.split('___SEPARATOR___')
    project_name = ''
    artifacts = get_artifacts(modules)
    dependencies = get_dependencies(go_dep_list, artifacts)

    udt = {
            'project': project_name,
            'artifacts': artifacts,
            'dependencies': dependencies,
            'language': 'go'
            }
    
    with open(project_name + 'udt.json', 'w') as out_file:
        json.dump(udt, out_file)
