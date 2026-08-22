# zilliztech/memsearch

A persistent, unified memory layer for all your AI agents (e.g. Claude Code, Codex), backed by Markdown and Milvus.

## features

- 🌐 **All Platforms, One Memory** — memories flow across [Claude Code](plugins/claude-code/README.md), [OpenClaw](plugins/openclaw/README.md), [OpenCode](plugins/opencode/README.md), and [Codex CLI](plugins/codex/README.md). A conversation in one agent becomes searchable context in all others — no extra setup
- 👥 **For Agent Users**, install a plugin and get persistent memory with zero effort; **for Agent Developers**, use the full [CLI](https://zilliztech.github.io/memsearch/cli/) and [Python API](https://zilliztech.github.io/memsearch/python-api/) to build memory and harness engineering into your own agents
- 📄 **Markdown is the source of truth** — inspired by [OpenClaw](https://github.com/openclaw/openclaw). Your memories are just `.md` files — human-readable, editable, version-controllable. Milvus is a "shadow index": a derived, rebuildable cache
- 🔍 **Progressive retrieval, hybrid search, smart dedup, live sync** — 3-layer recall (search → expand → transcript); dense vector + BM25 sparse + RRF reranking; SHA-256 content hashing skips unchanged content; file watcher auto-indexes in real time

---

## installation

/plugin marketplace add zilliztech/memsearch
/plugin install memsearch

## configuration

All plugins share the same memsearch backend. Configure once, works everywhere.

#### Embedding

Defaults to **ONNX bge-m3** — runs locally on CPU, no API key, no cost. On first launch the model (~558 MB) is downloaded from HuggingFace Hub.

```bash
memsearch config set embedding.provider onnx     # default — local, free
memsearch config set embedding.provider openai   # needs OPENAI_API_KEY
memsearch config set embedding.provider ollama   # local, any model
```

> All providers and models: [Configuration — Embedding Provider](https://zilliztech.github.io/memsearch/home/configuration/#embedding-provider)

#### Milvus Backend

Just change `milvus_uri` (and optionally `milvus_token`) to switch between deployment modes:

**Milvus Lite** (default) — zero config, single file. Great for getting started:

```bash

## tools

uv tool install "memsearch[onnx]"
pipx install "memsearch[onnx]"
pip install "memsearch[onnx]"
