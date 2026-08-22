# modelscope/FunASR

Open-source speech recognition toolkit for training, inference, streaming ASR, VAD, punctuation, speaker diarization pipelines, and OpenAI-compatible/MCP serving.

## installation

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/modelscope/FunASR/blob/main/examples/colab/funasr_quickstart.ipynb)

No local setup? Open the [Colab quickstart](./examples/colab/) to transcribe a public sample or upload your own audio in a browser.

```bash
# CPU-only installs can use the default PyPI wheels.
pip install torch torchaudio
pip install funasr
```

For GPU quickstarts, install the PyTorch and torchaudio wheels that match your
NVIDIA driver from [pytorch.org](https://pytorch.org/get-started/locally/)
before installing FunASR. After installation, confirm the GPU is visible:

```bash
python - <<'PY'
import torch
print(torch.cuda.is_available())
PY
```

Only use `device="cuda"` when this prints `True`; otherwise use `device="cpu"`
or reinstall PyTorch with the correct CUDA wheel.

**Flagship model — Fun-ASR-Nano** (LLM-ASR for Chinese, English, and Japanese, plus Chinese dialect groups and regional accents; needs a GPU):

```python
from funasr import AutoModel

model = AutoModel(model="FunAudioLLM/Fun-ASR-Nano-2512", device="cuda")
result = model.generate(input="https://isv-data.oss-cn-hangzhou.aliyuncs.com/ics/MaaS/ASR/test_audio/asr_example_zh.wav")
print(result[0]["text"])
# 欢迎大家来体验达摩院推出的语音识别模型。
```

For the separate 31-language checkpoint, use
[Fun-ASR-MLT-Nano-2512](https://huggingface.co/FunAudioLLM/Fun-ASR-MLT-Nano-2512).
Language coverage is checkpoint-specific, so Nano and MLT-Nano should be treated as distinct model choices.

On CPU (or for five-language ASR plus emotion and audio-event tags), use
**SenseVoiceSmall**. The pipeline below composes SenseVoiceSmall with FSMN-VAD
and CAM++; diarization is provided by the separate CAM++ model, not by the
SenseVoiceSmall checkpoint:
See the [SenseVoice paper](https://arxiv.org/abs/2407.04051),
[Hugging Face checkpoint](https://huggingface.co/FunAudioLLM/SenseVoiceSmall),
and [GGUF edge checkpoint](https://huggingface.co/FunAudioLLM/SenseVoiceSmall-GGUF).

```python
from funasr import AutoModel
from funasr.utils.postprocess_utils import rich_transcription_postprocess

model = AutoModel(model="iic/SenseVoiceSmall", vad_model="fsmn-vad", spk_model="cam++", device="cuda")  # use device="cpu" if you don't have a GPU
result = model.generate(
    input="https://isv-data.oss-cn-hangzhou.aliyuncs.com/ics/MaaS/ASR/test_audio/asr_example_zh.wav",
    batch_size_s=300,
)

# The AutoModel pipeline returns VAD segments with speaker ids and timestamps:
for seg in result[0]["sentence_info"]:
    print(f"[{seg['start']/1000:.1f}s] Speaker {seg['spk']}: {rich_transcription_postprocess(seg['sentence'])}")
```

**Output** — structured text with speaker labels, timestamps, and punctuation:
```
[0.6s] Speaker 0: 欢迎大家来体验达摩院推出的语音识别模型
```

One `AutoModel` pipeline call coordinates the configured ASR, VAD, and speaker
models and returns the combined result.

### Scale & deploy the flagship

At scale, accelerate Fun-ASR-Nano with vLLM (batch processing):

```python
from funasr.auto.auto_model_vllm import AutoModelVLLM

model = AutoModelVLLM(model="FunAudioLLM/Fun-ASR-Nano-2512", tensor_parallel_size=1)
results = model.generate(["audio1.wav", "audio2.wav"], language="auto")
```

> **Deploy as API server:** `funasr-server --device cuda` → OpenAI-compatible endpoint at localhost:8000
>
> **Use with AI agents:** [MCP Server](examples/mcp_server/) for Claude/Cursor · [OpenAI API](examples/openai_api/) for LangChain/Dify/AutoGen
>
> **Use with voice agents:** [OpenClaw realtime plugin](integrations/openclaw/) for self-hosted Talk and Voice Call transcription

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

# Chinese production (VAD + ASR + punctuation + speaker)
model = AutoModel(model="paraformer-zh", vad_model="fsmn-vad", punc_model="ct-punc", spk_model="cam++", device="cuda")
result = model.generate(input="https://isv-data.oss-cn-hangzhou.aliyuncs.com/ics/MaaS/ASR/test_audio/asr_example_zh.wav", hotword="关键词 20")
