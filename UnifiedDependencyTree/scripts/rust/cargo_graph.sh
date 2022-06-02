#!/bin/bash

cargo tree -f "{r} {p}" | \ #output nested ascii tree
    #format p -> package name + version, r -> dependency path (contains groupId)
sed -e "s/[][]//g" \ 
    -e "s/  / /g" \
    -e "s/([a-zA-Z0-9/*.-]*)//g" \ #remove trailing path
    -e "s/[\w]\-dependencies$//" | \
python3 parse_cargo_tree.py
