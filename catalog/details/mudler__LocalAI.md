# mudler/LocalAI

LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

## installation

**Script** (Linux, and macOS on Apple Silicon): it downloads the release binary for your machine and checks it against the release checksums.

```bash
curl -sSL https://localai.io/install.sh | sh
local-ai run qwen3-4b
```

**Container** (Docker, podman, ...):

```bash
docker run -ti --name local-ai -p 8080:8080 localai/localai:latest
```

**macOS app**: download [LocalAI.dmg](https://github.com/mudler/LocalAI/releases/latest/download/LocalAI.dmg). The DMG is signed with an Apple Developer ID and notarized.

The script, the app and the latest container image give version 4.12.1. The add-ons, Office, Sandbox and team features described below need a development build or a newer release.

Then open `http://localhost:8080`. To restart an existing container, use `docker start -i local-ai`. More ways to install: [Install LocalAI](https://localai.io/docs/start/install/).

<details>
<summary>GPU images (NVIDIA, AMD, Intel, Vulkan)</summary>

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
docker run -ti --name local-ai -p 8080:8080 --device=/dev/kfd --device=/dev/dri --group-add=video localai/localai:latest-gpu-hipblas

## tools

docker run -ti --name local-ai -p 8080:8080 --device=/dev/dri/card1 --device=/dev/dri/renderD128 localai/localai:latest-gpu-intel

# Vulkan
docker run -ti --name local-ai -p 8080:8080 localai/localai:latest-gpu-vulkan
```

LocalAI detects your GPU and downloads the matching backend. See [GPU Acceleration](https://localai.io/docs/models/gpu-acceleration/).

</details>

Load a model:

```bash
# From the model gallery (list it with `local-ai models list` or at https://models.localai.io)
local-ai run qwen3-4b
# From Hugging Face
local-ai run huggingface://TheBloke/phi-2-GGUF/phi-2.Q8_0.gguf
# From the Ollama OCI registry
local-ai run ollama://gemma:2b
# From a standard OCI registry (for example Docker Hub)
local-ai run oci://localai/phi-2:latest
```

To talk to a running server from the terminal, start the built-in agent in another shell. It asks you to approve anything that changes state. See the [Terminal agent](https://localai.io/docs/features/terminal-agent/) docs.

```bash
local-ai chat --model qwen3-4b
```

More in the [Quickstart](https://localai.io/docs/start/quickstart/).

## What you can do

| Area | What it gives you |
|---|---|
| [Chats](https://localai.io/docs/features/chats/) | Conversations the server keeps, with saved agents that use tools, [MCP](https://localai.io/docs/features/mcp/), skills and files, triggers, and chat apps |
| [Add-ons](https://localai.io/docs/addons/) | Office, Sandbox, Tables, Telegram, Slack, Discord, mail, calendar and more install from a library and run beside the server (development builds) |
| [Text generation](https://localai.io/docs/models/capabilities/text/text-generation/) | `llama.cpp`, `transformers`, `vllm` ... [and more](https://localai.io/docs/models/compatibility-table/), with an [OpenAI-compatible tools API](https://localai.io/docs/api/openai-functions/) and [constrained grammars](https://localai.io/docs/models/capabilities/text/constrained_grammars/) |
| Speech | [Text to audio](https://localai.io/docs/models/capabilities/audio/text-to-audio/), [audio to text](https://localai.io/docs/models/capabilities/audio/audio-to-text/), voice activity detection (Silero-VAD) and the [Realtime API](https://localai.io/docs/api/openai-realtime/) for speech-to-speech |
| Images and vision | [Image generation](https://localai.io/docs/models/capabilities/vision/image-generation/), the [Vision API](https://localai.io/docs/models/capabilities/vision/gpt-vision/) and [object detection](https://localai.io/docs/models/capabilities/vision/object-detection/) |
| Search | [Embeddings](https://localai.io/docs/models/capabilities/text/embeddings/) and a [reranker](https://localai.io/docs/models/capabilities/text/reranker/) |
| Operations | API key auth, user quotas and roles, [distributed mode](https://localai.io/docs/administration/distributed-mode/) (PostgreSQL + NATS) and [P2P inferencing](https://localai.io/docs/administration/p2p-federated-inference/) |
| Models and backends | [Models from Hugging Face](https://localai.io/docs/models/) and a [Backend Gallery](https://localai.io/docs/models/backends/) to install or remove backends on the fly, plus the integrated web UI |

LocalAI has more than 80 backends. Hardware acceleration covers NVIDIA (CUDA 12 and 13), AMD (ROCm), Intel (oneAPI/SYCL), Apple Silicon (Metal), Vulkan and NVIDIA Jetson (L4T). See the [Backend and Model Compatibility Table](https://localai.io/docs/models/compatibility-table/).

## Backends we build

Most backends wrap a best-in-class upstream engine. A handful of them are native C/C++/GGML engines (no Python at inference) developed and maintained by the LocalAI project itself:

| Backend | What it does |
|---------|-------------|
| [vllm.cpp](https://github.com/mudler/vllm.cpp) | From-scratch C++20 port of vLLM for text generation: paged KV cache, continuous batching, prefix caching, safetensors + GGUF loading, engine-enforced structured output, on CPU, CUDA, Metal and Vulkan. Also serves MiniMax-H3 joint video+audio generation |

