# agiwhitelist/auteur

The Claude Code skill that directs a website like a film. Commit-sheet, generated assets, build, and an executable anti-slop linter that gates every ship.

## installation

auteur is an [Agent Skill](https://code.claude.com/docs/en/skills): a `SKILL.md`
plus reference recipes and a few runnable scripts. ~1MB, no dependencies, no
API keys, no build step.

**Any agent — one command.** Detects what you have installed and writes to each
agent's skills folder:

```bash
npx skills add agiwhitelist/auteur
```

<sub>Claude Code · Codex · Cursor · OpenCode · Gemini CLI · Windsurf · Cline ·
Goose · Copilot · Hermes · Kiro · Roo · OpenHands — [75+ agents](https://www.skills.sh/),
project-level or `-g` for global.</sub>

**Claude Code, as a plugin** — installs and updates in place:

```
/plugin marketplace add agiwhitelist/auteur
/plugin install auteur@auteur
```

**OpenClaw:**

```bash
openclaw skills install git:agiwhitelist/auteur --global
```

**Anything else that reads a `SKILL.md`** — clone it into the agent's skills
directory:

```bash
git clone --depth 1 https://github.com/agiwhitelist/auteur ~/.claude/skills/auteur
```

Then just ask:

```
"build me a cinematic landing with auteur"
```

Claude runs the pipeline — commit-sheet → assets → build → gate — and hands you
the site.

## requirements

- **Claude Code** (the skill runs inside it).
- **Node 18+** for `slopscan` (zero dependencies).
- **Playwright** for `motionqa` / `shoot` / `refscout` / `moodboard`
  (`npx playwright install chromium`).
- Optional, for asset generation: whichever local media CLIs you have
  (Codex, Gemini/`agy`, Blender). The skill routes to what's present and
  degrades gracefully to hand-authored assets when they aren't.
