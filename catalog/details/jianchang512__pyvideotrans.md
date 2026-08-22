# jianchang512/pyvideotrans

Translate the video from one language to another and embed dubbing & subtitles.

## features

> [Technical Architecture and Principles](docs/architecture.md)

- **Fully Automatic Video Translation**: One-click workflow: Speech Recognition (ASR) → Subtitle Translation → Speech Synthesis (TTS) → Video Synthesis.
- **Audio Transcription / Subtitle Generation**: Batch convert audio/video to SRT subtitles, supporting **Speaker Diarization** to distinguish between different roles.
- **️Multi-Role AI Dubbing**: Assign different AI dubbing voices to different speakers.
- **Voice Cloning**: Integrates models like **F5-TTS, CosyVoice, GPT-SoVITS** for zero-shot voice cloning.
- **Powerful Model Support**:
  - **ASR**: Faster-Whisper (Local), OpenAI Whisper, Alibaba Qwen, ByteDance Volcano, Azure, Google, etc.
  - **LLM Translation**: DeepSeek, ChatGPT, Claude, Gemini, MiniMax, Ollama (Local), Alibaba Bailian, etc.
  - **TTS**: Edge-TTS (Free), OpenAI, Azure, Minimaxi, ChatTTS, ChatterBox, etc.
- **️Interactive Editing**: Supports pausing and manual proofreading at each stage (recognition, translation, dubbing) to ensure accuracy.
- **️Utility Toolkit**: Includes auxiliary tools such as vocal separation, video/subtitle merging, audio-video alignment, and transcript matching.
- **Command Line Interface (CLI)**: Supports headless operation, convenient for server deployment or batch processing.
- **Web Interface (WebUI)**: Browser-based interface for remote access or internal network deployment.


---

## installation

We provide a pre-packaged `.exe` version for Windows 10/11 users, requiring no Python environment configuration.

1. **Download**: [Click to download the latest pre-packaged version](https://github.com/jianchang512/pyvideotrans/releases)
2. **Unzip**: Extract the compressed file to a path without Chinese characters or spaces (e.g., `D:\pyVideoTrans`).
3. **Run**: Double-click `sp.exe` inside the folder to launch.

> **Note**:
> * Do not run directly from within the compressed archive.
> * To use GPU acceleration, ensure **CUDA 12.8** and **cuDNN 9.11** are installed.

---

## requirements

* **Python**: Recommended version 3.10
* **FFmpeg**: Must be installed and configured in the environment variables.
  * **macOS**: 
  ```
    brew install libsndfile  git  python@3.10
	
	brew uninstall --ignore-dependencies ffmpeg
	
	brew tap homebrew-ffmpeg/ffmpeg
	
	brew install homebrew-ffmpeg/ffmpeg/ffmpeg
  ```
  * **Linux (Ubuntu/Debian)**: `sudo apt-get install ffmpeg libsndfile1-dev`
  * **Windows**: [Download FFmpeg](https://ffmpeg.org/download.html) and configure Path, or place `ffmpeg.exe` and `ffprobe.exe` directly in the project directory.

## configuration

docker run -d -p 7860:7860 \
  -v ./data/output:/app/output \
  -v ./data/config:/app/videotrans \
  --name pyvideotrans pyvideotrans-webui
```

> [WebUI documentation](docs/webui.md)
