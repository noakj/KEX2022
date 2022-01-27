# Notes for Vulnerable Open Source Dependencies (those that matter)
## Overview
- 20% of vulnerabilities are not deployed
- 81% of known vulnerabilities can be fixed by updating dependency
- 1% of vulnerabilities due to halted dependencies
- libraries from same provider should be treated differently than 3rd party dependencies
- grouping procedure:
    - artifacts with same groupId within a path substituted in path by artifact closest to vulnerability
    - (x1, y1, y2, z1) --> (x1, y2, z1)
## RQ1: How many actually vulnerable dependencies does a library have?
- Vulnerable dependencies are only hazardous if they are deployed
- The number of vulnerable dependencies may be over inflated to do papers on distinguishing dependencies by scope.
- paper found that 20% of studied vulnerable dependencies are not deployed
## RQ2: Who is responsible for vulnerable dependencies?
- Developers of a project responsible for their own code
- a dependency tree with several library instances belonging to the same project, those dependencies should not be considered separately, as an update to one of those dependencies will bring on all new versions. Some transitive dependencies may be controlled from the project under analysis
- failure to distinguih between own vs third-party dependencies may cause a project with modular libraries to assume that its own broken/vulnerable code is due to an insecure eco system (dependency hell)
- to answer q2 we must know:
    - difference between own vs direct dependencies
    - # of vulnerable dependencies
- by grouping libraries by project/provider, the number of direct dependencies increased 87%
- developers responsible for 82%, not 37%, of vulnerabilities (solved by updating)
## RQ3: How many direct dependencies can be fixed?
- Simplest solution to outdated/ vulnerable direct dependency is to update
- Halted dependencies major problem:
    - contribute to project, develop new release
    - fork halted library and maintain as part of dependent library
- 13% direct 16% transitive dependencies halted


