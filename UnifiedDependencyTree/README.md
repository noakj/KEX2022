# Unified Dependency Tree

## About
- Set of scripts for extracting and analysing dependency trees of projects written in Go, Rust, & Java
- Created and used for bachelors thesis project.

## Extraction
- shell scripts for extracting dependency trees
- python scripts for reformatting native dependency trees into unified json schema.
- Usage:
    - copy both .sh and .py scripts (for particular language) into root directory of project
    - unified dependency tree stored as project_name + 'udt.json'
## Analysis
### Tree Analysis
- python scripts for exporting metrics of individual dependency tree
### Ecosystem Analysis
- python scripts for comparing dependency trees of same ecosystem
### Visualization
- python scripts for creating figures of data

## Ether Clients
- dependency trees of ethereum execution and consensus clients gathered using extraction scripts
- unified dependency trees of each client
- analysis of individual unified dependency tree
- analysis of unified dependency trees of ecosystems

## Contributors
- Noak Jönsson
