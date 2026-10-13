# huggingface/speech-to-speech

Build voice agents with open-source models

## installation

Use Python 3.10+ (3.11 recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install speech-to-speech
speech-to-speech local
```

Then talk: speak, pause, and the assistant answers through your speakers. Stop with `Ctrl+C`. The first run downloads the models, so give it a few minutes. Use headphones so the assistant does not hear itself, or add `--local_audio_block_mic_during_playback`.

On Ubuntu, first install the audio libraries with `sudo apt-get install libportaudio2 libsndfile1`. The default Linux Qwen3-TTS wheel targets CUDA 12.8 and Ubuntu 24.04; see the [CUDA note](#cuda-note-for-qwen3-tts) for other systems. On Windows, activate the environment with `.venv\Scripts\Activate.ps1`.

The command picks local models for your platform:

| Platform | LLM | Plan for |
|---|---|---|
| Apple Silicon Mac | [Qwen3.5-4B 4-bit](https://huggingface.co/mlx-community/Qwen3.5-4B-4bit) via MLX LM | 16 GB of unified memory |
| Linux / Windows with NVIDIA | [Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B) via Transformers | 24 GB of VRAM |
| Other machines | Qwen3.5-4B via Transformers on CPU | Slow replies |

Speech recognition and synthesis run locally too. After the first run, everything works [offline](#offline-operation). To use another model, a llama.cpp server, or a hosted provider, see [LLM backends](#llm-backends).

### Connect your own app

`local` runs a server and a microphone client in one process. To run only the server:

```bash
speech-to-speech serve
```

It listens at `ws://127.0.0.1:8765/v1/realtime`. Connect with:

- the packaged audio client: `speech-to-speech talk --url ws://127.0.0.1:8765/v1/realtime`
- the [browser demo](./demo/README.md#quick-start-local)
- any client using the core OpenAI Realtime events; the OpenAI Agents SDK is tested over both transports (see [Realtime API](#realtime-api))
- [LiveKit Agents](./demo/livekit/README.md), as the agent's realtime model

## Index

* [How it works](#how-it-works)
* [Quickstart](#quickstart)
* [Installation](#installation)
* [YAML configuration API](./docs/configuration.md)
* [Offline operation](#offline-operation)
* [Supported components](#supported-components)
* [Commands](#commands)
* [Realtime API](#realtime-api)
* [LLM backends](#llm-backends)
* [Multi-language support](#multi-language-support)
* [OmniVoice](#omnivoice)
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

Optional speech-to-viseme extraction adds timed mouth shapes for avatar and robot
clients after TTS. Enable it with `--enable_visemes`; see the
[viseme guide](src/speech_to_speech/STV/README.md) for client events and timing.

## Installation

`pip install speech-to-speech` (see the [Quickstart](#quickstart)) includes everything the default pipeline needs:

- Silero VAD and Parakeet TDT for listening
- Qwen3.5-4B for replies: MLX LM on macOS, Transformers elsewhere
- Qwen3-TTS for speech: `mlx-audio` on Apple Silicon, GGML elsewhere
- the local audio client and the Realtime server

Platform-specific dependencies are resolved automatically.

See the [configuration guide](./docs/configuration.md) for reusable blocks,
named pipelines, environment references, and explic

## tools

| Command | Behavior | Use it when |
|---|---|---|
| `serve` | Runs the pipeline server over OpenAI Realtime WebSocket and WebRTC. | You are building an app or device against the API. |
| `talk --url <full-realtime-url>` | Runs the packaged microphone/speaker client. | You want to talk to an existing Realtime server. |
| `local` | Composes `serve` and `talk` in-process over loopback. | You want to run the server and talk to it from one command. |

`serve` binds to `127.0.0.1` by default; pass `--host 0.0.0.0` explicitly for network exposure. `local` always binds to loopback and connects the same packaged client at `ws://127.0.0.1:<port>/v1/realtime`.

The command only decides how the server and client run. Where replies are generated is set by `--llm_backend`, which is local by default for every command.

The packaged `local` client buffers 196 ms of received audio when using the
OpenAI-compatible TTS backend, which absorbs short delivery gaps from HTTP
speech inference. Other `local` backends and `talk` start playback immediately
by default. Use `--playback-buffer-ms <milliseconds>` to override either
default: a larger value resists stuttering but delays the start of each
response, while a smaller value starts sooner but is more sensitive to jitter.
This setting only controls the packaged Python client's speakers; browser and
other Realtime clients manage their own playback buffers.

The packaged client can opt in to local Python tools with `talk --tool-module <module>` or `local --tool-module <module>`. The module contract, programmatic API, and web-search examples (Serper, or keyless You.com) are documented in [Tool calling design](./src/speech_to_speech/api/openai_realtime/README.md#packaged-python-client-tools).

### Migrating from `--mode`

`--mode` is deprecated and will stop working soon. During this migration window, `speech-to-speech --mode realtime` runs `speech-to-speech serve`, and `speech-to-speech --mode local` runs `speech-to-speech local`; both print a warning. All other mode values have been removed and exit with guidance to use the new commands.

### Local Mac

On macOS, `local` and `serve` already run all three models through MLX. The optional `--mac-optimal-settings` preset also makes MPS the default device for supported components. It only sets defaults: explicit `--device`, component-device flags such as `--qwen3_tts_device`, and `--stt`, `--llm_backend`, `--model_name`, and `--tts` all win.

`--tts pocket`, `--tts kokoro`, `--tts omnivoice`, and `--tts kitten` are also valid on macOS.

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

The server logs per-response STT, LLM, first TTS audio, and speech-to-audio
durations for supported backends, including vLLM-backed STT and TTS. See the
[response latency guide](./docs/response-latency.md) for the coverage matrix
and measurement boundaries.

Realtime mode supports the OpenAI Realtime protocol over WebSocket and WebRTC, with live transcription and low-latency turn-taking. WebSocket clients connect at `/v1/realtime`:

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:8765/v1",
    websocket_base_url="ws://localhost:8765/v1",
    api_key="not-needed",
)

with client.realtime.connect(model="local") as conn:
    conn.send(
        {
            "type": "session.update",
            "session": {
                "type": "realtime",
                "instructions": "You are a helpful assistant.",
                "audio": {
                    "input": {
                        "tur
