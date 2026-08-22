# RobThePCGuy/Claude-Patent-Creator

USPTO patent creation system with MCP server + Claude Code plugin. Hybrid RAG search over MPEP/USC/CFR, BigQuery access to 76M+ patents, automated 35 USC 112 compliance checks, prior art search, diagr

## installation

Never used Claude Code? It's Anthropic's AI assistant that runs in a terminal or as a desktop app — [install it first](https://claude.com/claude-code) (a paid Claude subscription is the only cost to start). Then come back here; setup is one command and the tool talks you through the rest.

Pick the path that fits your setup. All three get you to the same place.

## configuration

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

pip install -e .
patent-creator setup
```

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

## requirements

This project builds on excellent open source work: [FastMCP](https://github.com/jlowin/fastmcp), [FAISS](https://github.com/facebookresearch/faiss) (Meta AI Research), [Sentence Transformers](https://www.sbert.net/) (UKP Lab), [HuggingFace Transformers](https://huggingface.co/transformers/), [PyTorch](https://pytorch.org/), [rank-bm25](https://github.com/dorianbrown/rank-bm25), [PyMuPDF](https://pymupdf.readthedocs.io/), [Graphviz](https://graphviz.org/), [Pydantic](https://docs.pydantic.dev/), and [Google Cloud BigQuery](https://cloud.google.com/bigquery).
