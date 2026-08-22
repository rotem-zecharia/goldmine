# modelscope/FunClip

FunASR-powered video transcription, subtitle generation, and LLM-assisted clipping tool with a local Gradio UI.

## installation

### Python env install

FunClip basic functions rely on a python environment only.
```shell
# clone funclip repo
git clone https://github.com/modelscope/FunClip.git
cd FunClip
# install Python requirments
pip install -r ./requirements.txt
```

For a versioned snapshot, download [FunClip-2.1.1.tar.gz](https://github.com/modelscope/FunClip/releases/download/v2.1.1/FunClip-2.1.1.tar.gz) or [FunClip-2.1.1.zip](https://github.com/modelscope/FunClip/releases/download/v2.1.1/FunClip-2.1.1.zip), then verify it with the published [SHA256SUMS](https://github.com/modelscope/FunClip/releases/download/v2.1.1/SHA256SUMS). Model weights are downloaded separately when FunClip starts and are not included in these source archives.

FunClip v2.1.1 supports Gradio 4 with `starlette<1.0`. Existing installations should run `pip install -U -r requirements.txt` before restarting. Container users can pass `--listen` to bind all interfaces; a public Gradio sharing tunnel is created only when `--share` is also supplied.

FunClip's Fun-ASR-Nano, SenseVoice, and subtitle compatibility paths require `funasr>=1.3.29`. This release returns every SenseVoice VAD region through `sentence_info` when token timestamps are unavailable, so clipping and subtitle clients receive segment boundaries instead of an empty timeline. It also includes the real-time final-text and short-tail fixes from 1.3.28. If you installed FunClip before this requirement was updated, run `pip install -U "funasr>=1.3.29"` before starting the Gradio service. [Release notes](https://github.com/modelscope/FunASR/releases/tag/v1.3.29) · [PyPI](https://pypi.org/project/funasr/1.3.29/)

### imagemagick install (Optional)

If you want to clip video file with embedded subtitles

1. ffmpeg and imagemagick is required

- On Ubuntu
```shell
apt-get -y update && apt-get -y install ffmpeg imagemagick
sed -i 's/none/read,write/g' /etc/ImageMagick-6/policy.xml
```
- On MacOS
```shell
brew install imagemagick
sed -i '' 's/none/read,write/g' "$(brew --prefix imagemagick)/etc/ImageMagick-7/policy.xml" 
```
- On Windows

Download and install imagemagick https://imagemagick.org/script/download.php#windows

Find your python install path and change the `IMAGEMAGICK_BINARY` to your imagemagick install path in file `site-packages\moviepy\config_defaults.py`

2. Download font file to funclip/font

```shell
wget https://isv-data.oss-cn-hangzhou.aliyuncs.com/ics/MaaS/ClipVideo/STHeitiMedium.ttc -O font/STHeitiMedium.ttc
```
<a name="Usage"></a>
## Use FunClip

### A. Use FunClip as local Gradio Service
You can establish your own FunClip service which is same as [Modelscope Space](https://modelscope.cn/studios/iic/funasr_app_clipvideo/summary) as follow:
```shell
python funclip/launch.py
# '-m fun-asr-nano' for the flagship Fun-ASR-Nano model (Mandarin, English,
# Japanese, 7 Chinese dialect groups, and 26 regional accents)
# '-m sensevoice' for SenseVoice model (multilingual ASR + emotion + audio event detection)
# '-l en' for English audio recognize
# '-p xxx' for setting port number
# '-s True' for establishing service for public accessing
```

#### Model selection quick start

| Scenario | Command |
| --- | --- |
| Default Chinese video clipping with Paraformer | `python funclip/launch.py` |
| High-accuracy transcription with the flagship Fun-ASR-Nano checkpoint (use Paraformer for precise text-based clipping) | `python funclip/launch.py -m fun-asr-nano` |
| Multilingual ASR with emotion and audio event tags | `python funclip/launch.py -m sensevoice` |
| English video clipping with the Paraformer English model | `python funclip/launch.py -l en` |

If you only need offline speech transcription on CPU or edge devices and do not need FunClip's video clipping UI, use the FunASR llama.cpp / GGUF runtime instead: [funasr.com/llama-cpp](https://www.funasr.com/llama-cpp.html) · [Fun-ASR-Nano-GGUF](https://huggingface.co/FunAudioLLM/Fun-ASR-Nano-GGUF) · [SenseVoiceSmall-GGUF](https://huggingface.co/FunAudioLLM/SenseVoiceSm

## tools

mkdir -p examples
wget "https://huggingface.co/spaces/R1ckShi/FunClip/resolve/main/examples/2022%E4%BA%91%E6%A0%96%E5%A4%A7%E4%BC%9A_%E7%89%87%E6%AE%B5.mp4" -O "examples/2022云栖大会_片段.mp4"

# step1: Recognize
python funclip/videoclipper.py --stage 1 \
                       --file examples/2022云栖大会_片段.mp4 \
                       --output_dir ./output
# now you can find recognition results and entire SRT file in ./output/
# step2: Clip
python funclip/videoclipper.py --stage 2 \
                       --file examples/2022云栖大会_片段.mp4 \
                       --output_dir ./output \
                       --dest_text '我们把它跟乡村振兴去结合起来，利用我们的设计的能力' \
                       --start_ost 0 \
                       --end_ost 100 \
                       --output_file './output/res.mp4'
```

<a name="Community"></a>
## Community Communication🍟

FunClip was first open-sourced by the FunASR team, and useful PRs are welcome.

You can also scan the following DingTalk group or WeChat group QR code to join the community group for communication.

QR codes can expire. If scanning is unavailable, use [GitHub Discussions](https://github.com/modelscope/FunClip/discussions) for questions, ideas, and community projects.

|                           DingTalk group                            |                     WeChat group                      |
|:-------------------------------------------------------------------:|:-----------------------------------------------------:|
| <div align="left"><img src="docs/images/dingding.png" width="250"/> | <img src="docs/images/wechat.png" width="215"/></div> |

## Ecosystem

FunClip is part of the **FunAudioLLM** family:

| Project | Description | Stars |
|---------|-------------|-------|
| [FunASR](https://github.com/modelscope/FunASR) | Industrial speech recognition toolkit — VAD, ASR, punctuation, diarization | [![](https://img.shields.io/github/stars/modelscope/FunASR?style=social)](https://github.com/modelscope/FunASR) |
| [Fun-ASR-Nano](https://github.com/QwenAudio/Fun-ASR) | End-to-end LLM-based ASR — flagship and separate 31-language MLT checkpoints, streaming, hotwords ([HF model](https://huggingface.co/FunAudioLLM/Fun-ASR-Nano-2512)) | [![](https://img.shields.io/github/stars/QwenAudio/Fun-ASR?style=social)](https://github.com/QwenAudio/Fun-ASR) |
| [SenseVoice](https://github.com/QwenAudio/SenseVoice) | Multilingual speech understanding — ASR + emotion + audio events ([HF model](https://huggingface.co/FunAudioLLM/SenseVoiceSmall)) | [![](https://img.shields.io/github/stars/QwenAudio/SenseVoice?style=social)](https://github.com/QwenAudio/SenseVoice) |
| [CosyVoice](https://github.com/QwenAudio/CosyVoice) | Natural speech generation — multi-language, zero-shot cloning | [![](https://img.shields.io/github/stars/QwenAudio/CosyVoice?style=social)](https://github.com/QwenAudio/CosyVoice) |

📚FunASR Paper: <a href="https://arxiv.org/abs/2305.11013"><img src="https://img.shields.io/badge/Arxiv-2305.11013-orange"></a> 
📚SeACo-Paraformer Paper: <a href="https://arxiv.org/abs/2308.03266"><img src="https://img.shields.io/badge/Arxiv-2308.03266-orange"></a>

## License

- FunClip source code is licensed under the [MIT License](./LICENSE).
- Model weights are downloaded separately and are governed by the terms on their model pages. The default [Paraformer-Large](https://modelscope.cn/models/iic/speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-pytorch/summary), [SeACo-Paraformer](https://modelscope.cn/models/iic/speech_seaco_paraformer_large_asr_nat-zh-cn-16k-common-vocab8404-pytorch/summary), and [CAM++](https://modelscope.cn/models/iic/speech_campplus_sv_zh-cn_16k-common/summary) pages currently list Apache License 2.0; check the applicable model page before redistribution.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=modelscope/FunClip&type=Date)](https://star-history.com/#modelscope/FunClip&Date)
