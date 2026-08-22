# debpalash/VoiceStudio

VoiceStudio is the open-source, fully-local ElevenLabs alternative — voice cloning, voice design, video dubbing, dictation, transcription & audiobook creation in 646 languages.

## installation

| Platform | Package | Guide |
|---|---|---|
| macOS 13.3+ | DMG, Apple Silicon | [Install on macOS](docs/install/macos.md) |
| Windows 10/11 | MSI, x64 | [Install on Windows](docs/install/windows.md) |
| Linux | AppImage, x86_64 with glibc 2.39+ | [Install on Linux](docs/install/linux.md) |
| Docker | CUDA, ROCm, or CPU | [Run with Docker](docs/install/docker.md) |

Download packages from the [latest release](https://github.com/debpalash/VoiceStudio/releases/latest). First launch creates a managed Python environment and downloads the default model. Later launches reuse both.

> [!NOTE]
> On macOS, first launch needs a one-time right-click → **Open** approval. Intel Macs cannot run the local Python backend; use a [remote backend](docs/install/macos.md) instead.

## features

| Area | Included |
|---|---|
| **Voice Cloning** | Zero-shot synthesis from a short reference clip |
| **Voice Design** | Create a voice from age, accent, pitch, style, and delivery instructions |
| **Video Dubbing** | Transcribe, translate, preserve speakers, synthesize, and export video |
| **Stories and audiobooks** | Multi-voice scripts · EPUB/PDF import · chapter rendering · `.m4b` export |
| **[Dictation Widget](docs/features/dictation.md)** | System-wide shortcut, live transcription, optional local-LLM cleanup |
| **Vocal Isolation** | Demucs speech/background separation |
| **Speaker Diarization** | Pyannote and WhisperX speaker assignment |
| **Batch Queue** | Queue large sets of audio and video jobs with per-job progress |
| **Model Catalogue** | Install, remove, select, and route TTS, ASR, and LLM models |
| **Remote Model Downloads** | Install models on enrolled remote workers with live progress |
| **GPU Auto-Detect** | CUDA, MPS, ROCm, and CPU routing with per-engine checks |
| **AI Watermark** | AudioSeal embedding and detection |
| **MCP Server** | Synthesis and transcription tools for MCP clients |
| **Diagnostics** | Self-checks, error journal, logs, and scrubbed support bundles |
| **Local-first** | Core creation stays local; network-backed features are explicit opt-ins |
| **Extensible** | Registry-based TTS, ASR, and plugin interfaces |

<table>
<tr>
  <td width="50%"><img src="docs/media/0.5.0/catalogue.png" alt="VoiceStudio Model Catalogue" width="100%" /></td>
  <td width="50%"><img src="docs/media/0.5.0/gallery-save.png" alt="Saving a gallery voice as a local profile" width="100%" /></td>
</tr>
<tr>
  <td align="center"><sub>Model Catalogue: engine, device, and install state</sub></td>
  <td align="center"><sub>Gallery: save a shared voice as a local profile</sub></td>
</tr>
</table>

<a id="comparison"></a>

## requirements

Requirements vary by engine. These values cover the default local workflow.

| | **Minimum** | **Recommended** |
|---|---|---|
| **OS** | Windows 10 x64 · macOS 13.3 Apple Silicon · Linux x86_64 with glibc 2.39+ | Current supported OS release |
| **RAM** | 8 GB | 16 GB+ |
| **Disk** | 10 GB free | 20 GB+ SSD |
| **GPU** | Optional; CPU mode is supported | NVIDIA CUDA or Apple Silicon |
| **VRAM** | 4 GB when using a GPU | 8 GB+; large optional engines need more |
| **Python from source** | 3.11+ | 3.11–3.12 |

ROCm is Linux-only and opt-in. Windows AMD/Ryzen AI uses CPU. Systems with limited VRAM offload work to CPU when required. See [performance](docs/performance.md), [benchmarks](docs/benchmarks.md), and [engine disk usage](docs/engines/disk-usage.md).

<a id="engines"></a>

## tools

Point an OpenAI-compatible audio client at the local backend:

```diff
- base_url="https://api.openai.com/v1"
+ base_url="http://localhost:3900/v1"
```

| Endpoint | Purpose |
|---|---|
| `POST /v1/audio/speech` | TTS to `mp3`, `opus`, `aac`, `flac`, `wav`, or `pcm`; select a profile with `voice` and an engine with `model` |
| `POST /v1/audio/transcriptions` | STT to `json`, `text`, `verbose_json`, `srt`, or `vtt` |
| `GET /v1/audio/voices` | List local voice profiles and engines |

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:3900/v1", api_key="local")

with client.audio.speech.with_streaming_response.create(
    model="tts-1",
    voice="<profile-id>",
    input="Made on my own hardware.",
    response_format="wav",
) as response:
    response.stream_to_file("speech.wav")
```

The full API reference is in **Settings → OpenAPI Reference**. For LAN, Tailscale, or proxy access, read [API authentication](docs/api-auth.md) before exposing the backend.
