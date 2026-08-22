# Blue-B/WhisperSubTranslate

A free, local desktop app to extract subtitles (SRT) from video and translate them into any language — unlimited use, no signup, no cloud.

## features

- 100% local speech to text. Your video never leaves your machine, no account, no upload.
- Offline translation with the bundled Hy-MT2 model, or online engines (MyMemory, DeepL, OpenAI, Gemini) with your own keys.
- Automatic model download. No Python, no manual setup.
- Sync repair models (large-v2 Sync and Sync Lite) for videos where normal models drift out of sync.
- Queue, live progress, and local-only job history.

## installation

### Users

Download the latest portable archive from [Releases](https://github.com/Blue-B/WhisperSubTranslate/releases), extract it, and run `WhisperSubTranslate.exe`. Extraction runs fully offline on your PC. Translation is optional.

### Developers

```bash
npm install
npm start
```

- Node.js >= 22.12.0 (see `engines` in package.json; Electron 43 toolchain)
- whisper.cpp is downloaded during `npm install` (CUDA build on Windows, ~700MB)
- FFmpeg is included via npm; the selected GGML model downloads on first use

### Linux

```bash
sudo apt install cmake build-essential git ffmpeg   # Ubuntu/Debian
npm install   # whisper.cpp is built from source
npm start
```

For CUDA acceleration, install the NVIDIA CUDA Toolkit before `npm install`. Manual whisper.cpp build steps are in [CONTRIBUTING.md](CONTRIBUTING.md).

- **Linux keyring**: API keys are stored via Electron safeStorage (libsecret). Without a keyring daemon (headless SSH session, minimal desktop/WM), saving falls back to legacy AES with a hardcoded key: the app logs an explicit security warning and marks the save as `insecure`. That storage is **not secure** - install `gnome-keyring` (or run in a desktop session with a keyring) to enable secure storage.

### Build (Windows)

```bash
npm run build-win   # artifacts are emitted to dist2/
```

## Translation engines

Translate subtitles fully offline with the bundled Tencent Hy-MT2 model, or route to free/paid online engines using your own API keys.

| Engine | Offline | API key | Cost | Notes |
| --- | :---: | :---: | --- | --- |
| Hy-MT2 1.8B (local, default) | Yes | No | Free | ~1.13GB, VRAM 2GB / RAM 4GB, on-device |
| Hy-MT2 7B (local) | Yes | No | Free | ~6.16GB, VRAM 8GB / RAM 12GB, larger model |
| MyMemory | No | No | Free | ~50K chars/day per IP |
| DeepL | No | Yes | Free 500K/month | Deterministic output |
| OpenAI GPT-5.x (configurable, e.g. gpt-5.6-sol) | No | Yes | Paid | Default model; context-aware |
| Gemini 3.x (configurable, e.g. gemini-3.6-flash) | No | Yes | Free / low-cost | Recommended low-cost route ([get key](https://aistudio.google.com/app/apikey)) |
| Claude (configurable, e.g. claude-opus-5) | No | Yes | Paid | Strong at context understanding ([get key](https://console.anthropic.com/settings/keys)) |
| Custom OpenAI-compatible providers | No | Yes | Varies | Bring your own endpoint (OpenRouter, Ollama, vLLM, …) |

The local Hy-MT2 engine is the only option that needs no API key, no network, and no per-use cost, so your dialogue never leaves your machine.

### Translation quality (offline engine)

WhisperSubTranslate ships Tencent's Hy-MT2 models (1.8B default, 7B optional). Tencent's official evaluation shows the Hy-MT2 family competing with leading commercial translation APIs, and ahead of several of them on some benchmarks.

![Hy-MT2 translation benchmark, official Tencent figures, bundled in WhisperSubTranslate](assets/hy-mt2-benchmark.png)

Source: official benchmarks from Tencent: [Hy-MT2 repository](https://github.com/Tencent-Hunyuan/Hy-MT2), [technical report](https://arxiv.org/pdf/2605.22064), [models on HuggingFace](https://huggingface.co/tencent/Hy-MT2-1.8B). The chart is redrawn from Tencent's official Figure 1, with bundled-model (1.8B/7B) numbers checked against the paper tables. These figures measure the underlying model on standard machine translation benchmarks (WildMTBench, WMT25, FLORES-200, etc.), not a WhisperSubTranslate-specific benchmark.

For long videos (1hr+), MyMemory's daily limit can cause slowdowns. Use Gemini, DeepL, or a configured GPT model instead.

## Speech recognition models

Models download on demand into `_models/`. CUDA is used when available, otherwise CPU runs by default. Pick a size that fits your GPU.

| Model | Size | VRAM | Speed | Notes |
| --- | --- | --- | --- | --- |
| tiny | ~75MB | ~1GB | Fastest | Basic |
| base | ~142MB | ~1GB | Fast | Good |
| small | ~466MB | ~1GB | Medium | Better |
| medium | ~1.5GB | ~2GB | Medium | Great |
| large-v3 
