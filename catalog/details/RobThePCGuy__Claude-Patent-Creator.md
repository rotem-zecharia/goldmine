# RobThePCGuy/Claude-Patent-Creator

USPTO patent creation system with MCP server + Claude Code plugin. Hybrid RAG search over MPEP/USC/CFR, BigQuery access to 76M+ patents, automated 35 USC 112 compliance checks, prior art search, diagr

## installation

Never used Claude Code? It's Anthropic's AI assistant that runs in a terminal or as a desktop app — [install it first](https://claude.com/claude-code) (a paid Claude subscription is the only cost to start). Then come back here; setup is one command and the tool talks you through the rest.

Pick the path that fits your setup. All three get you to the same place.

### Option A: Claude Code Plugin (Easiest)

If you're already using Claude Code, this is the fastest way in:

```bash
# Add the marketplace and install
/plugin marketplace add RobThePCGuy/Claude-Patent-Creator
/plugin install claude-patent-creator-standalone@claude-patent-creator

# Run setup
/claude-patent-creator-standalone:setup-patent-system
```

### Option B: One-Line Install

```bash
pip install git+https://github.com/RobThePCGuy/Claude-Patent-Creator.git && patent-creator setup
```

This handles everything automatically: installs dependencies, detects your GPU, downloads MPEP PDFs (~500MB), builds the search index, and registers the MCP server with Claude Code. Restart Claude Code when it finishes.

### Option C: Manual Install

```bash
git clone https://github.com/RobThePCGuy/Claude-Patent-Creator.git
cd Claude-Patent-Creator

## configuration

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

pip install -e .
patent-creator setup
```

### Verify It Worked

After any install path, run:

```bash
patent-creator health
```

You should see a status report showing which components are ready. If something's off, the output will tell you what to fix.

---

## What Can I Actually Do With This?

Here are some real examples. You can type these directly in Claude Code and the right skill or tool kicks in automatically. Say it in your own words — the "what to say" column is a starting point, not a required incantation.

| What you want to do | What to say | What happens |
|---|---|---|
| Find out if a rule applies to you | "Search MPEP for claim definiteness requirements" — or just "do my claims have to be written a certain way?" | The tool searches the examiner's rulebook and returns the relevant sections, with citations you can read yourself |
| See if your idea already exists | "Search for patents about [your idea]" — e.g. "self-heating coffee mug" | Searches 100M+ existing patents and shows you the closest matches, so you know what you're up against |
| Get your draft claims checked | "Review these claims" (paste them in) | Flags unclear wording, terms used before they're introduced, and structural problems — the mechanical mistakes an examiner rejects first |
| Check a whole application | `/full-review` | Runs the claims, description, and formatting checks together and reports everything at once |
| Go from idea to draft application | `/create-patent` | A guided workflow: describe the invention, the tool searches prior art, drafts, checks, and assembles a reviewable package (typically about an hour) |
| Make a drawing | "Create a block diagram showing [your system]" | Produces a patent-style figure, no design software needed |
| Dig deep on whether your idea is new | "Conduct a prior art search for [your invention]" | A thorough multi-angle hunt through existing patents, with an honest verdict on what it found |

---

## How It Works

*Everything from here down gets progressively more technical. You do not need any of it to use the tool — the sections above plus the [Glossary](#glossary) are enough. This part is for developers, patent professionals, and the curious.*

The system has two modes that can work independently or together:

**MCP Server** is the engine. It exposes 20+ tools that any MCP-compatible client (Claude Code, Claude Desktop, etc.) can call programmatically. These tools handle search, analysis, and diagram generation.

**Claude Code Plugin** adds the interactive layer. Skills activate automatically based on what you're doing. Agents handle long-running tasks in the background. Slash commands give you quick access to common workflows.

Under the hood, patent regulation search uses a hybrid approach: FAISS vector search finds semantically similar content, BM25 lexical search catches exact terminology matches, and a cross-encoder reranker sorts the combined results by relevance. Patent search goes through Google BigQuery's public patent dataset.

```
You (Claude Code) ──> MCP Server ──> Search / Analysis / Diagrams
                           │
            ┌──────────────┼──────────────┐
            v              v              v
     MPEP/USC/CFR     BigQuery        Graphviz
     (hybrid RAG)    (100M+ patents)   (diagrams)
```

---

## tools

```bash
patent-creator setup             # Full setup wizard (downloads, builds index, registers MCP)
patent-creator health            # System health check (shows what's working and what isn't)
patent-creator status            # Same as health
patent-creator verify-config     # Check Claude Code MCP configuration
patent-creator serve             # Run the MCP server manually
patent-creator rebuild-index     # Rebuild the MPEP search index
patent-creator download-mpep     # Download MPEP PDFs only
patent-creator download-all      # Download all sources (MPEP + 35 USC + 37 CFR)
patent-creator check-bigquery    # Test BigQuery connection
```

---

## MCP Tools Reference

### Search

| Tool | What it does |
|---|---|
| `search_mpep` | Hybrid RAG search across MPEP, 35 USC, and 37 CFR with filters |
| `get_mpep_section` | Pull full content of a specific MPEP section |
| `search_patents_bigquery` | Search 100M+ patents by keyword |
| `get_patent_bigquery` | Get full details on a specific patent |
| `search_patents_by_cpc_bigquery` | Search by CPC classification code |
| `search_uspto_api` | Search via the USPTO API |
| `get_uspto_patent` | Get patent details from USPTO |
| `get_recent_uspto_patents` | Pull recent filings |

### Getting the campaign workflow (skills)

The MCP server above gives Claude the TOOLS. The campaign workflow — the
skill that runs mining, prior art, worth-it economics, drafting, and the
red teams end to end — ships as a Claude Code plugin. Two commands:

```bash
claude plugin marketplace add RobThePCGuy/Claude-Patent-Creator
claude plugin install claude-patent-creator-standalone@claude-patent-creator
```

Re-run the install command after upgrades to refresh the skills.

### Analysis

| Tool | What it does |
|---|---|
| `review_patent_claims` | 35 USC 112(b) compliance check (definiteness, antecedent basis, structure) |
| `review_specification` | 35 USC 112(a) adequacy check (written description, enablement, best mode) |
| `check_formalities` | MPEP 608 compliance (abstract, title, drawings, required sections) |
| `check_package` | Whole-package consistency: stale verification stamps, claim-count disagreements, status contradictions, commentary inside filing copies, date errors |

### Generation

| Tool | What it does |
|---|---|
| `render_diagram` | Generate patent-style diagrams from Graphviz DOT code |
| `create_flowchart` | Build a flowchart from a list of steps and connections |
| `create_block_diagram` | Build a block diagram from components and relationships |
| `add_diagram_references` | Add patent reference numbers to an existing SVG diagram |
| `get_diagram_templates` | List available diagram templates |

### System

| Tool | What it does |
|---|---|
| `get_index_stats` | Search index statistics |
| `check_bigquery_status` | BigQuery configuration status |
| `check_diagram_tools_status` | Graphviz availability |
| `check_uspto_api_status` | USPTO API connectivity |
| `get_patent_details` | Combined patent retrieval across sources |

---

## Skills, Agents, and Slash Commands

### Skills (activate automatically)

You don't need to call these directly. Just describe what you want to do and the right skill kicks in.

| Skill | When it activates | What it brings |
|---|---|---|
| **setup-assistant** | Installing, configuring, or troubleshooting | Full setup lifecycle guidance |
| **patent-reviewer** | Reviewing a complete application for compliance | Comprehensive review (claims + spec + formalities) |
| **patent-claims-analyzer** | Reviewing claims specifically for 35 USC 112(b) | Deep-dive claims analysis (definiteness, antecedent basis, structure) |
| **patent-search** | Searching patents or prior art | BigQuery search workflows via the MCP tools |
| **bigquery-patent-search** | Quick BigQuery-only patent search | Keyword, CPC, and patent detail retrieval across 100M+ patents |
| **mpep-search** | Finding MPEP sections or regulations | Hybrid RAG search |
| **patent-diagram-generator** | Creating tec

## requirements

### Minimum

- **Python:** 3.9 - 3.13 (3.14 is experimental)
- **RAM:** 8GB
- **Disk:** ~2GB (MPEP PDFs + search index)

### Optional (but recommended)

- **GPU:** NVIDIA with CUDA 12.8 (makes indexing 5-10x faster) or Apple Silicon (2-3x faster)
- **Google Cloud:** Project with BigQuery enabled (for patent search)
- **Graphviz:** System package (for diagram generation)

<details>
<summary><strong>Full dependency list</strong></summary>

| Package | Version | Purpose |
|---|---|---|
| mcp | >=1.21.0 | MCP server framework |
| sentence-transformers | >=5.1.2, <6.0.0 | Text embeddings |
| faiss-cpu | >=1.13.2 | Vector similarity search |
| numpy | >=1.26.0, <3.0.0 | Array operations |
| rank-bm25 | >=0.2.2 | Lexical search |
| transformers | >=4.57.6, <5.0.0 | HuggingFace models |
| google-cloud-bigquery | >=3.41.0 | Patent search |
| pydantic | >=2.12.5 | Data validation |
| graphviz | >=0.21 | Diagram generation |
| PyMuPDF | >=1.26.0 | PDF processing |

See `pyproject.toml` for the complete list.

</details>

---

## Architecture

```
claude-patent-creator/
├── .claude-plugin/          # Plugin manifest and marketplace config
├── mcp_server/              # Core MCP server
│   ├── server.py            # FastMCP entry point
│   ├── mpep_search.py       # Hybrid RAG search engine
│   ├── bigquery_search.py   # BigQuery patent search
│   ├── claims_analyzer.py   # 35 USC 112(b) analyzer
│   ├── specification_analyzer.py  # 112(a) analyzer
│   ├── formalities_checker.py     # MPEP 608 checker
│   ├── diagram_generator.py       # Graphviz diagrams
│   ├── tools/               # MCP tool definitions
│   └── index/               # FAISS + BM25 index (git-ignored)
├── skills/                  # Claude Code skills (13)
├── agents/                  # Autonomous agents (10)
├── commands/                # Slash commands (11)
├── hooks/                   # Event-driven automation
├── scripts/                 # Testing and utilities
├── docs/                    # Additional documentation
├── pdfs/                    # Downloaded MPEP PDFs (git-ignored)
└── CLAUDE.md                # Full project documentation
```

For the complete architecture documentation, development workflows, and troubleshooting guides, see [CLAUDE.md](CLAUDE.md).

---

## Performance

| Operation | Time | Notes |
|---|---|---|
| **MPEP Search** | 50-200ms | Hybrid FAISS + BM25 |
| **BigQuery Patent Search** | 1-3 sec | 100M+ patents |
| **USPTO API** | 500ms - 2s | Rate-limited by USPTO |
| **Index Build (GPU)** | 3-5 min | NVIDIA CUDA 12.8 |
| **Index Build (Apple Silicon)** | 8-12 min | MPS acceleration |
| **Index Build (CPU)** | 25-35 min | No GPU |

Resource usage: the loaded search index takes about 2-4GB of RAM and the index files are 500MB-1GB on disk. If you have a GPU, it'll use 1-2GB of VRAM for acceleration.

---

## limitations

> **This project is a work in progress.** Most features work, but expect some rough edges. Contributions, issues, and PRs are welcome.

Things to be aware of:

- **PyTorch install order matters.** Install PyTorch before `sentence-transformers`, or you'll end up with CPU-only PyTorch even on a GPU system. The setup wizard handles this, but it can bite you on manual installs.
- **BigQuery requires a Google Cloud project** with billing enabled. The patent data itself is free to query within the BigQuery free tier.
- **Some diagram types need Graphviz installed** as a system package (not just the Python bindings).
- **HyDE query expansion requires API keys** (Anthropic or OpenAI). It's optional and off by default.
- **Windows users need Git Bash** for the `claude mcp add` command. See [Windows setup notes](#configuration).

See [CLAUDE.md](CLAUDE.md) for the full troubleshooting guide.

---

## Glossary

If you're coming from the development side and patent terminology is new (or vice versa), here's a quick reference:

| Term | What it means |
|---|---|
| **MPEP** | Manual of Patent Examining Procedure. The handbook patent examiners use at the USPTO. Think of it as the rulebook. |
| **35 USC** | Title 35 of the United States Code. The federal patent statutes. |
| **37 CFR** | Title 37 of the Code of Federal Regulations. The rules that implement the patent statutes. |
| **USPTO** | United States Patent and Trademark Office. The agency that grants patents. |
| **CPC** | Cooperative Patent Classification. A system for categorizing patents by technology area. |
| **Prior Art** | Anything publicly available before your filing date that's relevant to your invention. Finding it is how you figure out if your idea is actually new. |
| **112(a)** | The section of patent law requiring your application to fully describe and enable the invention. |
| **112(b)** | The section requiring your claims to be definite and clear. |
| **MPEP 608** | The section covering formalities like abstract length, title format, and drawing requirements. |
| **RAG** | Retrieval Augmented Generation. Instead of relying only on what the AI was trained on, it searches a database first and uses those results to give a better answer. |
| **FAISS** | Facebook AI Similarity Search. A fast way to find similar text by comparing mathematical representations of meaning. |
| **BM25** | A text search algorithm that matches exact words and phrases. Works alongside FAISS to catch things vector search might miss. |
| **MCP** | Model Context Protocol. A standard for connecting AI tools to AI models. It's how this system talks to Claude. |
| **IDS** | Information Disclosure Statement. A form listing prior art references you need to disclose to the USPTO. |

---

## Roadmap

- [x] Support for international patent offices (EPO, WIPO/PCT)
- [ ] Web interface for non-Claude Code users
- [ ] Claim dependency graph visualization
- [ ] Automated obviousness analysis (35 USC 103)
- [ ] Patent portfolio analysis tools
- [ ] Integration with patent drafting software

---

## Contributing

This project is open to contributions. Since it's a work in progress, expect breaking changes and incomplete documentation. Issues and PRs are welcome.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the development setup, branch naming, commit conventions, and code style guide.

---

## Credits
