# tw93/Waza

🥷 Engineering habits you already know, turned into skills AI assistants like Claude Code, Codex and Cursor can run.

## installation

**Claude Code, Codex, Cursor, and other agents**

```bash
npx skills add tw93/Waza -a claude-code codex cursor -g -y
```

One copy lands in `~/.agents/skills`, the shared skills directory. Claude Code is symlinked in; Codex, Cursor, Gemini CLI, Copilot, Amp, Kimi Code CLI, and every other agent that reads that directory picks the eight skills up as `/check`, `/think`, and so on. Agents with a private skills directory take their id after `-a` (for example `antigravity-cli` or `qwen-code`). Update with `npx skills update -g -y`. You can also tell your agent to install it:
> Install Waza for me by reading https://github.com/tw93/Waza/blob/main/llms.txt

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

You decide how skills chain together. Each skill stops at the requested outcome; an explicitly authorized workflow continues without asking you to approve every transition.

**Common workflows:**

- **Plan a feature**: `/think` to settle the plan, implement after approval, then `/check` before merging
- **Ship a fix**: `/hunt` to find the root cause, fix it, then `/check` to review the changes and, when needed, handle release, publish, push, and issue follow-through
- **Research and write**: `/read` to fetch sources, `/learn` to synthesize, `/write` to polish

The stages a task moves through, and the rules each one holds, are in the [AI coding rules](https://github.com/tw93/Waza/blob/main/docs/ai-coding-rules.md).

## Project Context

Waza ships only generic engineering habits. `/check` becomes project-aware at runtime by reading the target repository's public context (READMEs, package manifests, Makefiles, CI workflows) and your task constraints, never private paths, credentials, or tokens. See [`skills/check/references/project-context.md`](skills/check/references/project-context.md) for the review context template.

## Extras

Curl URLs use the latest GitHub release asset. Set `WAZA_REF=main` before the command if you want bleeding-edge scripts.

### Statusline

A minimal statusline for Claude Code: context window, 5-hour quota, and 7-day quota. Color-coded by usage, no progress bars, no noise.

<div align="center">
  <img src="https://raw.githubusercontent.com/tw93/Waza/main/assets/statusline.png" width="1000" />
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

Optional rules apply beyond skill invocations when installed into your agent's persistent instructions. Installing Waza skills alone does not enable them. Copy the ones you want (swap `claude-code` for `codex` or `antigravity-cli` on those agents):

```bash
(
  set -e
  WAZA_RULE_SCRIPT="$(mktemp -t waza-rule.XXXXXX)"
  trap 
