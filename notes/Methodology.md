# Methodology Notes

- Go:
    - go mod init
    - go mod tidy 
    - go mod graph | sudo tee project_dependencies.txt
    - go list -m -f '{{.Path}} {{.Version}}' all | sudo tee go_all_mods.txt
- go mod graph:

    Usage:

    go mod graph [-go=version]
    The go mod graph command prints the module requirement graph (with replacements applied) in text form. For example:

    example.com/main example.com/a@v1.1.0
    example.com/main example.com/b@v1.2.0
    example.com/a@v1.1.0 example.com/b@v1.1.1
    example.com/a@v1.1.0 example.com/c@v1.3.0
    example.com/b@v1.1.0 example.com/c@v1.1.0
    example.com/b@v1.2.0 example.com/c@v1.2.0
    Each vertex in the module graph represents a specific version of a module. Each edge in the graph represents a requirement on a minimum version of a dependency.

    go mod graph prints the edges of the graph, one per line. Each line has two space-separated fields: a module version and one of its dependencies. Each module version is identified as a string of the form path@version. The main module has no @version suffix, since it has no version.

    The -go flag causes go mod graph to report the module graph as loaded by the given Go version, instead of the version indicated by the go directive in the go.mod file.

    See Minimal version selection (MVS) for more information on how versions are chosen. See also go list -m for printing selected versions and go mod why for understanding why a module is needed.
- module graph: The directed graph of module requirements, rooted at the main module. Each vertex in the graph is a module; each edge is a version from a require statement in a go.mod file (subject to replace and exclude statements in the main module’s go.mod file.
- module: A collection of packages that are released, versioned, and distributed together.
