# m-bain/whisperX

WhisperX: Automatic Speech Recognition with Word-level Timestamps (& Diarization)

## tools

If you’re looking for a transcription API for meetings, consider checking out [Recall.ai's Meeting Transcription API](https://www.recall.ai/product/meeting-transcription-api?utm_source=github&utm_medium=sponsorship&utm_campaign=mbain-whisperx), an API that works with Zoom, Google Meet, Microsoft Teams, and more. Recall.ai diarizes by pulling the speaker data and separate audio streams from the meeting platforms, which means 100% accurate speaker diarization with actual speaker names.


<p align="center">
  <a href="https://github.com/m-bain/whisperX/stargazers">
    <img src="https://img.shields.io/github/stars/m-bain/whisperX.svg?colorA=orange&colorB=orange&logo=github"
         alt="GitHub stars">
  </a>
  <a href="https://github.com/m-bain/whisperX/issues">
        <img src="https://img.shields.io/github/issues/m-bain/whisperx.svg"
             alt="GitHub issues">
  </a>
  <a href="https://github.com/m-bain/whisperX/blob/master/LICENSE">
        <img src="https://img.shields.io/github/license/m-bain/whisperX.svg"
             alt="GitHub license">
  </a>
  <a href="https://arxiv.org/abs/2303.00747">
        <img src="http://img.shields.io/badge/Arxiv-2303.00747-B31B1B.svg"
             alt="ArXiv paper">
  </a>
  <a href="https://twitter.com/intent/tweet?text=&url=https%3A%2F%2Fgithub.com%2Fm-bain%2FwhisperX">
  <img src="https://img.shields.io/twitter/url/https/github.com/m-bain/whisperX.svg?style=social" alt="Twitter">
  </a>      
</p>

<img width="1216" align="center" alt="whisperx-arch" src="https://raw.githubusercontent.com/m-bain/whisperX/refs/heads/main/figures/pipeline.png">

<!-- <p align="left">Whisper-Based Automatic Speech Recognition (ASR) with improved timestamp accuracy + quality via forced phoneme alignment and voice-activity based batching for fast inference.</p> -->

<!-- <h2 align="left", id="what-is-it">What is it 🔎</h2> -->

This repository provides fast automatic speech recognition (70x realtime with large-v2) with word-level timestamps and speaker diarization.

- ⚡️ Batched inference for 70x realtime transcription using whisper large-v2
- 🪶 [faster-whisper](https://github.com/guillaumekln/faster-whisper) backend, requires <8GB gpu memory for large-v2 with beam_size=5
- 🎯 Accurate word-level timestamps using wav2vec2 alignment
- 👯‍♂️ Multispeaker ASR using speaker diarization from [pyannote-audio](https://github.com/pyannote/pyannote-audio) (speaker ID labels)
- 🗣️ VAD preprocessing, reduces hallucination & batching with no WER degradation

**Whisper** is an ASR model [developed by OpenAI](https://github.com/openai/whisper), trained on a large dataset of diverse audio. Whilst it does produces highly accurate transcriptions, the corresponding timestamps are at the utterance-level, not per word, and can be inaccurate by several seconds. OpenAI's whisper does not natively support batching.

**Phoneme-Based ASR** A suite of models finetuned to recognise the smallest unit of speech distinguishing one word from another, e.g. the element p in "tap". A popular example model is [wav2vec2.0](https://huggingface.co/facebook/wav2vec2-large-960h-lv60-self).

**Forced Alignment** refers to the process by which orthographic transcriptions are aligned to audio recordings to automatically generate phone level segmentation.

**Voice Activity Detection (VAD)** is the detection of the presence or absence of human speech.

**Speaker Diarization** is the process of partitioning an audio stream containing human speech into homogeneous segments according to the identity of each speaker.

<h2 align="left", id="highlights">New🚨</h2>

- 1st place at [Ego4d transcription challenge](https://eval.ai/web/challenges/challenge-page/1637/leaderboard/3931/WER) 🏆
- _WhisperX_ accepted at INTERSPEECH 2023
- v3 transcript segment-per-sentence: using nltk sent_tokenize for better subtitlting & better diarization
- v3 released, 70x speed-up open-sourced. Using batched whisper with [faster-whisper](https://github.com/guillaumekln/faster-whi

## installation

To use WhisperX with GPU acceleration, install the CUDA toolkit 12.8 before WhisperX. Skip this step if using only the CPU.

- For **Linux** users, install the CUDA toolkit 12.8 following this guide:
  [CUDA Installation Guide for Linux](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/).
- For **Windows** users, download and install the CUDA toolkit 12.8:
  [CUDA Downloads](https://developer.nvidia.com/cuda-12-8-1-download-archive).

### 1. Simple Installation (Recommended)

The easiest way to install WhisperX is through PyPi:

```bash
pip install whisperx
```

Or if using [uvx](https://docs.astral.sh/uv/guides/tools/#running-tools):

```bash
uvx whisperx
```

### 2. Advanced Installation Options

These installation methods are for developers or users with specific needs. If you're not sure, stick with the simple installation above.

#### Option A: Install from GitHub

To install directly from the GitHub repository:

```bash
uvx git+https://github.com/m-bain/whisperX.git
```

#### Option B: Developer Installation

If you want to modify the code or contribute to the project:

```bash
git clone https://github.com/m-bain/whisperX.git
cd whisperX
uv sync --all-extras --dev
```

> **Note**: The development version may contain experimental features and bugs. Use the stable PyPI release for production environments.

You may also need to install ffmpeg, rust etc. Follow openAI instructions here https://github.com/openai/whisper#setup.

### Speaker Diarization

To **enable Speaker Diarization**, include your Hugging Face access token (read) that you can generate from [Here](https://huggingface.co/settings/tokens) after the `--hf_token` argument and accept the user agreement for the [speaker-diarization-community-1](https://huggingface.co/pyannote/speaker-diarization-community-1) model.

<h2 align="left" id="example">Usage 💬 (command line)</h2>

### English

Run whisper on example segment (using default params, whisper small) add `--highlight_words True` to visualise word timings in the .srt file.

    whisperx path/to/audio.wav

Result using _WhisperX_ with forced alignment to wav2vec2.0 large:

https://user-images.githubusercontent.com/36994049/208253969-7e35fe2a-7541-434a-ae91-8e919540555d.mp4

Compare this to original whisper out the box, where many transcriptions are out of sync:

https://user-images.githubusercontent.com/36994049/207743923-b4f0d537-29ae-4be2-b404-bb941db73652.mov

For increased timestamp accuracy, at the cost of higher gpu mem, use bigger models (bigger alignment model not found to be that helpful, see paper) e.g.

    whisperx path/to/audio.wav --model large-v2 --align_model WAV2VEC2_ASR_LARGE_LV60K_960H --batch_size 4

To label the transcript with speaker ID's (set number of speakers if known e.g. `--min_speakers 2` `--max_speakers 2`):

    whisperx path/to/audio.wav --model large-v2 --diarize --highlight_words True

To run on CPU instead of GPU (and for running on Mac OS X):

    whisperx path/to/audio.wav --compute_type int8 --device cpu

### Other languages

The phoneme ASR alignment model is _language-specific_, for tested languages these models are [automatically picked from torchaudio pipelines or huggingface](https://github.com/m-bain/whisperX/blob/f2da2f858e99e4211fe4f64b5f2938b007827e17/whisperx/alignment.py#L24-L58).
Just pass in the `--language` code, and use the whisper `--model large`.

Currently default models provided for `{en, fr, de, es, it}` via torchaudio pipelines and many other languages via Hugging Face. Please find the list of currently supported languages under `DEFAULT_ALIGN_MODELS_HF` on [alignment.py](https://github.com/m-bain/whisperX/blob/main/whisperx/alignment.py). If the detected language is not in this list, you need to find a phoneme-based ASR model from [huggingface model hub](https://huggingface.co/models) and test it on your data.

#### E.g. German

    whisperx --model large-v2 --language de path/to/audio.wav

https://user-images.githubusercontent.com/36994049/20
