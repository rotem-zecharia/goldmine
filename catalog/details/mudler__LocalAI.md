# mudler/LocalAI

LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

## installation

<p align="center">
<a href="https://github.com/mudler/LocalAI/releases/latest/download/LocalAI.dmg"><img src="https://img.shields.io/badge/Download%20for%20macOS-DMG%2C%20Apple%20silicon-111111?style=flat-square&logo=apple" alt="Download for macOS (DMG, Apple silicon)"></a>
<a href="https://github.com/mudler/LocalAI/releases/latest/download/LocalAI-Launcher-x86_64.AppImage"><img src="https://img.shields.io/badge/Download%20for%20Linux-AppImage%2C%20x86--64-1f6feb?style=flat-square&logo=linux&logoColor=white" alt="Download for Linux (AppImage, x86-64)"></a>
<a href="https://github.com/mudler/LocalAI/releases/latest/download/LocalAI-Launcher-arm64.AppImage"><img src="https://img.shields.io/badge/Download%20for%20Linux-AppImage%2C%20ARM64-1f6feb?style=flat-square&logo=linux&logoColor=white" alt="Download for Linux (AppImage, ARM64)"></a>
<a href="https://github.com/mudler/LocalAI/releases/latest/download/LocalAI-Launcher-Setup-x64.exe"><img src="https://img.shields.io/badge/Download%20for%20Windows-installer%2C%20x64%20(experimental)-0078d4?style=flat-square" alt="Download for Windows (installer, x64, experimental)"></a>
</p>

The buttons download the desktop app from the latest release. For other ways to install, see [Install LocalAI](https://localai.io/docs/start/install/).

**Script** (Linux, and macOS on Apple Silicon): it downloads the release binary for your machine and checks it against the release checksums.

```bash
curl -sSL https://localai.io/install.sh | sh
local-ai
# open http://localhost:8080 and install a model from there
```

The script installs the program and does not start it; `local-ai` starts the server. To run a model directly, name it, for example `local-ai run gemma-4-e2b-it-qat-q4_0`, a small Google Gemma 4 model for CPUs (4.3 GB to download: 3.35 GB for the model and 0.99 GB for the image projector).

**Container** (Docker Compose): the compose file keeps models, backends, settings and data in named volumes.

```bash
curl -fsSL https://localai.io/install/docker-compose.yaml -o docker-compose.yaml
docker compose up -d
```

**Desktop app**: it installs, updates, starts and stops the server for you and shows the web interface in its own window, on macOS and Linux (Windows is experimental). Use the download buttons above. See the [desktop app guide](https://localai.io/docs/start/install/desktop/).

The install script and the `latest` image give 5.0.0.

Then open `http://localhost:8080`. To upgrade the container, run `docker compose pull && docker compose up -d`. More ways to install, and `docker run` and Podman commands: [Containers](https://localai.io/docs/start/install/containers/).

<details>
<summary>GPU images (NVIDIA, AMD, Intel, Vulkan)</summary>

In `docker-compose.yaml`, change `image` to one of these tags and remove the `#` from the block for your GPU. With `docker run`, use these flags, and add the `-v` options from [Containers](https://localai.io/docs/start/install/containers/#quick-start) to keep your data:

```bash
# NVIDIA, CUDA 13
docker run -ti --name local-ai -p 8080:8080 --gpus all localai/localai:latest-gpu-nvidia-cuda-13

# NVIDIA, CUDA 12
docker run -ti --name local-ai -p 8080:8080 --gpus all localai/localai:latest-gpu-nvidia-cuda-12

# NVIDIA Jetson ARM64 (CUDA 12, for AGX Orin and similar)
docker run -ti --name local-ai -p 8080:8080 --gpus all localai/localai:latest-nvidia-l4t-arm64

# NVIDIA Jetson ARM64 (CUDA 13, for DGX Spark)
docker run -ti --name local-ai -p 8080:8080 --gpus all localai/localai:latest-nvidia-l4t-arm64-cuda-13

# AMD (ROCm)
docker run -ti --name local-ai -p 8080:8080 --device=/dev/kfd --device=/dev/dri localai/localai:latest-gpu-hipblas

## tools

docker run -ti --name local-ai -p 8080:8080 --device=/dev/dri/card1 --device=/dev/dri/renderD128 localai/localai:latest-gpu-intel

# Vulkan
docker run -ti --name local-ai -p 8080:8080 --device=/dev/dri localai/localai:latest-gpu-vulkan
```

LocalAI detects your GPU and downloads the matching backend. See [GPU Acceleration](https://localai.io/docs/models/gpu-acceleration/).

</details>

Load a model:

```bash
# From the model gallery (list it with `local-ai models list` or on the Models page of the web UI)
local-ai run gemma-4-e2b-it-qat-q4_0
# From Hugging Face
local-ai run huggingface://TheBloke/phi-2-GGUF/phi-2.Q8_0.gguf
# From the Ollama OCI registry
local-ai run ollama://gemma:2b
# From a standard OCI registry (for example Docker Hub)
local-ai run oci://localai/phi-2:latest
```

To talk to a running server from the terminal, start the built-in agent in another shell. It asks you to approve anything that changes state. See the [Terminal agent](https://localai.io/docs/features/terminal-agent/) docs.

```bash
local-ai chat --model gemma-4-e2b-it-qat-q4_0
```

More in the [Quickstart](https://localai.io/docs/start/quickstart/).

## What you can do

| Area | What it gives you |
|---|---|
| [Chats](https://localai.io/docs/features/chats/) | Conversations the server keeps, with saved agents that use tools, [MCP](https://localai.io/docs/features/mcp/), skills and files, triggers, and chat apps |
| [Add-ons](https://localai.io/docs/addons/) | Office, Sandbox, Tables, chat apps, mail, calendar and more install from a library and run beside the server |
| [Text generation](https://localai.io/docs/models/capabilities/text/text-generation/) | `llama.cpp`, `transformers`, `vllm` ... [and more](https://localai.io/docs/models/compatibility-table/), with an [OpenAI-compatible tools API](https://localai.io/docs/api/openai-functions/) and [constrained grammars](https://localai.io/docs/models/capabilities/text/constrained_grammars/) |
| Music and sound | Make music and sound effects from a text prompt with `/v1/sound-generation`. See [text to audio](https://localai.io/docs/models/capabilities/audio/text-to-audio/) |
| Speech | [Text to audio](https://localai.io/docs/models/capabilities/audio/text-to-audio/), [audio to text](https://localai.io/docs/models/capabilities/audio/audio-to-text/), voice activity detection (Silero-VAD) and the [Realtime API](https://localai.io/docs/api/openai-realtime/) for speech-to-speech |
| Images, video and vision | [Image generation](https://localai.io/docs/models/capabilities/vision/image-generation/), [video generation](https://localai.io/docs/models/capabilities/vision/video-generation/), the [Vision API](https://localai.io/docs/models/capabilities/vision/gpt-vision/) and [object detection](https://localai.io/docs/models/capabilities/vision/object-detection/) |
| Search | [Embeddings](https://localai.io/docs/models/capabilities/text/embeddings/) and a [reranker](https://localai.io/docs/models/capabilities/text/reranker/) |
| Operations | API key auth, user quotas and roles, [distributed mode](https://localai.io/docs/administration/distributed-mode/) (PostgreSQL + NATS) and [P2P](https://localai.io/docs/administration/p2p/) |
| Models and backends | [Models from Hugging Face](https://localai.io/docs/models/) and a [Backend Gallery](https://localai.io/docs/models/backends/) to install or remove backends on the fly, plus the integrated web UI |

LocalAI has more than 80 backends. Hardware acceleration covers NVIDIA (CUDA 12 and 13), AMD (ROCm), Intel (oneAPI/SYCL), Apple Silicon (Metal), Vulkan and NVIDIA Jetson (L4T). See the [Backend and Model Compatibility Table](https://localai.io/docs/models/compatibility-table/).

## Backends we build

Most backends wrap an upstream engine such as llama.cpp or vLLM. We wrote 18 of them ourselves: native C, C++ and GGML engines with no Python at inference.

| Backend | What it does |
|---------|-------------|
| [vllm.cpp](https://github.com/mudler/vllm.cpp) | From-scratch C
