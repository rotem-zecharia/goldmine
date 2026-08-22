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

Latest release from pypi:
```bash
uv tool install --force mlx-audio --prerelease=allow
```

Latest code from github:
```bash
uv tool install --force git+https://github.com/Blaizzy/mlx-audio.git --prerelease=allow
```

## tools

```python
from mlx_audio.tts.utils import load_model

## requirements

- Python 3.10+
- Apple Silicon Mac (M1/M2/M3/M4)
- MLX framework
- **ffmpeg** (required for MP3/FLAC/OGG/Opus/Vorbis audio encoding)
