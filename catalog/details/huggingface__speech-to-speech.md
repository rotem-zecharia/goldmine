# huggingface/speech-to-speech

Build voice agents with open-source models

## installation

Use CPython 3.11–3.14 (3.11 recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install speech-to-speech
speech-to-speech local
```

Then talk: speak, pause, and the assistant answers through your speakers. Stop with `Ctrl+C`. The first run downloads the models, so give it a few minutes. On speakers, add `--echo-cancellation` so the assistant does not hear itself and you can still interrupt it by voice; headphones don't need it. See [echo cancellation](docs/echo-cancellation.md) for requirements and limits.

By default, `local` and `talk` show final user transcripts and streaming assistant
replies once, hiding backend transcript copies, routine logs, tool details, and protocol
events. User messages are yellow and assistant replies are green in a color-capable
terminal. Startup shows `Loading models…`, followed by `Ready — start speaking.` once
the audio devices are running and the session is configured. Routine model-loading
output is hidden; startup failures show their diagnostics. Runtime warnings and errors
remain visible.

For diagnostic output, add `--verbose`:

```bash
speech-to-speech local --verbose
```

Use `--verbose --log_level debug` for more detailed local logs. Raw event output
(`local --local_audio_print_json` or `talk --print-json`) also enables diagnostic output.

On Ubuntu, first install the audio libraries with `sudo apt-get install libportaudio2 libsndfile1`. The default Linux Qwen3-TTS wheel targets CUDA 12.8 and Ubuntu 24.04; see the [CUDA note](#cuda-note-for-qwen3-tts) for other systems. On Windows, activate the environment with `.venv\Scripts\Activate.ps1`.

The default installation has the following CI coverage:

| Platform | Supported CPython versions | Checks |
|---|---|---|
| Linux | 3.11, 3.12, 3.13, 3.14 | Full test suite and installed package smoke test |
| Apple Silicon macOS | 3.11, 3.12, 3.13, 3.14 | Installed package smoke test |

Optional model backends can have narrower Python requirements. Windows is not
covered by this compatibility matrix. Python 3.10 is no longer supported following
its end of life on October 1, 2026.

Kokoro is optional on every platform. On macOS, its Misaki dependency requires
Python <3.13, so use Python 3.11 or 3.12 with `speech-to-speech[kokoro]`.
The default Qwen3-TTS backend does not require Misaki. Python 3.15 is not yet
supported on any platform: ONNX Runtime lacks CPython 3.15 wheels, and the pinned macOS PyTorch
release also lacks them. Newer Python versions will be added after the default
dependencies and CI checks pass; the package's `requires-python` lower bound does
not promise compatibility with future Python releases.

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
* [YAML configu

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

By default, user speech interrupts the assistant: the server cancels the
response and the packaged client drops the audio it has queued. Pass
`talk --no-interrupt-response` or `local --local_audio_interrupt_response false`
to let the reply finish. The microphone stays open and your speech is still
transcribed, unlike `--block-mic-during-playback`, which stops sending
microphone audio. `talk --vad-threshold <0-1>` and
`local --local_audio_vad_threshold <0-1>` set the session VAD threshold;
without them the server's `--thresh` applies. A higher threshold can reduce false
triggers in a noisy room, but it cannot tell your voice apart from other people
talking nearby. See [Interruption Handling](./src/speech_to_speech/api/openai_realtime/README.md#interruption-handling)
for the session fields other clients send.

The packaged client can opt in to local Python tools with `talk --tool-module <module>` or `local --tool-module <module>`. The module contract, programmatic API, and web-search examples (Serper, or keyless You.com) are documented in [Tool calling design](./src/speech_to_speech/api/openai_realtime/README.md#packaged-python-client-tools).

### Migrating from `--mode`

`--mode` is deprecated and will stop working soon. During this migration window, `speech-to-speech --mode realtime` runs `speech-to-speech serve`, and `speech-to-speech --mode local` runs `speech-to-speech local`; both print a warning. All other mode values have been removed and exit with guidance to use the new commands.

### Local Mac

On macOS, `local` and `serve` already run all three models through MLX. The optional `--mac-optimal-settings` preset also makes MPS the default device for supported components. It only sets defaults: explicit `--device`, component-device flags such as `--qwen3_tts_device`, and `--stt`, `--llm_backend`, `--model_name`, and `--tts` all win.

`--tts pocket`, `--tts phonon`, `--tts kokoro`, `--tts omnivoice`, and `--tts kitten` are also valid on macOS.

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
durations for supported b
