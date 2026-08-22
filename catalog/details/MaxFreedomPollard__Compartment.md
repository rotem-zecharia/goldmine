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

## configuration

Nothing here is required. Compartment installs configured, and this is the
whole surface if you want to change something.

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
