# crosswk/SayIt

Open-source voice typing for Windows — a Wispr Flow / Superwhisper alternative. Press a shortcut, speak, and AI-polished text lands at your cursor. Local models, your own API keys, or a self-hosted ba

## features

Typing is often the slowest part of working with AI. SayIt turns speech into text you can use immediately, while keeping the important choices in your hands:

- **Voice typing anywhere** — dictate into editors, chat apps, browsers, and other Windows software.
- **Editable AI cleanup** — remove filler words, repair recognition errors, format ideas, or keep a faithful transcript. Every prompt is yours to change.
- **Context-aware writing** (off by default) — reads the text around your cursor so new dictation matches its tone and terminology. Select text first and your speech becomes an editing instruction—translate, tighten, rewrite, or ask a question—replacing the selection directly. Password fields are skipped.
- **Flexible speech recognition** — use a cloud ASR provider, run a local GGUF model on your own GPU, connect to the public trial server, or host your own backend.
- **English and Chinese interface** — the UI follows your system language and can be switched at any time.
- **Hotwords and per-app rules** — improve names and technical terms, then change cleanup behavior automatically for different apps.
- **Overlay feedback** — a small waveform overlay shows recording state and elapsed time, with optional live captions while you speak.
- **Transparent data flow** — the app shows which mode is active and where audio and text are processed.
- **Local history and diagnostics** — review recordings, re-transcribe them, and collect useful troubleshooting details without guesswork.

## configuration

docker compose up -d --build
```

GPU speech recognition requires an NVIDIA GPU; 16 GB or more of VRAM is recommended for the default server model. See the [server guide](server/README.md) for configuration, deployment, security, and API details.
