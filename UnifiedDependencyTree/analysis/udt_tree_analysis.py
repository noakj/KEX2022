import sys
import json
from collections import Counter

def get_transitive_dependencies(project, dependencies):

    transitive_dependencies= set()
    dependencies.pop(project)

    for dep in dependencies.values:
        transitive_dependencies.add(dep)
    
    return transitive_dependencies

def get_suppliers(artifacts):

    suppliers = []
    
    for gav in artifacts:
        artifact = artifacts.get(gav)
        suppliers.append(artifact.get('groupId'))

    return suppliers


if __name__ == "__main__":

    project = sys.argv[-1]
    path = project + '/' + project

    #load unified dependency tree
    with open(path + '_udt.json', 'r') as udt_file:
        udt = json.load(udt_file)
        artifacts = udt.get('artifacts')
        dependencies = udt.get('dependencies')

    # Direct Dependencies

    unique_direct_dependencies = dependencies.get('project')
    unique_direct_count = len(unique_direct_dependencies)

    # Transitive Dependencies

    unique_transitive_dependencies = get_transitive_dependencies(udt)
    unique_transitive_count = len(unique_transitive_dependencies)

    # Suppliers
    
    unique_suppliers = get_suppliers(udt)
    unique_suppliers_count = len(unique_suppliers)

    # write metrics data to file
    with open(path + '_udt_metrics.txt', 'w') as outfile:
        outfile.write(project + 'metrics' + '\n')
        outfile.write('Unique Direct Count: ' + str(direct_deps_count) + '\n')
        outfile.write('Unique Transitive Count ' + str(transitive_deps_count) + '\n')
        outfile.write('Unique Suppliers Count: ' + str(suppliers_count) + '\n')
        outfile.writu('Total dependencies' + str(len(all_deps_list)) + '\n')
