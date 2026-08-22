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

## A Note from the Author *(not AI-generated)*

> I've spent months painstakingly putting this toolkit together and plan to keep iterating on it. AI makes things easier, but hard work still has huge value. Every video I create is a chance for improvement — every skill, template, tool, and workflow here has been refined through that cycle. It would be wonderful if others wanted to get involved with that: use it, refine it, and feed back into the repo via an issue or PR what you learn.
>
> My own use case is fairly specific: creating sprint review videos for the AI mobile development arm of [Digital Samba](https://www.digitalsamba.com/). But the idea behind this project is a reusable toolkit for using Claude Code to autonomously generate any kind of "explainer" style video — product demos, walkthroughs, presentations, whatever you need. Autonomous video creation is a lofty ideal for such a subjective field, but we can try :)
>
> What makes this work is that Claude Code is fantastically resourceful and flexible — give it the framing and tooling that this toolkit provides and it will adapt it to create templates and videos based on your prompting. The skills, templates, and tools here are building blocks. Claude Code is the builder. You are the director, editor, and designer.
>
> **If you're getting started**, run `/setup` then `/video` and let Claude Code guide you. Or start with `/template` to create a template for your own use case.
>
> **Cloud GPU** — I recommend [Modal](https://modal.com/) for running the toolkit's AI tools. The Starter plan gives you $30/month free compute, which is more than enough. [RunPod](https://runpod.io/) is also supported as an alternative. Run `/setup` to deploy the tools you need.
>
> My motto: **Be brave. Experiment.** And please share any videos you create or ideas you have back with the project — it helps me keep improving this toolkit for everyone.

## features

### Skills

Claude Code has deep knowledge in:

| Skill | Description |
|-------|-------------|
| **remotion** | React-based video framework — compositions, animations, rendering |
| **elevenlabs** | AI audio — text-to-speech, voice cloning, music, sound effects |
| **ffmpeg** | Media processing — format conversion, compression, resizing |
| **playwright-recording** | Browser automation — record demos as video |
| **frontend-design** | Visual design refinement for distinctive, production-grade aesthetics |
| **qwen-edit** | AI image editing — prompting patterns and best practices |
| **ideogram4** | AI image generation with best-in-class in-image text — title cards, thumbnails, exact brand colors |
| **acestep** | AI music generation — prompts, lyrics, scene presets, video integration |
| **ltx2** | AI video generation — text-to-video, image-to-video clips, prompting guide |
| **moviepy** | Python video composition — overlay text on LTX-2/SadTalker output, build.py-style projects |
| **runpod** | Cloud GPU — setup, Docker images, endpoint management, costs |

> The always-current catalog of skills, commands, tools, and templates lives in [`_internal/toolkit-registry.json`](_internal/toolkit-registry.json).

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

### Templates

Pre-built video structures in `templates/`:

- **sprint-review** — Sprint review videos with demos, stats, and voiceover
- **sprint-review-v2** — Composable scene-based sprint review with modular architecture
- **product-demo** — Marketing videos with dark tech aesthetic, stats, CTA
- **concept-explainer-short** — 9:16 vertical TikTok/Reels/Shorts explainers (Python/moviepy, no Remotion)

See `examples/` for finished projects you can learn from (newest first — scroll down to watch the toolkit evolve in reverse):

| Date | Demo | Description |
|------|------|-------------|
| 2026-06-09 | [hallucinations-short](https://demos.digitalsamba.com/video/hallucinations_short.mp4) | 3:41 vertical explainer on AI hallucinations — Ideogram 4 cards, LTX-2 b-roll, burned karaoke captions, Qwen3-TTS voice *clone* (reference sample from [Pixabay](https://pixabay.com/sound-effects/search/voice%20overs/)) |
| 2026-06-09 | [sky-blue-short](https://demos.digitalsamba.com/video/short-blue-sky.mp4) | 52s "Why is the sky blue?" — concept-explainer-short template showcase (`examples/sky-blue-short`), stock Qwen3-TTS voice |
| 2026-04-08 | [q2-townhall-stars](https://demos.digitalsamba.com/video/q2-townhall-stars.mp4) | GitHub star history time-lapse with animated chart and deadpan-to-excited commentary |
| 2026-04-08 | [q2-townhall-longarm-ad](https://demos.digitalsamba.com/video/q2-townhall-longarm-ad.mp4) | Super Bowl-style launch ad with dramatic Qwen3-TTS announcer and LTX-2 animated Lugh cameo |
| 2026-03-15 | [the-space-between](https://demos.digitalsamba.com/video/the-space-between.mp4) | AI-generated video essay — flux2 avatar, Qwen3-TTS voice, SadTalker animation |
| 2026-02-23 | [cortina](https://demos.digitalsamba.com/video/sprint-review.mp4) | Mobile platforms sprint review |
| 2026-01-25 | [schlumbergera](https://demos.digitalsamba.com/video/schlumbergera.mp4) | Android sprint review video |
| 2026-01-22 | [ds-remote-mcp](https://demos.digitalsamba.com/video/ds-remote-mcp.mp4) | Remote MCP server demo *(the jazz background music is a joke)* |
| 2025-12-10 | [digital-samba-skill-demo](https://demos.digitalsamba.com/video/digital-samba-skill-demo.mp4) | Product demo showcasing Claude Code skill |
| 2025-12-05 | [sprint-review-cho-oyu](https://demos.digitalsamba.com/sprint-review-cho-oyu.mp4) | iOS sprint review with demos |

### Scene Transitions

The toolkit includes a transitions library for scene-to-scene effects:

| Transition | Description |
|------------|-------------|
| `glitch()` | Digital distortion with RGB shift |
| `rgbSplit()` | Chromatic aberration effect |
| `zoomBlur()` | Radial motion blur |
| `lightLeak()` | Cinematic lens flare |
| `clockWipe()` | Radial sweep reveal |
| `pixelate()` | Digital mosaic dissolution |
| `checkerboard()` | Grid-based reveal (9 patterns) |

Plus official Remotion transitions: `slide()`, `fade()`, `wipe()`, `flip()`

Preview all
