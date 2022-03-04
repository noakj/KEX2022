#!/bin/bash

go list -m -f '{{.Path}} {{.Version}}' all | parse_go_mods.py
# go mod graph | sed "s/@/ /g" | parse_go_deps.py
