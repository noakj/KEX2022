# Methodology

## Project Pipeline

In order to generate a dataset depicting the software supply chain of the Ethereum ecosystem, each studied client was treated according to Figure \ref{pipeline} individually.
For each client, the latest version of the source code was downloaded from their respective github repository.
The build process was then invoked inorder to download all direct and transient dependencies.
The client software was then run to ensure that all dependencies were fetched and that the software was functional.
Using the native package manager of the client their dependency tree was output.
From this step in the pipeline until the analysis of the unified dependency trees, the implementation of the procedure varied depending on the package managers used.
In general terms the next step was to strip the raw dependency tree of data irrelevant to the study.
Examples of irrelevant data include internal (non-third-party) dependencies as well as paths pointing to the location of dependency source files on the system.
Next, the raw dependency tree was parsed. Individual packages were formated according to the artifacts schema, and the dependency relationships were formated according to the dependency schema, both defined in the next subsection and shown in \ref{schema}.
This process differed dependening on the format of the raw dependency trees, which were either nested trees as seen in figure \ref{cargo_tree}, or lists of package pairs as seen in figure \ref{go_tree}.
Once the data was structured in the unified dependency tree format, the same procedure for analysis was utilized for all clients.
Individual trees were analysed in order to collect metrics defined in section METHODOLOGY>METRICS.
Unified Dependency Trees of clients developed in the same programming language were also analysed together in order to collect data regarding to the intersection of their dependencies.
Details of differences in implementation, and technical difficulties, of clients are described below.

### GO
Package management in Go differs from most other programming languages in that it does not utilize a third-party package manager, nor a central repository to host software packages.
Where packages are hosted is instead left up to the supplier. From manual inspection of the dependencies in the studied Go clients, github is the most common hosting solution. 
Go does not use differentiate dependencies by scope, rather all dependencies are compiled when build procedures are invoked.
In order to define dependencies in a Go project, a developer lists each dependency by the url which points to where the package is hosted followed by its version.
This is done in a file named \texttt{go.mod} in the project directory.
The command \texttt{go mod graph} will output a list of all dependencies in the project, including internal non-third-party dependencies, with each line containing a dependent package and its dependency separated by a space.
In order to remove internal dependencies, the command \texttt{go list -m} is used to curate a list of third party packages.
These lists are used together to ensure that the unified dependency tree only consists of third party dependencies.

### Rust

### Java

## Schema
Define it
Motivate structure
Motivate need

## old metrics

With the dependency trees of all studied Ethereum clients in a unified format only a limited set of python scripts are needed to analyse all the data.

The supply chain of each dependency tree is analysed for the following quantitative metrics; unique direct dependencies, unique transitive dependencies, and unique suppliers.
This is achieved by running a script from the command line and providing the directory containing the unified tree as an argument as shown below \\
\texttt{python3 tree\_analysis.py besu} \\
Using the data structures as shown in Figure \ref{pipeline} the script iterates over artifacts of the dependency tree and utilizes the python \texttt{}{set()} datatype to collect the relevant data. Python \texttt{}{set()} is defined as a unordered collection, and is useful in this context as they do not allow duplicates, and thus ensure uniqueness.

All clients from the same ecosystem are also analysed together in order find the intersection of dependencies, as well as the most common suppliers present in the intersection. This is achieved using another script which is run in the same manner as above, but takes in multiple directories as arguments as shown below for the studied Java clients. \\
\texttt{python3 eco\_analysis.py besu teku} \\
The datatype \texttt{set()} is used as containers for the dependencies of each client provided, and the method \texttt{set.intersect()} is used to get the intersection.
This script also utilizes the python class \texttt{Counter} from the standard python library \texttt{Collections}, which is useful in providing the frequency of occurrences for each value in a large data set.

Manual analysis of the most prevalent suppliers and dependencies in each ecosystem has also been performed to identify qualitative measures such as functionality provided and the type of organisation. \todo{add the url to the GitHub repository containing the code and data of your analysis}


## Metrics
For the analysis of individual clients the following metrics were collected:
- Total Dependencies:
This metric is the sum of all dependency relationships. A package which is a dependency of several packages is counted once for each dependent package. If a dependent package is featured multiple times its dependencies are only counted once for the dependent package.
- Unique direct dependencies:
This metric is the sum of all packages which are direct dependencies of the analysed client. These packages are all declared in the source code of the client according to the procedures defined in section METHODOLOGY-PIPELINE
Unique transient dependencies
This metric is the sum of all packages 
Unique suppliers


## Qualitative Analysis

Categories of dependencies

## Research Questions
### RQ1
What is the supply chain of the 
### RQ2
### RQ3
