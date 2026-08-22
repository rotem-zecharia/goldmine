# Blaizzy/mlx-audio

A text-to-speech (TTS), speech-to-text (STT) and speech-to-speech (STS) library built on Apple's MLX framework, providing efficient speech analysis on Apple Silicon.

## features

- Fast inference optimized for Apple Silicon (M series chips)
- Multiple model architectures for TTS, STT, STS, and music generation
- Multilingual support across models
- Voice customization and cloning capabilities
- Adjustable speech speed control
- Interactive web interface with 3D audio visualization
- OpenAI-compatible REST API
- Quantization support (3-bit, 4-bit, 6-bit, 8-bit, and more) for optimized performance
- Swift package for iOS/macOS integration

## installation

### Using pip
```bash
pip install mlx-audio
```

### Using uv to install only the command line tools
Latest release from pypi:
```bash
uv tool install --force mlx-audio --prerelease=allow
```

Latest code from github:
```bash
uv tool install --force git+https://github.com/Blaizzy/mlx-audio.git --prerelease=allow
```

### For development or web interface:

```bash
git clone https://github.com/Blaizzy/mlx-audio.git
cd mlx-audio
pip install -e ".[dev, server]"
```

## Quick Start

### Command Line

```bash
# Basic TTS generation
mlx_audio.tts.generate --model mlx-community/Qwen3-TTS-12Hz-0.6B-CustomVoice-8bit --text 'Hello, world!' --voice Vivian

# With a different voice and language hint
mlx_audio.tts.generate --model mlx-community/Qwen3-TTS-12Hz-0.6B-CustomVoice-8bit --text 'Welcome to MLX-Audio!' --voice Ryan --lang_code English

# Play audio immediately
mlx_audio.tts.generate --model mlx-community/Qwen3-TTS-12Hz-0.6B-CustomVoice-8bit --text 'Hello!' --voice Vivian --play

# Save to a specific directory
mlx_audio.tts.generate --model mlx-community/Qwen3-TTS-12Hz-0.6B-CustomVoice-8bit --text 'Hello!' --voice Vivian --output_path ./my_audio

# Stream audio during generation
mlx_audio.tts.generate --model mlx-community/Qwen3-TTS-12Hz-0.6B-CustomVoice-8bit --text 'Hello!' --voice Vivian --stream

# Stream audio during generation and save it to disk
mlx_audio.tts.generate --model mlx-community/Qwen3-TTS-12Hz-0.6B-CustomVoice-8bit --text 'Hello!' --voice Vivian --stream --save

# Join multiple generated segments into one file
mlx_audio.tts.generate --model mlx-community/Qwen3-TTS-12Hz-0.6B-CustomVoice-8bit --text $'Hello!\nHow are you?' --voice Vivian --join_audio
```


By default, when generation yields multiple segments, mlx-audio saves numbered files such as `audio_000.wav` and `audio_001.wav`. Use `--join_audio` to save one combined file instead. When using `--stream`, add `--save` to write the streamed audio to disk.

## tools

```python
from mlx_audio.tts.utils import load_model

# Load model
model = load_model("mlx-community/Qwen3-TTS-12Hz-0.6B-CustomVoice-8bit")

# Generate speech
for result in model.generate(
    "Hello from MLX-Audio!",
    voice="Vivian",
    lang_code="English",
):
    print(f"Generated {result.audio.shape[0]} samples")
    # result.audio contains the waveform as mx.array
```

## Supported Models

### Text-to-Speech (TTS)

| Model | Description | Languages | Repo |
|-------|-------------|-----------|------|
| **Kokoro** | Fast, high-quality multilingual TTS | EN, JA, ZH, FR, ES, IT, PT, HI | [bf16](https://huggingface.co/mlx-community/Kokoro-82M-bf16), [8bit](https://huggingface.co/mlx-community/Kokoro-82M-8bit), [6bit](https://huggingface.co/mlx-community/Kokoro-82M-6bit), [4bit](https://huggingface.co/mlx-community/Kokoro-82M-4bit) |
| **KittenTTS** | Compact KittenTTS 0.8 models for edge-friendly TTS | EN | [nano](https://huggingface.co/mlx-community/kitten-tts-nano-0.8), [micro](https://huggingface.co/mlx-community/kitten-tts-micro-0.8), [mini](https://huggingface.co/mlx-community/kitten-tts-mini-0.8), [collection](https://huggingface.co/collections/mlx-community/kittentts) |
| **Qwen3-TTS** | Alibaba's multilingual TTS with voice design | ZH, EN, JA, KO, + more | [mlx-community/Qwen3-TTS-12Hz-1.7B-VoiceDesign-bf16](https://huggingface.co/mlx-community/Qwen3-TTS-12Hz-1.7B-VoiceDesign-bf16) |
| **Higgs Audio v3** | 4B conversational TTS with voice cloning and inline control tokens | 100 languages | [bosonai/higgs-audio-v3-tts-4b](https://huggingface.co/bosonai/higgs-audio-v3-tts-4b) |
| **OmniVoice** | Zero-shot multilingual TTS with voice cloning, batch generation, and nonverbal tags | 646+ languages | [mlx-community/OmniVoice-bf16](https://huggingface.co/mlx-community/OmniVoice-bf16) |
| **CSM / MisoTTS** | Sesame-style conversational speech models with voice cloning | EN | [mlx-community/csm-1b](https://huggingface.co/mlx-community/csm-1b), [MisoTTS bf16](https://huggingface.co/mlx-community/MisoLabs-MisoTTS-bf16), [MisoTTS 8bit](https://huggingface.co/mlx-community/MisoLabs-MisoTTS-8bit) |
| **Dia** | Dialogue-focused TTS | EN | [mlx-community/Dia-1.6B-fp16](https://huggingface.co/mlx-community/Dia-1.6B-fp16) |
| **OuteTTS** | Efficient TTS model | EN | [mlx-community/OuteTTS-1.0-0.6B-fp16](https://huggingface.co/mlx-community/OuteTTS-1.0-0.6B-fp16) |
| **Spark** | SparkTTS model | EN, ZH | [mlx-community/Spark-TTS-0.5B-bf16](https://huggingface.co/mlx-community/Spark-TTS-0.5B-bf16) |
| **Chatterbox** | Expressive multilingual TTS (v2/v3) | 23 languages | [v3](https://huggingface.co/mlx-community/chatterbox-multilingual-v3), [v2](https://huggingface.co/mlx-community/chatterbox-fp16) |
| **Soprano** | High-quality TTS | EN | [mlx-community/Soprano-1.1-80M-bf16](https://huggingface.co/mlx-community/Soprano-1.1-80M-bf16) |
| **Ming Omni TTS (BailingMM)** | Multimodal generation with voice cloning, style control, and speech/music/event generation | EN, ZH | [mlx-community/Ming-omni-tts-16.8B-A3B-bf16](https://huggingface.co/mlx-community/Ming-omni-tts-16.8B-A3B-bf16) |
| **Ming Omni TTS (Dense)** | Lightweight dense Ming Omni variant for voice cloning and style control | EN, ZH | [mlx-community/Ming-omni-tts-0.5B-bf16](https://huggingface.co/mlx-community/Ming-omni-tts-0.5B-bf16) |
| **KugelAudio** | SOTA 7B AR+Diffusion TTS for European languages | EN, DE, FR, ES, IT, PT, NL, PL, RU, UK, + 14 more | [kugelaudio/kugelaudio-0-open](https://huggingface.co/kugelaudio/kugelaudio-0-open) |
| **Voxtral TTS** | Mistral's 4B multilingual TTS (20 voices, 9 languages) | EN, FR, ES, DE, IT, PT, NL, AR, HI | [mlx-community/Voxtral-4B-TTS-2603-mlx-bf16](https://huggingface.co/mlx-community/Voxtral-4B-TTS-2603-mlx-bf16) |
| **LongCat-AudioDiT** | SOTA diffusion TTS in waveform latent space with voice cloning | ZH, EN | [mlx-community/LongCat-AudioDiT-1B-bf16](https://huggingface.co/mlx-community/LongCat-AudioDiT-1B-bf16) |
| **MeloTTS** 

## requirements

- Python 3.10+
- Apple Silicon Mac (M1/M2/M3/M4)
- MLX framework
- **ffmpeg** (required for MP3/FLAC/OGG/Opus/Vorbis audio encoding)
