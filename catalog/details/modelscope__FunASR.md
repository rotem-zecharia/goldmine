# modelscope/FunASR

Open-source speech recognition toolkit for training, inference, streaming ASR, VAD, punctuation, speaker diarization pipelines, and OpenAI-compatible/MCP serving.

## installation

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/modelscope/FunASR/blob/main/examples/colab/funasr_quickstart.ipynb)

No local setup? Open the [Colab quickstart](./examples/colab/) to transcribe a public sample or upload your own audio in a browser.

Found FunASR useful? [Star the project](https://github.com/modelscope/FunASR) so more builders can find it.

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
```

For the separate 31-language checkpoint, use
[Fun-ASR-MLT-Nano-2512](https://huggingface.co/FunAudioLLM/Fun-ASR-MLT-Nano-2512).
Language coverage is checkpoint-specific, so Nano and MLT-Nano should be treated as distinct model choices.

For a CPU-first example with five-language ASR plus emotion and audio-event
tags, use **SenseVoiceSmall**. The pipeline below combines it with FSMN-VAD and
CAM++ for speaker-aware VAD segments; these are not native speaker outputs of
the SenseVoiceSmall checkpoint.
See the [SenseVoice paper](https://arxiv.org/abs/2407.04051),
[Hugging Face checkpoint](https://huggingface.co/FunAudioLLM/SenseVoiceSmall),
and [GGUF edge checkpoint](https://huggingface.co/FunAudioLLM/SenseVoiceSmall-GGUF).

```python
from funasr import AutoModel
from funasr.utils.postprocess_utils import rich_transcription_postprocess

model = AutoModel(model="iic/SenseVoiceSmall", vad_model="fsmn-vad", spk_model="cam++", device="cpu")
result = model.generate(
    input="https://isv-data.oss-cn-hangzhou.aliyuncs.com/ics/MaaS/ASR/test_audio/asr_example_zh.wav",
    batch_size_s=300,
)

# The AutoModel pipeline returns VAD segments with speaker ids and timestamps:
for seg in result[0]["sentence_info"]:
    print(f"[{seg['start']/1000:.1f}s] Speaker {seg['spk']}: {rich_transcription_postprocess(seg['sentence'])}")
```

This prints each returned segment's start time in seconds, anonymous speaker
index, and text with SenseVoice tags removed. Text and segment boundaries depend
on the audio and checkpoint; no fixed transcript is asserted here.

CAM++ extracts `spk_embedding` vectors. `AutoModel` clusters those embeddings
and assigns speaker indices to VAD segments. Indices are local to a recording,
not known-person identities. See the [SDK contract](./docs/python_api.md) for
the component and result boundaries. Change to `device="cuda"` only after
verifying a compatible GPU environment as described above.

### Scale & deploy the flagship

At scale, accelerate Fun-ASR-Nano with vLLM (batch processing):

```python
from funasr.auto.auto_model_vllm import AutoModelVLLM

model = AutoModelVLLM(model="FunAudioLLM/Fun-ASR-Nano-2512", tensor_parallel_size=1)
results = model.generate(["audio1.wav", "audio2.wav"], language="auto")
```

> **Deploy as API server:** [Local SenseVoice CPU recipe](#deploy) · [Nano GPU serving and pinned vLLM setup](./docs/vllm_guide.md)
>
> **Use with AI agents:** [MCP Server](examples/mcp_server/) for Claude/Cursor · [OpenAI API](examples/openai_api/) for LangChain/Dify/AutoGen
>
> **Use with voice agents:** [OpenClaw realtime plugin](integrations/openclaw/)

## features

FunASR is a toolkit: choose the task, checkpoint, and runtime separately.
Support in one model or adapter does not imply support in every serving backend.

| Task | Checkpoint or pipeline | Runtime entrypoint | Important limitation |
|---|---|---|---|
| File transcription with emotion/event tags | SenseVoiceSmall | Python `AutoModel`, CPU or GPU | Five-language checkpoint; tags do not identify speakers. |
| LLM-based file transcription | Fun-ASR-Nano | `AutoModel`; split-engine `AutoModelVLLM` for the documented GPU path | Base Nano covers zh/en/ja and Chinese dialects/accents; timestamp support depends on checkpoint and path. |
| Broader multilingual transcription | Fun-ASR-MLT-Nano | Python `AutoModel` | Separate 31-language checkpoint; do not transfer its coverage to base Nano. |
| Chunked live transcription | Paraformer-zh-streaming | Streaming SDK or runtime WebSocket service | Use the streaming checkpoint and per-session cache, not an offline checkpoint. |
| Speaker-aware file transcription | SenseVoiceSmall + FSMN-VAD + CAM++ | `AutoModel` with VAD and embedding clustering | Anonymous indices within a recording, not enrolled-speaker identification. |
| Joint text, timestamps, and speakers | MOSS-Transcribe-Diarize, third-party OpenMOSS | FunASR adapter or upstream backend in the MOSS guide | Offline, recording-local anonymous labels; no external VAD/speaker pipeline for its unified path. |
| Native CPU/edge transcription | Fun-ASR-Nano or SenseVoiceSmall GGUF | llama.cpp runtime | Requires matching converted weights; GGUF is not a Python `AutoModel` checkpoint. |

See the [Model Zoo](./model_zoo/readme.md) and [deployment matrix](./docs/deployment_matrix.md)
for checkpoint, interface, and licensing boundaries. Benchmark on your own audio
and hardware before choosing a runtime.

Trying FunASR for the first time? Use the [Colab quickstart](./examples/colab/) before setting up a local environment. Choosing a first model? Start with the [model selection guide](./docs/model_selection.md). Planning a switch from Whisper or a cloud ASR provider? Use the [migration guide](./docs/migration_from_whisper.md) and [benchmark example](./examples/migration/) to test representative audio, map features, and roll out safely.

---

## tools

> [Python tutorial](./docs/tutorial/README.md) · [SDK parameters and outputs](./docs/python_api.md) · [Training](./docs/training.md) · [Model registration](./docs/model_registration.md)

```python
from funasr import AutoModel

# Chinese production (VAD + ASR + punctuation + speaker)
model = AutoModel(model="paraformer-zh", vad_model="fsmn-vad", punc_model="ct-punc", spk_model="cam++", device="cuda")
result = model.generate(input="https://isv-data.oss-cn-hangzhou.aliyuncs.com/ics/MaaS/ASR/test_audio/asr_example_zh.wav", hotword="关键词 20")
