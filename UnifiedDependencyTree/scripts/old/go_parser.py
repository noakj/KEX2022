import sys
import pprint


def format_artifact(module):
    
    path, version = module.split(' ')
    path_split = path.split('/')
    name = path_split.pop()
    provider = path_split.pop() if len(path_split) else name
    
    return {
            'name': path,
            'version': version,
            'gav': path + version
            }

if __name__ == "__main__":
    
    ether_implementation = sys.argv[1]
    modules = ether_implementation + "_all_mods.txt"
    graph = ether_implementation + "_graph_v2.txt"
    
    artifacts = {}
    dependencies = {}

    with open(modules) as mods_file:
        
        for mod in mods_file.read().splitlines():

            artifact = format_artifact(mod)
            gav = artifact['gav']
            artifacts[gav] = artifact

    with open(graph) as graph_file:
        for dep in graph_file.read().splitlines():
            
            split_dep = dep.split(' ')
            reverse_path = split_dep[0]
            reverse_version = 
            reverse_gav = reverse_path + reverse_version
            dependency_gav = split_dep[-2] + split_dep[-1]
            
            if reverse_gav in artifacts:
                if dependency_gav in artifacts:
                    temp = dependencies.get(reverse_gav, [])
                    temp.append(dependency_gav)
                    dependencies[reverse_gav] = temp


    total_deps = 0
    for dep_list in dependencies.values():
        total_deps += len(dep_list)

    pprint.pprint(dependencies)
    print('Artifacts: ' + str(len(artifacts.keys())))
    print('Dependencies: ' + str(total_deps)) 
