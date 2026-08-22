# QwenAudio/SenseVoice

Open-source SenseVoiceSmall model for Mandarin, Cantonese, English, Japanese, and Korean ASR, language ID, emotion recognition, and audio event detection.

## requirements

```shell
pip install -r requirements.txt
```

SenseVoiceSmall examples and the composed FunASR diarization path require `funasr>=1.3.26`. If you installed this repository earlier, run `pip install -U "funasr>=1.3.26"` before retrying the demos.

<a name="Usage"></a>

## tools

## Inference

Supports input of audio in any format and of any duration.

```python
from funasr import AutoModel
from funasr.utils.postprocess_utils import rich_transcription_postprocess

model_dir = "iic/SenseVoiceSmall"


model = AutoModel(
    model=model_dir,
    trust_remote_code=True,
    remote_code="./model.py",    
    vad_model="fsmn-vad",
    vad_kwargs={"max_single_segment_time": 30000},
    device="cuda:0",
)

# en
res = model.generate(
    input=f"{model.model_path}/example/en.mp3",
    cache={},
    language="auto",  # "zh", "en", "yue", "ja", "ko", "nospeech"
    use_itn=True,
    batch_size_s=60,
    merge_vad=True,  #
    merge_length_s=15,
)
text = rich_transcription_postprocess(res[0]["text"])
print(text)
```

<details><summary>Parameter Description (Click to Expand)</summary>

- `model_dir`: The name of the model, or the path to the model on the local disk.
- `trust_remote_code`:
  - When `True`, it means that the model's code implementation is loaded from `remote_code`, which specifies the exact location of the `model` code (for example, `model.py` in the current directory). It supports absolute paths, relative paths, and network URLs.
  - When `False`, it indicates that the model's code implementation is the integrated version within [FunASR](https://github.com/modelscope/FunASR). At this time, modifications made to `model.py` in the current directory will not be effective, as the version loaded is the internal one from FunASR. For the model code, [click here to view](https://github.com/modelscope/FunASR/tree/main/funasr/models/sense_voice).
- `vad_model`: This indicates the activation of VAD (Voice Activity Detection). The purpose of VAD is to split long audio into shorter clips. In this case, the inference time includes both VAD and SenseVoice total consumption, and represents the end-to-end latency. If you wish to test the SenseVoice model's inference time separately, the VAD model can be disabled.
- `vad_kwargs`: Specifies the configurations for the VAD model. `max_single_segment_time`: denotes the maximum duration for audio segmentation by the `vad_model`, with the unit being milliseconds (ms).
- `use_itn`: Whether the output result includes punctuation and inverse text normalization.
- `batch_size_s`: Indicates the use of dynamic batching, where the total duration of audio in the batch is measured in seconds (s).
- `merge_vad`: Whether to merge short audio fragments segmented by the VAD model, with the merged length being `merge_length_s`, in seconds (s).
- `ban_emo_unk`: Whether to ban the output of the `emo_unk` token.
</details>

### Speaker Diarization

This example composes SenseVoiceSmall with separate FSMN-VAD, CAM++, and punctuation models through FunASR. CAM++ provides the speaker labels; the SenseVoiceSmall checkpoint itself does not:

```python
from funasr import AutoModel
from funasr.utils.postprocess_utils import rich_transcription_postprocess

model = AutoModel(
    model="iic/SenseVoiceSmall",
    trust_remote_code=True,
    remote_code="./model.py",
    vad_model="fsmn-vad",
    vad_kwargs={"max_single_segment_time": 30000},
    spk_model="cam++",
    punc_model="ct-punc",
    device="cuda:0",
)
res = model.generate(
    input="example.wav",
    cache={},
    language="auto",
    use_itn=True,
    batch_size_s=60,
    merge_vad=True,
    merge_length_s=15,
)
# Per-sentence results with speaker labels
for sent in res[0]["sentence_info"]:
    text = rich_transcription_postprocess(sent["text"])
    print(f"Speaker {sent['spk']}: [{sent['start']}ms - {sent['end']}ms] {text}")
```

> Note: Requires installing FunASR from source: `pip install git+https://github.com/modelscope/FunASR.git`

If all inputs are short audios (<30s), and batch inference is needed to speed up inference efficiency, the VAD model can be removed, and `batch_size` can be set accordingly.
```python
model = AutoModel(model=model_dir, trust_remote_code=True, device="cuda:0")

res = model.generate(
    input=f"{model.mod

## installation

from pathlib import Path
from funasr_onnx import SenseVoiceSmall
from funasr_onnx.utils.postprocess_utils import rich_transcription_postprocess


model_dir = "iic/SenseVoiceSmall"

model = SenseVoiceSmall(model_dir, batch_size=10, quantize=True)

# inference
wav_or_scp = ["{}/.cache/modelscope/hub/{}/example/en.mp3".format(Path.home(), model_dir)]

res = model(wav_or_scp, language="auto", use_itn=True)
print([rich_transcription_postprocess(i) for i in res])
```
Note: ONNX model is exported to the original model directory.

#### Libtorch
```python
from pathlib import Path
from funasr_torch import SenseVoiceSmall
from funasr_torch.utils.postprocess_utils import rich_transcription_postprocess


model_dir = "iic/SenseVoiceSmall"

model = SenseVoiceSmall(model_dir, batch_size=10, device="cuda:0")

wav_or_scp = ["{}/.cache/modelscope/hub/{}/example/en.mp3".format(Path.home(), model_dir)]

res = model(wav_or_scp, language="auto", use_itn=True)
print([rich_transcription_postprocess(i) for i in res])
```
Note: Libtorch model is exported to the original model directory.
</details>

### Run on CPU / edge — llama.cpp / GGUF (no GPU, no Python)

Run SenseVoice as a **single self-contained binary** — this is to SenseVoice what [whisper.cpp](https://github.com/ggml-org/whisper.cpp) is to Whisper, but with far stronger Chinese & Cantonese accuracy. Built-in FSMN-VAD, no Python at runtime.

```bash
bash runtime/llama.cpp/download-funasr-model.sh sensevoice ./gguf
llama-funasr-sensevoice -m ./gguf/sensevoice-small-f16.gguf --vad ./gguf/fsmn-vad.gguf -a audio.wav
```

**Prebuilt binaries:** [Releases](https://github.com/QwenAudio/SenseVoice/releases) · **Download & quickstart:** [funasr.com/llama-cpp](https://www.funasr.com/llama-cpp.html) · **GGUF:** [Hugging Face](https://huggingface.co/FunAudioLLM/SenseVoiceSmall-GGUF) · **Docs & benchmarks:** [runtime/llama.cpp/](./runtime/llama.cpp/)

## Service
