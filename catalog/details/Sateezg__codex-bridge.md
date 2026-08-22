# Sateezg/codex-bridge

Image generation (gpt-image-2) and GPT-5 subagents for Claude Code — through the Codex CLI login you already have. No OpenAI API key.

## installation

**Prerequisites**

| | |
| :-- | :-- |
| Codex CLI | `npm i -g @openai/codex` or `brew install codex` |
| Logged in | `codex login` → verify with `codex login status` (should say *Logged in using ChatGPT*) |
| ChatGPT plan | Plus, Pro, or Team |
| Claude Code | any current version |

**Then:**

```
/plugin marketplace add Sateezg/codex-bridge
/plugin install codex-bridge@codex-bridge
```

Run `/reload-plugins` if Claude Code asks you to.

<details>
<summary>Other install methods</summary>

Try it for one session, no install:

```bash
git clone https://github.com/Sateezg/codex-bridge.git
claude --plugin-dir ./codex-bridge
```

Auto-load from your skills directory:

```bash
git clone https://github.com/Sateezg/codex-bridge.git ~/.claude/skills/codex-bridge
chmod +x ~/.claude/skills/codex-bridge/bin/*
```

Loads as `codex-bridge@skills-dir` on your next session.

</details>

## features

```bash
codex-imagegen "flat vector rocket icon, #2563EB on white, 2px stroke, minimal" ./rocket.png
codex-imagegen "change the sky to sunset orange, keep everything else identical" ./out.png --ref ./hero.png
codex-imagegen "settings gear, same style as the reference" ./settings.png --ref ./home.png
```

| Option | |
| :-- | :-- |
| `--size WxH` | `1024x1024`, `1536x1024`, `1024x1536`, `2048x2048`, `3840x2160`, … — see note below |
| `--ref <file>` | source or style reference, repeatable up to 4 — turns the call into an edit |
| `--model <name>` | model override |
| `--timeout <sec>` | default 600 |

A custom size is only accepted if all of these hold: longest edge ≤ 3840px, both edges multiples of 16, long-to-short ratio ≤ 3:1, total pixels between 655,360 and 8,294,400. Square is fastest. For anything outside that — favicons, a 1200×630 OG card — generate a large master and resample locally.

The wrapper prints the path it actually wrote. Codex is instructed not to overwrite existing assets, so it occasionally saves `out-v2.png`; the wrapper detects that (and the `~/.codex/generated_images/<session>/` default location) and reports the real path.

What makes this better than pasting prompts into a chat window: the skills teach Claude to pull your **actual palette** out of `tailwind.config.*` or your design tokens, to reuse one style contract across a whole set so the assets match, to derive size variants with ImageMagick instead of regenerating, and to **open the PNG and check it** before telling you it's done.

## limitations

- **Quota, not free.** Image turns burn ChatGPT plan quota roughly 3–5× faster than text turns. Set `OPENAI_API_KEY` and Codex switches to API billing instead.
- **Transparency takes two steps.** The default path can't emit alpha, so the skills generate on a flat `#00FF00` key and strip it with the `remove_chroma_key.py` helper Codex already ships. True native transparency needs Codex's CLI fallback plus an `OPENAI_API_KEY`; the skills surface that as a choice rather than switching silently.
- **Slow.** 1–4 minutes per image; a repo-wide Codex task can take 10+ minutes. Skills set long Bash timeouts accordingly.
- **Codex is blind to your conversation.** Every brief has to stand alone. This is exactly why the subagents verify before reporting.
- **macOS and Linux.** Not tested on Windows.
