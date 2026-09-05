# debpalash/VoiceStudio

VoiceStudio is the open-source, fully-local ElevenLabs alternative — voice cloning, voice design, video dubbing, dictation, transcription & audiobook creation in 646 languages.

## installation

Download a package from the [latest release](https://github.com/debpalash/VoiceStudio/releases/latest), then follow the platform guide.

| Platform | Package | Guide |
|---|---|---|
| macOS 13.3+ | Apple Silicon DMG | [Install on macOS](docs/install/macos.md) |
| Windows 10/11 | x64 MSI; choose the current-user build when listed to install without admin access | [Install on Windows](docs/install/windows.md#install-pre-built-msi) |
| Linux | AppImage, x86_64 with glibc 2.39+ | [Install on Linux](docs/install/linux.md) |
| Docker | CUDA, ROCm, CPU, and worker-only GPU profiles | [Run with Docker](docs/install/docker.md) |

First launch creates a managed Python environment and downloads the default model. Later launches reuse both.

> [!NOTE]
> On macOS, first launch needs a one-time right-click, then **Open** approval. Intel Macs cannot run the local Python backend; use a [remote backend](docs/install/macos.md) instead.

### Quick Docker run

```bash
docker run -d -p 127.0.0.1:3900:3900 -v omnivoice-data:/app/omnivoice_data --name voicestudio palashdeb/omnivoice-studio:stable
```

### First voice

1. Launch VoiceStudio and open **Voice Cloning**.
2. Add a clean voice sample. Three seconds works; 5 to 15 seconds usually gives a better prompt.
3. Enter text, choose a language, then select **Generate**.

> [!TIP]
> **Try without installing:** Run VoiceStudio in the cloud via the [Google Colab notebook](https://colab.research.google.com/github/debpalash/VoiceStudio/blob/main/notebooks/OmniVoice_Studio_Colab.ipynb). Explore audio quality comparisons in [benchmarks](docs/benchmarks.md) and prompt design tips in [expressive speech](docs/expressive-speech.md).

### Audio samples

Listen to sample outputs produced locally with VoiceStudio:

| Workflow | Prompt / Reference Audio | Generated Audio |
|---|---|---|
| **Voice Cloning** | [demo_voice.wav](backend/assets/samples/demo_voice.wav) | [demo_clone_output.wav](backend/assets/samples/demo_clone_output.wav) |
| **Voice Design** (US News Anchor) | *"Clear, authoritative American broadcast tone"* | [demo_voice_design_us_news_anchor.wav](backend/assets/samples/voice_design/demo_voice_design_us_news_anchor.wav) |
| **Voice Design** (UK Audiobook) | *"Warm, expressive British storytelling voice"* | [demo_voice_design_audiobook_uk_narrator.wav](backend/assets/samples/voice_design/demo_voice_design_audiobook_uk_narrator.wav) |
| **Video Dubbing** (Multilingual) | [source.src.wav](backend/assets/samples/demo/dubbing/source.src.wav) | [Spanish](backend/assets/samples/demo/dubbing/dubbed_es.src.wav) · [French](backend/assets/samples/demo/dubbing/dubbed_fr.src.wav) · [Japanese](backend/assets/samples/demo/dubbing/dubbed_ja.src.wav) · [Chinese](backend/assets/samples/demo/dubbing/dubbed_zh.src.wav) |

### Run from source

Install the [development prerequisites](.github/CONTRIBUTING.md#development-setup) (Node 20+/Bun and Python 3.11+), then:

```bash
git clone https://github.com/debpalash/VoiceStudio.git
cd VoiceStudio
bun install
bun run desktop
```

The desktop launcher configures Python dependencies on first run via `uv` automatically. Use `bun run dev` for the browser UI. See [Contributing](.github/CONTRIBUTING.md) for services, tests, and platform packages.

### If setup fails

- Run **Settings → About → Run self-check** or `uv run python backend/main.py --diagnose --deep`.
- Check [install troubleshooting](docs/install/troubleshooting.md).
- Save a scrubbed diagnostic bundle from the app when opening an issue.
- For slow generation, compare [measured benchmarks](docs/benchmarks.md) and [performance settings](docs/performance.md).

<a id="features"></a>

## features

| Area | Included |
|---|---|
| **Voice Cloning** | Zero-shot synthesis from a short reference clip ([guide](docs/engines/README.md)) |
| **Voice Design** | Create a voice from age, accent, pitch, style, and delivery instructions ([expressive speech](docs/expressive-speech.md)) |
| **Video Dubbing** | Transcribe, translate, preserve speakers, synthesize, and export video ([export guide](docs/dubbing/export.md)) |
| **Stories and audiobooks** | Multi-voice scripts · EPUB/PDF import · chapter rendering · `.m4b` export |
| **[Dictation Widget](docs/features/dictation.md)** | System-wide shortcut, live transcription, optional local-LLM cleanup |
| **Vocal Isolation** | Demucs speech/background separation |
| **Speaker Diarization** | Pyannote and WhisperX speaker assignment ([guide](docs/features/diarization.md)) |
| **Batch Queue** | Queue large sets of audio and video jobs with per-job progress, or watch a local folder for new videos |
| **Model Catalogue** | Install, remove, select, and route TTS, ASR, and LLM models ([catalogue](docs/engines/README.md)) |
| **Remote Model Downloads** | Install models on enrolled remote workers with live progress ([guide](docs/downloading-models.md)) |
| **GPU Auto-Detect** | CUDA, MPS, ROCm, and CPU routing with per-engine checks ([performance](docs/performance.md)) |
| **AI Watermark** | AudioSeal embedding and detection |
| **MCP Server** | Synthesis and transcription tools for MCP clients ([guide](docs/mcp.md)) |
| **Diagnostics** | Self-checks, error journal, logs, and scrubbed support bundles ([troubleshooting](docs/install/troubleshooting.md)) |
| **Local-first** | Core creation stays local; network-backed features are explicit opt-ins |
| **Extensible** | Registry-based TTS, ASR, and plugin interfaces ([acceptance](docs/engine-acceptance.md)) |

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

## Comparison

VoiceStudio trades managed cloud compute for local control. This is the practical difference:

| | **VoiceStudio** | **Typical hosted voice service** |
|---|---|---|
| **Best fit** | Private, offline, self-hosted, or high-volume work | Fast setup without local model management |
| **Data path** | Local by default; remote features are opt-in | Audio and text are processed by the provider |
| **Cost model** | Free software; you supply the hardware | Subscription, credits, or metered API use |
| **Setup** | Install the app and model weights | Create an account and use the web app or API |
| **Performance** | Depends on your engine and hardware | Provider manages compute and scaling |
| **Offline use** | Yes, after required models are installed | Usually requires a network connection |
| **Customization** | Source, engines, models, API, and routing are open | Limited to provider options |
| **Maintenance** | You manage updates, disk, and compute | Provider manages infrastructure |

<a id="requirements"></a>

## requirements

Requirements vary by engine. These values cover the default local workflow.

| | **Minimum** | **Recommended** |
|---|---|---|
| **OS** | Windows 10 x64 · macOS 13.3 Apple Silicon · Linux x86_64 with glibc 2.39+ | Current supported OS release |
| **RAM** | 8 GB | 16 GB+ |
| **Disk** | 10 GB free | 20 GB+ SSD |
| **GPU** | Optional; CPU mode is supported | NVIDIA CUDA or Apple Silicon |
| **VRAM** | 4 GB when using a GPU | 8 GB+; large optional engines need more |
| **Python from source** | 3.11+ | 3.11 or 3.12 |

ROCm is Linux-only and opt-in. Windows AMD/Ryzen AI uses CPU. Systems with limited VRAM offload work to CPU when required. See [performance](docs/performance.md), [benchmarks](docs/benchmarks.md), and [engine disk usage](docs/engines/disk-usage.md).

<a id="hardware-recommendations"></a>

### Recommended stack by hardware

| Hardware | Recommended TTS | Recommended ASR | Why |
|---|---|---|---|
| **Apple Silicon (M1–M4)** | [MLX-Audio](docs/engines/mlx-audio.md) · [OmniVoice](docs/engines/omnivoice.md) (MPS) | [MLX Whisper](docs/engines/mlx-whisper.md) · [Parakeet MLX](docs/engines/parakeet-mlx.md) | Native unified memory, lowest latency on macOS |
| **NVIDIA GPU (8 GB+ VRAM)** | [OmniVoice](docs/engines/omnivoice.md) · [CosyVoice 3](docs/engines/cosyvoice.md) | [WhisperX](docs/engines/whisperx.md) | High-fidelity zero-shot cloning, word timestamps, diarization |
| **Low VRAM / CPU-only** | [PocketTTS](docs/engines/pockettts.md) · [Sherpa-ONNX](docs/engines/sherpa-onnx.md) · [KittenTTS](docs/engines/kittentts.md) | [Moonshine](docs/engines/moonshine.md) · [Faster-Whisper](docs/engines/faster-whisper.md) (`int8`) | Low memory footprint, optimized CPU inference |

<a id="engines"></a>

## Engines

Engine support is capability-specific. Check cloning, language, platform, memory, and license before choosing one. Full setup guides: [docs/engines](docs/engines/README.md).

<a id="tts-engines"></a>

### Text to speech

| Engine | Languages | Clone | Instruct | Linux | macOS ARM | Windows | License |
|---|:---:|:---:|:---:|:---:|:---:|:---:|---|
| [**VoiceStudio** (default, powered by k2-fsa/OmniVoice)](docs/engines/omnivoice.md) | 600+ | Yes | Yes | CUDA/CPU | MPS | CUDA/CPU | [AGPL-3.0](LICENSE) app · [Apache-2.0 code, CC-BY-NC weights](https://huggingface.co/k2-fsa/OmniVoice#license)³ |
| [**CosyVoice 3**](docs/engines/cosyvoice.md) | 9 + 18 dialects | Yes | Yes | CUDA/CPU | CPU | CUDA/CPU | Apache-2.0 |
| [**GPT-SoVITS**](docs/engines/gpt-sovits.md) | 5 | Yes | No | CUDA/CPU | No | CUDA/CPU | MIT |
| [**VoxCPM2**](docs/engines/voxcpm2.md) | 30 | Yes | Yes | CUDA/CPU | MPS | CUDA/CPU | Apache-2.0 |
| [**MOSS-TTS-Nano**](docs/engines/moss-tts-nano.md) | 20 | Yes | No | CUDA/CPU | CPU | CUDA/CPU | Apache-2.0 |
| [**KittenTTS**](docs/engines/kittentts.md) | English | No | No | CPU | CPU | CPU | MIT |
| [**MLX-Audio**](docs/engines/mlx-audio.md) | Model-dependent | Varies | Varies | No | MLX | No | Varies |
| [**Sherpa-ONNX**](docs/engines/sherpa-onnx.md) | 20+ | No | No | CUDA/CPU | CPU | CUDA/CPU | Apache-2.0 |
| [**IndexTTS 2.5** ⚡](docs/engines/indextts.md) | ZH · EN · JA · ES · AR | Yes | No | CUDA/CPU | CPU | CUDA/CPU | Bilibili model license¹ |
| [**OmniVoice GGUF** ⚡](docs/engines/omnivoice-gguf.md) | 600+ | Yes | Yes | CUDA/CPU | MPS/CPU | CUDA/CPU | [AGPL-3.0](LICENSE) app · [review the derivative model terms](https://huggingface.co/Serveurperso/OmniVoice-GGUF#license)³ |
| [**OmniVoice (subprocess)** ⚡](docs/engines/omnivoice-subprocess.md) | 600+ | Yes | Yes | CUDA/CPU | MPS | CUDA/CPU | [AGPL-3.0](LICENSE) app · [Apache-2.0 code, CC-BY-NC weights](https://huggingface.co/k2-fsa/OmniVoice#license)³ |
| [**PocketTTS** ⚡](docs/engines/pockettts.md) | EN · FR · DE · PT · IT · ES | Yes | No | CPU | CPU | CPU | CC-BY-4.0, gated² |
| [**Supertonic 3** ⚡](docs/engines/supertonic3.md) | 31 | No | No | CPU | CPU | CPU | OpenRAIL-M |
| [**MOSS-TTS-v1.5** ⚡](docs/engines/moss-tts-v15.md) | 31 | Yes | No | CUDA/CPU | CPU | CUDA

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
| `WS /v1/audio/transcriptions/stream` | Live PCM/WebM transcription with partial, utterance, and session-final events |
| `GET /.well-known/voicestudio-speech` | Discover HTTP, WebSocket, MCP, and native dictation-control transports |
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

```bash
# Quick test via cURL
curl http://localhost:3900/v1/audio/speech \
  -H "Content-Type: application/json" \
  -d '{"model": "tts-1", "input": "Made on my own hardware.", "voice": "default", "response_format": "wav"}' \
  --output speech.wav
```

The bundled Rust control sidecar lets Herdr, coding agents, VS Code, desktop apps,
and TUIs trigger the system-wide dictation flow or reuse its native text
insertion. See the [speech platform guide](docs/speech-platform.md). The full API
reference is in **Settings → OpenAPI Reference**. For LAN, Tailscale, or proxy
access, read [API authentication](docs/api-auth.md) before exposing the backend.

### Agent skills

Install the VoiceStudio skills for Claude Code, Codex, Cursor, and other [skills.sh](https://skills.sh)-compatible agents:

```bash
npx skills add debpalash/VoiceStudio
```

- `omnivoice`: synthesize speech and transcribe audio through local VoiceStudio.
- `oss-maintainer`: the repository's open-source maintenance workflow.

### Model Context Protocol (MCP)

VoiceStudio mounts an MCP server at `http://localhost:3900/mcp` for Claude Desktop, Cursor, and AI agents:

```json
{
  "mcpServers": {
    "voicestudio": {
      "url": "http://localhost:3900/mcp"
    }
  }
}
```

For clients requiring stdio transport, use the bundled local shim (`docs/mcp.json`):

```json
{
  "mcpServers": {
    "voicestudio": {
      "command": "python",
      "args": ["-m", "backend.mcp_shim"],
      "cwd": "/path/to/VoiceStudio"
    }
  }
}
```

See the [MCP guide](docs/mcp.md) for tools (`generate_speech`, `clone_voice`, `transcribe`), file streaming modes, and client bindings.

### Google Colab

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/debpalash/VoiceStudio/blob/main/notebooks/OmniVoice_Studio_Colab.ipynb)

The [notebook](notebooks/OmniVoice_Studio_Colab.ipynb) runs the app and web UI on a Colab GPU. Colab is remote compute, so uploaded audio and project data do not remain local to your machine.

<a id="documentation"></a>

## Documentation

| Need | Read |
|---|---|
| Install | [macOS](docs/install/macos.md) · [Windows](docs/install/windows.md) · [Linux](docs/install/linux.md) · [Docker](docs/install/docker.md) |
| Fix setup | [Troubleshooting](docs/install/troubleshooting.md) · [model downloads](docs/downloading-models.md) · [Hugging Face token](docs/setup/huggingface-token.md) |
| Choose an engine | [Engine guides](docs/engines/README.md) · [benchmarks](docs/benchmarks.md) · [expressive speech](docs/expressive-speech.md) |
| Tune hardware | [Performance](docs/performance.md) · [remote workers](docs/remote-workers.md) |
| Build integrations | [Speech platform](docs/speech-platform.md) · [Private production API](docs/production-private-api.md) · [API auth](docs/api-auth.md) · [MCP](docs/mcp.md) · [examples](examples/README.md) |
| Build VoiceStudio | [Contributing](.github/CO
