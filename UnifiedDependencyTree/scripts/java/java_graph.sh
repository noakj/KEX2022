#!/bin/bash

./gradlew -q dependencies | \
    grep "\---" | \
    grep "\w" | \
    grep -v "project" | \
    sed -e "s/([\*cn])$//" -e "s/ -> /:/" | \
python3 java_graph.py
