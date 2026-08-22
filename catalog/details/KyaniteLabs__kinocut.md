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
