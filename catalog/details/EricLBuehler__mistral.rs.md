# EricLBuehler/mistral.rs

Fast, flexible LLM inference

## features

- **Automatic model loading**: Architecture, weight format, and chat template are detected for supported Hugging Face models and GGUF files, with flags available for explicit selection.
- **True multimodality**: Text, vision, video, and audio, speech generation, image generation, and embeddings in one engine.
- **Quantization selection**: `--quant` selects a matching artifact from GGUF repositories. For other Hugging Face repositories, it uses a prebuilt UQFF when available and otherwise applies ISQ. [Docs](https://docs.mistralrs.dev/guides/quantization/quantize-a-model/)
- **OpenAI + Anthropic compatible serving**: The same `mistralrs serve` process exposes OpenAI-compatible `/v1` endpoints and Anthropic-compatible Messages endpoints.
- **Prometheus metrics**: `mistralrs serve` exposes a `/metrics` endpoint in Prometheus format, recording per-request counts and latency labeled by method, route, and status. [Docs](https://docs.mistralrs.dev/reference/http-api/)
- **Built-in web UI**: Served at `/ui` by default. Shows reasoning, code execution, plots, and files inline. Edit any message and the new branch runs with its own Python state. Pass `--no-ui` to disable.
- **Hardware-aware**: `mistralrs tune` recommends quantization and device mapping from the model config and your detected hardware.
- **Flexible SDKs**: Python package and Rust crate to build your projects.
- **Native agentic support**: built-in [agentic loop](https://docs.mistralrs.dev/guides/agents/) with web search, local Python code execution, shell execution, OpenAI-compatible Skills, session management, and custom tool hooks.

## installation

### Install

**Linux/macOS:**
```bash
curl --proto '=https' --tlsv1.2 -sSf https://raw.githubusercontent.com/EricLBuehler/mistral.rs/master/install.sh | sh
```

**Windows (PowerShell):**
```powershell
irm https://raw.githubusercontent.com/EricLBuehler/mistral.rs/master/install.ps1 | iex
```

Downloads a self-contained prebuilt binary for your platform (Metal on Apple Silicon; per-GPU CUDA or CPU on Linux; CPU on Windows), falling back to a source build if none matches. Standard acceleration needs no Rust or CUDA toolkit. Optional cuTile acceleration requires NVIDIA's separately installed `tileiras` tool.

[Manual installation, accelerator details & other platforms](https://docs.mistralrs.dev/quickstart/)

### Run Your First Model

```bash
# Interactive chat
mistralrs run -m Qwen/Qwen3-4B

# One-shot prompt (no interactive session)
mistralrs run -m Qwen/Qwen3-4B -i "What is the capital of France?"

# One-shot with an image
mistralrs run -m google/gemma-4-E4B-it --image photo.jpg -i "Describe this image"

# Run a local GGUF or select a published 4-bit GGUF
mistralrs run -f /path/to/model.gguf
mistralrs run -m unsloth/Qwen3.5-4B-GGUF --quant 4

# Agentic REPL: search + code execution + shell from the terminal
mistralrs run --agent -m Qwen/Qwen3-4B

## tools

mistralrs serve -m google/gemma-4-E4B-it
```

For the server command, visit `http://localhost:1234/ui` for the web chat interface. OpenAI-compatible clients use `http://localhost:1234/v1`; Anthropic-compatible clients use `http://localhost:1234`.

### The `mistralrs` CLI

The CLI uses the same `run`, `serve`, and `bench` commands for model repositories, local directories, and GGUF files.

- **Auto-detection**: Automatically detects model architecture, quantization format, and chat template
- **All-in-one**: Single binary for chat, server, benchmarks, and web UI (`run`, `serve`, `bench`)
- **Hardware-aware tuning**: `mistralrs tune` recommends quantization and device mapping for your model and hardware
- **Model formats**: Hugging Face checkpoints, [GGUF files](https://docs.mistralrs.dev/guides/models/run-gguf/), and [UQFF quantizations](https://docs.mistralrs.dev/reference/uqff-format/)

```bash

## configuration

mistralrs tune -m Qwen/Qwen3-4B --emit-config config.toml

# Run using the generated config
mistralrs from-config -f config.toml

# Diagnose system issues (CUDA, Metal, Hugging Face connectivity)
mistralrs doctor
```

[Full CLI documentation](https://docs.mistralrs.dev/reference/cli/)

<details open>
  <summary><b>UI Demo</b></summary>
  <br>
  <img src="https://raw.githubusercontent.com/EricLBuehler/mistral.rs/master/res/ui.gif" alt="UI Demo" />
</details>

## What Makes It Fast

**Performance**
- Continuous batching support by default on all devices.
- CUDA with FlashAttention V2/V3, Metal, and [multi-GPU/distributed inference](https://docs.mistralrs.dev/guides/perf/distributed-inference/)
- [PagedAttention](https://docs.mistralrs.dev/guides/perf/paged-attention/) for high throughput continuous batching on CUDA or Apple Silicon, prefix caching (including multimodal)

**Quantization** ([full docs](https://docs.mistralrs.dev/reference/quantization-types/))
- [In-situ quantization (ISQ)](https://docs.mistralrs.dev/guides/quantization/quantize-a-model/) for Hugging Face models
- [GGUF](https://docs.mistralrs.dev/reference/gguf-support/) (2-8 bit), GPTQ, AWQ, HQQ, FP8, BNB support
- ⭐ [Per-layer topology](https://docs.mistralrs.dev/guides/perf/topology/): Fine-tune quantization per layer for optimal quality/speed
- ⭐ Auto-select fastest quant method for your hardware

**Flexibility**
- [LoRA & X-LoRA](https://docs.mistralrs.dev/guides/customize/lora-adapters/) with per-request LoRA selection and X-LoRA adapter mixing
- AnyMoE: Create mixture-of-experts on any base model
- [Multiple models](https://docs.mistralrs.dev/guides/serve/multiple-models/): Load/unload at runtime

**Agentic Features**
- Integrated [tool calling](https://docs.mistralrs.dev/guides/agents/tool-calling-basics/) with grammar enforcement and strict schema mode
- ⭐ Server-side [agentic loop](https://docs.mistralrs.dev/guides/agents/tool-calling-basics/): auto-execute tools and feed results back
- ⭐ [Python code execution](https://docs.mistralrs.dev/guides/agents/enable-code-execution/): persistent Jupyter-like sessions with matplotlib capture and multimodal feedback
- ⭐ [Shell execution](https://docs.mistralrs.dev/guides/agents/enable-shell/): persistent command-line sessions with sandboxing and approval controls
- ⭐ [OpenAI-compatible Skills](https://docs.mistralrs.dev/guides/agents/skills/): uploaded skill bundles for Responses API agents
- ⭐ [OpenAI-compatible file inputs](https://docs.mistralrs.dev/guides/agents/file-inputs/): `/v1/files`, Responses `input_file`, Chat `file`, and workdir mounts
- ⭐ [Web search integration](https://docs.mistralrs.dev/guides/agents/web-search/) with embedding-based ranking
- ⭐ [Tool dispatch URL](https://docs.mistralrs.dev/guides/agents/tool-calling-basics/): POST tool calls to your own endpoint
- ⭐ [MCP client](https://docs.mistralrs.dev/guides/agents/connect-mcp-server/): Connect to external tools via Process, HTTP, or WebSocket
- Python/Rust [tool callbacks](https://docs.mistralrs.dev/guides/agents/tool-calling-basics/) for custom execution

[Full feature documentation](https://docs.mistralrs.dev/)

## Supported Models

Text, multimodal, speech, image generation, and embedding models across 45+ architectures. The **[supported models reference](https://docs.mistralrs.dev/reference/supported-models/)** is the single source of truth: it explains how to check whether your model's `config.json` is supported, lists every architecture with copy-paste run commands, and is generated directly from the engine's loader registry so it never drifts.

[Supported models reference](https://docs.mistralrs.dev/reference/supported-models/) | [Request a new model](https://github.com/EricLBuehler/mistral.rs/issues/156)

## Python SDK

```bash
pip install mistralrs
```

In-process inference from Python: load a model with `Runner` and send OpenAI-shaped requests, no server required. Accelerator-specific wheels (CUDA, Metal, MKL, Accelerate) are lis
