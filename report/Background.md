# Background Section

## Software Supply Chains
Software supply chains are all the resources required to produce a software product.
This includes human resources, such as developers, teams, and larger organizations.
Technical procedures such as automatic testing and build processes.
Lastly, this also includes other software products such as standard libraries, tools, and third party software packages.
The focus of this report will be on the software diversity in software supply chains with regard to third party open source software (OSS) packages and their suppliers.
## Software Dependencies
The use of OSS by developers to create a new product is a cornerstone of modern development practices.
In order to feasibly facilitate the reuse and distribution of OSS developers often rely on package managers.
Package managers are programming language specific repositories of OSS packages.
Not only do they host the source code for OSS packages, but also provide methods for downloading, updating, and building packages.
Examples of package managers are Gradle and Maven for Java, PyPi for Python, and Cargo for Rust.
Go, which is used to develop two of the clients studied in this report, does not utilize a package manager.
Although Go does not have central repositories, the language does provide a tool for downloading and updating packages.
In order to utilize the functionality provided by an OSS package in a project, a developer must declare it as a dependency.
Software dependencies are packages that are required by another package in order to function.
Declaration of dependencies is accomplished through the use of a file in the root of the project directory. 
\reference{cargo.toml} shows an example of how dependencies are listed for a project developed in the langauge Rust, utilizing the cargo package manager.
Common for all package managers is to list the name of the package, which is unique. Most, although not all, package managers also require a specific version of the dependency package to be declared.
Any package referenced explicitly as a dependency in a project is defined as a direct dependency to said project.
As direct dependencies themselves may have their own dependencies, they are also dependencies to the project.
These dependencies are defined as transient dependencies.

## Software Supply Chain Attacks
Software supply chain attacks are directed attempts to inject malicious code into a software package, in order to compromise any and all software packages which are dependent on the targeted package.
2021 the EU Agency for Cybersecurity reported that 66% of cyber attacks target the software supply chain.
As Decan et al. showed in a 2017 report analysing trends in seven different software ecosystems, that a majority of software packages are dependent on a minority of core packages. This highlights how a succesful and well targeted attack can affect the majority of a software ecosystem.
Software supply chain attacks targetting the dependency tree can be split into two categories; those infecting existing packages, and those that create new packages containing malicious code \cite{backstabber}.
When infecting an existing package culprits often rely on existing known vulnerabilities in the code. Otherwise they need access to the project, which can be achieved through social engineering, ie manipulating their way to get maintainer privilidges for the project, or by gaining the credentials of a person who is a maintainer of the project.
When creating new packages containing malicious code the culprit must still inject the package into some software supply chain. This is most commonly acheived through Typosquatting, which is when a package given a name that is a slight spelling variation to that of a popular package. For example a package could be named 'bloons-db' instead of 'blooms-db', as seen in \ref{cargo.toml}. Other ways of injecting a malicious package includes creating a Trojan Horse, where a package claims to provide some functionality, but has a built-in backdoor mechanism to allow culprits to extract data from the end users of the project.

## Software Diversity

Software diversity is a concept with a broad scope in the study of software development.
In general, it refers to the existence of multiple software components which are functionally similar, but implemented and created in seperate ways.
The aim of software diversity is to encourage fault tolereance, security, and reusability \cite{softare_diversity}.
This report deals mostly with the concept of design diversity and managed natural diversity.
Design diversity refers to the practice of independently developing multiple software projects according to the same specification.
Utilizing these projects simultaneously yields a more fault tolerant system due to "the independence of failures among the diverse solutions" \cite{software_diversity}.
Managed natural diversity emerges as a result of development practices.
As open source licenses give anyone the right to copy, modify, and redistribute an OSS packages, this practice has the potential to yield vast amounts of software diversity \cite{opensource.org}.
The opposite of software diversity is monoculture, where a single software supplier, or a single package, is heavily reoccuring in a software supply chain.
Monoculture provides malicious actors a definite target from which a malicious code injection could have a tremendous impact.

## Blockchain/Ethereum
Ethereum is an open-source decentralised software platform used for finance, digital art, and a host of web3 applications.
Based on blockchain technology, Ethereum functions by allowing users to share and trade digital assets through smart-contracts, which are recorded in a digital ledger.
The contents of the digital ledger are maintained and agreed upon by a vast number of nodes, which are computers that support the Ethereum Virtual Machine (EVM).

## Ethereum Clients
The Ethereum Foundation promotes design diversity, in the form of client diversity.
There is no official implimentation, rather there are several clients developed in different programming languages, as to increase software diversity by leveraging several ecosystems of OSS packages.


### Eth1 Execution
The function of the execution layer (Eth1) is to add new blocks of transactions to the shared state of the network.
Eth1 uses a proof-of-work (PoW) mechanism in order to ensure that the new state is valid.
When a transaction occurs, and is to be added to the blockchain, nodes running an Eth1 client compete against each other in completing a computionally heavy task.
The first node to complete the task is allocated the block, and all other nodes with point to it as the correct state.
The currently available Eth1 clients, the language they are developed in, and the percentage of nodes running them are;
GoEthereum - Go - 84.33\%
Erigon - Go - 7.26\%
OpenEthereum - Rust - 5.77\%
Nethermind - C# - 1.78\%
Besu - Java - 1.22\%
### Eth2 Consensus
The function of the consensus layer (Eth2) is to make sure that the updated state of a new block being added to the chain is distributed amongst all the nodes in the network.
Eth2 uses proof-of-stake (PoS) validation. This consensus method is more energy efficient, as no computationally heavy task is required.
In this method, nodes stake their own capital as collateral in order to ensure that they behave correctly.
The currently available Eth2 clients, the language they are developed in, and the percentage of nodes running them are;
Prysm - Go - 38.34\%
Lighthouse - Rust - 33.51\%
Teku - Java - 16.51\%
Nimbus - Nim - 11.54\%
