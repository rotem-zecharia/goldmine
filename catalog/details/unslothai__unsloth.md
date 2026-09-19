# unslothai/unsloth

Local UI to run and train LLMs and diffusion models. Supports GGUF, MLX, Qwen3.8, DeepSeek-V4, MiniMax-H3, Gemma 4, FLUX and more.

## features

Unsloth works on **Windows, Linux, WSL** and **macOS**. We support **Multi GPU setups, NVIDIA, AMD, Intel GPUs, CPUs** and the **Vulkan** backend.

### Run & Build with AI
* Run and train LLMs, MLX, GGUF, diffusion, embedding, audio models: [Qwen3.8](https://unsloth.ai/docs/models/qwen3.8), [GLM-5.3-Flash](https://unsloth.ai/docs/models/glm-5.3-flash), [Kimi K3](https://unsloth.ai/docs/models/kimi-k3), MiniMax-H3, [DeepSeek-V4](https://unsloth.ai/docs/models/deepseek-v4), [Gemma 4](https://unsloth.ai/docs/models/gemma-4).
* **Agents & Tools:** Use local models with [Claude Code](https://unsloth.ai/docs/basics/claude-code), [Codex](https://unsloth.ai/docs/basics/codex), and [MCP](https://unsloth.ai/docs/basics/mcp), including tool calling and code execution.
* **Search & RAG:** Use private and unlimited web search, deep research, auto-compaction (rolling context window) and RAG.
* **Image and video:** Run and train [image](https://unsloth.ai/docs/basics/diffusion-image) and video diffusion or multimodal models
* **Remote & LAN:** Access your local models from any device on [LAN](https://unsloth.ai/docs/basics/lan) or remotely through secure [Cloudflare](https://unsloth.ai/docs/basics/how-to-serve-local-llms-anywhere-secure-remote-access-with-cloudflare-and-unsloth) HTTPS.
* **Connect:** Serve models through an [OpenAI compatible API](https://unsloth.ai/docs/basics/api). Also connect your ChatGPT/Codex subscription and [cloud providers](https://unsloth.ai/docs/integrations/connections)


### Train & Deploy
* **Fine-tuning:** Train LLMs, diffusion, TTS, and embedding models 2× faster with 70% less VRAM with [no accuracy loss](https://unsloth.ai/blog#training)
* **Complete support:** Supports [reinforcement learning](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide), LoRA, QLoRA, full fine tuning, pretraining, RL, GRPO, DPO, and FP8.
* **Export & Deploy:** [Export](https://unsloth.ai/docs/new/studio/export) or Deploy models with including [GGUF](https://unsloth.ai/docs/basics/inference-and-deployment/saving-to-gguf), NVFP4, FP8 and more formats.
* **Datasets:** Build datasets from PDFs, CSVs, DOCX files, and more with [Data Recipes](https://unsloth.ai/docs/new/studio/data-recipe).
  
## 🚀 Unsloth Start

[Unsloth Start](https://unsloth.ai/docs/integrations/unsloth-start) connects [Claude Code](https://unsloth.ai/docs/basics/claude-code), [Codex](https://unsloth.ai/docs/basics/codex) and other agents to local models with one command.

```bash
unsloth start claude --model unsloth/Qwen3.8-27B-GGUF:UD-Q4_K_XL
```

| Agent | Command |
| --- | --- |
| Claude Code | `unsloth start claude` |
| OpenAI Codex | `unsloth start codex` |
| DeepSeek Harness | `unsloth start dsh` |
| Hermes Agent | `unsloth start hermes` |
| OpenCode | `unsloth start opencode` |
| OpenClaw | `unsloth start openclaw` |

## installation

Unsloth can be used in three ways: **[Unsloth Desktop](https://unsloth.ai/download)**, the desktop app; **[Unsloth Studio](https://unsloth.ai/docs/new/studio/)**, the web UI; or **Unsloth Core**, the code based version.

### Unsloth Desktop (recommended)

<table>
  <tr>
    <td><b>Platform</b></td>
    <td><b>Link</b></td>
  </tr>
  <tr>
    <td><b>Windows</b></td>
    <td><a href='https://github.com/unslothai/unsloth/releases/latest/download/Unsloth-Desktop-Windows.exe'>Download</a></td>
  </tr>
  <tr>
    <td><b>macOS</b></td>
    <td><a href='https://github.com/unslothai/unsloth/releases/latest/download/Unsloth-Desktop-MacOS.dmg'>Download</a></td>
  </tr>
  <tr>
    <td><b>Linux / Ubuntu (deb)</b></td>
    <td><a href='https://github.com/unslothai/unsloth/releases/latest/download/Unsloth-Desktop-Ubuntu.deb'>Download</a></td>
  </tr>
  <tr>
    <td><b>Linux (AppImage)</b></td>
    <td><a href='https://github.com/unslothai/unsloth/releases/latest/download/Unsloth-Desktop-Linux.AppImage'>Download</a></td>
  </tr>
  <tr>
    <td><b>Windows ARM64</b></td>
    <td><a href='https://github.com/unslothai/unsloth/releases/download/v0.1.811-beta/Unsloth-Desktop-Windows-ARM64.exe'>Download</a></td>
  </tr>
</table>

### Unsloth Studio (web UI)

#### macOS, Linux, WSL:
```bash
curl -fsSL https://unsloth.ai/install.sh | sh
```

#### Windows:
```powershell
irm https://unsloth.ai/install.ps1 | iex
```

#### Launch
```bash
unsloth studio
```

#### HTTP Secure Deployment
```bash
unsloth studio --secure
```

#### Docker
Use our [Docker image](https://hub.docker.com/r/unsloth/unsloth) ```unsloth/unsloth```. On Linux, set up GPU access once with `curl -fsSL https://raw.githubusercontent.com/unslothai/unsloth/main/docker/install_nvidia_toolkit.sh -o install_nvidia_toolkit.sh && sudo -E bash install_nvidia_toolkit.sh` (Windows: [Docker Desktop with WSL 2](https://unsloth.ai/docs/get-started/install/docker)).

**Linux / WSL (Bash):**
```bash
# use  -e UNSLOTH_STUDIO_SECURE=1  instead of -p 8000:8000 for a public Cloudflare HTTPS link
docker run -d --name unsloth --gpus all --ipc=host \
  -p 8000:8000 -p 8888:8888 \
  -v "$PWD":/workspace/host \
  -v "$HOME/.cache/huggingface":/workspace/.cache/huggingface \
  -v unsloth-studio:/opt/unsloth-studio \
  unsloth/unsloth && docker logs -f unsloth
```
The log ends with your links and a generated JupyterLab password, plus a generated Unsloth Studio password on the first run against a new `unsloth-studio` volume; change that one on first sign-in or Unsloth Studio stops after an hour. A reused volume keeps the password already stored on it, and `docker exec unsloth unsloth studio reset-password --username unsloth` mints a new one and prints it. Ctrl-C stops following the log, not the container; `docker rm -f unsloth` deletes it. The Hugging Face cache keeps your models and the `unsloth-studio` volume keeps your accounts, chats and trained models, both across `docker rm`; a volume from an older image is migrated on first start, its old code kept under `.unsloth-studio-legacy/`. Those ports publish on every interface: on a cloud host add `-e UNSLOTH_STUDIO_SECURE=1`, drop `-p 8000:8000` and bind JupyterLab to `-p 127.0.0.1:8888:8888`, or bind both to `127.0.0.1` and use an SSH tunnel. Tags (`unsloth/unsloth:core` for notebooks only), GPU support and options: [Docker Hub](https://hub.docker.com/r/unsloth/unsloth).

On AMD there is a separate image, [`unsloth/unsloth-rocm`](https://hub.docker.com/r/unsloth/unsloth-rocm), with the run command and the supported cards on its [Docker Hub page](https://hub.docker.com/r/unsloth/unsloth-rocm). It carries the training stack only, so there is no Unsloth Studio or JupyterLab in it, and it needs native Linux: WSL exposes `/dev/dxg` rather than the `/dev/kfd` that ROCm needs.

#### Remote HTTPS & LAN Access
Server-side tools are on by default - so **be careful**! Keep your password safe, or use `--disable-tools` when exposing Unsloth.

**Global HTTPS Access**:
Creates a f
