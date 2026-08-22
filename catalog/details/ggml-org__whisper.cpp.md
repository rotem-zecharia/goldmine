# ggml-org/whisper.cpp

Port of OpenAI's Whisper model in C/C++

## installation

First clone the repository:

```bash
git clone https://github.com/ggml-org/whisper.cpp.git
```

Navigate into the directory:

```
cd whisper.cpp
```

Then, download one of the Whisper [models](models/README.md) converted in [`ggml` format](#ggml-format). For example:

```bash
sh ./models/download-ggml-model.sh base.en
```

Now build the [whisper-cli](examples/cli) example and transcribe an audio file like this:

```bash

## tools

| Model  | Disk    | Mem     |
| ------ | ------- | ------- |
| tiny   | 75 MiB  | ~273 MB |
| base   | 142 MiB | ~388 MB |
| small  | 466 MiB | ~852 MB |
| medium | 1.5 GiB | ~2.1 GB |
| large  | 2.9 GiB | ~3.9 GB |

## requirements

- Docker must be installed and running on your system.
- Create a folder to store big models & intermediate files (ex. /whisper/models)

## limitations

- Inference only

## configuration

* --vad-threshold: Threshold probability for speech detection. A probability
for a speech segment/frame above this threshold will be considered as speech.

* --vad-min-speech-duration-ms: Minimum speech duration in milliseconds. Speech
segments shorter than this value will be discarded to filter out brief noise or
false positives.

* --vad-min-silence-duration-ms: Minimum silence duration in milliseconds. Silence
periods must be at least this long to end a speech segment. Shorter silence
periods will be ignored and included as part of the speech.

* --vad-max-speech-duration-s: Maximum speech duration in seconds. Speech segments
longer than this will be automatically split into multiple segments at silence
points exceeding 98ms to prevent excessively long segments.

* --vad-speech-pad-ms: Speech padding in milliseconds. Adds this amount of padding
before and after each detected speech segment to avoid cutting off speech edges.

* --vad-samples-overlap: Amount of audio to extend from each speech segment into
the next one, in seconds (e.g., 0.10 = 100ms overlap). This ensures speech isn't
cut off abruptly between segments when they're concatenated together.
