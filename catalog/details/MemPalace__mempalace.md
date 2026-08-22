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

### Android / Termux

Native Termux installation is not currently supported because compiled
dependencies such as ChromaDB and ONNX Runtime publish Linux wheels, not
Android wheels. Android ARM64 users can run the regular Linux packages in an
isolated Debian PRoot container instead. See the
[Termux installation guide](website/guide/termux.md) for the tested setup and
an argv-preserving launcher.

### Docker

A container image is also available for running the MCP server or the CLI
without a local Python toolchain. Multi-arch (amd64 + arm64), so it runs
natively on Apple Silicon:

```bash
docker pull ghcr.io/mempalace/mempalace:latest
```

Everything persists under `/data` — palace, config, and the cached embedding
model — so mount a volume there and reuse it across runs:

```bash
# MCP server over stdio — note the `-i` flag (JSON-RPC needs stdin)
docker run -i --rm -v mempalace-data:/data ghcr.io/mempalace/mempalace

# Run any CLI command instead. The container only sees what you mount, so
# mount the directory you want to mine — read-only is enough, mining never
# writes to the source.
docker run --rm -v mempalace-data:/data -v /path/to/project:/work:ro \
  ghcr.io/mempalace/mempalace mine /work
docker run --rm -v mempalace-data:/data ghcr.io/mempalace/mempalace search "why GraphQL"
```

The first command that needs embeddings downloads the model into `/data`
(~80 MB for the default `minilm`, ~300 MB for `embeddinggemma`). It is a
one-off as long as the volume persists, but it does mean the first call is
slow and needs network — worth knowing before assuming a hung container.

Wire it into an MCP client (e.g. Claude Code) as a stdio server. Mount
anything you want the server to be able to mine — it cannot reach your
transcripts otherwise:

```json
{
  "mcpServers": {
    "mempalace": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "-v", "mempalace-data:/data",
        "-v", "/absolute/path/to/.claude/projects:/transcripts:ro",
        "ghcr.io/mempalace/mempalace"
      ]
    }
  }
}
```

Use a real absolute path there — `~` and `$HOME` are not expanded by every
MCP client. Paths are container paths from then on: mine `/transcripts`, not
`~/.claude/projects`.

**Mount permissions on Linux.** The image runs as uid 1000 and bind mounts
keep their host ownership, so a mounted directory has to be readable by that
uid — an ordinary `0755` checkout is fine, a `0700` directory is not, and the
failure surfaces as `PermissionError: [Errno 13]` rather than anything about
Docker. Docker Desktop maps uids on macOS and Windows, so this only bites on
Linux. Do **not** work around it with `--user`: `/data` is owned by uid 1000
inside the image, so another uid cannot write the palace at all.

`docker compose run --rm mcp` works too (see `docker-compose.yml`), and
`deploy/docker-compose.server.yml` stands up the team server. To build the
image yourself instead of pulling — required for the GPU variant, which is not
published:

```bash
docker build -t mempalace .                                  # CPU
docker build --build-arg EXTRAS="extract,spellcheck" -t mempalace .
docker build -f Dockerfile.gpu -t mempalace:gpu .            # CUDA; run with --gpus all
```

The GPU imag

## tools

uv run python benchmarks/longmemeval_bench.py /path/to/longmemeval_s_cleaned.json
```

---

## Knowledge graph

MemPalace includes a temporal entity-relationship graph with validity
windows — add, query, invalidate, timeline — backed by local SQLite.
Usage and tool reference:
[mempalaceofficial.com/concepts/knowledge-graph](https://mempalaceofficial.com/concepts/knowledge-graph.html).

## MCP server

44 MCP tools cover palace reads/writes, knowledge-graph operations,
cross-wing navigation, drawer management, agent diaries, and agent
coordination (logstream events + artifact handoffs). Installation
and the full tool list:
[mempalaceofficial.com/reference/mcp-tools](https://mempalaceofficial.com/reference/mcp-tools.html).

## Agents

Each specialist agent gets its own wing and diary in the palace.
Discoverable at runtime via `mempalace_list_agents` — no bloat in your
system prompt:
[mempalaceofficial.com/concepts/agents](https://mempalaceofficial.com/concepts/agents.html).

## Auto-save hooks

Auto-save hooks for **Claude Code, Codex CLI, and Cursor IDE** save
periodically and before context compression:

- Claude Code + Codex →
  [mempalaceofficial.com/guide/hooks](https://mempalaceofficial.com/guide/hooks.html)
- Cursor IDE (adds session-start recall and a transcript snapshot before
  compaction) →
  [mempalaceofficial.com/guide/cursor-hooks](https://mempalaceofficial.com/guide/cursor-hooks.html)

If you are installing under time pressure, start with the
[Claude Code retention setup checklist](https://mempalaceofficial.com/guide/claude-code-retention.html):
wire the hooks, back up existing JSONL transcripts, and backfill them with
`mempalace mine ~/.claude/projects/ --mode convos`.

For per-message recall on top of the file-level chunks the hooks produce,
run `mempalace sweep <transcript-dir>` periodically — it stores one
verbatim drawer per user/assistant message, idempotent and resume-safe.

---

## requirements

- Python 3.9+
- A vector-store backend (ChromaDB by default)
- ~300 MB disk for the embedding model. Onboarding (`python -m mempalace.onboarding`) offers `embeddinggemma-300m` (multilingual, 100+ languages, recommended) or `all-MiniLM-L6-v2` (English-only, ~30 MB). See the docstring at [`mempalace/embedding.py`](mempalace/embedding.py) for details and migration notes.
- Optional — compute embeddings on a server instead of locally. Set `embedding_model: "openai-compat"` in `~/.mempalace/config.json` together with `embedding_api_url` / `embedding_api_model` (and `embedding_api_key` if the server needs auth) to use any OpenAI-compatible `/v1/embeddings` endpoint — LM Studio, llama.cpp, vLLM, Ollama's OpenAI shim, or a self-hosted server (e.g. a larger multilingual or GPU-served embedder). Each key is overridable via the matching `MEMPALACE_EMBEDDING_API_*` env var. When the endpoint is on your machine or LAN, no content leaves your network. Switching to it requires `mempalace repair rebuild-index` (different vector space).

No API key is required for the core benchmark path.

## Docs

- Getting started → [mempalaceofficial.com/guide/getting-started](https://mempalaceofficial.com/guide/getting-started.html)
- CLI reference → [mempalaceofficial.com/reference/cli](https://mempalaceofficial.com/reference/cli.html)
- Python API → [mempalaceofficial.com/reference/python-api](https://mempalaceofficial.com/reference/python-api.html)
- Full benchmark methodology → [benchmarks/BENCHMARKS.md](benchmarks/BENCHMARKS.md)
- Release notes → [CHANGELOG.md](CHANGELOG.md)
- Corrections and public notices → [docs/HISTORY.md](docs/HISTORY.md)

## Contributing

PRs welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT — see [LICENSE](LICENSE).

<!-- Link Definitions -->
[version-shield]: https://img.shields.io/badge/version-3.8.0-4dc9f6?style=flat-square&labelColor=0a0e14
[release-link]: https://github.com/MemPalace/mempalace/releases
[python-shield]: https://img.shields.io/badge/python-3.9+-7dd8f8?style=flat-square&labelColor=0a0e14&logo=python&logoColor=7dd8f8
[python-link]: https://www.python.org/
[license-shield]: https://img.shields.io/badge/license-MIT-b0e8ff?style=flat-square&labelColor=0a0e14
[license-link]: https://github.com/MemPalace/mempalace/blob/main/LICENSE
[discord-shield]: https://img.shields.io/badge/discord-join-5865F2?style=flat-square&labelColor=0a0e14&logo=discord&logoColor=5865F2
[discord-link]: https://discord.com/invite/ycTQQCu6kn
