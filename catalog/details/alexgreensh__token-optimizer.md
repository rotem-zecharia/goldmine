# alexgreensh/token-optimizer

Find the ghost tokens. Fix them. Survive compaction. Avoid context quality decay.

## installation

**Claude Code (recommended):**

```
/plugin marketplace add alexgreensh/token-optimizer
/plugin install token-optimizer@alexgreensh-token-optimizer
```

Then in Claude Code: `/token-optimizer`

> **Enable auto-update after installing.** Claude Code ships third-party marketplaces with auto-update off by default. `/plugin` → **Marketplaces** tab → select `alexgreensh-token-optimizer` → **Enable auto-update**. One-time, 10 seconds.
>
> After install, run `/token-optimizer` once to set up hooks. From there, everything runs automatically: compression, checkpoints, quality scoring, dashboard updates. You don't need to run any command again unless you want an audit.

<details>
<summary><b>Other platforms and install methods</b></summary>

**Codex:**
```bash
codex plugin marketplace add alexgreensh/token-optimizer
```
Then in the Codex TUI: `/plugins` and install Token Optimizer. See [`docs/codex.md`](docs/codex.md).

**OpenCode:** add `token-optimizer-opencode` to the `plugin` array in your `opencode.json`:
```jsonc
{ "$schema": "https://opencode.ai/config.json", "plugin": ["token-optimizer-opencode"] }
```
See [`opencode/README.md`](opencode/README.md).

**OpenClaw:**
```bash
openclaw plugins install github:alexgreensh/token-optimizer
```
See [`openclaw/README.md`](openclaw/README.md).

**Hermes:**
```bash
git clone https://github.com/alexgreensh/token-optimizer.git
token-optimizer/install.sh --hermes
```
See [`hermes/README.md`](hermes/README.md).

**GitHub Copilot:**
```bash
git clone --depth 1 https://github.com/alexgreensh/token-optimizer.git
cd token-optimizer
bash install.sh --copilot
```
See [`docs/copilot.md`](docs/copilot.md).

**macOS/Linux script install (alternative to plugin):**
```bash
tmp="$(mktemp -d)"
release_json="$(curl -fsSL https://api.github.com/repos/alexgreensh/token-optimizer/releases/latest)"
tag="$(python3 -c 'import json,sys; print(json.load(sys.stdin)["tag_name"])' <<<"$release_json")"
git clone --branch "$tag" --depth 1 https://github.com/alexgreensh/token-optimizer.git ~/.claude/token-optimizer
bash ~/.claude/token-optimizer/install.sh
rm -rf "$tmp"
```

**Windows users:** Use the plugin install only. Do not run `install.sh` on Windows. If you hit `EBUSY` errors, close all Claude Code and Git Bash windows, kill lingering `git.exe` processes, delete `C:\Users\<you>\.claude\token-optimizer` and `C:\Users\<you>\.claude\plugins\marketplaces\alexgreensh-token-optimizer`, then retry.

**If `install.sh` fails with `$'\r': command not found`** (a clone made before LF line endings were enforced converted the script to CRLF), strip the carriage returns once and re-run — the repo now ships a `.gitattributes` that prevents this on fresh clones:
```bash
sed -i 's/\r$//' ~/.claude/token-optimizer/install.sh

## tools

<details>
<summary><b>Show all commands</b></summary>

| Command | What it does | Docs |
|---|---|---|
| `/token-optimizer` | Full audit with 6 parallel agents, guided fixes | [→](https://alexgreensh.github.io/token-optimizer/start/quickstart/) |
| `/token-coach` | 30-day trend analysis, prioritized fixes | [→](https://alexgreensh.github.io/token-optimizer/features/token-coach/) |
| `quick` | 10-second health check | [→](https://alexgreensh.github.io/token-optimizer/reference/cli/) |
| `doctor` | Installation check, score out of 10 | [→](https://alexgreensh.github.io/token-optimizer/reference/cli/) |
| `dashboard` | Open the HTML dashboard | [→](https://alexgreensh.github.io/token-optimizer/features/dashboard/) |
| `savings` | Dollar savings report | [→](https://alexgreensh.github.io/token-optimizer/reference/cli/) |
| `report` | Per-component token breakdown | [→](https://alexgreensh.github.io/token-optimizer/reference/cli/) |
| `quality` | Context-quality analysis of live session | [→](https://alexgreensh.github.io/token-optimizer/features/quality-signals/) |
| `trends` | Skill adoption, model mix, overhead over time | [→](https://alexgreensh.github.io/token-optimizer/reference/cli/) |
| `compression-stats` | Measured savings from active compression | [→](https://alexgreensh.github.io/token-optimizer/features/active-compression/) |
| `memory-review` | MEMORY.md structural audit | [→](https://alexgreensh.github.io/token-optimizer/features/memory-health/) |
| `git-context` | Suggest files for your current diff | [→](https://alexgreensh.github.io/token-optimizer/reference/cli/) |
| `drift` | Side-by-side comparison vs your last snapshot | [→](https://alexgreensh.github.io/token-optimizer/reference/cli/) |
| `conversation` | Per-message token and cost breakdown | [→](https://alexgreensh.github.io/token-optimizer/reference/cli/) |
| `pricing-tier` | View or switch pricing tiers | [→](https://alexgreensh.github.io/token-optimizer/reference/cli/) |
| `expand` | Retrieve an archived tool result (progressive disclosure) | [→](https://alexgreensh.github.io/token-optimizer/reference/cli/) |
| `resume-lean` | Reopen a cold session with token-free reconstruction | [→](https://alexgreensh.github.io/token-optimizer/reference/cli/) |

[Full CLI reference →](https://alexgreensh.github.io/token-optimizer/reference/cli/)

</details>
