# Introduction
## Software Supply Chain
The software supply chain is comprised of all resources, human and technological, required to produce a software product.
A significant component of this software supply chain are package managers, which are programming language specific collections of open-source software packages.
Package managers distribute open-source packages through online repositories, and provide methods of collecting all dependencies required for a certain package.
These package managers are often refered to as ecosystems, as the packages they consitute are interconnected through dependencies.
The use of open source packages from these software ecosystems is not only limited to use for other open source projects, rather it has been shown that 85\% of the source code for an average enterprise application is from open source packages.
## Software Supply Chain Attacks
Software supply chain attacks is a common method used by malicious actors in order to compromise software, and a growing concern for both developers and policy makers alike. \cite octoverse
This is acheived by injecting malicious code into a software package with the intent of the code being executed by dependent projects further down the supply chain.
As software ecosystems are highly connected, and the majority of packages are dependent on a minority of projects, a well target attack can have far reaching effects \cite{decan}
## Software diversity
Software diversity 
Software diversity can be both the result of design, as well arise naturally \cite{software_diversity}.
Software diversity in terms of diversity of dependencies, as opposed to mono-culture 
A strategy to mitigate the risk of software supply chain attacks is to increase software diversity.
## Ethereum Blockchain
Ethereum is an open-source decentralised software platform used for finance, digital art, and a host of web3 applications.
Based on blockchain technology, Ethereum functions by allowing users to share and trade digital assets through smart-contracts, which are recorded in a digital ledger.
The contents of the digital ledger are maintained and agreed upon by a vast number of nodes, which are computers that support the Ethereum Virtual Machine (EVM).

## Ethereum Clients + Diversity
To increase mitigate the potential risks caused by bugs and directed attacks, the Ethereum foundation promotes client diversity.
Several Ethereum clients are developed independently according to the same specification.



## Problem Statement
In this paper, an analysis of the software supply chain of three pairs of Ethereum clients is presented.

The analysis is narrowed down to focus specifically on the software diversity of open source dependencies and suppliers.
The studied clients are GoEthereum and Prysm, developed in Go, Besu and Teku, developed in Java, and OpenEthereum and Lighthouse, developed in Rust.
These clients are chosen for two reasons; they include the most popular clients in use, combined they total over 90\% of all nodes in the Eth1 execution and Eth2 consensus layer currently in use; each

The analysis is conducted through downloading and building the source code.
Outputting the dependency trees of each client using their native package manager.
Reformatting the dependency trees into a uniform json schema.
Analysis is then performed on individual trees, as well as on trees developed in the same language.
The direct dependencies were also researched in order to classify their area of use.

## Contributions
- Unified Dependency Tree
- Novel information comparing 3 ecosystems
