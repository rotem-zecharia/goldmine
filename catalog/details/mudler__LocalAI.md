# mudler/LocalAI

LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

## installation

### macOS

<a href="https://github.com/mudler/LocalAI/releases/latest/download/LocalAI.dmg">
  <img src="https://img.shields.io/badge/Download-macOS-blue?style=for-the-badge&logo=apple&logoColor=white" alt="Download LocalAI for macOS"/>
</a>

> **Note:** The DMG is not signed by Apple. After installing, run: `sudo xattr -d com.apple.quarantine /Applications/LocalAI.app`. See [#6268](https://github.com/mudler/LocalAI/issues/6268) for details.

### Containers (Docker, podman, ...)

> Already ran LocalAI before? Use `docker start -i local-ai` to restart an existing container.

#### CPU only:

```bash
docker run -ti --name local-ai -p 8080:8080 localai/localai:latest
```

#### NVIDIA GPU:

```bash
# CUDA 13
docker run -ti --name local-ai -p 8080:8080 --gpus all localai/localai:latest-gpu-nvidia-cuda-13

# CUDA 12
docker run -ti --name local-ai -p 8080:8080 --gpus all localai/localai:latest-gpu-nvidia-cuda-12

# NVIDIA Jetson ARM64 (CUDA 12, for AGX Orin and similar)
docker run -ti --name local-ai -p 8080:8080 --gpus all localai/localai:latest-nvidia-l4t-arm64

# NVIDIA Jetson ARM64 (CUDA 13, for DGX Spark)
docker run -ti --name local-ai -p 8080:8080 --gpus all localai/localai:latest-nvidia-l4t-arm64-cuda-13
```

#### AMD GPU (ROCm):

```bash
docker run -ti --name local-ai -p 8080:8080 --device=/dev/kfd --device=/dev/dri --group-add=video localai/localai:latest-gpu-hipblas
```

#### Intel GPU (oneAPI):

```bash
docker run -ti --name local-ai -p 8080:8080 --device=/dev/dri/card1 --device=/dev/dri/renderD128 localai/localai:latest-gpu-intel
```

#### Vulkan GPU:

```bash
docker run -ti --name local-ai -p 8080:8080 localai/localai:latest-gpu-vulkan
```

### Loading models

```bash
# From the model gallery (see available models with `local-ai models list` or at https://models.localai.io)
local-ai run llama-3.2-1b-instruct:q4_k_m
# From Huggingface
local-ai run huggingface://TheBloke/phi-2-GGUF/phi-2.Q8_0.gguf
# From the Ollama OCI registry
local-ai run ollama://gemma:2b

## configuration

local-ai run https://gist.githubusercontent.com/.../phi-2.yaml
# From a standard OCI registry (e.g., Docker Hub)
local-ai run oci://localai/phi-2:latest
```

To work with a running LocalAI server from the terminal, start the built-in agent from another shell. It answers questions, reads your files and runs commands on your machine, asking you to approve anything that changes state. Inside a session, `/models` lists installed models and `/model <name>` switches between them. See the [Terminal agent](https://localai.io/docs/features/terminal-agent/) docs.

```bash
# Terminal 1
local-ai run llama-3.2-1b-instruct:q4_k_m

# Terminal 2
local-ai chat --model llama-3.2-1b-instruct:q4_k_m
```

> **Automatic Backend Detection**: LocalAI automatically detects your GPU capabilities and downloads the appropriate backend. For advanced options, see [GPU Acceleration](https://localai.io/features/gpu-acceleration/).

For more details, see the [Getting Started guide](https://localai.io/basics/getting_started/).

## Latest News

- **October 2026**: **LocalAI 4.11.0** — Audio scenes with transcription, speaker labels, and sound detection. Also the Decisions API (`/v1/systemone`), model failover chains, signed OCI galleries, and Kimodo text-to-animation. [Release notes](https://github.com/mudler/LocalAI/releases/tag/v4.11.0)
- **September 2026**: **LocalAI 4.10.0** — A fleet operations dashboard, one credentials file for private model sources, and `local-ai benchmark` for measuring model latency and throughput. [Release notes](https://github.com/mudler/LocalAI/releases/tag/v4.10.0)
- **August 2026**: **LocalAI 4.9.0** — Deny-by-default authentication, opt-in chat context compression, unified model and backend management, and MiniMax-H3 video generation with audio. [Release notes](https://github.com/mudler/LocalAI/releases/tag/v4.9.0)
- **August 2026**: **LocalAI 4.8.0** — Introducing **vllm.cpp (alpha development builds)**, image-to-3D generation with a built-in viewer, and `audio.cpp` for speech, transcription, VAD, diarization, source separation and sound generation. [Release notes](https://github.com/mudler/LocalAI/releases/tag/v4.8.0)
- **July 2026**: **LocalAI 4.7.0** — Managed voice cloning profiles, local video and talking-avatar generation, and interleaved reasoning with tool calls. [Release notes](https://github.com/mudler/LocalAI/releases/tag/v4.7.0)
- **July 2026**: **LocalAI 4.6.0** — AMD ROCm fixes, predictable realtime pipeline warmup, conversation forking, and more reliable distributed model loading. [Release notes](https://github.com/mudler/LocalAI/releases/tag/v4.6.0)
- **June 2026**: **LocalAI 4.5.0** — Native depth estimation and sound-event detection, NER-based PII filtering, and speaker-aware realtime conversations with automatic history compaction. [Release notes](https://github.com/mudler/LocalAI/releases/tag/v4.5.0)

<details>
<summary>Older news</summary>

- **June 2026**: New native biometric backends from the LocalAI team: [voice-detect.cpp](https://github.com/localai-org/voice-detect.cpp) for speaker recognition and voice analysis (ECAPA-TDNN, WeSpeaker, ERes2Net, CAM++, wav2vec2 age/gender/emotion) and [face-detect.cpp](https://github.com/mudler/face-detect.cpp) for face detection, recognition, demographics and anti-spoofing (SCRFD/ArcFace, YuNet/SFace). Both are from-scratch C++/ggml engines with no Python or onnxruntime at inference, self-contained GGUF weights, bit-exact parity with the reference, and GPU cuDNN parity, replacing the heavier Python `insightface` and `speaker-recognition` backends ([PR #10441](https://github.com/mudler/LocalAI/pull/10441)).
- **June 2026**: New [realtime voice assistant demo](https://github.com/localai-org/localai-realtime-demo) (a tiny Go client for the Realtime API with a full talk-back voice loop and tool calling), plus [streaming of the realtime LLM / TTS / transcription pipeline stages](https://github.com/mudler/LocalAI/pull/10176) and [configurable WebRTC ICE candidates](https:/

## features

- [Text generation](https://localai.io/features/text-generation/) (`llama.cpp`, `transformers`, `vllm` ... [and more](https://localai.io/model-compatibility/))
- [Text to Audio](https://localai.io/features/text-to-audio/)
- [Audio to Text](https://localai.io/features/audio-to-text/)
- [Image generation](https://localai.io/features/image-generation)
- [OpenAI-compatible tools API](https://localai.io/features/openai-functions/)
- [Realtime API](https://localai.io/features/openai-realtime/) (Speech-to-speech)
- [Embeddings generation](https://localai.io/features/embeddings/)
- [Constrained grammars](https://localai.io/features/constrained_grammars/)
- [Download models from Huggingface](https://localai.io/models/)
- [Vision API](https://localai.io/features/gpt-vision/)
- [Object Detection](https://localai.io/features/object-detection/)
- [Reranker API](https://localai.io/features/reranker/)
- [P2P Inferencing](https://localai.io/features/distribute/)
- [Distributed Mode](https://localai.io/features/distributed-mode/) — Horizontal scaling with PostgreSQL + NATS
- [Model Context Protocol (MCP)](https://localai.io/docs/features/mcp/)
- [Built-in Agents](https://localai.io/features/agents/) — Autonomous AI agents with tool use, RAG, skills, SSE streaming, and [Agent Hub](https://agenthub.localai.io)
- [Backend Gallery](https://localai.io/backends/) — Install/remove backends on the fly via OCI images
- Voice Activity Detection (Silero-VAD)
- Integrated WebUI

## Supported Backends & Acceleration

LocalAI supports **60+ backends** including llama.cpp, vLLM, SGLang, transformers, whisper.cpp, diffusers, MLX, MLX-VLM, and many more. Hardware acceleration is available for **NVIDIA** (CUDA 12/13), **AMD** (ROCm), **Intel** (oneAPI/SYCL), **Apple Silicon** (Metal), **Vulkan**, and **NVIDIA Jetson** (L4T). All backends can be installed on-the-fly from the [Backend Gallery](https://localai.io/backends/).

See the full [Backend & Model Compatibility Table](https://localai.io/model-compatibility/) and [GPU Acceleration guide](https://localai.io/features/gpu-acceleration/).

### Backends built by us

Most backends wrap a best-in-class upstream engine. A handful of them are native C/C++/GGML engines (no Python at inference) developed and maintained by the LocalAI project itself:

| Backend | What it does |
|---------|-------------|
| [vllm.cpp](https://github.com/mudler/vllm.cpp) | From-scratch C++20 port of vLLM for text generation: paged KV cache, continuous batching, prefix caching, safetensors + GGUF loading, engine-enforced structured output, on CPU, CUDA, Metal and Vulkan. Also serves MiniMax-H3 joint video+audio generation |
| [parakeet.cpp](https://github.com/mudler/parakeet.cpp) | C++/GGML port of NVIDIA NeMo Parakeet ASR (tdt/ctc/rnnt/hybrid), with cache-aware streaming transcription |
| [moss-transcribe.cpp](https://github.com/localai-org/moss-transcribe.cpp) | C++/GGML port of OpenMOSS MOSS-Transcribe-Diarize: joint long-form transcription, speaker diarization and timestamping in a single pass |
| [moss-tts.cpp](https://github.com/mudler/moss-tts.cpp) | C++/GGML port of the OpenMOSS MOSS-TTS family: text-to-speech (MOSS-TTS-Local v1.5, 48 kHz stereo) with reference-audio voice cloning, through the MOSS-Audio-Tokenizer neural codec |
| [magpie-tts.cpp](https://github.com/mudler/magpie-tts.cpp) | C++/GGML port of NVIDIA's Magpie TTS Multilingual 357M: 22.05 kHz mono text-to-speech in 5 voices and 9+ languages, with the NanoCodec neural codec and tokenizer/G2P embedded in a single GGUF |
| [ced.cpp](https://github.com/localai-org/ced.cpp) | C++/GGML port of the CED audio-tagging models: sound-event classification (527-class AudioSet) over REST and the realtime API for live recognition |
| [voice-detect.cpp](https://github.com/localai-org/voice-detect.cpp) | Speaker recognition and voice analysis (ECAPA-TDNN, WeSpeaker, ERes2Net, CAM++, wav2vec2 age/gender/emotion), replacing the Python speaker-recognition backend |
| [voxtral-tts.c](https
