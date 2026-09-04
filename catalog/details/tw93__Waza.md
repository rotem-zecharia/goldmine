# tw93/Waza

🥷 Engineering habits you already know, turned into skills Claude can run.

## installation

**Claude Code, Codex, Cursor, and other agents**

```bash
npx skills add tw93/Waza -a claude-code codex cursor -g -y
```

One copy lands in `~/.agents/skills`, the shared skills directory. Claude Code is symlinked in; Codex, Cursor, Gemini CLI, Copilot, Amp, Kimi Code CLI, and every other agent that reads that directory picks the eight skills up as `/check`, `/think`, and so on. Agents with a private skills directory take their id after `-a` (for example `antigravity-cli` or `qwen-code`). Update with `npx skills update -g -y`.

**Host plugin**, if you prefer the host's own update command (skills are namespaced, `/waza:check`)

```bash
# Claude Code (update: claude plugin update waza)
/plugin marketplace add tw93/Waza
/plugin install waza@waza

# Codex (update: codex plugin marketplace upgrade waza, then codex plugin add waza@waza)
codex plugin marketplace add tw93/Waza
codex plugin add waza@waza
```

**Claude Desktop**: download [waza.zip](https://github.com/tw93/Waza/releases/latest/download/waza.zip), open Customize > Skills > "+" > Create skill, and upload the ZIP. To update, click "..." on the skill card, choose Replace, and upload the latest ZIP.

**Pi**: `pi install npm:@tw93/waza`, update with `pi update npm:@tw93/waza`.

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
  bash "$WAZA_RULE_SCRIPT" anti-patterns claude-code

  # Routing hint: tells non-Claude hosts to prefer Waza skills when a request matches their triggers
  ba
