import os
import json
from collections import Counter

def get_suppliers(artifacts):
    
    suppliers = []
    for gav in artifacts:
        artifact = artifacts.get(gav)
        suppliers.append(artifact.get('group'))

    return Counter(suppliers)

def get_all_deps(dependencies):

    all_deps = []

    for deps in dependencies.values():
        all_deps += deps

    return all_deps


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

    path = os.getcwd()
    project = path.split('/').pop(-1)
    
    artifacts = {}
    dependencies = {}

    suppliers = {}
    direct_deps_count = 0
    transitive_deps_count = 0
    redundant_deps = {}

    with open(project + '_artifacts.json', 'r') as artifacts_file:
        artifacts = json.load(artifacts_file)

    with open(project + '_dependencies.json', 'r') as dependencies_file:
        dependencies = json.load(dependencies_file)

    suppliers = get_suppliers(artifacts)
    print(suppliers)
        
    direct_deps_list = get_direct_deps(project, dependencies)
    direct_deps_count = len(direct_deps_list)
        
    transitive_deps_list = get_transitive_deps(project, dependencies)
    transitive_deps_count = len(transitive_deps_list)
    
    all_deps_list = direct_deps_list + transitive_deps_list

    redundant_deps = get_redundant_libraries(all_deps_list, artifacts)
    
