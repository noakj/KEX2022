#!/bin/bash

./gradlew -q dependencies | \
    grep "\---" | \ #only pass lines with dependenencies
    grep "\w" | \ #only pass lines containing words
    grep -v "project" | \ #remove internal dependencies
    sed -e "s/([\*cn])$//" -e "s/ -> /:/" | \ #remove trailing characters and reformat duplicate version separator
    python3 java_graph.py #output tree in unified format
