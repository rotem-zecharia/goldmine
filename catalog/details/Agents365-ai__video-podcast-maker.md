# Agents365-ai/video-podcast-maker

Topic → 4K narrated video for coding agents. v4.0: all TTS via the ttsCN engine component (11 platforms incl. MiniMax voice clone, native word-level subtitle sync), manifest-based Asset Engine, Remoti

## features

- **Topic → 4K video** - research, narration script, TTS audio, Remotion composition, 4K render + BGM in one pipeline
- **11 TTS backends** - Edge (free), Azure, CosyVoice, Doubao, Tencent, Baidu, MiniMax, Xunfei, ElevenLabs, OpenAI, Google — all synthesized by the required [ttscn](https://github.com/Agents365-ai/ttsCN) component skill
- **Asset engine** - per-video manifest with license provenance; producers are user files, assetseeker stock, imagencn AI stills, videogencn AI B-roll, and Hyperframes overlays — paid generation always asks first
- **4K output + Remotion-native subtitles** - 3840×2160; SRT rendered in React at 4K (legacy FFmpeg burn-in available)
- **Design learning** - extract style profiles from reference videos/images; auto-applied when topics match
- **Vertical shorts** - 9:16 highlight clips generated from long-form sections
- **Multi-platform & multi-language** - Bilibili / YouTube / Xiaohongshu / Douyin / WeChat Channels × zh-CN / en-US, with per-platform publish info
- **Pronunciation control** - global + per-project phoneme dictionaries for Chinese polyphones

## installation

**1. Install** — via the [365-skills marketplace](https://github.com/Agents365-ai/365-skills) (recommended) or by cloning this repo.

**2. Set up** — Python 3.8+, Node.js 18+, FFmpeg, and a Remotion project:

```bash
brew install ffmpeg node python3          # macOS (Ubuntu: sudo apt install ffmpeg nodejs python3)
pip install -r skills/video-podcast-maker/requirements.txt
npx create-video@latest my-video-project   # or reuse an existing Remotion project
cd my-video-project && npm i
```

**3. Configure** — set `TTS_BACKEND` plus its API keys (see [TTS Backends](#tts-backends) and [Environment Variables](#environment-variables)).

**4. Tell your agent:**

> "Create a video podcast about [your topic]"

The agent runs the whole workflow (research → script → TTS → Remotion composition → Studio review → 4K render + BGM). Preview and iterate in Remotion Studio (`npx remotion studio src/remotion/index.ts`); the agent waits for your explicit "render 4K" confirmation before the final render.

## requirements

| Software | Version | Purpose |
| ---------- | --------- | --------- |
| **macOS / Linux** | - | Tested on macOS, Linux compatible |
| **Python** | 3.8+ | TTS script, automation |
| **Node.js** | 18+ | Remotion video rendering |
| **FFmpeg** | 4.0+ | Audio/video processing |

> **Marketplace install (recommended):** users typically install this skill via the [365-skills marketplace](https://github.com/Agents365-ai/365-skills) rather than cloning. SKILL.md, scripts, and templates then live under the agent's `${SKILL_DIR}`; paths in this README are written from the repo-root perspective for contributors.

## configuration

Add to `~/.zshrc` or `~/.bashrc`:

```bash
export TTS_BACKEND="edge"                  # azure / cosyvoice / doubao / tencent / baidu / minimax / xunfei / elevenlabs / openai / google
export TTS_VOICE="zh-CN-XiaoxiaoNeural"    # optional; unset = platform default
export TTS_RATE="+5%"                      # optional; also settable in user_prefs.json (global.tts.rate)
export TTS_STYLE="gentle"                  # optional; azure only
export AZURE_SPEECH_KEY="..."              # keys for the active platform only (see table above)
export GEMINI_API_KEY="..."                # optional: AI thumbnails
export DASHSCOPE_API_KEY="..."             # optional: AI thumbnails (also the cosyvoice TTS key)
```

Then reload: `source ~/.zshrc`
