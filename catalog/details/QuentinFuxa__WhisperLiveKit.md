# QuentinFuxa/WhisperLiveKit

Real-time, local speech-to-text with streaming ASR, speaker diarization, translation, and OpenAI/Deepgram-compatible APIs.

## installation

```bash
pip install whisperlivekit
```

#### Quick Start

```bash

# Start the server — open http://localhost:8000 and start talking
wlk --model base --language en


# Auto-pull model and start server
wlk run whisper:tiny

# Transcribe a file (no server needed)
wlk transcribe meeting.wav

# Generate subtitles
wlk transcribe --format srt podcast.mp3 -o podcast.srt

# Manage models
wlk models                             # See what's installed
wlk pull large-v3                      # Download a model
wlk rm large-v3                        # Delete a model

# Benchmark speed and accuracy
wlk bench
```

#### API Compatibility

WhisperLiveKit exposes compatibility-oriented subsets of popular APIs:

```bash

## tools

curl http://localhost:8000/v1/audio/transcriptions -F file=@audio.wav

# Works with the OpenAI Python SDK
client = OpenAI(base_url="http://localhost:8000/v1", api_key="unused")

# Deepgram-compatible WebSocket

## configuration

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--model` | Whisper model size. List and recommandations [here](https://github.com/QuentinFuxa/WhisperLiveKit/blob/main/docs/default_and_custom_models.md) | `small` |
| `--model-path` | Local .pt file/directory **or** Hugging Face repo ID containing the Whisper model. Overrides `--model`. Recommandations [here](https://github.com/QuentinFuxa/WhisperLiveKit/blob/main/docs/default_and_custom_models.md) | `None` |
| `--language` | List [here](docs/supported_languages.md). If you use `auto`, the model attempts to detect the language automatically, but it tends to bias towards English. | `auto` |
| `--target-language` | If sets, translates using [NLLW](https://github.com/QuentinFuxa/NoLanguageLeftWaiting). [200 languages available](docs/supported_languages.md). If you want to translate to english, you can also use `--direct-english-translation`. The STT model will try to directly output the translation. | `None` |
| `--translation-backend` | `nllb` (in-process, CPU-friendly) or `alignatt`: streaming LLM translation through an [Alignatt4LLM](https://github.com/QuentinFuxa/Alignatt4LLM) sidecar, with attention-gated append-only commits. See [docs/translation-alignatt.md](docs/translation-alignatt.md). | `nllb` |
| `--diarization` | Enable speaker identification | `False` |
| `--backend-policy` | Streaming strategy: `1`/`simulstreaming` uses AlignAtt SimulStreaming, `2`/`localagreement` uses the LocalAgreement policy | `simulstreaming` |
| `--backend` | ASR backend selector. `auto` picks MLX on macOS (if installed), otherwise Faster-Whisper, otherwise vanilla Whisper. Options: `mlx-whisper`, `faster-whisper`, `whisper`, `openai-api` (LocalAgreement only), `funasr` (SenseVoiceSmall, LocalAgreement only), `voxtral-mlx` (Apple Silicon), `voxtral` (HuggingFace), `qwen3-vllm`, `qwen3-vllm-metal` (Apple Silicon), `qwen3-streaming` (HuggingFace, CUDA/MPS/CPU), `canary` (NeMo, CUDA/CPU, LocalAgreement only) | `auto` |
| `--pause-segmentation-seconds` | Create a stable transcript boundary when a VAD pause is longer than this many seconds. Use `0` to disable pause-based segmentation. | `5.0` |
| `--asr-coalesce-min-s` | Defer an ASR call until this much new audio has accrued. Trades update cadence for fewer encoder passes; use `0` to disable. | `0` |
| `--no-vac` | Disable Voice Activity Controller. NOT ADVISED | `False` |
| `--no-vad` | Disable Voice Activity Detection. NOT ADVISED | `False` |
| `--warmup-file` | Audio file path for model warmup | `jfk.wav` |
| `--host` | Server host address | `localhost` |
| `--port` | Server port | `8000` |
| `--ssl-certfile` | Path to the SSL certificate file (for HTTPS support) | `None` |
| `--ssl-keyfile` | Path to the SSL private key file (for HTTPS support) | `None` |
| `--forwarded-allow-ips` | Ip or Ips allowed to reverse proxy the whisperlivekit-server. Supported types are  IP Addresses (e.g. 127.0.0.1), IP Networks (e.g. 10.100.0.0/16), or Literals (e.g. /path/to/socket.sock) | `None` |
| `--cors-origins` | Comma-separated list of allowed CORS origins. Empty disables CORS; use `*` to allow all origins. | empty |
| `--pcm-input` | raw PCM (s16le) data is expected as input and FFmpeg will be bypassed. Frontend will use AudioWorklet instead of MediaRecorder | `False` |
| `--lora-path` | Path or Hugging Face repo ID for LoRA adapter weights (e.g., `qfuxa/whisper-base-french-lora`). Only works with native Whisper backend (`--backend whisper`) | `None` |

| Translation options | Description | Default |
|-----------|-------------|---------|
| `--nllb-backend` | `transformers` or `ctranslate2` | `transformers` |
| `--nllb-size` | `600M` or `1.3B` | `600M` |

| Diarization options | Description | Default |
|-----------|-------------|---------|
| `--diarization-backend` |  `diart` or `sortformer` | `sortformer` |
| `--sortformer-model-path` | Path to a local Sortformer `.nemo` file, a directory containing exactly one `.nemo` file, o

## requirements

- Docker installed on your system
- For GPU support: NVIDIA Docker runtime installed
