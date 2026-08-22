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
# Claude Code: install, then `claude plugin update waza`
/plugin marketplace add tw93/Waza
/plugin install waza@waza

# Codex: install, then `codex plugin marketplace upgrade waza`
codex plugin marketplace add tw93/Waza
codex plugin add waza@waza
```

**Claude Desktop**: download [waza.zip](https://github.com/tw93/Waza/releases/latest/download/waza.zip), then Customize > Skills > "+" > Create skill, and upload the ZIP. Re-upload the latest ZIP to update.

**Pi**: `pi install npm:@tw93/waza` (update with `pi update npm:@tw93/waza`). `/health` audits Pi settings alongside Claude Code and Codex.

## Chaining Skills

Skills chain together, but every transition is a manual step you trigger. Each skill finishes its task and stops, waiting for you to decide what comes next.

**Common workflows:**

- **Plan a feature**: `/think` → approve → say "implement X" → `/check` → merge
- **Ship a fix**: `/hunt` → fix → `/check` → release/publish/push/issue follow-through
- **Research and write**: `/read` (fetch sources) → `/learn` (synthesize) → `/write` (polish)
- **Debug and verify**: `/hunt` (find root cause) → fix → `/check` (review changes)

## Project Context

Waza ships only generic engineering habits. `/check` becomes project-aware at runtime by reading the target repository's public context (READMEs, package manifests, Makefiles, CI workflows) and your task constraints, never private paths, credentials, or tokens. See [`skills/check/references/project-context.md`](skills/check/references/project-context.md) for the review context template.

## Extras

### Statusline

A minimal statusline for Claude Code: context window, 5-hour quota, and 7-day quota. Color-coded by usage, no progress bars, no noise.

<div align="center">
  <img src="https://gw.alipayobjects.com/zos/k/y9/RUgevg.png" width="1000" />
</div>

```bash
(
  set -e
  WAZA_STATUSLINE_SCRIPT="$(mktemp -t waza-statusline.XXXXXX)"
  trap 'rm -f "$WAZA_STATUSLINE_SCRIPT"' EXIT
  curl -fL https://github.com/tw93/Waza/releases/latest/download/setup-statusline.sh -o "$WAZA_STATUSLINE_SCRIPT"
  # review it first: less "$WAZA_STATUSLINE_SCRIPT"
  bash "$WAZA_STATUSLINE_SCRIPT"
)
```

**Codex** has native statusline items. Add to `~/.codex/config.toml`:

```toml
[tui]
status_line = ["model-with-reasoning", "current-dir", "context-used", "five-hour-limit", "weekly-limit"]
status_line_use_colors = true
```

Codex shows remaining quota; the Claude Code statusline above shows used percentage (upstream does not yet expose `five-hour-used` / `weekly-used`).

### Optional Rules

Three independent toggles. Copy the ones you want (swap `claude-code` for `codex` or `antigravity-cli` on those agents):

```bash
(
  set -e
  WAZA_RULE_SCRIPT="$(mktemp -t waza-rule.XXXXXX)"
  trap 'rm -f "$WAZA_RULE_SCRIPT"' EXIT
  curl -fL https://github.com/tw93/Waza/releases/latest/download/setup-rule.sh -o "$WAZA_RULE_SCRIPT"
  # review it first: less "$WAZA_RULE_SCRIPT"

  # English coaching: appends a short 😇 correction when your prompt has an English mistake
  bash "$WAZA_RULE_SCRIPT" english claude-code

  # Anti-patterns: always-on cross-skill guardrails (read before acting, no scope creep, no unsolicited summaries)
  bash "$WAZA_RULE_SCRIPT" anti-patte
