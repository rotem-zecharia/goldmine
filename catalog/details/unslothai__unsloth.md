# unslothai/unsloth

Local UI to run and train LLMs and diffusion models. Supports GGUF, MLX, Qwen3.8, Kimi K3, MiniMax-H3, Gemma 4, FLUX and more.

## features

Unsloth works on **Windows, Linux, WSL** and **macOS**. We support **Multi GPU setups, NVIDIA, AMD, Intel GPUs, CPUs** and the **Vulkan** backend.

### Run & Build with AI
* Run and train LLMs, diffusion, embedding, audio models: [Qwen3.8](https://unsloth.ai/docs/models/qwen3.8), [Kimi K3](https://unsloth.ai/docs/models/kimi-k3), MiniMax-H3, [Muse Glimmer](https://unsloth.ai/docs/models/muse-glimmer), [DeepSeek-V4](https://unsloth.ai/docs/models/deepseek-v4), [Gemma 4](https://unsloth.ai/docs/models/gemma-4).
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
| Hermes Agent | `unsloth start hermes` |
| OpenClaw | `unsloth start openclaw` |
| OpenCode | `unsloth start opencode` |

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
Use our [Docker image](https://hub.docker.com/r/unsloth/unsloth) ```unsloth/unsloth``` container. Run:
```bash
docker run -d -e JUPYTER_PASSWORD="mypassword" \
  -p 8888:8888 -p 8000:8000 -p 2222:22 \
  -v $(pwd)/work:/workspace/work \
  --gpus all \
  unsloth/unsloth
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

#### Password management & headless starts
Headless starts:
```bash
UNSLOTH_STUDIO_PASSWORD='your-strong-password' unsloth studio --secure   # via env var
```
Reset your password:
```bash
unsloth studio reset-password
```

#### Developer, Nightly, Uninstall
To see developer, nightly and uninstallation etc. instructions, see [advanced installation](#-advanced-installation).

### Unsloth Core (code-based)
#### Linux, WSL:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv unsloth_env --python 3.13
source unsloth_env/bin/activate
uv pip install unsloth --torch-backend=auto
```
#### Windows:
```powershell
winget install -e --id Python.Python.3.13
winget install --id=astral-sh.uv  -e
uv venv unsloth_env --python 3.13
.\unsloth_env\Scripts\activate
uv pip install unsloth --torch-backend=auto
```

#### AMD, Intel, DGX Spark, Blackwell:
See our [Blackwell guide](https://unsloth.ai/docs/blog/fine-tuning-llms-with-blackwell-rtx-50-series-and-unsloth) and [DGX Spark guide](https://unsloth.ai/docs/blog/fine-tuning-llms-with-nvidia-dgx-spark-and-unsloth). <br>
To install Unsloth on **AMD** and **Intel** GPUs, follow our [AMD Guide](https://unsloth.ai/docs/basics/amd) and [Intel Guide](https://unsloth.ai/docs/get-started/install/intel).

## 📒 Free Notebooks

Train for free with our notebooks.
Read our [guide](https://unsloth.ai/docs/get-started/fine-tuning-llms-guide). Add dataset, run, then deploy your trained model.

| Model | Free Notebooks | Performance | Memory use |
|-----------|---------|--------|----------|
| **Unsloth Studio**      | [▶️ Start for free](https://colab.research.google.com/github/unslothai/unsloth/blob/main/studio/Unsloth_Studio_Colab.ipynb)               |  |  |
| **Gemma 4 (E2B)**      | [▶️ Start for free](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma4_(E2B)-Vision.ipynb)               | 1.5x faster | 50% 
