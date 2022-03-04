#!/bin/bash

go list -m -f '{{.Path}} {{.Version}}' all | sed 's/ /@/' | python3 parse_go_mods.py
go mod graph | python3 parse_go_deps.py
