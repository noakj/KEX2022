import sys
import json


if __name__ == "__main__":

    project = sys.argv[-1]
    path = project + '/' + project

    artifacts = {}
    dependencies = {}

    with open(path + '_artifacts.json', 'r') as art_file:
        artifacts = json.load(art_file)

    with open(path + '_dependencies.json', 'r') as dep_file:
        dependencies = json.load(dep_file)

    unique_artifacts = artifacts.keys()
    direct_dependencies = set(dependencies[project])
    transitive_dependencies = unique_artifacts - direct_dependencies

    print(len(unique_artifacts))
    print(len(direct_dependencies))
    print(len(transitive_dependencies))


