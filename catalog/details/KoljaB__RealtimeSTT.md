# KoljaB/RealtimeSTT

A robust, efficient, low-latency speech-to-text library with advanced voice activity detection, wake word activation and instant transcription.

## features

RealtimeSTT includes native support for `kroko_onnx`, the local streaming ASR
engine from the Kroko/Banafo team.

This integration has been on my wishlist for a long time. Kroko is a strong fit
for RealtimeSTT's goals: fast, accurate local speech recognition.

Start with the public Community models for local testing, or see Kroko/Banafo's
commercial model options if you need production licensing and higher-end models.

```bash
pip install "RealtimeSTT[kroko-builder,silero-onnx-cpu]"
stt-install-kroko --build
```

The `silero-onnx-cpu` extra gives `AudioToTextRecorder` a local VAD backend for
recorder-based smoke tests and live microphone use.

See the [Kroko-ONNX engine guide](docs/engines/kroko-onnx.md),
[Kroko ASR docs](https://docs.kroko.ai/on-premise/), and
[kroko-onnx on GitHub](https://github.com/kroko-ai/kroko-onnx).

## installation

Use Python 3.11 or newer for the current pinned dependency set.

```bash
pip install "RealtimeSTT[faster-whisper]"
```

On Linux, install PortAudio headers before installing the package:

```bash
sudo apt-get update
sudo apt-get install python3-dev portaudio19-dev
```

On macOS:

```bash
brew install portaudio
```

For CUDA, platform notes, and optional engine stacks, see
[docs/installation.md](docs/installation.md).

## configuration

Every `AudioToTextRecorder` constructor parameter is documented in
[docs/configuration.md](docs/configuration.md), including model/engine
selection, realtime transcription, VAD timing, wake words, callbacks, external
audio, logging, and executor injection.
