# huggingface/speech-to-speech

Build voice agents with open-source models

## installation

Choose where the language model should run. All three configurations use local Parakeet TDT speech recognition and Qwen3-TTS speech output **by default**. You can change the STT, LLM, and TTS models and backends; see [Supported components](#supported-components). Each configuration runs from one terminal with the packaged microphone/speaker client.

| Starting configuration | Hardware to plan for | Conversation data sent to a provider |
|---|---|---|
| [Apple Silicon, fully local](#apple-silicon-fully-local) | Apple Silicon Mac; budget 16 GB or more of unified memory | None |
| [NVIDIA GPU, fully local](#nvidia-gpu-fully-local) | Linux with an NVIDIA GPU; budget 24 GB of VRAM for the unquantized LLM, speech models, and caches below, plus system RAM | None |
| [Local speech with a hosted LLM](#local-speech-with-a-hosted-llm) | Apple Silicon: budget ~8 GB of available unified memory (16 GB total recommended); Linux/NVIDIA: ~8 GB of available VRAM, plus system RAM | Transcribed text, instructions, and conversation history; microphone audio stays local |

The memory figures are planning estimates for one conversation, not measured minimum requirements. Actual use depends on context length, audio length, and backend versions. All configurations need internet access for the first model downloads; the hosted LLM also needs an API key and internet access during conversations.

### Install for these examples

Use Python 3.10+ (Python 3.11 recommended) and install the package in a virtual environment.

On Ubuntu, install the local audio libraries first: `sudo apt-get install libportaudio2 libsndfile1`. The default Linux Qwen3-TTS wheel targets CUDA 12.8 and glibc 2.39 (Ubuntu 24.04); check the [CUDA installation note](#cuda-note-for-qwen3-tts) if your system differs.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install speech-to-speech
```

Run the configuration you chose with this environment activated. Activate the same environment in any additional terminal where you run `speech-to-speech`. The first run downloads and warms up the models before connecting the microphone. Allow microphone access if prompted, use headphones to avoid speaker feedback, then speak and pause for a reply. Stop with `Ctrl+C`.

If speaker feedback interrupts replies, add `--local_audio_block_mic_during_playback` to your `speech-to-speech local` command. This pauses microphone capture during playback, so you cannot interrupt the assistant while it speaks.

### Apple Silicon, fully local

Run all three models locally on an Apple Silicon Mac, using a quantized LLM through MLX. No API key is needed.

```bash
speech-to-speech local \
    --mac-optimal-settings \
    --model_name mlx-community/Qwen3-4B-Instruct-2507-4bit
```

The Mac preset selects Parakeet TDT through MLX, the 4-bit Qwen3-4B language model through MLX LM, and the 6-bit Qwen3-TTS CustomVoice model through MLX Audio. The core model weights total approximately **7.5 GB**: [STT](https://huggingface.co/mlx-community/parakeet-tdt-0.6b-v3/tree/main), [LLM](https://huggingface.co/mlx-community/Qwen3-4B-Instruct-2507-4bit/tree/main), and [TTS](https://huggingface.co/mlx-community/Qwen3-TTS-12Hz-1.7B-CustomVoice-6bit/tree/main). Allow additional disk space for dependencies and auxiliary model assets.

For a separate local LLM server, see [Combining with llama.cpp](#combining-with-llamacpp). For a model that accepts audio directly, see the [Gemma 4 12B example](./examples/gemma4-12b-macos/README.md).

### NVIDIA GPU, fully local

Run all three models locally on a Linux workstation with a CUDA-capable NVIDIA GPU. Transformers loads the LLM in the speech process, so no separate LLM server or API key is needed.

```bash
speech-to-speech local \
    --device cuda \
    --stt parakeet-tdt \
    --llm_backend transformers \
    --model_name Qwen/Qwen3-4B-Instruct-2507 \
    --llm_torch_dtype float16 \
    --tts qwen3 \
    --qwen3_tts_backend ggml
```

The [LLM weights alone are approximately **8 G

## tools

| Command | Behavior | Use it when |
|---|---|---|
| `serve` | Runs the pipeline server over OpenAI Realtime WebSocket and WebRTC. | You are building an app or device against the API. |
| `talk --url <full-realtime-url>` | Runs the packaged microphone/speaker client. | You want to talk to an existing Realtime server. |
| `local` | Composes `serve` and `talk` in-process over loopback. | You want to run the server and talk to it from one command. |

`serve` binds to `127.0.0.1` by default; pass `--host 0.0.0.0` explicitly for network exposure. `local` always binds to loopback and connects the same packaged client at `ws://127.0.0.1:<port>/v1/realtime`.

The packaged `local` client buffers 196 ms of received audio when using the
OpenAI-compatible TTS backend, which absorbs short delivery gaps from HTTP
speech inference. Other `local` backends and `talk` start playback immediately
by default. Use `--playback-buffer-ms <milliseconds>` to override either
default: a larger value resists stuttering but delays the start of each
response, while a smaller value starts sooner but is more sensitive to jitter.
This setting only controls the packaged Python client's speakers; browser and
other Realtime clients manage their own playback buffers.

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

Start with [Apple Silicon, fully local](#apple-silicon-fully-local). Its `--mac-optimal-settings` preset supplies MPS defaults for supported components, Parakeet TDT for STT, MLX LM for the LLM, and Qwen3-TTS through `mlx-audio` with the `6bit` variant.

The preset supplies these as defaults only: explicit `--device`, component-device flags such as `--qwen3_tts_device`, and `--stt`, `--llm_backend`, `--model_name`, and `--tts` all win. Use it with `serve` instead of `local` when you want to expose the server without starting the microphone/speaker client.

`--tts pocket`, `--tts kokoro`, and `--tts omnivoice` are also valid on macOS.

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

The compose file starts a llama.cpp server with Gemma 4 and the Realtime server, exposing
