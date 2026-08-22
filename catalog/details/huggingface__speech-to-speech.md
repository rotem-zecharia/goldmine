# huggingface/speech-to-speech

Build voice agents with open-source models

## installation

```bash
pip install speech-to-speech
export OPENAI_API_KEY=...
speech-to-speech serve
```

This starts an OpenAI Realtime-compatible server at `ws://localhost:8765/v1/realtime` using Parakeet TDT for local STT, an OpenAI-compatible LLM, and Qwen3-TTS for local speech output.

Talk to it from a second terminal:

```bash
speech-to-speech talk --url ws://127.0.0.1:8765/v1/realtime
```

To start the server and packaged microphone/speaker client in one command:

```bash
speech-to-speech local
```

Prefer to keep the LLM on your own machine? Serve Gemma 4 with llama.cpp:

```bash
llama-server -hf ggml-org/gemma-4-E4B-it-GGUF -np 2 -c 65536 -fa on --swa-full
```

Then point the OpenAI-compatible LLM backend at it:

```bash
speech-to-speech serve \
    --model_name "ggml-org/gemma-4-E4B-it-GGUF" \
    --responses_api_base_url "http://127.0.0.1:8080/v1" \
    --responses_api_api_key ""
```

Clients using the implemented core Realtime event set can connect. The official OpenAI Agents SDK is tested over both stock transports; see [Realtime API](#realtime-api) for the tested surface and [LLM backends](#llm-backends) for provider and local-server options.

## Index

* [How it works](#how-it-works)
* [Installation](#installation)
* [Offline operation](#offline-operation)
* [Supported components](#supported-components)
* [Commands](#commands)
* [Realtime API](#realtime-api)
* [LLM backends](#llm-backends)
* [Multi-language support](#multi-language-support)
* [Pocket TTS](#pocket-tts)
* [CLI reference](#cli-reference)
* [Contributing](#contributing)
* [Star history](#star-history)
* [Citations](#citations)

## How it works

The pipeline is a cascade of four components, each running in its own thread and connected by queues:

1. **Voice Activity Detection (VAD)**: [Silero VAD v5](https://github.com/snakers4/silero-vad) detects speech boundaries and turn-taking.
2. **Speech to Text (STT)**: transcribes the user's turn, with optional live partial transcripts.
3. **Language Model (LLM)**: generates the response, streaming text and tool calls.
4. **Text to Speech (TTS)**: synthesizes audio and streams it back to the client.

Every stage has multiple interchangeable backends, selected via CLI flags. The code is designed for easy modification, with a focus on models available through Transformers and the Hugging Face Hub.

## Installation

Requires Python 3.10+.

```bash
pip install speech-to-speech
```

The default install covers the standard realtime path:

- Parakeet TDT for STT
- OpenAI-compatible API for the language model
- Qwen3-TTS for speech output, using the GGML backend by default on non-macOS platforms and `mlx-audio` on Apple Silicon
- local audio and realtime server modes

macOS and non-macOS dependencies are resolved automatically via platform markers in `pyproject.toml`.

### CUDA Note for Qwen3-TTS

On Linux, the Qwen3-TTS GGML backend comes from `faster-qwen3-tts[ggml]`. Its default `qwentts-cpp-python` wheel on PyPI targets CUDA 12.8. If your machine does not have the CUDA 12 runtime that wheel expects, install the matching wheel from the Hugging Face wheelhouse before installing `speech-to-speech`:

```bash
# CUDA 13.x
pip install "qwentts-cpp-python==0.3.1+cu130" \
  -f https://huggingface.co/datasets/andito/qwentts-cpp-python-wheels/tree/main/whl/cu130

# CUDA 12.4
pip install "qwentts-cpp-python==0.3.1+cu124" \
  -f https://huggingface.co/datasets/andito/qwentts-cpp-python-wheels/tree/main/whl/cu124

# CPU-only fallback
pip install "qwentts-cpp-python==0.3.1+cpu" \
  -f https://huggingface.co/datasets/andito/qwentts-cpp-python-wheels/tree/main/whl/cpu

pip install speech-to-speech
```

To use the previous CUDA-graphs implementation instead of GGML, pass `--qwen3_tts_backend torch`.

### Optional Components

Optional components are installed with pip extras:

```bash
pip install "speech-to-speech[kokoro]"          # Kokoro-82M TTS on non-macOS
pip install "speech-to-speech[pocket]"          # Pocket TTS
pip install "speech-to-s

## tools

| Command | Behavior | Use it when |
|---|---|---|
| `serve` | Runs the pipeline server over OpenAI Realtime WebSocket and WebRTC. | You are building an app or device against the API. |
| `talk --url <full-realtime-url>` | Runs the packaged microphone/speaker client. | You want to talk to an existing Realtime server. |
| `local` | Composes `serve` and `talk` in-process over loopback. | You want to run the server and talk to it from one command. |

`serve` binds to `127.0.0.1` by default; pass `--host 0.0.0.0` explicitly for network exposure. `local` always binds to loopback and connects the same packaged client at `ws://127.0.0.1:<port>/v1/realtime`.

The packaged client can opt in to local Python tools with `talk --tool-module <module>` or `local --tool-module <module>`. The module contract, programmatic API, and a Serper web-search example are documented in [Tool calling design](./src/speech_to_speech/api/openai_realtime/README.md#packaged-python-client-tools).

### Migrating from `--mode`

`--mode` is deprecated and will stop working soon. During this migration window, `speech-to-speech --mode realtime` runs `speech-to-speech serve`, and `speech-to-speech --mode local` runs `speech-to-speech local`; both print a warning. All other mode values have been removed and exit with guidance to use the new commands.

### Realtime Server

```bash
export OPENAI_API_KEY=...
speech-to-speech serve
```

This is equivalent to:

```bash
speech-to-speech serve \
    --thresh 0.6 \
    --stt parakeet-tdt \
    --llm_backend responses-api \
    --tts qwen3 \
    --qwen3_tts_model_name Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice \
    --qwen3_tts_speaker Aiden \
    --qwen3_tts_language auto \
    --qwen3_tts_backend ggml \
    --qwen3_tts_non_streaming_mode True \
    --qwen3_tts_mlx_quantization 6bit \
    --model_name gpt-5.6-terra \
    --chat_size 30 \
    --responses_api_stream \
    --enable_live_transcription
```

The default model is `gpt-5.6-terra` through the OpenAI Responses API with reasoning effort `none`, preserving the previous default model's latency-oriented reasoning behavior. Override the model with `--model_name`, the effort with `--responses_api_reasoning_effort`, and set `--responses_api_base_url` for another OpenAI-compatible provider or server.

### Local Mac

```bash
speech-to-speech local --mac-optimal-settings
```

Optionally with a specific LLM:

```bash
speech-to-speech local \
    --mac-optimal-settings \
    --model_name mlx-community/Qwen3-4B-Instruct-2507-bf16
```

This setting:

- Uses MPS defaults for supported model components.
- Sets Parakeet TDT for STT.
- Sets MLX LM as the LLM backend.
- Sets Qwen3-TTS for TTS, using `mlx-audio` with the `6bit` MLX variant by default.

The preset supplies these as defaults only: explicit `--device`, component-device flags such as `--qwen3_tts_device`, and `--stt`, `--llm_backend`, `--model_name`, and `--tts` all win. Use it with `serve` instead of `local` when you want to expose the server without starting the microphone/speaker client.

`--tts pocket` and `--tts kokoro` are also valid on macOS.

To compare the MLX quantization variants locally:

```bash
python scripts/benchmark_tts.py \
    --handlers qwen3 \
    --iterations 3 \
    --qwen3_mlx_quantizations bf16 4bit 6bit 8bit
```

### Docker

Install the [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html), then:

```bash
docker compose up
```

The compose file starts a llama.cpp server with Gemma 4 and the Realtime server, exposing ports `8080` and `8765`.

## Realtime API

Realtime mode supports the OpenAI Realtime protocol over WebSocket and WebRTC, with live transcription and low-latency turn-taking. WebSocket clients connect at `/v1/realtime`:

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:8765/v1",
    websocket_base_url="ws://localhost:8765/v1",
    api_key="not-needed",
)

with client.realtime.connect(model="lo
