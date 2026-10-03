# DietrichGebert/ponytail

Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

## installation

The most effort ponytail will ever ask of you:

The Claude Code and Codex plugins (and the Cursor hooks) run two tiny Node.js lifecycle hooks, so `node` needs to be on your PATH (note for Nix/nvm users: it must be on the non-interactive shell's PATH). If it isn't, the skills still work, but every hook call shows a harmless `node: command not found` error; installing Node (or putting it on that PATH) makes it go away.

### Claude Code

```
/plugin marketplace add DietrichGebert/ponytail
```
```
/plugin install ponytail@ponytail
```
(You have to send two separate prompts for the install to work) 

Same steps in the Claude Code Desktop app's Code tab: type the two `/plugin` commands above into the prompt box, or click the **+** button next to it, choose **Plugins** → **Add plugin** to browse your configured marketplaces, and manage marketplaces from **Customize** in the sidebar.

### Codex

```bash
codex plugin marketplace add DietrichGebert/ponytail
codex plugin add ponytail@ponytail
```

Run `codex` and open `/hooks`, review and trust its two lifecycle hooks, and start a new thread.

This same install also covers the Codex desktop app: restart the app after installing and it picks up the plugin.

### GitHub Copilot CLI

```bash
copilot plugin marketplace add DietrichGebert/ponytail
copilot plugin install ponytail@ponytail
```

In an interactive Copilot CLI session, use the slash equivalents:

```
/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail
```

Copilot CLI namespaces plugin commands by plugin name. For example:

```text
/ponytail:ponytail ultra
/ponytail:ponytail-review
```

### Pi agent harness

```
pi install git:github.com/DietrichGebert/ponytail
```

### OpenCode

Add to `opencode.json`:

```json
{ "plugins": ["@dietrichgebert/ponytail"] }
```

Run from a checkout instead (the plugin reuses `hooks/` and `skills/`):

```json
{ "plugins": ["./.opencode/plugins"] }
```

Injects the ruleset every turn at the active level; adds the `/ponytail` commands (see [Commands](#commands)). OpenCode also auto-loads this repo's `AGENTS.md`, so the rules hold even without the plugin. The plugin adds the `lite/full/ultra/off` levels.

OpenCode 2 only. The `./` path resolves against your project's `opencode.json`; to share one checkout across projects, point it at the absolute path of the checkout's `.opencode/plugins` directory. A `plugins` entry must name a **directory**, not a file: OpenCode 2 rejects a path to `ponytail.mjs` with `configured plugin path must be a directory`. Opening this repo in OpenCode 2 needs no entry at all: it loads `.opencode/plugins/index.js` on its own.

OpenCode 1 uses the older `plugin` key: `{ "plugin": ["@dietrichgebert/ponytail"] }`, or from a checkout the file path: `{ "plugin": ["./.opencode/plugins/ponytail.mjs"] }`.

### Gemini CLI

```bash
gemini extensions install https://github.com/DietrichGebert/ponytail
```

Loads the ruleset as always-on context every session and registers the `/ponytail` commands; the `skills/` ship too, activated when a task needs them.
The Gemini adapter intentionally does not ship a root `hooks/hooks.json`: Gemini auto-loads that path, while Ponytail's lifecycle hooks use Claude/Codex event names.

### Qoder

Qoder auto-loads `AGENTS.md` from the repo root as always-on context, so running ponytail from a checkout works with zero setup. For per-project rules, copy [`.qoder/rules/ponytail.md`](.qoder/rules/ponytail.md) into your project's `.qoder/rules/`. The six ponytail skills (`/ponytail`, `/ponytail-review`, `/ponytail-audit`, `/ponytail-debt`, `/ponytail-gain`, `/ponytail-help`) are available via Qoder's Skill system; the plugin manifest at [`.qoder-plugin/plugin.json`](.qoder-plugin/plugin.json) points at the `skills/` directory.

For full plugin-tier support (automatic mode activation + ruleset injection on every prompt), add the hooks from [`hooks/qoder-hooks.json`](hooks/qoder-hooks.json) to your `.qoder/settings.json`. Replace `PONYT

## tools

| Command | What it does |
|---------|--------------|
| `/ponytail [lite \| full \| ultra \| off]` | Set the intensity, or turn it off. No argument switches ponytail on at the default level if it is off, and otherwise reports the current level. |
| `/ponytail-review` | Review the current diff for over-engineering, hands back a delete-list. |
| `/ponytail-audit` | Audit the whole repo for over-engineering, not just the diff. |
| `/ponytail-debt` | Harvest the `ponytail:` shortcuts you've deferred into a ledger, so "later" doesn't become "never". |
| `/ponytail-gain` | Show the measured impact scoreboard (less code, less cost, more speed) from the benchmark. |
| `/ponytail-help` | Quick reference for the commands above. |

Commands need a skill-capable host (Claude Code, Codex, Devin CLI, OpenCode, Gemini, pi, Swival, Hermes Agent, Qoder, Grok Build). In Codex CLI and the IDE extension they're skills; invoke with `$ponytail-review`. Cursor with the [hooks](#cursor) gets `/ponytail` level switching only, typed as a plain message. The instruction-only adapters (Cursor's rule file, Windsurf, Cline, Copilot, Kiro, Antigravity) load the always-on ruleset without the commands.

## Development

When changing the compact rule text, keep the agent copies aligned:

```bash
node scripts/check-rule-copies.js
npm test
```

The OpenClaw skill package (`.openclaw/skills/`) is generated from `skills/`; rerun `node scripts/build-openclaw-skills.js` after changing a skill, the test suite fails if it is stale. To publish the skills to ClawHub, run `clawhub login` once, then `node scripts/publish-openclaw-skills.js` (it publishes all six at the `package.json` version; pass `--dry-run` to preview).

The correctness benchmark spawns Python for email and CSV checks; `python3` is tried before `python`. CSV checks need `pandas` installed locally.

## FAQ

**Can I use it with [caveman](https://github.com/JuliusBrussee/caveman)?**
Yes, and you should. Caveman shrinks what the agent says; ponytail shrinks what it builds. Different halves, no overlap: caveman leaves code byte-for-byte exact, ponytail stays out of the prose. Terse talk about minimal code.

**Does it need a config file?**
No. An optional `~/.config/ponytail/config.json` or `PONYTAIL_DEFAULT_MODE` env var can set the default level, but nothing is required.

**What if I really need the 120-line cache class?**
You don't. Insist anyway and he'll build it. Slowly. Correctly. While looking at you.

**Does it scale?**
The code you never wrote scales infinitely. Zero bugs, zero CVEs, 100% uptime since forever.

**Why "ponytail"?**
You know exactly why.

## Sponsors

<p align="center">
  <a href="https://greenpt.com/">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="assets/logo-greenpt-dark.svg">
      <img src="assets/logo-greenpt.svg" width="260" alt="GreenPT">
    </picture>
  </a>
</p>

## License

[MIT](LICENSE). The shortest license that works.

## Star History

<a href="https://www.star-history.com/dietrichgebert/ponytail#history">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=DietrichGebert/ponytail&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=DietrichGebert/ponytail&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=DietrichGebert/ponytail&type=Date" />
 </picture>
</a>
