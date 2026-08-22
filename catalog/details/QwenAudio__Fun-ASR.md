# QwenAudio/Fun-ASR

Open-source LLM-based ASR model family for Chinese, dialect, accent, and multilingual speech, with FunASR, vLLM, streaming, and llama.cpp runtimes.

## features

**Fun-ASR** focuses on high-precision speech recognition, checkpoint-specific multilingual support, and industry customization capabilities.

- **Far-field High-noise Recognition:** Deeply optimized for far-distance sound pickup and high-noise scenarios (such as conference rooms, in-vehicle environments, industrial sites, etc.), improving recognition accuracy to **93%**.
- **Chinese Dialects and Regional Accents:**
  - Supports **7 major dialects**: Wu, Cantonese, Min, Hakka, Gan, Xiang, Jin
  - Covers **26 regional accents**: including Henan, Shaanxi, Hubei, Sichuan, Chongqing, Yunnan, Guizhou, Guangdong, Guangxi and more than 20 other regions
- **Checkpoint-specific language coverage:** Fun-ASR-Nano supports Chinese, English, Japanese, and Chinese dialects and accents. Fun-ASR-MLT-Nano supports **31 languages**, with emphasis on East and Southeast Asian languages.
- **Music Background Lyric Recognition:** Enhanced speech recognition performance under music background interference, supporting accurate recognition of lyric content in songs.

## installation

```shell
git clone https://github.com/QwenAudio/Fun-ASR.git
cd Fun-ASR
pip install -r requirements.txt
```

<a name="usage-tutorial"></a>

# Capability boundaries

- [ ] Reliable checkpoint-native timestamps
  > The released Fun-ASR-Nano `model.pt` checkpoint does not include trained `ctc_decoder.*` / `ctc.*` weights. Any timestamp output is therefore not reliable. For accurate character-level timestamps, use Paraformer, for example `AutoModel(model="paraformer-zh", vad_model="fsmn-vad", ...)`. See [issue #106](https://github.com/QwenAudio/Fun-ASR/issues/106).
- [ ] Checkpoint-native speaker diarization
  > Fun-ASR-Nano and Fun-ASR-MLT-Nano do not emit speaker labels by themselves. Compose them in FunASR with the separate `fsmn-vad` and `cam++` models, as shown below.
- [x] Model training

## tools

## Inference

### Run on CPU / edge — llama.cpp / GGUF (no GPU, no Python)

Run Fun-ASR-Nano as a **single self-contained binary** — like [whisper.cpp](https://github.com/ggml-org/whisper.cpp) but for FunASR, with strong Chinese accuracy. Built-in FSMN-VAD, no Python at runtime.

```bash
bash runtime/llama.cpp/download-funasr-model.sh nano ./gguf
llama-funasr-cli --enc ./gguf/funasr-encoder-f16.gguf -m ./gguf/qwen3-0.6b-q8_0.gguf -a audio.wav --vad ./gguf/fsmn-vad.gguf
```

`fsmn-vad.gguf` is hosted in the shared [FunAudioLLM/fsmn-vad-GGUF](https://huggingface.co/FunAudioLLM/fsmn-vad-GGUF) repo, not inside the Nano GGUF repo. The `nano` downloader above fetches it automatically; to fetch only VAD from the Hugging Face UI/CLI, use:

```bash
hf download FunAudioLLM/fsmn-vad-GGUF --include "*.gguf" --local-dir ./gguf
```

**Prebuilt binaries:** [Releases](https://github.com/QwenAudio/Fun-ASR/releases) · **Download & quickstart:** [funasr.com/llama-cpp](https://www.funasr.com/llama-cpp.html) · **GGUF:** [Nano encoder/LLM](https://huggingface.co/FunAudioLLM/Fun-ASR-Nano-GGUF) · [FSMN-VAD](https://huggingface.co/FunAudioLLM/fsmn-vad-GGUF) · **Docs & benchmarks:** [runtime/llama.cpp/](./runtime/llama.cpp/)

### Using funasr for inference

```python
from funasr import AutoModel


def main():
    model_dir = "FunAudioLLM/Fun-ASR-Nano-2512"
    model = AutoModel(
        model=model_dir,
        trust_remote_code=True,
        remote_code="./model.py",
        device="cuda:0",
        # hub：download models from ms (for ModelScope) or hf (for Hugging Face).
        hub="hf"
    )

    wav_path = f"{model.model_path}/example/zh.mp3"
    res = model.generate(
        input=[wav_path],
        cache={},
        batch_size=1,
        hotwords=["开放时间"],
        # 中文、英文、日文 for Fun-ASR-Nano-2512
        # 中文、英文、粤语、日文、韩文、越南语、印尼语、泰语、马来语、菲律宾语、阿拉伯语、
        # 印地语、保加利亚语、克罗地亚语、捷克语、丹麦语、荷兰语、爱沙尼亚语、芬兰语、希腊语、
        # 匈牙利语、爱尔兰语、拉脱维亚语、立陶宛语、马耳他语、波兰语、葡萄牙语、罗马尼亚语、
        # 斯洛伐克语、斯洛文尼亚语、瑞典语 for Fun-ASR-MLT-Nano-2512
        language="中文",
        itn=True, # or False
    )
    text = res[0]["text"]
    print(text)

    model = AutoModel(
        model=model_dir,
        trust_remote_code=True,
        vad_model="fsmn-vad",
        vad_kwargs={"max_single_segment_time": 30000},
        remote_code="./model.py",
        device="cuda:0",
    )
    res = model.generate(input=[wav_path], cache={}, batch_size=1)
    text = res[0]["text"]
    print(text)


if __name__ == "__main__":
    main()
```

### Faster batch transcription (no vLLM)

When transcribing long audio or many files on the `funasr` (PyTorch) path, pass
`batch_size_s` to batch the VAD segments through the LLM decoder together. This
greatly improves GPU utilization:

```python
res = model.generate(
    input=[wav_path],
    cache={},
    language="中文",
    itn=True,
    batch_size_s=120,   # batch VAD segments up to ~120s of audio per LLM call
)
```

On Fun-ASR-Nano-2512 (184 Chinese files / 11,539 s, single H100) this is about
**1.6x faster** than the default per-segment decoding (RTFx 19.8 -> 31.8) with no
loss in accuracy. For the highest throughput, use the vLLM path below.

### Speaker Diarization

This example is a composed FunASR pipeline: FSMN-VAD segments the audio,
Fun-ASR-Nano transcribes it, CAM++ assigns speaker labels, and CT-Punc restores
punctuation. The `start` and `end` values are VAD segment boundaries, not
reliable checkpoint-native character timestamps.

```python
from funasr import AutoModel


def main():
    model_dir = "FunAudioLLM/Fun-ASR-Nano-2512"
    model = AutoModel(
        model=model_dir,
        trust_remote_code=True,
        remote_code="./model.py",
        vad_model="fsmn-vad",
        vad_kwargs={"max_single_segment_time": 30000},
        spk_model="cam++",
        punc_model="ct-punc",
        device="cuda:0",
        hub="hf",
    )

    wav_path = f"{model.model_path}/example/zh.mp3"
    res = model.generate(input=[wav_path], cache={}, batch_size=1, language="中文
