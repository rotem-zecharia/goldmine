# genomoncology/biomcp

BioMCP: Biomedical Model Context Protocol

## features

- **Search the literature:** `search article` fans out across PubTator3 and
  Europe PMC, deduplicates PMID/PMCID/DOI identifiers, and can add a Semantic
  Scholar leg when your filters support it.
- **Pivot without rework:** move from a gene, variant, drug, disease, pathway,
  protein, or article straight into the next built-in view instead of
  rebuilding filters by hand.
- **Choose a playbook:** `biomcp skill list` shows shipped worked examples
  so you can open the matching `biomcp skill <slug>` workflow.
- **Analyze studies locally:** `study` commands cover local query, cohort, survival,
  compare, and co-occurrence workflows with native terminal, SVG, and PNG
  charts for downloaded cBioPortal-style datasets.
- **Follow the paper trail:** `article citations`, `article references`,
  `article recommendations`, and `article entities` turn one known paper into a
  broader evidence map.
- **Enrich and batch:** use `biomcp enrich` for top-level g:Profiler
  enrichment and `biomcp batch` for up to 10 focused `get` calls in one
  command.

## installation

First useful query in under 30 seconds:

```bash
uv tool install biomcp-cli
biomcp health --apis-only
biomcp skill list
biomcp list gene
biomcp search all --gene BRAF --disease melanoma  # unified cross-entity discovery
biomcp get gene BRAF pathways hpa
```

## Installation

### Binary install

```bash
curl -fsSL https://biomcp.org/install.sh | bash
```

### PyPI tool install

```bash
uv tool install biomcp-cli
# or: pip install biomcp-cli
```

> **PyPI package warning:** install `biomcp-cli`, not `biomcp`. The `biomcp`
> PyPI package is unrelated to this project.

MCP Registry ownership marker: `mcp-name: io.github.genomoncology/biomcp`.

This installs the `biomcp` binary in `~/.local/bin`. If that directory is not
already on `PATH`, the installer prints one command to add it; it never edits
your shell startup files.

### Homebrew

```bash
brew tap genomoncology/biomcp
brew install biomcp
```

The separate `genomoncology/homebrew-biomcp` tap repository must exist before these commands can work.

### Docker

```bash
docker run --rm ghcr.io/genomoncology/biomcp --version
docker run --rm ghcr.io/genomoncology/biomcp list
docker run --rm -i ghcr.io/genomoncology/biomcp serve
```

Use the GHCR image for quick CLI checks or stdio MCP clients without a local install.

### Claude Code plugin

Install the `biomcp` binary first, then add the hosted plugin marketplace and
install the BioMCP plugin in Claude Code:

```text
/plugin marketplace add genomoncology/biomcp
/plugin install biomcp@biomcp
```

The plugin wires Claude Code to the local stdio MCP server with `biomcp serve`.
For guided BioMCP workflows, also install the skill assets below.

### Codex MCP server

Install the `biomcp` binary first, then register the same stdio MCP server with
Codex:

```bash
codex mcp add biomcp -- biomcp serve
```

### Claude Desktop extension (.mcpb)

Install BioMCP from the Anthropic Directory in Claude Desktop when that path is
available for your environment. For local/manual setups, use the JSON MCP
config below.

### Install skills

Install guided investigation workflows into your agent directory:

```bash
biomcp skill install ~/.claude --force
```

### MCP clients

```json
{
  "mcpServers": {
    "biomcp": {
      "command": "biomcp",
      "args": ["serve"]
    }
  }
}
```

### Remote HTTP server

For shared or remote deployments:

```bash
biomcp serve-http --host 127.0.0.1 --port 8080
```

Remote clients connect to `http://127.0.0.1:8080/mcp`. Probe routes are
`GET /health`, `GET /readyz`, and `GET /`.

Runnable demo:

```bash
uv run --script examples/streamable-http/streamable_http_client.py
```

See [Remote HTTP Server](https://biomcp.org/getting-started/remote-http/) for
the newcomer guide.

### From source

```bash
make install
"$HOME/.local/bin/biomcp" --version
```

For repo-local verification, run the standard gates directly: `make lint`,
`make test`, and `make spec`. `make test` includes both Rust nextest and the
Python/docs contract lane, while `make release-gate` adds the named full-feature
proof and runs specs against the all-feature release binary.
There is no supported `make check` command. Use `make verify` only for opt-in
live public-upstream confidence; `make release-live-smoke` remains a
compatibility alias.

## Command grammar

```text
search <entity> [filters]    → discovery
skill list                   → playbook catalog for how-to questions
discover <query>             → concept resolution before entity selection
get <entity> <id> [sections] → focused detail
<entity> <helper> <id>       → cross-entity pivots
enrich <GENE1,GENE2,...>     → gene-set enrichment
batch <entity> <id1,id2,...> → parallel gets
search all [slot filters]    → counts-first cross-entity orientation
```

## Entities and sources

The tables below distinguish detail-card entities from search-only surfaces so
agents do not synthesize unsupported `get` commands.

### Gettable entities

| Entity | Upstream providers used by BioMCP | Example |
|--------|---

## tools

Most commands work without credentials. Optional keys improve rate limits or
unlock optional enrichments:

```bash
export NCBI_API_KEY="..."        # PubTator, PubMed/efetch, PMC OA, NCBI ID converter
export S2_API_KEY="..."          # Optional Semantic Scholar auth; dedicated quota at 1 req/sec
export OPENFDA_API_KEY="..."     # OpenFDA rate limits
export NCI_API_KEY="..."         # NCI CTS trial search (--source nci)
export ONCOKB_TOKEN="..."        # OncoKB variant helper
export ALPHAGENOME_API_KEY="..." # AlphaGenome variant effect prediction
```

`search article`, `get article`, `article batch`, `get article ... tldr`, and
the explicit Semantic Scholar helpers all work without `S2_API_KEY`. With the
key, BioMCP sends authenticated requests and uses a dedicated rate limit at
1 req/sec. Without it, BioMCP uses the shared unauthenticated pool at 1 req/2sec.
`search article --source` supports `all`, `pubtator`, `europepmc`, `pubmed`,
`semanticscholar`, and `litsense2`. The default compatible article federation
uses PubTator3, Europe PMC, PubMed, and automatic Semantic Scholar; use
`--source semanticscholar` or `--source litsense2` explicitly when you want one
of those sources alone. Explicit source selection also disables cross-provider
row enrichment. References
and recommendations can be empty for paywalled papers because of publisher
elision in Semantic Scholar upstream coverage.

## configuration

### Claude Desktop extension settings

The directory bundle exposes only the optional settings needed for the first
reviewer-facing build:

| Claude Desktop field | Runtime env var | Purpose |
|----------------------|-----------------|---------|
| OncoKB Token | `ONCOKB_TOKEN` | Enables `biomcp variant oncokb "<gene> <variant>"` therapy and level evidence |
| DisGeNET API Key | `DISGENET_API_KEY` | Enables scored DisGeNET sections on gene and disease lookups |
| Semantic Scholar API Key | `S2_API_KEY` | Improves reliability for article TLDR, citation, reference, and recommendation helpers |

The first directory build exposes only those three optional settings. Advanced
CLI-only env vars remain documented in
[API Keys](docs/getting-started/api-keys.md) for the general BioMCP CLI path.
