'''
a artifacts = set of nodes modelling maven artifacts
c calendar = set of nodes 
d dependencies = set of edges linking artifacts
n version_precedence = set of artifacts with version precedence rules

'''

# Imported Data
deps_list = './data/besu/besu-21.10.6_dependencies_all_gav.txt' 
deps_tree = './data/besu/besu-21.10.6_dependencies_tree.txt' 
deps_conflicts = '/data/besu/besu-21.10.6_dependencies_conflicts.txt'

# Formatted data structures
artifacts = {}
calendar = {}
dependencies = {}
precedence = {}
scope = ['COMPILE', 'RUNTIME', 'PROVIDED', 'TEST', 'SYSTEM', 'IMPORT']
# packaging = ['JAR', 'WAR', 'POM', 'EAR']


def format_artifact(gav, date, packaging):
    [groupId, artifactId, verion] = gav.split(':')
    return {
            coordinates: gav,
            groupId: groupId,
            artifactId,
            version,
            releaseDate,
            packaging
            }

def format_date():
    return {
            year,
            month,
            day
            }


def format_dependency():

    return {
            user,
            provider
            }

def format_precedence():

    return {
            artifactId,
            precedence_order
            }


def main:
    calendar = read_date()
    artifats = read_all()
    dependencies = read_tree()
    precedence = read_precedence()

