# MaxFreedomPollard/Compartment

Encrypted, fully offline agentic memory. One click install, GUI w/ memory map, all OS and agents. Superior memory creation, storage and retrieval.

## installation

**One line install, works on all operating systems.**

```bash
pip install compartment && compartment init
```

Then connect it to the agent you use:

```bash
compartment integrate claude
```

`claude`, `hermes` and `openclaw` are the three auto-connect targets. Each one
also gets the **`/compartmentalize`** skill installed into its own skills
directory.

**`/compartmentalize` saves the conversation and relevant facts about it completely, 
when you have more important conversations that you feel deserve greater analysis and retention.** 
This is an additional option to, and not a replacement for, the constant background 
memory creation. 

**One click install (for people not good with command line).** Download
**Compartment.pkg** from the [latest release](https://github.com/MaxFreedomPollard/Compartment/releases/latest)
and open it. Python, the embedding model and every dependency are inside it.
macOS only.

After install, everything is managed from the minimal app: the **menu bar** on macOS,
the **notification area** on Windows, and a **window** from your applications
menu on Linux. We design to be one of the many hundreds of software applications
you have on your computer, we don't make the design mistake of assuming the user
cares about Compartment and is going to study how to use it. All functions are there
in simple button and selection format, and you dont need to fiddle with ratios or 
specifics, we have the best high level mathematical and logical functions by default. 

Compartment is an MCP server, so it works with all MCP capable agentic AI out
of the box. Every option is in [Configuration](#configuration).

#### What sets it apart

**Install it in one step**

- One command installs it, creates the vault, and wires your agent. No API
  key, no cloud account, no daemon.
- On the Mac, open one `.pkg` and you are done. Python, the embedding model
  and every dependency are inside it.
- An app runs the whole thing without a terminal on all three systems: vault
  state, unlock, lock, and the last five memories it saved. The macOS menu
  bar, the Windows notification area, a window on Linux.
- Every feature toggles in that panel instead of a config file:
  model-independent capture, starter facts in search, auto-lock.
- `/compartmentalize` is installed into every agent it connects, so one command
  banks a whole conversation before compaction throws it away.
- Your vault ships full. The 6,718 seeded facts are ordinary memories,
  editable and forgettable, and one switch keeps them out of search.
- Runs under what you already use: Hermes ("no setup needed"), Claude Code
  and Desktop over MCP, OpenClaw, every MCP client, plus a CLI for scripts
  and cron.

**Remembers the right things**

- "OK" is a decision, and Compartment files it as one, with the question it
  answered. That is the record you need later.
- Decisions beat preferences, preferences beat machine details, machine
  details beat chatter. A fixed ranking, not a model's mood.
- It forgets nothing. Small talk is kept and ranked last.
- It replaces your host's built-in memory instead of fighting it: imports
  what Claude Code already wrote, then supersedes it.
- It captures even when the model does not cooperate. A hook writes the fact
  whether or not the model calls the tool.
- A graph, not a pile. Explicit relations with validity windows answer who
  worked where, and when.

**Search that beats a network call**

- 0.68 ms vector search. About 12 ms for the full hybrid pipeline. A cloud memory
  spends longer than that saying hello.
- Exact below 20k records: recall = 1.0 by construction, not an
  approximation.
- Hybrid always: meaning and keywords, fused.
- One pinned embedding space, enforced every time the vault opens, so your
  comparisons stay valid forever.

**Encrypted, offline, and yours**

- Every byte at rest is AEAD-encrypted, embedding vectors included. Most
  tools leave vectors in the clear, and vectors invert back toward text.
- Only your passp

## features

Namespace, tag, date and starter-fact filters run *after* ranking, so a
candidate pool sized to the number of results requested can be emptied by them
while matching memories sit just past the cut. The pool starts at 200 per
channel and widens up to three times when filtering leaves too few.

### Measured

Against the previous scorer, end to end through `Vault.search`, on a real
6,705-memory vault with 44 queries in four families:

| | before | after |
|---|---|---|
| Recall@1 | 0.523 | **0.773** |
| Recall@5 | 0.705 | **0.977** |
| MRR@10 | 0.601 | **0.845** |
| nDCG@10 | 0.627 | **0.878** |
| exact identifiers found in top 5 | 4/10 | **10/10** |
| facts past the encoder window | 0/6 | **5/6** |
| paraphrases | 16/16 | 16/16 |
| median search latency | 4.4 ms | 11.6 ms |

Nothing regressed in any family. The weights were chosen from a sensitivity
sweep and are deliberately round: the result is flat around them, because a
ranker that only works at `w_lex = 0.37` is a ranker that does not work.

## Wiring each agent

One command per platform. Each installs the package, creates your
encrypted vault, and wires the agent.

Every one of these is also a button in the app. Click the Compartment icon
in your menu bar or notification area, and under **CONNECT AN AGENT** press
Claude, Hermes or OpenClaw. The button runs the same `compartment integrate`
command for you, so nobody has to open a terminal a second time.

**Claude (Code + Desktop)** - macOS / Linux:
```bash
pip install compartment && compartment init && compartment integrate claude
```
Windows (PowerShell):
```powershell
py -m pip install compartment; compartment init; compartment integrate claude
```
Registers the MCP server with the Claude Code CLI (user scope, all
projects), **imports any memories Claude Code already wrote to its own
file-based memory** (copy-only - the Markdown files are never modified;
`--no-import` opts out, `compartment import-claude` does it later), and prints
the Claude Desktop config block. The server describes
itself over the MCP handshake - it tells the model to recall before answering
and to store durable facts, credentials, names, and decisions - so Claude
treats Compartment as its memory with no hand-written instruction; `integrate
claude` also writes a managed, idempotent block into your CLAUDE.md as backup.

**Hermes** - macOS / Linux:
```bash
pip install compartment && compartment init && compartment integrate hermes
```
Windows (PowerShell):
```powershell
py -m pip install compartment; compartment init; compartment integrate hermes
```
Installs the provider plugin, wires the Hermes venv, and runs
`hermes memory setup compartment`. Compartment then appears in the
`hermes memory setup` picker beside hindsight and mem0, the only entry
marked **"no setup needed"**: no API key, no cloud account, no daemon.
Verify with `hermes memory status`. See everything Hermes remembers at
any time with **`compartment dash`** - one command, and the vault opens in
your browser (memories by kind, growth, the relation graph, live
search); Ctrl-C closes it.

Hermes also reads the portable [Agent Plugins](https://agent-plugins.org)
format, and this repository is one. That route installs the MCP server and
the `/compartmentalize` skill straight from GitHub, and wants Hermes 0.20.0
or newer, which is where the portable plugin loader arrived:
```bash
pip install compartment && compartment init
hermes plugins install MaxFreedomPollard/Compartment
hermes plugins enable compartment
```
The provider above remains the fuller integration, because recall and
persistence run automatically on every turn where the portable package is
tool-invoked. On macOS and Windows the two resolve to the same plugin
directory name, so install one or the other.

**OpenClaw** - macOS / Linux:
```bash
pip install compartment && compartment init && compartment integrate openclaw
```
Windows (PowerShell):
```powershell
py -m pip install compartment; compartment init; compartment integrate openc

## configuration

Nothing here is required. Compartment installs configured, and this is the
whole surface if you want to change something.

### In the app

The panel behind the icon: **Unlock** and **Lock**, **Change password**,
**Create memories automatically** (the capture hook), **Search starter
facts**, **Auto-lock** (15, 30, 60 minutes or never), the **CONNECT AN
AGENT** buttons for Claude, Hermes and OpenClaw, **Refresh** and **Quit**.

`compartment panel --login on | off | status` controls starting at login,
which on Linux is the applications menu entry.

## tools

| Command | What it does |
|---|---|
| `init` | create the vault. `--passphrase`, `--creator`, `--keychain`, `--no-session`, `--no-app` |
| `unlock` / `lock` | open or close it. `--passphrase-stdin`, `--keyfile`, `--keychain`, `--once`; `lock --sign --identity` |
| `status` / `verify` / `selftest` | what is in it, is it intact, does it work |
| `store` / `get` / `forget` | one memory. `--namespace`, `--tag`, `--importance`, `--quarantined`, `forget --shred` |
| `search` / `recent` | find things. `--namespace`, `--tag`, `--top-k`, `--limit`, `--all`, `--json` |
| `link` / `relations` / `unlink` | the relation graph, with validity windows (`--from`, `--to`, `--as-of`) |
| `panel` (`menubar`, `tray`) | the app. `--show`, `--self-check`, `--render`, `--login` |
| `integrate <agent>` | wire claude, hermes or openclaw, and install `/compartmentalize` for it. `--no-import`, `--no-hooks` |
| `hook` | capture hook: `install --pin-vault`, `uninstall`, `status`, `capture` |
| `serve` | the MCP server, over stdio |
| `dash` | read the vault in a browser: 127.0.0.1, one-time token, GET only |
| `export` / `import` | `export --plaintext` writes it unencrypted; `import` reads it back |
| `import-claude` | pull in what Claude Code already wrote. `--dir`, `--namespace`, `--dry-run` |
| `rekey` | change the passphrase. `--new-passphrase-stdin` |
| `2fa` | `enable`, `disable`, `status` - a keyfile as a second factor |
| `audit` | `verify`, `repair` the hash-chained history |
| `pack` | `build`, `install`, `remove`, `list`, `export` signed memory packs (`--trusted-key`) |
| `reindex` | rebuild the index, and give long records the embedding windows they are missing. `--int8`, `--f32`, `--re-embed`, `--model` |
| `bench` | `--records`, `--longmemeval`, `--variant`, `--limit` |
| `setup` | `download-model`, `download-longmemeval`, `airgap-bundle` |
| `update` | upgrade in place. `--source` takes GitHub main, `--no-app` skips the restart |
| `uninstall` | remove it. The vault is kept unless you pass `--purge` |

Global flags, before the command: `--vault PATH`, `--caller NAME`,
`--keyfile PATH`, `--assert-offline`, `--version`.

### The /compartmentalize skill

`compartment integrate <agent>` writes one file into that agent's own skills
directory, and `compartment uninstall` takes it back:

| Agent | Path |
|---|---|
| Claude Code | `~/.claude/skills/compartmentalize/SKILL.md` |
| Hermes | `$HERMES_HOME` or `~/.hermes/skills/compartmentalize/SKILL.md` |
| OpenClaw | `$OPENCLAW_HOME` or `~/.openclaw/skills/compartmentalize/SKILL.md` |

All three read the same Agent Skills layout, so it is one packaged file. It is
user-invoked only: no agent runs it on its own guess. Edit your copy freely -
a later install backs up anything that differs rather than overwriting it, and
leaves the backup behind when the skill is removed. Invoking it makes the agent
sweep the conversation and write to the vault, so expect a burst of
`memory_store` calls; that is the point of it.

### Settings file

`<vault>.config.json`, beside the vault, holding grants per caller and:

| Setting | Default | Meaning |
|---|---|---|
| `auto_lock_minutes` | `30` | idle time before it locks. `0` never locks |
| `search_starter_facts` | `true` | whether the seeded facts join search results |
| `include_packs_in_search` | `true` | the same, for installed packs |
| `duplicate_threshold` | `0.97` | cosine similarity at which a store is a duplicate |
| `index_precision` | `"f32"` | `"int8"` uses a quarter of the RAM |
| `retag_interval_hours` | `6` | how often the background pass re-derives tags. `0` turns it off |
| `retag_prune` | `false` | whether that pass may also REMOVE tags the vault no longer supports |
| `unlock_tool_enabled` | `false` | lets an agent unlock the vault. Off because the passphrase would cross the model's context |
