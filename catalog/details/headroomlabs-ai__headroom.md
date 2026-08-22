# headroomlabs-ai/headroom

Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.

## features

- **Library** — `compress(messages)` in Python or TypeScript, inline in any app
- **Proxy** — `headroom proxy --port 8787`, zero code changes, any language
- **Agent wrap** — `headroom wrap claude|codex|grok|copilot|cursor|aider|opencode|cline|continue|goose|openhands|openclaw|vibe|omp|zcode` in one command; undo with `headroom unwrap <tool>`
- **MCP server** — `headroom_compress`, `headroom_retrieve`, `headroom_stats` for any MCP client
- **Cross-agent memory** — shared store across Claude, Codex, Gemini, Grok, auto-dedup
- **`headroom learn`** — mines failed sessions, writes corrections to `CLAUDE.local.md` (default, gitignored) or `CLAUDE.md` / `AGENTS.md` / `GEMINI.md` / `GROK.md`
- **Output token reduction** — trims what the model *writes back* (not just what you send): drops ceremony/restated code and skips deep "thinking" on routine steps. See [Output token reduction](#output-token-reduction-cut-what-the-model-writes-back).
- **Reversible (CCR)** — originals are cached for retrieval on demand

## How it works (30 seconds)

```
 Your agent / app
   (Claude Code, Cursor, Codex, LangChain, Agno, Strands, your own code…)
        │   prompts · tool outputs · logs · RAG results · files
        ▼
    ┌────────────────────────────────────────────────────┐
    │  Headroom   (runs locally — your data stays here)  │
    │  ────────────────────────────────────────────────  │
    │  CacheAligner  →  ContentRouter  →  CCR            │
    │                    ├─ SmartCrusher   (JSON)        │
    │                    ├─ CodeCompressor (AST)         │
    │                    └─ Kompress-v2-base (text, HF)  │
    │                                                    │
    │  Cross-agent memory  ·  headroom learn  ·  MCP     │
    └────────────────────────────────────────────────────┘
        │   compressed prompt  +  retrieval tool
        ▼
 LLM provider  (Anthropic · OpenAI · Bedrock · …)
```

- **ContentRouter** — detects content type, selects the right compressor
- **SmartCrusher / CodeCompressor / Kompress-v2-base** — compress JSON, AST, or prose
- **CacheAligner** - detects and warns about volatile content that can bust provider KV cache prefixes; never rewrites prompts
- **CCR** — stores originals locally; LLM calls `headroom_retrieve` if it needs them

→ [Architecture](https://headroom-docs.vercel.app/docs/architecture) · [CCR reversible compression](https://headroom-docs.vercel.app/docs/ccr) · [Kompress-v2-base model card](https://huggingface.co/chopratejas/kompress-v2-base)

## Get started (60 seconds)

```bash

## installation

uv tool install --python 3.13 "headroom-ai[all]"  # CLI as a global tool in a self-contained virtual env
pip install "headroom-ai[all]"                    # Python — ships the `headroom` CLI
npm install headroom-ai                           # TypeScript SDK only — no `headroom` CLI

# 2 — Pick your mode  (the `headroom` commands below come from the uv or pip install)
headroom deploy                         # turnkey local deployment + agent config
headroom wrap claude                    # wrap a coding agent
headroom proxy --port 8787              # drop-in proxy, zero code changes
# or: from headroom import compress      # inline library

# 3 — Verify setup and see the savings
headroom doctor                         # health check — confirms routing is working
headroom perf
headroom dashboard                      # live savings dashboard (proxy must be running)
```

To use headroom, it is recommended you launch a wrapped agent session each time so that all necessary setup is completed. When wrapping a coding agent, headroom starts a local proxy, installs **Serena** for semantic code navigation, and launches a coding agent session configured to proxy requests through headroom.

Serena is registered at **user scope** (for Claude Code, in `~/.claude.json`), so it stays available in your other projects until you run `headroom unwrap`. To skip it entirely, wrap with `--code-memory none`.

The `headroom` CLI ships **only** via the PyPI package. The npm `headroom-ai` is the TypeScript SDK — a library you import (`import { compress } from 'headroom-ai'`), not a CLI, so it provides no `headroom` command.

Granular extras: `[proxy]`, `[mcp]`, `[ml]`, `[code]`, `[memory]`, `[vector]` (optional HNSW backend — needs a C++ toolchain, not in `[all]`), `[relevance]`, `[image]`, `[agno]`, `[langchain]`, `[evals]`, `[pytorch-mps]` (Apple-GPU memory-embedder offload — set `HEADROOM_EMBEDDER_RUNTIME=pytorch_mps`). Requires **Python 3.10+**.

### Codex / global install

If Codex or another MCP client cannot inherit a shell `PATH` reliably, install Headroom as a persistent uv tool and point the client at the absolute binary path:

```bash
uv tool install "headroom-ai[all]"
command -v headroom
```

Then use the returned path in MCP config:

```toml
[mcp_servers.headroom]
command = "/absolute/path/from/command-v/headroom"
args = ["mcp", "serve"]
```

`command = "headroom"` only works when the client starts with a `PATH` that already includes the uv tool directory.

## Proof

**Savings on real agent workloads:**

| Workload                      | Before | After  | Savings |
|-------------------------------|-------:|-------:|--------:|
| Code search (100 results)     | 17,765 |  1,408 | **92%** |
| SRE incident debugging        | 65,694 |  5,118 | **92%** |
| GitHub issue triage           | 54,174 | 14,761 | **73%** |
| Codebase exploration          | 78,502 | 41,254 | **47%** |

**Accuracy preserved on standard benchmarks:**

| Benchmark  | Category | N   | Baseline | Headroom | Delta      |
|------------|----------|----:|---------:|---------:|------------|
| GSM8K      | Math     | 100 |    0.870 |    0.870 | **±0.000** |
| TruthfulQA | Factual  | 100 |    0.530 |    0.560 | **+0.030** |
| SQuAD v2   | QA       | 100 |        — |  **97%** | 19% compression |
| BFCL       | Tools    | 100 |        — |  **97%** | 32% compression |

Reproduce: `python -m headroom.evals suite --tier 1` · [Full benchmarks & methodology](https://headroom-docs.vercel.app/docs/benchmarks)

## Output token reduction (cut what the model writes back)

Everything above shrinks the prompt you **send**. But you also pay for every
token the model **writes back** — and on Opus-class models output costs 5× input.
A lot of that output is waste: "Great, let me…" preambles, re-printing code you
just showed it, and deep "thinking" on routine steps like reading a file.

Headroom can trim that too, from the proxy, without you changing any code:

- **Verbosity steering** — appends a short 

## configuration

If `pip install "headroom-ai[all]"` fails with `CERTIFICATE_VERIFY_FAILED`
(`unable to get local issuer certificate`), your network uses **SSL inspection** — a MITM
proxy presenting a company-issued CA. The build backend (`maturin`) downloads `rustup` over a
connection your TLS stack doesn't trust. **Install Rust first** so the build doesn't fetch it:

```bash
# macOS / Linux
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh && rustup default stable
# Windows
winget install Rustlang.Rustup && rustup default stable
```

Restart your shell, then `pip install "headroom-ai[all]"`. A prebuilt wheel avoids the Rust
build entirely where available: `pip install --only-binary headroom-ai headroom-ai`. Prebuilt
wheels are published for Windows (`win_amd64`), Linux (`x86_64` / `aarch64`), and macOS
(Apple Silicon and Intel), so installs on those platforms never need a local Rust toolchain — the
Rust-first dance above is only for the platform-independent sdist fallback when no wheel matches.

Two runtime assets are fetched over TLS; if they are blocked, trust your corporate CA via
`REQUESTS_CA_BUNDLE` / `SSL_CERT_FILE` / `CURL_CA_BUNDLE`:

- **`cdn.pyke.io`** — the ONNX Runtime for the Rust core. Alternatively pre-provide it with
  `ORT_STRATEGY=system` and `ORT_LIB_LOCATION=/path/to/onnxruntime`.
- **`huggingface.co`** — the `kompress-base` compression model. Pre-download it and run with
  `HF_HUB_OFFLINE=1`, or set `HF_ENDPOINT` to a trusted mirror.

Running with compression disabled (pure gateway) requires neither asset.

#### Intel macOS (x86_64-apple-darwin): no prebuilt ONNX Runtime binary (#941)

`ort-sys` ships no prebuilt ONNX Runtime binary for Intel macOS, so a source
build fails by default even outside a corporate-proxy environment. The same
`ORT_STRATEGY=system` mechanism above fixes it — point it at a system ONNX
Runtime instead:

```bash
brew install onnxruntime
ORT_STRATEGY=system \
ORT_LIB_LOCATION="$(brew --prefix onnxruntime)/lib" \
ORT_PREFER_DYNAMIC_LINK=1 \
  pip install "headroom-ai[all]"

# ORT is dlopen'd at runtime too:
export ORT_DYLIB_PATH="$(brew --prefix onnxruntime)/lib/libonnxruntime.dylib"
```

`ORT_LIB_LOCATION` must point at `lib/` (not the bare prefix) and
`ORT_PREFER_DYNAMIC_LINK=1` is required, or `ORT_STRATEGY=system` still
attempts static linking, which the Homebrew keg doesn't provide.

#### "Basic Constraints of CA cert not marked critical" (Python 3.13+ strict mode)

A **different** failure from the one above. If TLS fails with:

```
[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed:
Basic Constraints of CA cert not marked critical
```

then the corporate CA *is* found and trusted — adding it to a CA bundle changes nothing.
Python 3.13 + OpenSSL 3.x enable `VERIFY_X509_STRICT` by default, which enforces RFC 5280
§4.2.1.9: a CA cert's `basicConstraints` must be marked *critical*. Inspection roots like
Zscaler set `CA:TRUE` without the critical bit, so the chain is rejected.

Set **`HEADROOM_TLS_STRICT=0`** to clear *only* the strict flag from every TLS context
Headroom controls — the proxy's httpx upstream client **and** the urllib3/`huggingface_hub`
path used for model downloads. Chain validation, signature, expiry, and hostname checks all
stay on; this is strictly narrower than disabling verification.

```bash
HEADROOM_TLS_STRICT=0 headroom proxy --port 8787
```

The Rust core's ONNX download (`cdn.pyke.io`) uses a separate TLS stack (rustls / OS trust
store), unaffected by `HEADROOM_TLS_STRICT`. On Windows the corporate root must be in the
**machine** certificate store (browsers already trust it there); or pre-provision ONNX
Runtime with `ORT_STRATEGY=system` + `ORT_LIB_LOCATION=/path/to/onnxruntime` to skip the
download entirely.

## headroom learn

<p align="center">
  <img src="headroom_learn.gif" alt="headroom learn in action" width="720">
</p>

`headroom learn` — mines failed sessions, writes corrections to `CLAUDE.local.md` (default, gitignored; use `--target CLAUDE.
