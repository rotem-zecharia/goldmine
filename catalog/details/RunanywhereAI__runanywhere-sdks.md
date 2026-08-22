# RunanywhereAI/runanywhere-sdks

Production ready toolkit to run AI locally

## installation

The fastest way to feel it. Install, load, generate, all local:

```bash
pip install runanywhere
```

```python
import runanywhere as ra
from runanywhere import LlmOptions

ra.initialize()

## features

| Feature | Swift | Kotlin | Flutter | RN | Web | Electron | Python | rcli |
|---------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| LLM generation + streaming | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Vision language models (VLM) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Computer-use agent (CUA) | Yes | Yes | Yes | Yes | API only | n/a | n/a | n/a |
| Speech-to-Text | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Text-to-Speech | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Voice activity detection | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Voice agent pipeline | Yes | Yes | Yes | Yes | Yes | Yes | Stub | Yes |
| Wake word | No | No | No | No | No | No | No | No |
| Embeddings | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| RAG (with streaming) | Yes | Yes | Yes | Yes | Yes* | Yes | Yes | n/a |
| Structured output (JSON) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | n/a |
| Tool calling | Yes | Yes | Yes | Yes | Yes | Yes | Yes | n/a |
| Image generation (diffusion) | Yes | Yes | Yes | Yes | n/a | n/a | Stub | Yes |
| LoRA adapters | Yes | Yes | Yes | Yes | Yes | Partial | Stub | Yes |
| Diarization (standalone) | Yes | Yes | Gated | Yes | Yes | n/a | Stub | n/a |
| Segmentation | Yes | Yes | Gated | Yes | Yes | n/a | Stub | n/a |
| `capabilities()` discovery | Yes | Yes | Yes | Yes | Yes | Partial | Yes | n/a |

\* Web RAG may be limited to one session per process — check `capabilities().rag.multiSession`.
`Stub` / `Gated` / `Partial` mean the verb is absent, preflight-fails, or only partially wired; call `capabilities()` for the installed build.
| Hexagon NPU (QHexRT) | n/a | Yes | Yes | Yes | n/a | n/a | n/a | n/a |
| MLX (Apple silicon) | Yes | n/a | Yes | Yes | n/a | n/a | n/a | Yes |
| OpenAI-compatible server | n/a | n/a | n/a | n/a | n/a | n/a | Yes | Yes |
| Model download + progress | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| **Connect (LAN host/client)** | Host (macOS) / Client (iOS, iPadOS) | Client | — | — | — | — | — | — |

## requirements

| Platform | Minimum |
|----------|---------|
| iOS | 17.5+ |
| macOS | 14.5+ |
| Android | API 24 (7.0), arm64 recommended |
| Web | Chrome 96+ / Edge 96+, Chrome 120+ for WebGPU |
| React Native | 0.83.1+, 0.85+ recommended (Node.js 22.12+) |
| Flutter | 3.44+ (Dart 3.12+) |
| Electron | Windows x64 (preview) |
| Python | 3.9+ on Windows, macOS, Linux (3.12+ recommended) |
| rcli | macOS arm64, Linux x86_64 / aarch64, Windows x86_64 |

Hexagon NPU: Snapdragon with Hexagon v75 / v79 / v81, Android arm64.
MLX: Apple silicon, physical devices.
Memory: 2 GB minimum, 4 GB+ recommended for larger models.

---
