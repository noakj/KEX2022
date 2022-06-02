# Kandidat Examens Arbete 2022

## TODO

- [.] Background:
    - [ ] Rewrite about ethereum ecosystem
    - [ ] What is the role of the Ethereum clients?:
        - [ ] how these clients are made out of open-source software?
        - [ ] You can refer to some stats in their GitHub repositories there
        - [ ] You can add a general figure
    - [ ] Add a couple of paragraphs to introduce the notion of client diversity:
        - [ ] Why it is important?
        - [ ] What the community can do to promote this diversity?
        - [ ] Why it is important to study this diversity?
    - [X] Formally define the following:
        - [X] Blockchain
        - [X] Ethereum client (debrief the differences between Eth1 and Eth2)
        - [X] Software supply chain
        - [X] Software dependencies
        - [X] Supply chain attack
        - [X] Sofware diversity (as an attempt to mitigate software monoculture)
    - [ ] You can cite the Solarwinds incident to motivate your study.
- [ ] Introduction:
    - [ ] add problem statement:
        - [ ] why it is relevant
        - [ ] how it will be addressed
    - [ ] Add one paragraph about blockchain and Ethereum: Why should the reader care or be excited about this particular technology?
    - [ ] Add one paragraph about the Ethereum clients:
        - [ ] How do they communicate in the decentralized network?
        - [ ] How do they sign and verify contracts? 
        - [ ] Why is security so important in this context
    - [ ] Add one paragraph about the need of hardening the software supply chain of Ethereum clients?:
        - [ ] What types of attacks are they susceptible to by relying on open source dependencies?
        - [ ] E.g., malware introduced by malicious contributors, typosquatting, etc. Give one example of previous events related to dependency vulnerabilities (e.g., log4j event).
    - [ ] Add one paragraph about how this reports aims to shed some light on the supply chain of Ethereum clients. Why is this report novel?
    - [ ] citations to related works
    - [ ] bullet point list summarizing main contributions to report
- [ ] Methodology:
    - [ ] Specific implementation irrelevant - explain what metrics and why
    - [ ] How do you determine most prevalent suppliers?
    - [ ] Fig 2 needs several improvements. The figure should be conceptual (no implementation details there). Illustrate whatkind of data are you processing and filtering, not how are you doing it. Add colors to represent each phase (have a look at Fig 2 in this paper for inspiration about the colors and the structure). Make it two columns, at the top of page 3. 
    - [ ] Refer to Fig 2 and describe each section
    - [ ] Ecosystems are not the programming languages, but the community and technology around it (i.e., the package managers, virtual machines, tooling, etc.). 
    - [ ] Remove all the implementation details, and explain what are you going to do, not how.
    - [ ] You need to properly define each quantitative metric that you use separately (conceptually). No need to explain how you compute them.
    - [ ] Elaborate on the need of having a “Unified Dependency Tree”:
        - [ ] Why is it difficult to analyze dependency trees from different package managers?
        - [ ] Why do we require a universal dependency tree model?
    - [ ] Explain in detail and motivate (at least two paragraphs) the qualitative analysis that you performed. This is not clear in the report. 
    - [ ] Introduce and motivate each research question in this section.
- [ ] Results:
    - [ ] RQ1:
        - [ ] Descibe Table1 - explain each column - give ranges per project/metrics
        - [ ] Fig 1 is good. But I prefer making the distinction: use “Programming language” and “Package manager” instead of “Ecosystem”
        - [ ] Table 1, place the caption on top of the table.
        - [ ] Add a summary at the end of each research question, look at this paper as an example.
    - [ ] RQ2:
        - [ ] Add a two columns table with the 10 most common dependencies shared across different clients, and add a brief description of each.
        - [ ] elaborate on "rust is 'better'..."
    - [ ] RQ3:
        - [ ] You should perform a qualitative analysis of the categories of dependencies of the different trees. At least elaborate a table with the 10 most common types of dependencies (e.g., IO, Database handling, data structures, networking, etc.) and suppliers (Apache, Eclipse, Google, etc.), according to your manual classification.
- [ ] Discussion:
    - [ ] 3 to 5 paragraphs 
    - [ ] about the ways to mitigate supply chain attacks from the perspective of the Ethereum client maintainers. Look at this paper for inspiration.
- [ ] Conclussion:
    - [ ] single paragraph
    - [ ] descirbe what has been done (past tense)
    - [ ] This points to that the Eth2 consensus layer is a more complex system of cryptography procedures, requiring far more external software packages in order to function” This is a strong finding of your analysis. I suggest moving this to the Results Section.
    - [ ] “As time progresses, developers tend to choose software packages supplied by reputable vendors, and larger reputable organizations outlast and take over development from smaller vendors” Move this part to the Discussion Section.
    - [ ] source for hype driven development
- [ ] Abstract:
    - [ ] Introduce/explain software supply chain
    - [ ] fix method summary - say what you do, not how you do it (do not reference scripting)
    - [ ] explicitly state clients studied
    - [ ] explicitly state metrics
    - [ ] provide precise data to claims
- [ ] References:
    - [ ] check all arkivx refs


## Research Questions
1. What is the supply chain of the Ethereum Clients?
2. What is the diversity of dependencies in the supply chain of Ethereum Clients?
3. What are the key functianalities in the software supply chain across the different ecosystems of Ethereum Clients?
