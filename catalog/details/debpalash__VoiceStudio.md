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

### First voice

1. Launch VoiceStudio and open **Voice Cloning**.
2. Add a clean voice sample. Three seconds works; 5–15 seconds usually gives a better prompt.
3. Enter text, choose a language, then select **Generate**.

### Run from source

Install the [development prerequisites](.github/CONTRIBUTING.md#development-setup), then:

```bash
git clone https://github.com/debpalash/VoiceStudio.git
cd VoiceStudio
bun install
bun run desktop
```

Use `bun run dev` for the browser UI. See [Contributing](.github/CONTRIBUTING.md) for services, tests, and platform packages.

### If setup fails

- Run **Settings → About → Run self-check** or `uv run python backend/main.py --diagnose --deep`.
- Check [install troubleshooting](docs/install/troubleshooting.md).
- Save a scrubbed diagnostic bundle from the app when opening an issue.
- For slow generation, compare [measured benchmarks](docs/benchmarks.md) and [performance settings](docs/performance.md).

<a id="features"></a>

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
| **Python from source** | 3.11+ | 3.11–3.12 |

ROCm is Linux-only and opt-in. Windows AMD/Ryzen AI uses CPU. Systems with limited VRAM offload work to CPU when required. See [performance](docs/performance.md), [benchmarks](docs/benchmarks.md), and [engine disk usage](docs/engines/disk-usage.md).

<a id="engines"></a>

## Engines

Engine support is capability-specific. Check cloning, language, platform, memory, and license before choosing one. Full setup guides: [docs/engines](docs/engines/README.md).

<a id="tts-engines"></a>

### Text to speech

| Engine | Languages | Clone | Instruct | Linux | macOS ARM | Windows | License |
|---|:---:|:---:|:---:|:---:|:---:|:---:|---|
| **VoiceStudio** (default, powered by k2-fsa/OmniVoice) | 600+ | Yes | Yes | CUDA/CPU | MPS | CUDA/CPU | [AGPL-3.0](LICENSE) app · [Apache-2.0](LICENSE-NOTICE.md) model |
| **CosyVoice 3** | 9 + 18 dialects | Yes | Yes | CUDA/CPU | CPU | CUDA/CPU | Apache-2.0 |
| **GPT-SoVITS** | 5 | Yes | — | CUDA/CPU | — | CUDA/CPU | MIT |
| **VoxCPM2** | 30 | Yes | Yes | CUDA/CPU | MPS | CUDA/CPU | Apache-2.0 |
| **MOSS-TTS-Nano** | 20 | Yes | — | CUDA/CPU | CPU | CUDA/CPU | Apache-2.0 |
| **KittenTTS** | English | — | — | CPU | CPU | CPU | MIT |
| **MLX-Audio** | Model-dependent | Varies | Varies | — | MLX | — | Varies |
| **Sherpa-ONNX** | 20+ | — | — | CUDA/CPU | CPU | CUDA/CPU | Apache-2.0 |
| **IndexTTS 2.5** ⚡ | ZH · EN · JA · ES · AR | Yes | — | CUDA/CPU | CPU | CUDA/CPU | Bilibili model license¹ |
| **OmniVoice GGUF** ⚡ | 600+ | Yes | Yes | CUDA/CPU | MPS/CPU | CUDA/CPU | [AGPL-3.0](LICENSE) app · [Apache-2.0](LICENSE-NOTICE.md) model |
| **OmniVoice (subprocess)** ⚡ | 600+ | Yes | Yes | CUDA/CPU | MPS | CUDA/CPU | [AGPL-3.0](LICENSE) app · [Apache-2.0](LICENSE-NOTICE.md) model |
| **PocketTTS** ⚡ | EN · FR · DE · PT · IT · ES | Yes | — | CPU | CPU | CPU | CC-BY-4.0, gated² |
| **Supertonic 3** ⚡ | 31 | — | — | CPU | CPU | CPU | OpenRAIL-M |
| **MOSS-TTS-v1.5** ⚡ | 31 | Yes | — | CUDA/CPU | CPU | CUDA/CPU | Apache-2.0 |
| **dots.tts** ⚡ | 24 | Yes | — | CUDA/CPU | CPU | — | Apache-2.0 |
| **Confucius4-TTS** ⚡ | 14 | Yes | — | CUDA/CPU | CPU | CUDA/CPU | Apache-2.0 |

⚡ Installed or registered on demand.

¹ IndexTTS 2.5 requires a separate written Bilibili license above 100 million monthly active users or RMB 1 billion annual revenue. Review the [model license](https://huggingface.co/IndexTeam/IndexTTS-2.5/blob/main/LICENSE).

² PocketTTS shows its gated-access and CC-BY-4.0 terms before first use.

Clone-less engines cannot preserve a reference speaker in dubbing or pinned-voice batch jobs. VoiceStudio rejects those jobs instead of silently changing engines. Heavy engines have separate memory and platform limits; check their engine guide first.

<a id="asr-engines"></a>

### Speech to text

| Engine | ID | Languages | Best fit |
|---|---|:---:|---|
| **WhisperX** (default) | `whisperx` | ~100 | Dubbing, subtitles, word-level timing |
| **Faster-Whisper** | `faster-whisper` | ~100 | General cross-platform transcription |
| **Faster-Whisper (isolated)** | `faster-whisper-isolated` | ~100 | Crash-isolated batch transcription |
| **MLX Whisper** | `mlx-whisper` | ~100 | Apple Silicon |
| **PyTorch Whisper** | `pytorch-whisper` | ~100 | CUDA, MPS, and CPU fallback |
| **Parakeet TDT** | `nemo-parakeet` | English + 25 EU | Fast CPU/CUDA transcription |
| **Parakeet TDT v3 (MLX)** | `parakeet-mlx` | 25 EU | Apple Silicon dictation and word timestamps |
| **Moonshine** | `moonshine` | English | Low-power, low-la

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

### Agent skills

Install the VoiceStudio skills for Claude Code, Codex, Cursor, and other [skills.sh](https://skills.sh)-compatible agents:

```bash
npx skills add debpalash/omnivoice-studio
```

- `omnivoice`: synthesize speech and transcribe audio through local VoiceStudio.
- `oss-maintainer`: the repository's open-source maintenance workflow.

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
| Build integrations | [API auth](docs/api-auth.md) · [MCP](docs/mcp.md) · [examples](examples/README.md) |
| Build VoiceStudio | [Contributing](.github/CONTRIBUTING.md) · [engine acceptance](docs/engine-acceptance.md) |
| Track changes | [Changelog](CHANGELOG.md) · [roadmap](docs/ROADMAP.md) · [latest release](https://github.com/debpalash/VoiceStudio/releases/latest) |
| Remove everything | [Uninstall guide](docs/install/uninstall.md) |

## FAQ

<details>
<summary><strong>Does it work on Apple Silicon and Intel Macs?</strong></summary>

Apple Silicon is supported with MPS and MLX options. Intel Macs cannot run the local backend because current PyTorch wheels are unavailable; they can connect to a remote backend. See [macOS installation](docs/install/macos.md).
</details>

<details>
<summary><strong>How much VRAM do I need?</strong></summary>

A GPU is optional. Use 4 GB VRAM as the minimum for accelerated work and 8 GB+ for the default multi-stage workflow. Large optional engines can require 12–16 GB or more. Check the [benchmarks](docs/benchmarks.md) and engine guide.
</details>

<details>
<summary><strong>Why does a longer reference clip not always improve the clone?</strong></summary>

Cloning is zero-shot: the clip is a prompt, not training data. Use 5–15 seconds of one speaker, close to the microphone, without music, noise, or reverb. Match the tone and pace you want in the output. For training, see [data preparation](docs/data_preparation.md) and [training](docs/training.md).
</details>

<details>
<summary><strong>Can I use generated audio commercially?</strong></summary>

Yes 
