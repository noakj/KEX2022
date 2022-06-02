#!/bin/bash

go list -m -f '{{.Path}} {{.Version}}' all | \ #list all 3rd party go dependencies 
    sed 's/ /@/' | \ 
    sudo python3 parse_go_mods.py #create artifacts in unified structure
go mod graph | \ #output dependency tree (includes non 3rd party dependencies)
    python3 parse_go_deps.py #create dependencies (unified structure) - reads from artifacts.json so to not include non 3rd party dependencies
