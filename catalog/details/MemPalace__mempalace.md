# MemPalace/mempalace

The best-benchmarked open-source AI memory system. And it's free.

## installation

MemPalace ships a CLI, so install it in an isolated environment to avoid
PEP 668 errors on Debian/Ubuntu/Homebrew Pythons and to keep mempalace's
deps (`chromadb`, `numpy`, `grpcio`, …) from conflicting with anything
else in your global site-packages.

We recommend [`uv`](https://docs.astral.sh/uv/) — `uv tool install` puts
the `mempalace` CLI in an isolated environment on your PATH:

```bash
uv tool install mempalace
mempalace init ~/projects/myapp
```

[`pipx`](https://pipx.pypa.io/) works the same way if you prefer it:
`pipx install mempalace`.

Prefer plain `pip` only inside an activated virtualenv where you
explicitly want `import mempalace` available:

```bash
python -m venv .venv && source .venv/bin/activate
pip install mempalace
```

## tools

uv run python benchmarks/longmemeval_bench.py /path/to/longmemeval_s_cleaned.json
```

---

## requirements

- Python 3.9+
- A vector-store backend (ChromaDB by default)
- ~300 MB disk for the embedding model. Onboarding (`python -m mempalace.onboarding`) offers `embeddinggemma-300m` (multilingual, 100+ languages, recommended) or `all-MiniLM-L6-v2` (English-only, ~30 MB). See the docstring at [`mempalace/embedding.py`](mempalace/embedding.py) for details and migration notes.
- Optional — compute embeddings on a server instead of locally. Set `embedding_model: "openai-compat"` in `~/.mempalace/config.json` together with `embedding_api_url` / `embedding_api_model` (and `embedding_api_key` if the server needs auth) to use any OpenAI-compatible `/v1/embeddings` endpoint — LM Studio, llama.cpp, vLLM, Ollama's OpenAI shim, or a self-hosted server (e.g. a larger multilingual or GPU-served embedder). Each key is overridable via the matching `MEMPALACE_EMBEDDING_API_*` env var. When the endpoint is on your machine or LAN, no content leaves your network. Switching to it requires `mempalace repair rebuild-index` (different vector space).

No API key is required for the core benchmark path.
