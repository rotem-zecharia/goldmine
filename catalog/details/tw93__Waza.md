# tw93/Waza

🥷 Engineering habits you already know, turned into skills Claude can run.

## installation

One command installs all eight skills, with no prompts and no errors. Copy and run:

```bash
npx skills add tw93/Waza -a claude-code codex cursor antigravity-cli -g -y
```

One canonical copy lands in the shared `~/.agents/skills` store (the agents.md standard directory) with Claude Code symlinked in, so Codex, Cursor, Kimi Code CLI, Amp, Cline, Antigravity CLI, and every other agent reading that directory picks Waza up automatically. Models routed through these harnesses (GLM or Kimi K2 behind Claude Code-compatible endpoints) need nothing extra; tools with a private skills directory append their agent id (e.g. `-a qwen-code iflow-cli antigravity-cli`). Update later with `npx skills update -g -y`.

**Native plugin** (for host-native update commands)

```bash
