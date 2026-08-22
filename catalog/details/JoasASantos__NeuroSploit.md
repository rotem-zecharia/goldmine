# JoasASantos/NeuroSploit

NeuroSploit is an advanced, AI-powered penetration testing framework designed to automate and augment various aspects of offensive security operations.

## installation

**Linux / macOS** (x64 & arm64):
```bash
curl -fsSL https://raw.githubusercontent.com/JoasASantos/NeuroSploit/main/setup.sh | bash
```

**Windows** (PowerShell, x64 & arm64):
```powershell
irm https://raw.githubusercontent.com/JoasASantos/NeuroSploit/main/install.ps1 | iex
```

### Supported platforms

| OS | x64 | arm64 |
|----|-----|-------|
| **Linux** (Kali recommended) | ✅ | ✅ |
| **macOS** | ✅ | ✅ (Apple Silicon) |
| **Windows** | ✅ | ✅ |

Pure Rust + stdlib, so it builds natively everywhere a stable Rust toolchain runs.
The installer auto-detects OS/arch and installs Rust if missing. On native Windows
use `install.ps1`; under WSL2 / Git Bash the `setup.sh` one-liner also works.

The installer auto-installs Rust if needed, clones the repo to `~/.neurosploit`,
builds the release binary, and links `neurosploit` into `~/.local/bin`. Re-run it
any time to update. Tweak with env vars: `NEUROSPLOIT_REF` (branch/tag),
`NEUROSPLOIT_DIR`, `PREFIX`.

Prefer to build by hand?

```bash
git clone https://github.com/JoasASantos/NeuroSploit && cd NeuroSploit/neurosploit-rs
cargo build --release      # → target/release/neurosploit
```

## ⚡ Quick start (60 seconds)

```bash
# easiest path — just run it; the interactive session asks everything:
neurosploit

## tools

neurosploit run http://testphp.vulnweb.com/ --subscription --model anthropic:claude-opus-4-8 -v

# white-box — review a source repository (SAST agents, file:line evidence):
git clone https://github.com/digininja/DVWA /tmp/DVWA
neurosploit whitebox /tmp/DVWA --subscription --model anthropic:claude-opus-4-8 -v

# grey-box — review the code AND exploit the running app together:
neurosploit greybox /tmp/DVWA --url http://localhost:8080/ --creds creds.yaml \
  --subscription --model anthropic:claude-opus-4-8 --mcp -v

# host / infra — Linux / Windows / Active Directory (SSH/Win creds in creds.yaml):
neurosploit host 10.0.0.10 --creds creds.yaml --subscription --model anthropic:claude-opus-4-8 -v

# 🛰  Mission Control TUI — live panels (header/feed/findings/targets) + a composer
#    you can type in WHILE the run streams (summary · pause · errors · notes):
neurosploit tui http://testphp.vulnweb.com/ --subscription --model anthropic:claude-opus-4-8 --mcp
```

> Full step-by-step for every mode (black/white/grey/host) is in **[TUTORIAL.md](TUTORIAL.md)**.

No login? Use an **API key** instead — see [Authentication](#authentication--run-via-api-key-or-subscription).

---

## 🔌 Integrations (GitHub · GitLab · Jira)

Wire NeuroSploit into your SDLC. Toggle from the REPL (`/integrations`) or the CLI
(`neurosploit integrations enable github|gitlab|jira`). **Tokens are never stored**
— only the *name* of the env var is saved; the value is read from your environment.

```bash
export GITHUB_TOKEN=ghp_...                 # PAT with `repo` scope (private repos)
neurosploit integrations enable github

# Review a Pull Request's code (clones the PR head, white-box) and comment back:
neurosploit pr digininja/DVWA 42 --subscription --model anthropic:claude-opus-4-8 --comment

# Same, but BLOCK the merge on a confirmed critical: fails the check, sets a
# `neurosploit/security` commit status, and posts a REQUEST_CHANGES review.
neurosploit pr digininja/DVWA 42 --model anthropic:claude-opus-4-8 --comment --fail-on critical

# Watch a branch and re-review on every new commit:
neurosploit watch myorg/private-app --branch main --subscription --model anthropic:claude-opus-4-8

# Private GitLab repo (token-injected clone) — works in whitebox/greybox:
export GITLAB_TOKEN=glpat-... ; neurosploit integrations enable gitlab
neurosploit whitebox https://gitlab.com/myorg/private-svc --subscription --model anthropic:claude-opus-4-8

# Open a Jira card per finding (any engagement):
export JIRA_EMAIL=you@org.com JIRA_API_TOKEN=...      # set base/project once: /integrations setup jira
neurosploit whitebox https://github.com/myorg/app --jira --subscription --model anthropic:claude-opus-4-8
```

| Integration | What you get | Env vars |
|-------------|--------------|----------|
| **GitHub** | private clone · `pr` review + comment · **PR gate** (`--fail-on`: fail check + commit status + REQUEST_CHANGES) · `watch` branch | `GITHUB_TOKEN` |
| **GitLab** | private clone for whitebox/greybox | `GITLAB_TOKEN` |
| **Jira** | one card per finding (`--jira`) | `JIRA_EMAIL`, `JIRA_API_TOKEN` |

### Automations (GitHub Actions)

Two ready-made workflows ship in [`examples/github-actions/`](examples/github-actions) — copy
them into your repo:

- **`neurosploit-pr-gate.yml`** — reviews every PR and blocks the merge on a
  confirmed critical. Make it enforcing: *Settings → Branches → require the
  `neurosploit-pr-gate` status check* (and/or require review to honor the
  REQUEST_CHANGES). Set `ANTHROPIC_API_KEY` (or swap the model) in Actions secrets;
  the built-in `GITHUB_TOKEN` covers statuses/reviews.
- **`neurosploit-mention.yml`** — comment **`@neurosploit`** on a PR or issue to
  trigger a scan (only repo writers can). Text after the mention is the
  instruction (any language): `@neurosploit focus SQLi and IDOR`, or
  `@neurosploit scan https://staging.app` for a black-box run.

📖 Step-by-step setup for each tool: **[TUTORIAL-INTEGRATION.md](TUTORIAL-INTEGRATION.md)**.

---



## configuration

| Flag | Meaning |
|------|---------|
| `--model provider:model` | Repeatable. First = primary; the rest fail over **and** form the voting jury. |
| `--subscription` | Use the local CLI login (Claude/Codex/Gemini/Grok) instead of an API key. |
| `--mcp` | Enable Playwright MCP (auto-provisioned via `npx`; backends without MCP use built-in tools). |
| `--vote-n N` | How many models must agree a finding is real (default 3 / 2 for whitebox). |
| `--max-agents N` | Cap agents run (`0` = all matching the recon). |
| `--offline` | Exercise the full pipeline without calling any model. |
| `-v, --verbose` | Log each agent as it launches, recon, and votes. |
