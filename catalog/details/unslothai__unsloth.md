# unslothai/unsloth

Local UI to run and train LLMs and diffusion models, including Qwen3.8, Kimi K3, MiniMax-H3, Gemma 4, DeepSeek-V4, FLUX and more.

## features

Unsloth lets you run, train, and deploy AI models locally, with support for all types of models.

### Run & Build with AI
* Run and train LLMs, diffusion, embedding, audio models: [Kimi K3](https://unsloth.ai/docs/models/kimi-k3), MiniMax-H3, Qwen3.8, [Muse Glimmer](https://unsloth.ai/docs/models/muse-glimmer), [DeepSeek-V4](https://unsloth.ai/docs/models/deepseek-v4), [Gemma 4](https://unsloth.ai/docs/models/gemma-4).
* **Agents & Tools:** Use local models with [Claude Code](https://unsloth.ai/docs/basics/claude-code), [Codex](https://unsloth.ai/docs/basics/codex), and [MCP](https://unsloth.ai/docs/basics/mcp), including tool calling and code execution.
* **Search & RAG:** Use private and unlimited web search, deep research, and RAG.
* **Image and video:** Run and train [image](https://unsloth.ai/docs/basics/diffusion-image) and video diffusion or multimodal models
* **Search:** Use private and unlimited web search, deep research, and RAG.
* **Hardware:** Supports CPU, Apple, NVIDIA, AMD, Intel, and multi GPU setups.
* **Remote Access:** Serve your local models remotely through secure [Cloudflare](https://unsloth.ai/docs/basics/how-to-serve-local-llms-anywhere-secure-remote-access-with-cloudflare-and-unsloth) HTTPS.
* **Connect:** Serve models through an [OpenAI compatible API](https://unsloth.ai/docs/basics/api). Also connect your ChatGPT/Codex subscription and [cloud providers](https://unsloth.ai/docs/integrations/connections)


### Train & Deploy
* **Fine-tuning:** Train LLMs, diffusion, TTS, and embedding models 2× faster with 70% less VRAM with [no accuracy loss](https://unsloth.ai/blog#training)
* **Complete support:** Supports [reinforcement learning](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide), LoRA, QLoRA, full fine tuning, pretraining, RL, GRPO, DPO, and FP8.
* **Export & Deploy:** [Export](https://unsloth.ai/docs/new/studio/export) or Deploy models with including [GGUF](https://unsloth.ai/docs/basics/inference-and-deployment/saving-to-gguf), NVFP4, FP8 and more formats.
* **Datasets:** Build datasets from PDFs, CSVs, DOCX files, and more with [Data Recipes](https://unsloth.ai/docs/new/studio/data-recipe).
  
## 🚀 Unsloth Start

[Unsloth Start](https://unsloth.ai/docs/integrations/unsloth-start) connects [Claude Code](https://unsloth.ai/docs/basics/claude-code), [Codex](https://unsloth.ai/docs/basics/codex) and other agents to local models with one command.

Start Unsloth, load a model, open your project folder, then run:

```bash
unsloth start claude
```

Replace `claude` with any supported agent:

| Agent | Command |
| --- | --- |
| Claude Code | `unsloth start claude` |
| OpenAI Codex | `unsloth start codex` |
| Hermes Agent | `unsloth start hermes` |
| OpenClaw | `unsloth start openclaw` |
| OpenCode | `unsloth start opencode` |

Claude Code, Codex and OpenCode can keep their current model and use Unsloth as a local
subagent:

```bash
unsloth start claude --as-subagent --model unsloth/model-GGUF:quant
```

## installation

Unsloth can be used in three ways: **[Unsloth Desktop](https://unsloth.ai/download)**, the desktop app; **[Unsloth Studio](https://unsloth.ai/docs/new/studio/)**, the web UI; or **Unsloth Core**, the code based version.

### Unsloth Desktop (recommended)

The Tauri based desktop app is the easiest way to use Unsloth and needs no setup, so start here.

<table>
  <tr>
    <td><b>Platform</b></td>
    <td><b>Link</b></td>
  </tr>
  <tr>
    <td><b>Windows</b></td>
    <td><a href='https://github.com/unslothai/unsloth/releases/download/v0.1.801-beta/Unsloth-Desktop-0_1_801_beta-Windows.exe'>Download</a></td>
  </tr>
  <tr>
    <td><b>macOS</b></td>
    <td><a href='https://github.com/unslothai/unsloth/releases/download/v0.1.801-beta/Unsloth-Desktop-0_1_801_beta-MacOS.dmg'>Download</a></td>
  </tr>
  <tr>
    <td><b>Linux / Ubuntu (deb)</b></td>
    <td><a href='https://github.com/unslothai/unsloth/releases/download/v0.1.801-beta/Unsloth-Desktop-0_1_801_beta-Ubuntu.deb'>Download</a></td>
  </tr>
  <tr>
    <td><b>Linux (AppImage)</b></td>
    <td><a href='https://github.com/unslothai/unsloth/releases/download/v0.1.801-beta/Unsloth-Desktop-0_1_801_beta-Linux.AppImage'>Download</a></td>
  </tr>
  <tr>
    <td><b>Linux (Arm64)</b></td>
    <td><a href='https://github.com/unslothai/unsloth/releases/download/v0.1.801-beta/Unsloth-Desktop-0_1_801_beta-ARM64.app.tar.gz'>Download</a></td>
  </tr>
</table>

### Unsloth Studio (web UI)
Unsloth Studio (Beta) works on **Windows, Linux, WSL** and **macOS**.

* **CPU:** Supported for Chat and Data Recipes currently
* **NVIDIA:** Training works on RTX 30/40/50, Blackwell, DGX Spark, Station and more
* **macOS:** Training, MLX and GGUF inference are ALL supported.
* **AMD:** Training, RL, chat and deployment work on Windows, WSL and Linux. [Read the AMD guide](https://unsloth.ai/docs/basics/amd).
* **Intel:** Training and GGUF inference are supported on Intel GPUs (XPU).
* **Vulkan:** GGUF inference is supported on [compatible GPUs, including Intel GPUs](https://github.com/unslothai/unsloth/pull/5819). Vulkan accelerates GGUF inference only; training still requires a supported PyTorch or MLX backend.
* **Multi-GPU:** Available now, with a major upgrade on the way

#### macOS, Linux, WSL:
```bash
curl -fsSL https://unsloth.ai/install.sh | sh
```
Use the same command to update.

The GGUF inference backend can be changed from **Settings > System > GGUF inference engine** once Studio is running: pick CPU, CUDA, ROCm or Vulkan (only the ones with a build for your machine are listed) and Apply. The choice is recorded with the install, so updates keep it, and Automatic returns to hardware detection.

To pick it before the first launch instead, set `UNSLOTH_LLAMA_CPP_BACKEND` **before installing or updating**. It selects the llama.cpp binary bundle, so setting it only when launching Studio cannot replace an existing one, and it overrides whatever was chosen in Settings:

```bash
export UNSLOTH_LLAMA_CPP_BACKEND=vulkan   # or cpu, cuda, rocm, auto
curl -fsSL https://unsloth.ai/install.sh | sh
```

On Linux and WSL this is the path for the AMD GPUs Unsloth has no ROCm PyTorch wheels for: Polaris (RX 470/480/570/580/590) and RDNA 1 (RX 5500/5600/5700). torch stays on CPU there, so training and GPU inference are unavailable, but GGUF chat runs on the GPU through Vulkan. Not every pre-RDNA 2 card is in this group: Vega 20 (Radeon VII, MI50, `gfx906`) keeps a ROCm PyTorch path and the installer routes it there. The older `UNSLOTH_FORCE_VULKAN=1` still works and is read when `UNSLOTH_LLAMA_CPP_BACKEND` is unset.

macOS has no Vulkan llama.cpp bundle and does not need one: the installer always uses the Metal build, which covers Apple Silicon and the AMD GPUs in Intel Macs, and it says so and carries on if the variable is set.

#### Windows:
```powershell
irm https://unsloth.ai/install.ps1 | iex
```
Use the same command to update.

To pick the GGUF inference backend before the first launch, set the environment var
