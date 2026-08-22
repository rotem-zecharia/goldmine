# vitali87/code-graph-rag

The ultimate RAG for your monorepo. Query, understand, and edit multi-language codebases with the power of AI and knowledge graphs

## features

Point Code-Graph-RAG at a repository and it reads every source file, extracts functions, classes, methods, modules, and the relationships between them, and stores the result as an interconnected graph. Once the graph exists you can:

- Ask questions about the codebase in natural language and get answers grounded in the real structure.
- Retrieve the actual source of any function, class, or method by name or by intent.
- Edit code through the agent with AST-based surgical patching and a diff preview before anything changes.
- Optimise code against language best practices or your own coding standards.
- Find dead code by walking call and reference edges from entry points.
- Search and rewrite structurally by AST pattern with ast-grep.
- Overlay runtime behaviour: trace a test run (or pull production eBPF profiles) with `cgr trace` and merge the calls that actually happened into the graph, exposing dispatch that static analysis cannot see.

## installation

`cgr` is published to PyPI. Install it system-wide with the `treesitter-full` (all languages) and `semantic` (vector search) extras:

```bash
