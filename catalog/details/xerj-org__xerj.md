# xerj-org/xerj

XERJ is the new way for AI to search data. Its autoindex capability activates agents to know your data without the token waste of grep and sed. One command indexes code, docs, logs and PDFs for search

## installation

```sh
curl -fsSL https://xerj.org/get | sh
```

Windows PowerShell:

```powershell
irm https://xerj.org/get.ps1 | iex
```

One static binary, no JVM, no dependencies. Prebuilt for Linux, macOS and Windows on x86-64
and arm64. You can also [build from source](#build-from-source). It speaks the Elasticsearch
API, so existing clients, dashboards and tooling work against it unchanged.

First commands after install (the installer prints where `xerj` landed; add it to your PATH
if needed): `xerj --insecure --data-dir ./data &`, wait until `http://localhost:9200`
responds, then `xerj autoindex ~/my-project`. See [Index a folder](#index-a-folder).

For a host with no runtime internet access, follow the
[air-gapped deployment recipe](./docs/recipes/air-gapped-deployment.md). The default lexical
embedder is offline; neural mode needs the three model files staged locally before the first
semantic operation.

## Index a folder

Start the server, then point `autoindex` at anything:

```sh
xerj --insecure --data-dir ./data &     # local dev: no TLS, no auth
xerj autoindex ~/my-project
```

If your server has auth on, which is the default for every start without `--insecure`
(including any start from a config file), hand `autoindex` the same key. It never picks the
key up from `xerj.toml`; pass `--api-key` or set `XERJ_API_KEY`, or every request comes back
`401 Unauthorized`:

```sh
xerj --data-dir ./data &                          # auth on: key minted on first boot
export XERJ_API_KEY="$(cat ./data/admin.key)"     # <data_dir>/admin.key
xerj autoindex ~/my-project
```

That is the whole setup. There is no schema to write and no pipeline to configure. XERJ
sniffs each file, works out what it is, and creates one index per dataset it finds:

```
phase A: 593 datasets inferred, 1955 junk/skipped files
phase B: indexing 25329 files with 8 workers
done in 158.1s, 593 datasets, 83103 records live, 790 junk records
```

Source files go through tree-sitter, so code arrives with its symbols and line numbers
instead of as flat text. CSV, JSON, JSONL, XML, YAML, SQLite, PDF, DOCX, HTML and common log
formats are all handled. Unity projects get first-class treatment: text-serialized scenes,
prefabs and assets become one record per GameObject/Component, `.meta` files become a
GUID-to-path table, and MonoBehaviour records carry `script_class`/`script_path` so "which
scenes use this script?" is a single query (binary-serialized assets need Force Text to be
readable; generated dirs like `Library/` are auto-skipped and recorded).

## Search it

This is the Elasticsearch API, so you already know this part:

```sh
# what did it find?
curl localhost:9200/_cat/indices

# full-text
curl "localhost:9200/ax-*/_search?q=checkout+error"

# structured
curl localhost:9200/ax-orders/_search -H 'content-type: application/json' -d '{
  "query": { "range": { "total": { "gte": 100 } } },
  "aggs":  { "by_status": { "terms": { "field": "status" } } }
}'
```

Vector and hybrid search use the same `knn` and `semantic` syntax you would send to
Elasticsearch. Any Elasticsearch client library works if you point it at `localhost:9200`.

## Connect an agent over MCP

Not every agent can run a shell command. Desktop assistants and function-calling hosts reach
tools through the Model Context Protocol, and the binary you just installed is the MCP
server. There is nothing else to download and nothing to compile:

```sh
xerj --insecure --data-dir ./data &     # 1. the node the tools query
xerj mcp                                # 2. MCP stdio server (your client runs this)
```

`xerj mcp` speaks MCP over stdio and proxies to the node named by `XERJ_URL` (default
`http://localhost:9200`). It does not start a node; step 1 is the prerequisite. Drop this
into your MCP client's config:

```json
{
  "mcpServers": {
    "xerj": {
      "command": "/home/you/.local/bin/xerj",
      "args": ["mcp"],
      "env": { "XERJ_URL": "http://localhost:9200" }
    }
  }
}
```

Use an absolute path. The 

## features

Agents burn their context window reading files. The PHP in WordPress core is about 5.2
million tokens, or 26 full context windows, so an agent cannot simply read it. Grep does not
solve this either, because a grep hit is a line, and judging that line means opening the
whole file.

Querying an index costs kilobytes per question instead. In
[an AI security audit of WordPress core](https://xerj.org/use-cases/code-security-audit.html),
an agent worked across 1,492 PHP files on roughly 26,000 tokens, which is what it takes to
load about half a percent of the tree.

## Use cases

- [Reference coding](https://xerj.org/case-studies/reference-coding.html): your coding agent
  retrieves how peer projects already solved it instead of re-deriving. Measured 2.7x fewer
  output tokens than grep-driven coding (26x vs memory alone); users report ~5x in real
  development.
- [Code search and security audits](https://xerj.org/use-cases/code-security-audit.html):
  AST-aware indexing, so an agent finds a function instead of a line.
- [AI search and RAG](https://xerj.org/use-cases/ai-search-retrieval.html): full-text, vector
  and hybrid retrieval in one query, with no separate vector database.
- [Agent memory](https://xerj.org/use-cases/second-brain.html): durable recall with a
  knowledge graph over your own documents.
- [Log analytics and observability](https://xerj.org/use-cases/unified-observability.html):
  logs, metrics and traces in one engine.
- [Elasticsearch replacement](https://xerj.org/use-cases/elasticsearch-replacement.html):
  same wire protocol, one binary.

Runnable examples live in [`recipes/`](./recipes) and [`docs/examples/`](./docs/examples).

## Elasticsearch compatibility

XERJ implements the Elasticsearch REST API: indices, documents, bulk, search, aggregations,
mappings, kNN, scroll, reindex and the `_cat` endpoints. Kibana and the official client
libraries connect to it directly. One boundary worth knowing before you point export tooling
at it: scroll is a bounded up-front snapshot, not a segment-walking cursor, so a query whose
exact total exceeds the snapshot window is refused with a `400` rather than silently
truncated. Use `search_after` for result sets of any size
([the cap](https://xerj.org/docs/api-es-compat.html#scroll-cap)).

The conformance suite runs on every commit and currently passes 1366 of 1369 cases. It lives
in [`engine/tests/es-compat-yaml`](./engine/tests/es-compat-yaml), and the remaining gaps are
listed there rather than hidden. XERJ is compatible with the API. It is not a
reimplementation of Elasticsearch internals, and it is not a fork.

## Benchmarks

XERJ is benchmarked head to head against Elasticsearch 8.13.4 across ingest, full-text
search, aggregations, vector search, and reads issued under a concurrent write flood. The
latest closed-loop run scores 55 wins, 26 ties, 4 losses, including 1.72x ingest throughput
and a 1.61x smaller on-disk footprint.

All four losses are the same gap: read p99 while a high-rate writer runs. It is
[written up in full](./demo/playbooks/MIXED_READ_UNDER_WRITE_FINDING_2026-07-08.md) rather
than left out. Results, methodology and the harness are at
[xerj.org/benchmarks](https://xerj.org/benchmarks) and in
[`demo/playbooks`](./demo/playbooks), so you can rerun them yourself. Treat any number you
cannot reproduce with skepticism, including ours.

## Build from source

You need a stable Rust toolchain.

```sh
git clone https://github.com/xerj-org/xerj
cd xerj/engine
cargo build --release -p xerj-server
./target/release/xerj --insecure --data-dir ./data
```

To run the conformance suite against a running server:

```sh
cargo run --release -p es-yaml-runner -- --dir tests/es-compat-yaml/yaml
```

## Documentation

- [Guides and API reference](https://xerj.org/docs/)
- [Recipes](https://xerj.org/recipes) for common tasks
- [Roadmap](./ROADMAP.md): what ships today versus what is coming, verified against the
  release binary. Release-by-release view:
  [milestones](https
