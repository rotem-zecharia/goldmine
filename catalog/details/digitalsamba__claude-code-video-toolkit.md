# digitalsamba/claude-code-video-toolkit

AI-native video production toolkit for Claude Code

## installation

```bash
git clone https://github.com/digitalsamba/claude-code-video-toolkit.git
cd claude-code-video-toolkit
python3 -m pip install -r tools/requirements.txt   # Optional: AI voiceover, image gen, music, moviepy examples
claude                                              # Open Claude Code in the toolkit
```

Then in Claude Code:

```
/setup                    # Configure cloud GPU, storage, voice (~5 min, mostly free)
/video                    # Create your first video
```

**That's it.** `/setup` walks you through everything interactively — cloud GPU provider, file transfer, voice config. `/video` creates a project from a template and guides you through the whole workflow.

**What's free:** The toolkit leans heavily on open-source AI models — voiceovers (Qwen3-TTS), image generation (FLUX.2), music (ACE-Step), and more. You deploy them to your own cloud GPU account and run them at cost. Cloudflare R2 has a generous free tier (10GB, zero egress), and Modal gives $30/month free compute on the Starter plan — more than enough for a few 5-minute videos a month.

**Requirements:** [Node.js](https://nodejs.org/) 18+ and [Claude Code](https://docs.anthropic.com/en/docs/claude-code). Python 3.9+ recommended for AI tools. FFmpeg optional.

> **Want to skip setup and just render something?**
> ```bash
> cd examples/hello-world && npm install && npm run render
> ```
> No API keys needed — outputs an MP4 immediately.

---

## tools

| Command | Description |
|---------|-------------|
| `/setup` | First-time setup — cloud GPU, file transfer, voice, prerequisites |
| `/video` | Video projects — list, resume, or create new |
| `/scene-review` | Scene-by-scene review in Remotion Studio |
| `/design` | Focused design refinement session for a scene |
| `/brand` | Brand profiles — list, edit, or create new |
| `/template` | List available templates or create new ones |
| `/skills` | List installed skills or create new ones |
| `/contribute` | Share improvements — issues, PRs, examples |
| `/record-demo` | Record browser interactions with Playwright |
| `/generate-voiceover` | Generate AI voiceover from a script |
| `/redub` | Redub existing video with a different voice |
| `/voice-clone` | Record, test, and save a cloned voice to a brand |
| `/publish` | Publish a finished video to YouTube (metadata auto-filled from `project.json`) |
| `/versions` | Check dependency versions and toolkit updates |

> **Note:** After creating or modifying commands/skills, restart Claude Code to load changes.
