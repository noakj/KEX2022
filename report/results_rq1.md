# Results Summary RQ1

After analyzing all Ethereum clients individually, there is an evident size difference between the supply chains of the two Ethereum layers as shown in Table \ref{tab:tree_metrics_eth}.
Besides Besu having more unique direct dependencies than Teku, the supply chain metrics gathered are much larger for the Eth2 clients compared to the Eth1 clients of the same ecosystem.
The biggest difference is seen in the Go ecosystem, in which the metrics of the Eth2 client Prysm is at least twice the size of the metrics of the Eth1 client Geth.

All the Eth1 clients require roughly the same amount of unique direct dependencies, while having vastly different amounts of unique transitive dependencies.
For Geth (Go), there are 3.2 unique transient dependencies per unique direct dependencies; for OpenEthereum (Rust) this ratio is 5.7; for Besu (Java) it is 3.0.
Although the Eth2 clients have vastly differing amounts of unique direct dependencies, the ratio of unique direct dependencies to unique transient dependencies are similar to the Eth1 clients from the same ecosystem; Prysm (Go) 4.3; Lighthouse (Rust) 5.6; Teku (Java) 3.0.

There are no clear patterns between the number of suppliers in the different Ethereum layers. There are however clear similiarities between the number of suppliers per unique dependencies between clients written in the same ecosystem. 
For the Go ecosystem each supplier provides on average 1.7 and 2.0 unique artifacts for Geth and Prysm respectively.
For the Rust ecosystem each supplier provides on average 1.5 and 1.3 unique artifacts for OpenEthereum and Lighthouse respectively.
For the Java ecosystem this value is 2.7 and 2.4 for Besu and Teku respectively.
