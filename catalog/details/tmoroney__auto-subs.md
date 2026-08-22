# tmoroney/auto-subs

On-device subtitle generation that connects directly to DaVinci Resolve, Premiere, and After Effects.

## installation

**Debian/Ubuntu (.deb):**
```bash
wget https://github.com/tmoroney/auto-subs/releases/latest/download/AutoSubs-linux-x86_64.deb
sudo apt install ./AutoSubs-linux-x86_64.deb
```

**Fedora/openSUSE (.rpm):**
Download [AutoSubs-linux-x86_64.rpm](https://github.com/tmoroney/auto-subs/releases/latest/download/AutoSubs-linux-x86_64.rpm) and open it with your package manager.

<a href="https://www.buymeacoffee.com/tmoroney" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 48px !important;width: 173px !important;" ></a>

---

## Quick Start

### Standalone Mode
1. Launch AutoSubs and select an audio or video file.
2. Pick your model and language/translation options.
3. Click **Transcribe**. Edit speakers and subtitles as needed.
4. Export as SRT, text, or copy to clipboard.

### DaVinci Resolve Mode
1. Open DaVinci Resolve → **Workspace → Scripts → AutoSubs**.
2. Select your timeline/audio source and settings.
3. Click **Transcribe**. Edit speakers and subtitles as needed.
4. Send styled subtitles back to Resolve.

> [!WARNING]
> Mac App Store version not supported - download DaVinci Resolve from [blackmagicdesign.com](https://www.blackmagicdesign.com/products/davinciresolve/) instead.

### Adobe Premiere Pro / After Effects Mode
1. Launch AutoSubs and open Premiere Pro or After Effects (the CEP extension loads automatically).
2. Select the Adobe integration from AutoSubs to export timeline audio for transcription, or import generated subtitles into your project.
3. In Premiere Pro, subtitles are imported as caption tracks; in After Effects, SRT entries are created as text layers.

### Command Line Interface

For command-line usage, see the **[CLI Guide](CLI.md)** with complete reference, examples, and troubleshooting.

---

## Documentation

- **[CLI Guide](CLI.md)** - Command-line interface reference
- **[Contributing Guide](CONTRIBUTING.md)** - Development setup and contribution workflow
- **[AutoSubs-App README](AutoSubs-App/README.md)** - Technical architecture and code organization
- **[Resolve Integration](Resolve-Integration/README.md)** - DaVinci Resolve integration architecture and development
- **[Adobe Extension](Adobe-Extension/README.md)** - Adobe Premiere Pro/After Effects integration details

> [!TIP]
> I highly recommend checking out **[DeepWiki](https://deepwiki.com/tmoroney/auto-subs)** for asking questions and understanding the codebase.
>
> [![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/tmoroney/auto-subs)

---

## Supported Models

AutoSubs ships with several local transcription model families. All run fully on-device — nothing is sent to the cloud. Models are downloaded on demand from the in-app Model Manager.

> Accuracy is a relative 1–4 rating within AutoSubs (higher is better). Sizes and RAM figures are approximate.

### Whisper

OpenAI's Whisper, via `whisper-rs` (GGML). Each size is available in a multilingual variant and an `.en` English-only variant (the `.en` models are slightly more accurate on English audio).

| Model | Size | RAM | Languages | Accuracy |
|---|---|---|---|---|
| tiny / tiny.en | 80 MB | 1 GB | Multilingual / English | ★ |
| base / base.en | 150 MB | 1 GB | Multilingual / English | ★ |
| small / small.en | 480 MB | 2 GB | Multilingual / English | ★★ |
| medium / medium.en | 1.5 GB | 5 GB | Multilingual / English | ★★★ |
| large-v3-turbo | 1.6 GB | 6 GB | Multilingual | ★★★ |
| large-v3 | 3.1 GB | 10 GB | Multilingual | ★★★★ |

### Moonshine

Useful Sensors' Moonshine, via ONNX Runtime. The `tiny` English model is quantized; the language-specific `tiny` variants and the `base` model are float-precision.

| Model | Size | RAM | Language | Accuracy |
|---|---|---|---|---|
| moonshine-tiny | 60 MB | 1 GB | English | ★ |
| moonshine-tiny-ar | 120 MB | 1 GB | Arabic | ★★★ |
| moonshine-tiny-zh | 120 MB | 1 GB | Chinese | ★★★ |
| moonshine-tiny-ja | 120 MB | 1 GB | Japanese | ★★★ |
| moonshine-ti
