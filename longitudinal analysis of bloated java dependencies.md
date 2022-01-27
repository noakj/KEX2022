# Article Notes for 'Longitudinal analyis of java bloat'

## Definitions

- Bloated dependencies:
    - dependency d € D in a software project p i said to be bloated if there is no path in the dependency tree of p, between p and d, such that none of the elements in the API of d are used, directly or indirectly, by p.

## Data
- 48469 distinct dependencies
- 31515 versions of dependency trees
- 435 open source projects

## Research Questions
### 1. Bloat Trend
- bloated transitve dependncies grow over time (1695->286228 during 2011-2020)
- bloated direct grow at significantly slower pace
- trend for direct dependencies:
    - 56.3% projects increased bloat
    - 24.4% projects decreased bloat
    - 19.3% projects stable
- regardless of direct bloat trend, transitive bloat will evolve
- 61% projects with decreasing bloated direct dependencies, transitive bloat evolved regardlessly
### 2. Usage Patterns
- 89.9% of bloated direct dependencies remain bloated through time
- 93.3% of transitive bloat remains bloat
- direct pattern:
    - 64.3% used
    - 29.9% bloat
    - 94.2% remain unchanged
- transitive pattern:
    - 12.8% used
    - 78.8% bloat
    - 91.1% remain unchanged
### 3. Unnecessary Updates
- developers account for majority of updates (dependatbot very few)
- both devs and bot update 22% of bloated dependencies
### 4. Bloat Origin
- direct:
    - new dependency (84.3%) > removed code (8.8%) > updated code (6.9%) > new version (2.1%)
- transitive:
    - new dependency (97.9%) > updated core (1.6%) > removed code (0.6%) > new version (0.4%)
- majority of bloat is introduced due to developers adding new dependencies.
- majority of bloat is bloated at time of introduction, or will remain bloated upon detection

## Reflections
- are bloated transitive dependencies similar for different users of the same provider?
- how much transitive bloat does a provider introduce to user of their project?
- can a developer gain knowledge/improve code base by knowing what dependencies/features are un used?
- are there repeat offenders which cause majority of transitive bloat (pareto principle?)
- requires solidarity on parts of all developers to clean bloat in hosue to have cumulative effect on eco system
- can providers used knowledge of user bloat to break package into core parts (think unix)
