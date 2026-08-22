# getagentseal/codeburn

Free, local tool to track AI coding token usage and cost across 37 tools and agents (Claude Code, Cursor, Codex, Gemini and more), by model, project, and task. npx codeburn

## installation

**Run it instantly**, no install needed:

```bash
npx codeburn
```

That opens the interactive dashboard (last 7 days by default). Arrow keys switch periods, `q` quits. That is the 30-second version. You now know where your AI budget goes.

**Install it** for a permanent `codeburn` command:

```bash
npm install -g codeburn
```

Also runs via `bunx codeburn` or `pnpm dlx codeburn`, or `brew install codeburn` on macOS.

**Menu bar app** for macOS, with your spend always in the menu bar:

```bash
codeburn menubar
```

The same command installs the tray app on Windows; see [Windows](#windows). On Linux, a GNOME Shell extension gives it in the top panel; see [Linux (GNOME)](#linux-gnome).

Requires **Node.js 22.13+** and at least one supported tool with session data on disk. For Cursor and OpenCode, `better-sqlite3` installs automatically.

## Your month at a glance

```bash
codeburn overview                                    # this month, clean tables
codeburn overview --no-color                         # plain text, ready to paste
codeburn overview --from 2026-06-01 --to 2026-06-15  # any date range
codeburn overview -p all                             # last 6 months
codeburn overview -p lifetime                        # full history (uncapped)
codeburn overview --provider claude                  # one tool only
```

`codeburn overview` prints a copy-pasteable summary of where your AI spend went: totals (cost, tokens, cache hit), a breakdown by tool and by top model, your highest-value days, top projects, a per-day table, and activity and tool usage. Pipe it anywhere (into `pbcopy`, a PR, Slack, or a tweet); color drops automatically when the output is not a terminal, or pass `--no-color`.

```text
CodeBurn  June 2026

Totals
  Cost       $2,795.10
  Tokens     3.49B   in 23.9M / out 20.2M / cache-w 72.5M / cache-r 3.38B
  Calls      14,755   sessions 753
  Cache hit  99.3%

By tool
┌──────────┬───────────┬────────┬───────┐
│ Tool     │      Cost │ Tokens │ Share │
├──────────┼───────────┼────────┼───────┤
│ claude   │ $2,662.37 │  3.34B │   95% │
│ codex    │   $119.12 │ 128.1M │    4% │
└──────────┴───────────┴────────┴───────┘

(plus Top models, Highest-value days, Top projects, a per-day table, By activity, and Tools)
```

## Find and fix waste

```bash
codeburn optimize                       # scan the last 30 days
codeburn optimize -p today              # today only
codeburn optimize -p week               # last 7 days
codeburn optimize --provider claude     # restrict to one provider
codeburn optimize --format json         # setup health + findings as JSON
```

`codeburn optimize` scans your sessions and your `~/.claude/` setup for waste patterns:

For Claude Code, the optimize session count, the per-session findings, coaching,
and model-default recommendations use user-started (main) sessions. Subagent
sidechain transcripts are excluded from that population because their delegated
context and delivery behavior are structurally different, and so is the re-read
finding, since a subagent starts on a fresh context. Findings about how Claude
uses tools (junk reads, read:edit ratio) and every spend, MCP, and
configuration-overhead finding keep counting them.

- Files Claude re-reads across sessions (same content, same context, over and over)
- Low Read:Edit ratio (editing without reading leads to retries and wasted tokens)
- Wasted bash output (uncapped `BASH_MAX_OUTPUT_LENGTH`, trailing noise)
- Unused MCP servers still paying their tool-schema overhead every session
- Ghost agents, skills, and slash commands defined in `~/.claude/` but never invoked
- Bloated `CLAUDE.md` files (with `@-import` expansion counted)
- Cache creation overhead and junk directory reads
- Context-heavy sessions where effective input/cache tokens swamp output
- Possibly low-worth expensive sessions with no edit turns or repeated retries
  when no `git`/`gh` delivery command is observed

Findings are grouped into three classes: **Fix now** (CodeBurn c

## tools

See one total across your laptop, desktop, and work machine on the same network. On each other device, share its usage:

```bash
codeburn share --pair           # opens a pairing window and prints a PIN
```

Then add it once from your main device (the PIN authorizes the pairing):

```bash
codeburn devices add            # find nearby devices and pair, or: add <host> --pin <pin>
codeburn devices                # combined totals by machine
codeburn devices rm <name>      # forget a device
```

Pairing is PIN-authorized and stays on your local network. You can also discover and pair devices straight from the browser dashboard.

## Menu bar

### macOS

```bash
codeburn menubar
```

One command: downloads the latest `.app`, installs into `~/Applications`, and launches it. Re-run with `--force` to reinstall. The native Swift and SwiftUI app lives in `mac/` (see `mac/README.md` for build details).

The menubar icon shows the spend period selected in Settings (Today by default; Week, Month, and 6 Months are also available). Non-today periods add a short suffix such as `$42 / mo` so the menu bar value stays clear. Click to open a popover with agent tabs, period switcher (Today, 7 Days, 30 Days, Month, All), Trend, Forecast, Pulse, Stats, and Plan insights, activity and model breakdowns, optimize findings, and CSV/JSON export. Refreshes every 30 seconds.

You can also set the menubar status period from Terminal:

```bash
defaults write org.agentseal.codeburn-menubar CodeBurnMenubarPeriod -string month
```

Allowed values are `today`, `week`, `month`, and `sixMonths`. Relaunch the app to apply external defaults changes.

**Compact mode** shrinks the menubar item to fit the text, dropping decimals (e.g. `$110` instead of `$110.20`):

```bash
defaults write org.agentseal.codeburn-menubar CodeBurnMenubarCompact -bool true
```

Relaunch the app to apply. To revert: `defaults delete org.agentseal.codeburn-menubar CodeBurnMenubarCompact`.

**Refresh cadence** is set in Settings under Usage Refresh. Auto (the default) refreshes every 30 seconds on AC power and backs off on battery, in Low Power Mode, and while the display sleeps; fixed 1, 5, or 15 minute cadences and a Manual mode (refresh only when you open the popover or click Refresh Now) are also available. From Terminal:

```bash
defaults write org.agentseal.codeburn-menubar CodeBurnMenubarRefreshSeconds -int 300
```

Seconds between refreshes: `60`, `300`, or `900`; `0` is Manual and `-1` is Auto. Takes effect on the next refresh tick, no relaunch needed.

**Preferred terminal** decides where Full Report and Optimize open. Set it in Settings → General → Terminal, or from Terminal:

```bash
defaults write org.agentseal.codeburn-menubar CodeBurnPreferredTerminal -string iterm2
```

Allowed values are `terminal` (macOS Terminal.app, the default) and `iterm2`. Anything else falls back to `terminal`. Only terminals that can script a command into a live window are offered; if the chosen app is missing or fails to accept the command, CodeBurn tries Terminal.app and then runs the command in the background, logging each step to Console.app. Takes effect on the next launch of a command, no relaunch needed.

### Windows

Windows gets the same ambient view from the system tray, from the same one command:

```powershell
codeburn menubar
```

It downloads the `.msi` for your CLI version, verifies its sha256, runs it through `msiexec /passive`, and launches the tray app. Re-run with `--force` to reinstall; an already-installed matching version is just launched. You can also download the `.msi` yourself from the [latest Windows Menubar release](https://github.com/getagentseal/codeburn/releases/tag/windows-v0.9.20).

Today's spend sits in the tray as a number beside the flame icon (turn it off in Settings, and the tooltip always carries it). Click for the same popover the macOS app shows: agent tabs, period switcher, Trend, Forecast, Pulse, Stats and Plan insights, activity and model breakdowns, optimize 

## features

<details>
<summary><strong>Pricing, task categories, plans, currency, filtering, and more</strong></summary>

### Pricing

Prices every API call using input, output, cache read, cache write, and web search token counts, with a fast mode multiplier for Claude. Prices are fetched from [LiteLLM](https://github.com/BerriAI/litellm) and cached locally for 24 hours at `~/.cache/codeburn/`. Hardcoded fallbacks for all Claude and GPT-5 models prevent fuzzy-matching mispricing.

### Task Categories

13 categories classified from tool usage patterns and user message keywords. No LLM calls, fully deterministic.

| Category | What triggers it |
|---|---|
| Coding | Edit, Write tools |
| Debugging | Error/fix keywords + tool usage |
| Feature Dev | "add", "create", "implement" keywords |
| Refactoring | "refactor", "rename", "simplify" |
| Testing | pytest, vitest, jest in Bash |
| Exploration | Read, Grep, WebSearch without edits |
| Planning | EnterPlanMode, TaskCreate tools |
| Delegation | Agent tool spawns |
| Git Ops | git push/commit/merge in Bash |
| Build/Deploy | npm build, docker, pm2 |
| Brainstorming | "brainstorm", "what if", "design" |
| Conversation | No tools, pure text exchange |
| General | Skill tool, uncategorized |

### Breakdowns

Daily cost chart, per-project, per-model (Opus, Sonnet, Haiku, GPT-5, GPT-4o, Gemini, Kiro, and more), per-activity with one-shot rate, core tools, shell commands, and MCP servers.

### One-Shot Rate

For categories that involve code edits, CodeBurn tracks file-aware retry cycles. A retry is when the same file is re-edited after a shell command in between (Edit foo.ts, Bash, Edit foo.ts). Editing different files across shell steps is not a retry. The one-shot column shows the percentage of edit turns that succeeded without retries. Coding at 90% means the AI got it right first try 9 out of 10 times. File-level tracking is available for Claude, Codex, and Goose; other providers fall back to tool-name-based detection.

### Plans

```bash
codeburn plan set claude-max                                  # $200/month
codeburn plan set claude-pro                                  # $20/month
codeburn plan set cursor-pro                                  # $20/month
codeburn plan set custom --monthly-usd 200 --provider codex   # ChatGPT Pro-style custom plan
codeburn plan reset --provider codex                          # remove one provider plan
codeburn plan set none                                        # disable plan view
codeburn plan                                                 # show configured plans
codeburn plan reset                                           # remove plan config
```

Subscription tracking for Claude Pro, Claude Max, Cursor Pro, and custom provider plans. Plans are stored per provider, so you can track Claude and Codex/Cursor subscriptions at the same time; the dashboard shows one overage line per active provider plan. A legacy/custom `all` plan remains a single aggregate plan and is replaced when you add a provider-specific plan, avoiding double-counted overage rows. Existing single-plan config is still read as a fallback. Presets use publicly stated plan prices (as of April 2026); they do not model exact token allowances, because vendors do not publish precise consumer-plan limits.

### Currency

```bash
codeburn currency GBP          # set to British Pounds
codeburn currency AUD          # set to Australian Dollars
codeburn currency JPY          # set to Japanese Yen
codeburn currency CNY          # set to Chinese Yuan
codeburn currency RON          # set to Romanian Leu
codeburn currency              # show current setting
codeburn currency --reset      # back to USD
```

Any [ISO 4217 currency code](https://en.wikipedia.org/wiki/ISO_4217#List_of_ISO_4217_currency_codes) is supported (162 currencies). Exchange rates fetched from [Frankfurter](https://www.frankfurter.app/) (European Central Bank data, free, no API key) and cached for 24 hours. Config stored at `~/.config

## configuration

<details>
<summary><strong>Override data directories and paths</strong></summary>

| Variable | Description |
|----------|-------------|
| `CLAUDE_CONFIG_DIR` | Override Claude Code data directory (default: `~/.claude`) |
| `CLAUDE_CONFIG_DIRS` | OS-delimited list of Claude data directories to scan together (e.g. `~/.claude-work:~/.claude-personal`). Sessions merge into one row per project. Overrides `CLAUDE_CONFIG_DIR` when set. |
| `CODEX_HOME` | Override Codex data directory (default: `~/.codex`) |
| `CODEBUFF_DATA_DIR` | Override Codebuff data directory (default: `~/.config/manicode`) |
| `CODEWHALE_HOME` | Override the exact CodeWhale home directory; sessions are read from `<CODEWHALE_HOME>/sessions` |
| `FACTORY_DIR` | Override Droid data directory (default: `~/.factory`) |
| `KIMI_SHARE_DIR` | Override Kimi Code CLI share directory (default: `~/.kimi`) |
| `KIMI_MODEL_NAME` | Override Kimi model name when Kimi sessions do not record the model |
| `LINGTAI_HOME` | Override LingTai data directory (default: `~/.lingtai`) |
| `LINGTAI_TUI_HOME` | Alternate override for LingTai data directory; `LINGTAI_HOME` takes precedence |
| `LINGTAI_TUI_GLOBAL_DIR` | Override LingTai TUI global directory used for project registry discovery (default: `~/.lingtai-tui`) |
| `OPENCODE_DATA_DIR` | Override the OpenCode-compatible data directory (default: `$XDG_DATA_HOME/opencode` or `~/.local/share/opencode`). Point at a renamed/forked build, e.g. `~/.local/share/mimicode`. Exact directory; no `opencode` suffix is appended. |
| `OPENCODE_DB_PREFIX` | Override the SQLite DB filename prefix for OpenCode discovery (default: `opencode`, matching `opencode*.db`); e.g. `mimicode` discovers `mimicode*.db`. SQLite storage only. |
| `QWEN_DATA_DIR` | Override Qwen data directory (default: `~/.qwen/projects`) |
| `VIBE_HOME` | Override Mistral Vibe home directory (default: `~/.vibe`) |
| `WARP_DB_PATH` | Override Warp database path (default: Warp Stable, then Warp Preview) |

</details>

## Sponsoring CodeBurn

CodeBurn is free, runs entirely on your machine, and exists to cut your AI bill. If it has already saved you more than a sponsorship costs, consider sending a little of that back.

Keeping 41 integrations accurate is constant work. The tools underneath change every week: Cursor reshapes its database, Claude moves a config path, new models ship at new prices. Sponsorship keeps CodeBurn current with all of it, so the numbers you see are always the real ones.

Where your sponsorship goes:

- **Honest numbers.** New models and price changes are mapped quickly, so your cost is the real cost, not a guess.
- **More tools.** Every one of the 41 providers started as a single file. Sponsorship funds the next one.
- **Fast fixes.** When a vendor breaks something, paid time is what gets it patched now instead of someday.

Sponsoring as a team or company? Your logo lands right here, in front of every developer who opens the repo. The first sponsor gets it to themselves until the next one shows up.

<p align="center">
  <a href="https://github.com/sponsors/iamtoruk"><img src="https://img.shields.io/badge/Sponsor_CodeBurn-♥-F97316?style=for-the-badge&logo=github&labelColor=1a1a1a" alt="Sponsor CodeBurn" /></a>
</p>

## Star History

<p align="center">
<!-- star-history:start -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/star-history/star-history-dark.svg">
  <img alt="Star history" src="assets/star-history/star-history-light.svg">
</picture>
<!-- star-history:end -->
</p>

## License

MIT.

CodeBurn is an AgentSeal open-source project and is not affiliated with CodeBurn Bt. or codeburn.hu.

## Credits

Pricing data from [LiteLLM](https://github.com/BerriAI/litellm). Exchange rates from [Frankfurter](https://www.frankfurter.app/).

Built by [AgentSeal](https://agentseal.org).
