# jundot/omlx

LLM inference server with continuous batching & SSD caching for Apple Silicon — managed from the macOS menu bar

## installation

### macOS App

Download the `.dmg` from [Releases](https://github.com/jundot/omlx/releases), drag to Applications, done. The app includes in-app auto-update, so future upgrades are just one click. The macOS app also installs a lightweight `~/.omlx/bin/omlx` CLI shim so terminal commands and Apple Shortcuts can control the app-managed server.

### Homebrew

```bash
brew tap jundot/omlx https://github.com/jundot/omlx
brew install jundot/omlx/omlx

# Upgrade to the latest version
brew update && brew upgrade omlx

# Run as a background service (auto-restarts on crash)
omlx start

# Optional: MCP (Model Context Protocol) support
/opt/homebrew/opt/omlx/libexec/bin/pip install mcp
```

Optional GLM-5.2 / MiniMax M3 native custom kernels currently require a HEAD build:

```bash
brew install jundot/omlx/omlx --HEAD --with-custom-kernel
```

### From Source

```bash
git clone https://github.com/jundot/omlx.git
cd omlx
pip install -e .          # Core only
pip install -e ".[mcp]"   # With MCP (Model Context Protocol) support

# GLM-5.2 / MiniMax M3 / Qwen3.5 native custom kernels (strongly recommended
# if you serve those families -- see note below)
OMLX_WITH_CUSTOM_KERNEL=1 pip install -e .
```

Requires macOS 15.0+ (Sequoia), Python 3.11–3.13, and Apple Silicon (M1/M2/M3/M4/M5).

> **Note on native custom kernels:** a plain `pip install -e .` does NOT build
> them, and the affected model families then silently fall back to much slower
> generic paths -- for GLM-5.2 the fused DSA prefill is roughly 30x faster with
> the kernels (measured 845 vs ~29 tok/s on an M3 Ultra), and the fallback also
> uses more memory (#2137). Building them requires the Metal toolchain, which
> Command Line Tools alone do not provide (`xcrun: error: unable to find utility
> "metal"`): install full Xcode, or use the official DMG which ships the kernels
> precompiled. Homebrew can build them with `brew install jundot/omlx/omlx --HEAD
> --with-custom-kernel`, but that build also needs full Xcode. To verify your
> install:
>
> ```bash
> python -c "from omlx.custom_kernels import native_kernel_status; print(native_kernel_status())"
> ```

## Quickstart

### macOS App

Launch oMLX from your Applications folder. The Welcome screen guides you through three steps - model directory, server start, and first model download. That's it. To connect OpenClaw, OpenCode, Codex, Hermes Agent, or Copilot, see [Integrations](#integrations).

<p align="center">
  <img src="docs/images/Screenshot 2026-02-10 at 00.36.32.png" alt="oMLX Welcome Screen" width="360">
  <img src="docs/images/Screenshot 2026-02-10 at 00.34.30.png" alt="oMLX Menubar" width="240">
</p>

### CLI

```bash
# Managed background server (macOS app or Homebrew install)
omlx start
omlx stop
omlx restart

# Foreground server attached to this terminal
omlx serve --model-dir ~/models
```

The server discovers LLMs, VLMs, embedding models, and rerankers from subdirectories automatically. Any OpenAI-compatible client can connect to `http://localhost:8000/v1`. A built-in chat UI is also available at `http://localhost:8000/admin/chat`.

### Homebrew Service

If you installed via Homebrew, you can run oMLX as a managed background service:

```bash
omlx start                    # Start via brew services
omlx stop                     # Stop
omlx restart                  # Restart

brew services start omlx    # Start (auto-restarts on crash)
brew services stop omlx     # Stop
brew services restart omlx  # Restart
brew services info omlx     # Check status
```

The service runs `omlx serve` with zero-config defaults (`~/.omlx/models`, port 8000). `omlx start`, `omlx stop`, and `omlx restart` are the portable lifecycle commands; Homebrew installs delegate them to `brew services`. To customize, either set environment variables (`OMLX_MODEL_DIR`, `OMLX_PORT`, etc.) or run `omlx serve --model-dir /your/path` once to persist settings to `~/.omlx/settings.json`.

Logs are written to two locations:
- **Service log**: `$(brew --prefix)

## features

Supports text LLMs, vision-language models (VLM), OCR models, embeddings, and rerankers on Apple Silicon.

### Admin Dashboard

Web UI at `/admin` for real-time monitoring, model management, chat, benchmark, and per-model settings. Supports English, Korean, Japanese, Chinese, French, Russian, Spanish, and Brazilian Portuguese. All CDN dependencies are vendored for fully offline operation.

<p align="center">
  <img src="docs/images/Screenshot 2026-02-10 at 00.45.34.png" alt="oMLX Admin Dashboard" width="720">
</p>

### Experimental Multi-Mac Inference

Source builds can split one downloaded language model across unequal-memory Macs
using MLX pipeline ranks over Ring or Thunderbolt RDMA/JACCL. The Cluster
dashboard handles read-only peer discovery, strict SSH/runtime verification,
byte-aware unequal shard planning, measured compute/link rebalancing,
headroom-aware execution tuning, activation, and a live shard/performance map
on both Macs. Interactive, balanced, and throughput profiles expose coalesced
batching, prompt-cache affinity, rotating-KV limits, Ring connection tuning,
and a capability-gated experimental token-only output path. See
[Distributed inference across Macs](docs/distributed-cluster.md) for setup,
security boundaries, current limitations, and the physical-hardware validation
checklist.

### Vision-Language Models

Run VLMs with the same continuous batching and tiered KV cache stack as text LLMs. Supports multi-image chat, base64/URL/file image inputs, and tool calling with vision context. OCR models (DeepSeek-OCR, DOTS-OCR, GLM-OCR) are auto-detected with optimized prompts.

### Tiered KV Cache (Hot + Cold)

Block-based KV cache management inspired by vLLM, with prefix sharing and Copy-on-Write. The cache operates across two tiers:

- **Hot tier (RAM)**: Frequently accessed blocks stay in memory for fast access.
- **Cold tier (SSD)**: When the hot cache fills up, blocks are offloaded to SSD in safetensors format. On the next request with a matching prefix, they're restored from disk instead of recomputed from scratch - even after a server restart.

<p align="center">
  <img src="docs/images/omlx_hot_cold_cache.png" alt="oMLX Hot & Cold Cache" width="720">
</p>

### Continuous Batching

Handles concurrent requests through mlx-lm's BatchGenerator. Max concurrent requests is configurable via CLI or admin panel.

### Claude Code Optimization

Context scaling support for running smaller context models with Claude Code. Scales reported token counts so that auto-compact triggers at the right timing, and SSE keep-alive prevents read timeouts during long prefill.

### Multi-Model Serving

Load LLMs, VLMs, embedding models, and rerankers within the same server. Models are managed through a combination of automatic and manual controls:

- **LRU eviction**: Least-recently-used models are evicted automatically when memory runs low.
- **Manual load/unload**: Interactive status badges in the admin panel let you load or unload models on demand.
- **Model pinning**: Pin frequently used models to keep them always loaded.
- **Per-model TTL**: Set an idle timeout per model to auto-unload after a period of inactivity.
- **Process memory enforcement**: Total memory limit (default: system RAM - 8GB) prevents system-wide OOM.

### Per-Model Settings

Configure sampling parameters, chat template kwargs, TTL, model alias, model type override, and more per model directly from the admin panel. Changes apply immediately without server restart.

- **Model alias**: set a custom API-visible name. `/v1/models` returns the alias, and requests accept both the alias and directory name.
- **Model type override**: manually set a model as LLM or VLM regardless of auto-detection.
- **Profiles**: save named bundles of per-model settings and switch between them from the admin panel. A profile can optionally be exposed as its own model: `/v1/models` then also lists `<model>:<profile>` (e.g. `qwen3-8b:thinking`), which serves on the same engine as the b

## tools

Drop-in replacement for OpenAI and Anthropic APIs. Supports streaming usage stats (`stream_options.include_usage`), Anthropic adaptive thinking, and vision inputs (base64, URL).

| Endpoint | Description |
|----------|-------------|
| `POST /v1/chat/completions` | Chat completions (streaming) |
| `POST /v1/completions` | Text completions (streaming) |
| `POST /v1/messages` | Anthropic Messages API |
| `POST /v1/embeddings` | Text embeddings |
| `POST /v1/rerank` | Document reranking |
| `GET /v1/models` | List available models |

### Tool Calling & Structured Output

Supports all function calling formats available in mlx-lm, JSON schema validation, and MCP tool integration. Tool calling requires the model's chat template to support the `tools` parameter. The following model families are auto-detected via mlx-lm's built-in tool parsers:

| Model Family | Format |
|---|---|
| Llama, Qwen, DeepSeek, etc. | JSON `<tool_call>` |
| Qwen3.5 Series | XML `<function=...>` |
| Gemma | `<start_function_call>` |
| GLM (4.7, 5) | `<arg_key>/<arg_value>` XML |
| MiniMax | Namespaced `<minimax:tool_call>` |
| Mistral | `[TOOL_CALLS]` |
| Kimi K2 | `<\|tool_calls_section_begin\|>` |
| Longcat | `<longcat_tool_call>` |

Models not listed above may still work if their chat template accepts `tools` and their output uses a recognized `<tool_call>` XML format. For tool-enabled streaming, assistant text is emitted incrementally while known tool-call control markup is suppressed from visible content; structured tool calls are emitted after parsing the completed turn.

## Models

Point `--model-dir` at a directory containing MLX-format model subdirectories. Two-level organization folders (e.g., `mlx-community/model-name/`) are also supported.

```
~/models/
├── Step-3.5-Flash-8bit/
├── Qwen3-Coder-Next-8bit/
├── gpt-oss-120b-MXFP4-Q8/
├── Qwen3.5-122B-A10B-4bit/
└── bge-m3/
```

Models are auto-detected by type. You can also download models directly from the admin dashboard.

| Type | Models |
|------|--------|
| LLM | Any model supported by [mlx-lm](https://github.com/ml-explore/mlx-lm) |
| VLM | Qwen3.5 Series, GLM-4V, Pixtral, and other [mlx-vlm](https://github.com/Blaizzy/mlx-vlm) models |
| OCR | DeepSeek-OCR, DOTS-OCR, GLM-OCR |
| Embedding | BERT, BGE-M3, ModernBERT |
| Reranker | ModernBERT, XLM-RoBERTa |

## configuration

```bash
