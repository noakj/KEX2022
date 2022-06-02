# Article Notes for Maven Dependency Graph

## Overview
- snapshot of whole maven central @ september 2020
- stored in neo4j (graph) database
- api/cypher infrastructure to query
- zenodo.org/record/1489120

## Data
- 2.4M maven artifacts (projects)
- 9M dependencies
- artifacts := GroupId.ArtifactId.version
- Graph := (A, C, D, N):
    - A == set of nodes that model maven artifacts
    - C == calendar nodes (a --> release date --> calendar node)
    - D == dependencies:
        - provider --> provider of library
        - has scope (enum: compile,runtime...)
    - N == version precedence relationship (artifact, next_version_of_artifact)

## Research Opportunities
### 1. Library Maintenence
- Users do not update dependencies, providers choose to maintain parallel versions
-   Why does this happen?
- Maven Dependency Graph can help by:
    - identifying libraries with multiple versions
    - clients who do not update
### 2. Library Adoption Trends
- hype driven development
- wisdom of collective opinion vs single expert
- rogers theory [13] diffusion of innovation
- citation 1 has built library recommendation system on smaller data set
### 3. House of cards vs sustainable software
- Similar to Pashcenko [10] work on javascript eco system, maven graph can be used to implement methodology to assess developers quantifying the vulnerability of their own tools

## Reflections
- RO3 similar to questions/reflections on longitudinal analysis of java bloat:
    - how can developers quantify bloat potential
- What data should be presented to developers in order to best influence library adoption trends?
    - provider status?
    - risk of halted dependency
    - average bloat introduced
- why do clients not update libraries?
