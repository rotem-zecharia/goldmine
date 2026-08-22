# 54yyyu/zotero-mcp

Zotero MCP: Connects your Zotero research library with Claude and other AI assistants via the Model Context Protocol to discuss papers, get summaries, analyze citations, and more.

## features

### 🧠 AI-Powered Semantic Search
- **Vector-based similarity search** over your entire research library (requires `[semantic]` extra)
- **Multiple embedding models**: Default (free, local), OpenAI, Gemini, and Ollama
- **Intelligent results** with similarity scores and contextual matching
- **Auto-updating database** with configurable sync schedules

### 🔍 Search Your Library
- Find papers, articles, and books by title, author, or content
- Perform complex searches with multiple criteria
- Browse collections, tags, and recent additions
- Semantic search for conceptual and topic-based discovery

### 📚 Access Your Content
- Retrieve detailed metadata for any item (markdown or BibTeX export)
- Get full text content (when available)
- Look up items by BetterBibTeX citation key

### 📝 Work with Annotations
- Extract and search PDF annotations with page numbers
- Access Zotero's native annotations
- Create and update notes and annotations
- Extract PDF table of contents / outlines (requires `[pdf]` extra)

### ✏️ Write Operations
- **Add papers by DOI** with auto-fetched metadata and open-access PDF cascade (Unpaywall, arXiv, Semantic Scholar, PMC)
- **Add papers by URL** (arXiv, DOI links, generic webpages) or from local files
- Create and manage collections, update item metadata, batch-update tags
- Find and merge duplicate items with dry-run preview
- **Hybrid mode**: local reads + web API writes for local-mode users

### 📊 Scite Citation Intelligence (optional `[scite]` extra)
- **Citation tallies**: See how many papers support, contrast, or mention each item — the MCP version of the [Scite Zotero Plugin](https://github.com/scitedotai/scite-zotero-plugin)
- **Retraction alerts**: Scan your library for retracted or corrected papers
- No Scite account required — uses public API endpoints

### 🌐 Flexible Access Methods
- Local mode for offline access (no API key needed)
- Web API for cloud library access
- Hybrid mode: read from local Zotero, write via web API

### ⌨️ Standalone CLI (`zotero-cli`)
- Search, browse, and edit your library directly from the terminal — no AI assistant required
- Ideal for scripting, automation, and quick lookups
- Short aliases (`s`, `g`, `ann`, `coll`) for interactive use

## installation

> **New to the command line?** Try the community-built [Zotero MCP Setup](https://github.com/ehawkin/zotero-mcp-setup) — includes a macOS GUI installer (DMG), one-click install scripts for Mac/Windows, and a step-by-step guide. No Terminal experience needed.

### Default Installation (core tools only)

The base install is lightweight — it includes search, metadata retrieval, annotations, and write operations. No ML/AI dependencies are pulled in.

#### Installing via uv (recommended)

```bash
uv tool install zotero-mcp-server
zotero-mcp setup  # Auto-configure (Claude Desktop supported)
```

#### Installing via pip

```bash
pip install zotero-mcp-server
zotero-mcp setup  # Auto-configure (Claude Desktop supported)
```

#### Installing via pipx

```bash
pipx install zotero-mcp-server
zotero-mcp setup  # Auto-configure (Claude Desktop supported)
```

### Optional Extras

Heavy ML/PDF dependencies are separated into optional extras so the base install stays fast and small:

| Extra | What it adds | Install command |
|-------|-------------|-----------------|
| `semantic` | Semantic search via ChromaDB, sentence-transformers, OpenAI/Gemini embeddings | `pip install "zotero-mcp-server[semantic]"` |
| `pdf` | PDF outline extraction (PyMuPDF) and EPUB annotation support | `pip install "zotero-mcp-server[pdf]"` |
| `scite` | [Scite](https://scite.ai) citation intelligence — tallies and retraction alerts (no account needed) | `pip install "zotero-mcp-server[scite]"` |
| `all` | Everything above | `pip install "zotero-mcp-server[all]"` |

For example, with uv:
```bash
uv tool install "zotero-mcp-server[all]"    # Full install with all features
uv tool install "zotero-mcp-server[semantic]" # Just semantic search
```

If you only need basic library access (search, read, annotate, write), the default install with no extras is all you need.

#### Updating Your Installation

Keep zotero-mcp up to date with the smart update command:

```bash
# Check for updates
zotero-mcp update --check-only

## configuration

zotero-mcp update
```

## 🧠 Semantic Search

Zotero MCP now includes powerful AI-powered semantic search capabilities that let you find research based on concepts and meaning, not just keywords.

## tools

zotero-mcp update-db --openai-batch

# Check and import completed OpenAI Batch API embeddings
zotero-mcp openai-batch-status
zotero-mcp openai-batch-import

# Force realtime OpenAI embeddings even if Batch API is enabled in config
zotero-mcp update-db --no-openai-batch

# Build with full-text extraction (slower, more comprehensive)
zotero-mcp update-db --fulltext

# Use your custom zotero.sqlite path
zotero-mcp update-db --fulltext --db-path "/Your_custom_path/zotero.sqlite"

# If you have embedding conflicts or changed models, force a rebuild
zotero-mcp update-db --force-rebuild

# Check database status
zotero-mcp db-status
```

**Example Semantic Queries in your AI assistant:**
- *"Find research similar to machine learning concepts in neuroscience"*
- *"Papers that discuss climate change impacts on agriculture"*
- *"Research related to quantum computing applications"*
- *"Studies about social media influence on mental health"*
- *"Find papers conceptually similar to this abstract: [paste abstract]"*

The semantic search provides similarity scores and finds papers based on conceptual understanding, not just keyword matching.

### Text Extraction Settings

PDFs are parsed with [pdf-inspector](https://github.com/firecrawl/pdf-inspector), which produces Markdown with the document's heading structure intact. These keys live under `semantic_search.extraction` in `~/.config/zotero-mcp/config.json`:

```json
{
  "semantic_search": {
    "extraction": {
      "pdf_max_pages": 50,
      "fulltext_display_max_pages": 10,
      "attachment_priority": ["markdown", "pdf", "html", "other"]
    }
  }
}
```

| Key | Default | What it does |
|---|---|---|
| `pdf_max_pages` | `50` | Pages extracted per PDF when indexing. Raising it does not widen what search sees on its own — that is bounded by the embedding model's token limit or `chunking.max_chunks_per_item`. |
| `fulltext_display_max_pages` | `10` | Pages returned by `zotero_get_item_fulltext`. Separate from the above because reading a paper is bounded by your assistant's context, not by recall. |
| `attachment_priority` | `["pdf", "html", "other"]` | Order in which attachment kinds are tried when an item has several readable files. |

**`attachment_priority`** exists for the case where you have converted a paper to clean Markdown yourself and attached it next to the original PDF. By default the PDF still wins; listing `"markdown"` first makes your converted copy the one that gets read and indexed. Valid entries are `pdf`, `html`, `markdown`, `text` and `other`. `other` is a catch-all matching every kind not named elsewhere in the list, so the default sweeps Markdown and plain text into one bucket where the larger file wins. Omitting `other` means anything unlisted is never chosen.

Changing this setting marks affected items for re-extraction, so a following `zotero-mcp update-db` refreshes text that came from a now-deprioritized attachment rather than leaving stale embeddings behind.

To read one specific attachment regardless of priority, pass that attachment's own key to `zotero_get_item_fulltext` (find it with `zotero_get_item_children`) — an attachment key bypasses the priority order and reads exactly that file.
