#!/bin/bash

get_go_deps() {
    go list -m -f '{{.Path}} {{.Version"}}' all | \
    sed 's/ /@/'
}

get_go_tree() {
    go mod graph
}

(get_go_deps; echo ___SEPARATOR___; get_go_tree;) | parse_go_tree.py
