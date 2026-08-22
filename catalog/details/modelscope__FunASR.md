# modelscope/FunASR

Open-source speech recognition toolkit for training, inference, streaming ASR, VAD, punctuation, speaker diarization pipelines, and OpenAI-compatible/MCP serving.

## installation

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/modelscope/FunASR/blob/main/examples/colab/funasr_quickstart.ipynb)

No local setup? Open the [Colab quickstart](./examples/colab/) to transcribe a public sample or upload your own audio in a browser.

```bash

## features

Whisper is a single model; **FunASR is a toolkit** — you pick the right model
per job: **Fun-ASR-Nano** (Chinese, English, Japanese, and Chinese dialects;
GPU), **Fun-ASR-MLT-Nano** (31 languages), **SenseVoiceSmall** (five-language
ASR plus emotion and audio events), and **Paraformer** (low-latency streaming).
The table shows toolkit-level capabilities and names the model or pipeline that
provides each one:

| | FunASR (toolkit) | Whisper | Cloud APIs |
|---|---|---|---|
| Top speed | **340x realtime** (Fun-ASR-Nano + vLLM) | 13x realtime | ~1x realtime |
| Speaker ID | ✅ via VAD + CAM++ pipeline | ❌ Needs pyannote | ✅ Extra cost |
| Emotion | ✅ via SenseVoice | ❌ | ❌ |
| Languages | Checkpoint-specific (for example Qwen3-ASR 52, MLT-Nano 31, Nano zh/en/ja) | 57 | Varies |
| Streaming | ✅ WebSocket (Paraformer) | ❌ | ✅ |
| CPU viable | ✅ 17x realtime (SenseVoice) | ❌ Too slow | N/A |
| Self-hosted | ✅ Yes (toolkit: MIT; model licenses vary) | ✅ MIT license | ❌ Cloud only |
| Cost | Free | Free | $0.006/min+ |

Trying FunASR for the first time? Use the [Colab quickstart](./examples/colab/) before setting up a local environment. Choosing a first model? Start with the [model selection guide](./docs/model_selection.md). Planning a switch from Whisper or a cloud ASR provider? Use the [migration guide](./docs/migration_from_whisper.md) and [benchmark example](./examples/migration/) to test representative audio, map features, and roll out safely.

---

## tools

> Full examples with parameter docs: [Tutorial →](https://modelscope.github.io/FunASR/tutorial.html)

```python
from funasr import AutoModel
