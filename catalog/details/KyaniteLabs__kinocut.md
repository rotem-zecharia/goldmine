# KyaniteLabs/kinocut

Guardrailed video editing MCP server for AI agents. FFmpeg, Hyperframes, repurposing tools, Python client, and CLI. Local, fast, free.

## features

AI agents can write FFmpeg commands, but they should not have to guess flags, parse brittle stderr, or silently publish broken media. Kinocut gives agents typed operations, inspectable tool metadata, structured results, preflight guardrails, and quality checkpoints so a video workflow can be automated and reviewed without turning into shell-command roulette.

Use it when you want an AI assistant to:

- trim, merge, resize, crop, rotate, transcode, or export video;
- add text, subtitles, watermarks, overlays, filters, fades, effects, and transitions;
- extract audio, normalize audio, synthesize audio, add generated audio, or create waveforms;
- detect scenes, make thumbnails, generate storyboards, compare quality, and create release checkpoints;
- match, grade, and gate still packages with establish-locked color cohesion, or analyze product images for colors and palettes;
- scaffold cinematic projects, read STYLE_/NEG_ blocks, parse storyboard tables, and expand shot prompts;
- create new Hyperframes projects, inspect rendered layouts, capture websites, generate local speech, remove backgrounds, and post-process the result with FFmpeg tools;
- repurpose one source video into vertical, horizontal, and square local delivery packages with manifests and review artifacts;
- drive repeatable media workflows from Claude Code, Cursor, Codex-style clients, scripts, or CI.

## installation

Prerequisite: [FFmpeg](https://ffmpeg.org/) must be installed and available on `PATH`.

```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt install ffmpeg
```

Run without a global install:

```bash
uvx --from kinocut kino doctor
```

Or install with pip:

```bash
pip install kinocut
kino doctor
```

For Claude Desktop-style MCPB installs, Kinocut includes a staged local package at
`mcpb/` and a local build script:

```bash
python3 scripts/build-mcpb.py
```

This package is honest about its runtime: it launches an existing Python environment with
Kinocut installed and still requires local FFmpeg. Native self-contained bundles remain blocked
pending FFmpeg provenance, licensing, and clean-machine gates. See [docs/MCPB.md](docs/MCPB.md).

Optional **C2PA** signing for final MP4 exports is available on the development tip when
`c2patool` and a manifest/signer are configured. Signing is off by default and only reports
`signed` after a verification read succeeds. See [docs/C2PA_PROVENANCE.md](docs/C2PA_PROVENANCE.md).

Hyperframes tools additionally need Node.js 22+ and a resolvable Hyperframes CLI. Install/pin Hyperframes in the active Node package layout, add `hyperframes` to `PATH`, or set `MCP_VIDEO_HYPERFRAMES_COMMAND`.

### Which extra do I need?

The core install covers all FFmpeg editing tools. Optional features ship as extras — install only what you use:

| You want | Install | Approx. extra size |
|---|---|---|
| Speech-to-text subtitles (Whisper) | `pip install "kinocut[transcribe]"` | ~1 GB (torch) |
| Image analysis (colors, layout, contrast) | `pip install "kinocut[image]"` | ~50 MB |
| Vocal/instrument stem separation | `pip install "kinocut[stems]"` | ~2 GB (torch + demucs) |
| AI upscaling | `pip install "kinocut[upscale]"` | ~2 GB (Python ≤3.12) |
| Procedural audio/music tools | `pip install "kinocut[audio]"` | ~30 MB (numpy) |
| Everything AI | `pip install "kinocut[ai]"` | several GB |

Mix freely, e.g. `pip install "kinocut[transcribe,image]"`. Run `kino doctor` afterward — it reports exactly which features are available and what is missing.

### Upgrading from mcp-video

Kinocut preserves the original surface during the rename window. Existing installs can upgrade without changing code:

```bash
pip install --upgrade mcp-video
mcp-video doctor
```

Published `mcp-video==1.6.11` is a metadata-only compatibility installer for `kinocut==1.15.0`. The `mcp_video` import, `mcp-video` command, `MCP_VIDEO_*` environment variables, `~/.mcp-video` data directory, `mcp-video://` resource URIs, and existing receipt keys remain supported on the 1.14.x+ line. New integrations should use `kinocut`, `from kinocut import Client`, and the `kino` command.

## En español

Kinocut es un servidor MCP de edición de video para agentes de IA. La última versión publicada es **1.15.0** (`pip install kinocut`, **196 herramientas MCP / 167 CLI**). Incluye ensamblaje 360 de dual-cam desde un MP4 equirectangular ya stitched (no `.insv`), import perezoso PEP 562 y el mismo surface FFmpeg tipado para recortar, unir, subtitular, mezclar audio, efectos y reutilizar contenido (Shorts, Reels, TikTok), motor de flujos (`workflow`) con recibos verificables, rescate de video, revisión AI-video gobernada y barreras de seguridad antes de renderizar. Programas humanos residuales (directorios, lanzamiento) no se reclaman completos.

Requisito: [FFmpeg](https://ffmpeg.org/) instalado y disponible en el `PATH`.

```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt install ffmpeg

# Instalación y diagnóstico
pip install kinocut
kino doctor
```

Para Claude Code:

```bash
claude mcp add kinocut -- uvx --from kinocut kino
```

`kino doctor` informa qué funciones están disponibles y qué falta instalar. La documentación completa está en inglés; los mensajes de error principales son bilingües.

## Quick Start

### Golden path (60 seconds)

Prove the install works before wiring an agent host:

```bash
pip install -e .          # or: pip insta

## tools

On the **published 1.15.0** surface (and matching tip), kino registers **196 MCP tools** and **167 CLI commands**. The table summarizes core categories — `search_tools` discovers the exact operation without loading every description.

| Category | Count | Highlights |
| --- | ---: | --- |
| Core video editing | 32 | trim, merge, resize, crop, rotate, convert, overlays, subtitles, export, cleanup, templates, merge-compatibility guardrails |
| Project-backed inspection | 3 | content-addressed ingest, unified preflight, temporal evidence packages |
| Governed AI-video | 4 | exact-asset verdicts, acceptance evaluation, audio-preserving body swaps, lineage-bound salvage |
| Agent workflow engine | 4 | validate, plan, render, resume, inspect multi-step jobs with provenance receipts |
| Dedicated rescue | 3 | diagnose, approve, render, verify, quarantine, and resume local content-preserving repairs |
| Post-rescue planning | 8 | semantic timelines/query, EDLs, visual transforms, restoration, composition, autopilot, explicit egress |
| Cinematic creation | 4 | project scaffold, style-pack parsing, storyboard parsing, shot prompt expansion |
| AI-assisted media | 11 | transcription, scene detection, upscaling, stem separation, silence removal, color grading |
| Hyperframes | 18 | init, preview, render, snapshots, inspect, catalog, website capture, local TTS, transcription, background removal, diagnostics, benchmark, post-process |
| Repurposing | 2 | dry-run manifests, platform-ready variants, thumbnails, storyboards, release checkpoints |
| Procedural audio | 7 | synthesize, compose, presets, effects, sequences, generated audio, spatial audio, mix-parameter guardrails |
| Visual effects | 8 | vignette, glow, noise, scanlines, chromatic aberration, luma key, mask, shape mask, bounded filter parameters |
| Transitions | 3 | glitch, morph, pixelate |
| Layout and motion | 6 | grid, picture-in-picture, split-screen, animated text, counters, progress bars, auto-chapters, layout mismatch warnings |
| Analysis | 8 | scene detection, thumbnail, preview, storyboard, quality compare, metadata, waveform, release checkpoint |
| Image analysis | 3 | extract colors, generate palettes, analyze product images |
| Still / plate editing | 5 | still-match, still-grade, still-gate, image-edit, still-package — establish-locked color match with cohesion gate |
| Discovery | 1 | `search_tools` |

```python
from kinocut import Client

editor = Client()
matches = editor.search_tools("subtitle")
print(matches["tools"])
```

Full reference: [docs/TOOLS.md](docs/TOOLS.md)

## Agent-Safe Workflow

For autonomous agents, the intended path is inspect, edit, verify, then ask a human to review release artifacts:

```python
from kinocut import Client

client = Client()

print(client.inspect("trim"))

result = client.pipeline(
    [
        {"op": "trim", "input": "source.mp4", "start": "00:01:00", "duration": "00:00:45"},
        {"op": "add_text", "text": "Launch clip", "position": "top-center"},
        {"op": "normalize_audio"},
        {"op": "resize", "aspect_ratio": "9:16"},
        {"op": "export", "quality": "high"},
        {"op": "release_checkpoint"},
    ],
    output_path="final-short.mp4",
)
```

Safety contract:

- Media-producing calls return structured results with output paths.
- High-risk edit paths now run preflight guardrails before FFmpeg execution: filter bounds, merge compatibility, audio mix volume/timing, overlay/watermark/chroma opacity and similarity, animated text timing/overflow, and grid/split-screen mismatch warnings.
- Analysis and discovery calls return structured JSON reports.
- Tool discovery is available through `search_tools()` and `Client.inspect()`.
- Unexpected keyword errors are converted into actionable `MCPVideoError` guidance.
- Do not publish agent-generated video without `video_quality_check`, `video_release_checkpoint`, and human visual/audio inspection.
- For governed AI-video derivatives, require stored identities, act
