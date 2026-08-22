# MontFerret/ferret

Declarative data automation language and Go runtime for structured extraction workflows.

## features

- Purpose-built declarative language for querying, transforming, synchronizing, and automating structured data
- Embeddable Go runtime with reusable compiled plans and isolated execution sessions
- Capability-based host values for exposing application objects, resources, and external systems directly to FQL
- Unified query model for browsers, APIs, databases, documents, and custom data sources
- Extensible runtime through namespaced functions, modules, hooks, and custom value types
- Event-driven synchronization and dispatch for interacting with asynchronous and stateful resources
- Managed resource lifecycle for files, connections, cursors, streams, and other host resources
- Bytecode VM and portable programs for efficient repeated execution and precompiled artifacts

## installation

```bash
go get github.com/MontFerret/ferret/v2@latest
```

There are currently two ways to start with Ferret v2:
- Native v2 API - recommended for new projects
- `compat` module - recommended as a first migration step for existing v1 integrations
