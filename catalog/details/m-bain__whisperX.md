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
