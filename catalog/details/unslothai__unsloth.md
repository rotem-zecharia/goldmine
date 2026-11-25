# unslothai/unsloth

Local UI to run and train LLMs and diffusion models. Supports GGUF, MLX, Qwen3.8, DeepSeek-V4.1, MiniMax-H3, Gemma 4, FLUX and more.

## features

Unsloth works on **Windows, Linux, WSL** and **macOS**. We support **Multi GPU setups, NVIDIA, AMD, Intel GPUs, CPUs** and the **Vulkan** backend.

### Run & Build with AI
* Run and train LLMs, MLX, GGUF, diffusion, decision, embedding, audio models: [Qwen3.8](https://unsloth.ai/docs/models/qwen3.8), [GLM-5.3-Flash](https://unsloth.ai/docs/models/glm-5.3-flash), [Kimi K3](https://unsloth.ai/docs/models/kimi-k3), [Qwen-Image-2.1](https://unsloth.ai/docs/models/qwen-image-2.1), MiniMax-H3, [DeepSeek-V4](https://unsloth.ai/docs/models/deepseek-v4), [Gemma 4](https://unsloth.ai/docs/models/gemma-4).
* **Agents & Tools:** Use local models with [Claude Code](https://unsloth.ai/docs/basics/claude-code), [Codex](https://unsloth.ai/docs/basics/codex), and [MCP](https://unsloth.ai/docs/basics/mcp), including tool calling and code execution.
* **Browser & Computer use:** Have local LLMs [edit your desktop](https://unsloth.ai/docs/basics/computer-use), [Edit files & sites](https://unsloth.ai/docs/basics/browser-use), fill out forms, read PDFs
* **Sandboxing:** [Limit file access](https://unsloth.ai/docs/new/studio/sandboxing-in-unsloth) for commands your model runs.
* **Search & RAG:** Use private and unlimited web search, deep research, auto-compaction (rolling context window) and RAG.
* **Image and video:** Run and train [image](https://unsloth.ai/docs/basics/diffusion-image) and video diffusion or multimodal models
* **Remote & LAN:** Access your local models from any device on [LAN](https://unsloth.ai/docs/basics/lan) or remotely through secure [Cloudflare](https://unsloth.ai/docs/basics/how-to-serve-local-llms-anywhere-secure-remote-access-with-cloudflare-and-unsloth) HTTPS.
* **API:** Serve models through an [OpenAI compatible API](https://unsloth.ai/docs/basics/api). Connect your ChatGPT/Codex subscription, Claude and [cloud providers](https://unsloth.ai/docs/integrations/connections)

### Train & Deploy
* **Fine-tuning:** Train LLMs, diffusion, decision, TTS, and embedding models 2× faster with 70% less VRAM with [no accuracy loss](https://unsloth.ai/blog#training)
* **Complete support:** Supports [reinforcement learning](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide), LoRA, QLoRA, full fine tuning, pretraining, RL, GRPO, DPO, and FP8.
* **Export & Deploy:** [Export](https://unsloth.ai/docs/new/studio/export) or Deploy models including [GGUF](https://unsloth.ai/docs/basics/inference-and-deployment/saving-to-gguf), NVFP4, FP8 and more formats.
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
| Visual Studio Code | `unsloth start vscode` |
| DeepSeek Harness | `unsloth start dsh` |
| OpenCode | `unsloth start opencode` |
| Hermes Agent | `unsloth start hermes` |
| Pi | `unsloth start pi` |
| OpenClaw | `unsloth start openclaw` |
| Mistral Vibe | `unsloth start vibe` |

## installation

Unsloth can be used in three ways: **[Unsloth Desktop](https://unsloth.ai/download)**, the desktop app; **[Unsloth Studio](https://unsloth.ai/docs/new/studio/)**, the web UI; or **Unsloth Core**, the code based version.

### Unsloth Desktop (recommended)

<table>
  <tr>
    <td><b>Platform</b></td>
    <td><b>Link</b></td>
  </tr>
  <tr>
    <td><b>Windows (x64 and ARM64)</b></td>
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
    <td><b>Linux / Ubuntu (ARM64) (deb)</b></td>
    <td><a href='https://github.com/unslothai/unsloth/releases/latest/download/Unsloth-Desktop-Ubuntu-ARM64.deb'>Download</a></td>
  </tr>
  <tr>
    <td><b>Linux (AppImage)</b></td>
    <td><a href='https://github.com/unslothai/unsloth/releases/latest/download/Unsloth-Desktop-Linux.AppImage'>Download</a></td>
  </tr>
</table>

For Desktop's local HTTP port, set `UNSLOTH_DESKTOP_PORT=9000` in its launch environment and fully restart the app. Unset or empty uses `8888`. Choose `1024–65515`. If the port is busy, Desktop tries the next 20. It rejects ranges with browser-restricted ports. This covers backend restarts after updates. `unsloth studio -p` and LAN use separate ports.

### Unsloth Studio (web UI)

#### macOS, Linux, WSL:
```bash
curl -fsSL https://unsloth.ai/install.sh | sh
```

#### Windows:
```powershell
irm https://unsloth.ai/install.ps1 | iex
```

#### Homebrew:
```bash
brew install --cask unsloth
```

#### Docker
Use our [Docker image](https://hub.docker.com/r/unsloth/unsloth) ```unsloth/unsloth```. On Linux and Mac, set up GPU access once with
```bash
curl -fsSL https://raw.githubusercontent.com/unslothai/unsloth/main/docker/install_nvidia_toolkit.sh -o install_nvidia_toolkit.sh && sudo -E bash install_nvidia_toolkit.sh
```
For Windows instructions and more information, read our [Unsloth Docker Guide](https://unsloth.ai/docs/get-started/install/docker).

**Linux / WSL (Bash):**
```bash
# for a public Cloudflare HTTPS link: use  -e UNSLOTH_STUDIO_SECURE=1  instead of -p 8000:8000, and  -p 127.0.0.1:8888:8888  instead of -p 8888:8888
docker run -d --name unsloth --gpus all --ipc=host \
  -p 8000:8000 -p 8888:8888 \
  -v "$PWD":/workspace/host \
  -v unsloth-workspace:/workspace \
  -v "$HOME/.cache/huggingface":/workspace/.cache/huggingface \
  -v unsloth-studio:/opt/unsloth-studio \
  unsloth/unsloth && docker logs -f unsloth
```
See [Docker docs](https://unsloth.ai/docs/get-started/install/docker) for more information. For notebooks only, use the `unsloth/unsloth:core` tag; all tags and options are on [Docker Hub](https://hub.docker.com/r/unsloth/unsloth).<br>For **AMD** there is a separate image: [`unsloth/unsloth-rocm`](https://hub.docker.com/r/unsloth/unsloth-rocm).

---

#### Launch
```bash
unsloth studio
```

#### HTTP Secure Deployment
```bash
unsloth studio --secure
```

#### Remote HTTPS & LAN Access
Server-side tools are on by default - so **be careful**! Keep your password safe, or use `--disable-tools` when exposing Unsloth.

**Global HTTPS Access**:
Creates a free Cloudflare link that serves Unsloth - you can access the link globally (even on your phone!)
```bash
unsloth studio --secure
```
`-H 0.0.0.0` and different ports also work:
```bash
unsloth studio -H 0.0.0.0 -p 8888
```
**LAN Access (home network)**: `Settings > API keys > LAN access`

For a **reverse proxy or custom domain**, run the proxy on the same machine as Desktop (e.g., Cloudflare Named Tunnel, nginx, or Caddy). Set a comma-separated list of allowed hostnames, then quit and reopen Desktop.
```bash
export UNSLOTH_STUDIO_PROXY_HOSTS=st
