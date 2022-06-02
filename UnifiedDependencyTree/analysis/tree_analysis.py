import sys
import json
from collections import Counter

def get_suppliers(artifacts):
    
    suppliers = []
    for gav in artifacts:
        artifact = artifacts.get(gav)
        suppliers.append(artifact.get('groupId'))

    return suppliers

def get_artifacts_list(artifacts):

    return artifacts.keys()

def get_all_deps(dependencies):

    all_deps = []

    for deps in dependencies.values():
        all_deps += deps

    return all_deps

def rec_all_deps(cur, dependencies):

    count = 0
    cur_deps = dependencies[cur]
    for dep in cur_deps:
        count += rec_all_deps(dep, dependencies)

    return count


def get_direct_deps(project, dependencies):
    
    direct_deps = dependencies.get(project)

    return direct_deps


def get_transitive_deps(project, depenedencies):

    transitive_dependencies = dependencies.pop(project) 
    transitive_deps = get_all_deps(dependencies)

    return transitive_deps

def get_redundant_libraries(deps_list, artifacts):

    libraries = [artifacts[dep].get('artifactId') for dep in deps_list]

    return Counter(deps_list)
    


if __name__ == "__main__":

    project = sys.argv[-1]
    path = project + '/' + project
    
    artifacts = {}
    dependencies = {}

    suppliers = {}
    direct_deps_count = 0
    transitive_deps_count = 0
    redundant_deps = {}

    with open(path+ '_artifacts.json', 'r') as artifacts_file:
        artifacts = json.load(artifacts_file)

    with open(path + '_dependencies.json', 'r') as deps_file:
        dependencies = json.load(deps_file)

    suppliers = get_suppliers(artifacts)
    suppliers_set = set(suppliers)
    suppliers_count = len(suppliers_set)
    artifacts_count = len(get_artifacts_list(artifacts))
        
    direct_deps_list = get_direct_deps(project, dependencies)
    direct_deps_count = len(direct_deps_list)
    transitive_deps_count = artifacts_count - direct_deps_count
    
    all_deps_list = get_all_deps(dependencies)
    redundant_deps = get_redundant_libraries(all_deps_list, artifacts)
    total_redundancy = sum([dep for dep in redundant_deps.values() if dep > 1])
    print(rec_all_deps(project, dependencies)
    '''
    with open(path + '_metadata.txt', 'w') as outfile:
        outfile.write('Direct: ' + str(direct_deps_count) + '\n')
        outfile.write('Transitive: ' + str(transitive_deps_count) + '\n')
        outfile.write('Suppliers: ' + str(suppliers_count) + '\n')
        outfile.write('Total dependencies' + str(len(all_deps_list)) + '\n')
        outfile.write('Redundancy: ' + str(total_redundancy) + '\n')
        '''
