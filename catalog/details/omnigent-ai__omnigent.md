# omnigent-ai/omnigent

Omnigent is an open-source AI agent framework and meta-harness: orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies and sandboxing, and c

## features

Omnigent lets you:

- **📱 Work with agents from any device, including your phone.** Sessions
  follow you: start in your terminal, continue in the browser, pick it up on
  your phone. Messages, sub-agents, terminals, and files stay in sync.

- **🤖 Supervise multiple agents.** Mix Claude Code, Codex, Cursor, OpenCode,
  Hermes, Pi, and custom agents (defined in YAML) together in the same
  session. Ask one agent to review another's work, or split a task across
  agents that are each good at different things.

- **🔌 Use any model.** A first-party API key, a Claude/ChatGPT subscription,
  or any compatible gateway. All first-class.

- **🤝 Collaborate.** Share a session so teammates can chat with your agent
  and watch it work live, co-drive it on your machine, or fork the
  conversation to continue on their own.

- **☁️ Run agents in cloud sandboxes.** No laptop required: run sessions in
  disposable [Modal](https://modal.com), [Daytona](https://www.daytona.io),
  [Blaxel](https://blaxel.ai),
  [Islo](https://islo.dev), [E2B](https://e2b.dev),
  [CoreWeave](https://docs.coreweave.com/products/sandboxes),
  [Kubernetes](https://kubernetes.io), [OpenShell](https://github.com/NVIDIA/OpenShell),
  [Boxlite](https://github.com/boxlite-ai/boxlite), or
  [Databricks](https://www.databricks.com) sandboxes, launched from the
  CLI or provisioned by the server per session (*managed hosts*).

- **🛡️ Govern your agents.** Create
  [policies](#6-govern-your-agents-with-policies) to pause for your approval
  before risky actions, cap spend, or limit which tools an agent reaches.
  They apply to the whole server, one agent, or a single chat.

---

## installation

### 1. Install

One command installs Omnigent and everything it needs:

```bash
curl -fsSL https://raw.githubusercontent.com/omnigent-ai/omnigent/main/scripts/install_oss.sh | sh
```

<details>
<summary>Optional integrations and extras</summary>

Need an optional integration? Pass one or more extras to the installer:

```bash
curl -fsSL https://raw.githubusercontent.com/omnigent-ai/omnigent/main/scripts/install_oss.sh | sh -s -- --extra databricks
curl -fsSL https://raw.githubusercontent.com/omnigent-ai/omnigent/main/scripts/install_oss.sh | sh -s -- --extra modal,e2b
```

Available user-facing extras include:

- **Model providers:** `databricks`, `bedrock`, `vertex`
- **Sandbox providers:** `modal`, `daytona`, `blaxel`, `boxlite`, `cwsandbox`, `e2b`,
  `openshell`, `kubernetes`
- **SDK harnesses:** `antigravity`, `copilot`, `cursor`, `agents-sdk`
- **Storage and memory:** `s3`, `hindsight`

</details>

<details>
<summary>Prefer to install manually?</summary>

Omnigent needs **Python 3.12+**. Install the `omnigent` package:

```bash
uv tool install omnigent        # or: pip install "omnigent"
```

Manual installs use the same extras syntax, for example:

```bash
uv tool install "omnigent[databricks,modal]"
```

Or with [Homebrew](https://github.com/omnigent-ai/homebrew-tap):

```bash
brew install omnigent-ai/tap/omnigent
```

Or install straight from the repo:

```bash
uv tool install -q --python 3.12 git+https://github.com/omnigent-ai/omnigent.git
```

</details>

<details>
<summary>Toolchain and prerequisites (if the installer reports a missing tool)</summary>

- **`uv`** (required). https://docs.astral.sh/uv/getting-started/installation/
  The installer offers to set this up for you.
- **`git`** (required).
- **Node.js 22 LTS or newer** with **`npm`** (for the coding-harness CLIs
  installed by `omnigent run`) and **`pnpm`** (for the web UI). You can get
  both from a single Node install; pnpm is available via
  `corepack enable` or `npm install -g pnpm`.
- **Kiro CLI** (optional), for `omnigent kiro`: install with
  `curl -fsSL https://cli.kiro.dev/install | bash`, then sign in with Kiro.
  Kiro tool approvals stay answerable in the embedded Terminal; supported
  one-time approvals also appear as Chat cards. See
  `docs/kiro-native-elicitation.md`.
- **`tmux`**, required by the native `omnigent <harness>` terminal wrappers
  (`claude`, `codex`, `cursor`, `hermes`, `kiro`, `pi`)
  (`brew install tmux` / `apt install tmux`; the installer offers
  to install it for you).
- **`bubblewrap`** (`bwrap`), **Linux only**. The native `omnigent <harness>`
  terminal wrappers and the `pi` harness wrap each agent
  terminal in a `bwrap` OS-sandbox; on Linux that isolation is mandatory, so a
  missing `bwrap` binary makes those terminals fail to start
  (`apt install bubblewrap`; the installer offers to install it for you). macOS
  uses the built-in `seatbelt` sandbox and needs nothing extra.
- **Databricks** (optional). To use a Databricks workspace as your model
  provider, install Omnigent with the `databricks` extra:
  `uv tool install "omnigent[databricks]"` — or pass it to the bootstrap
  installer with `... | sh -s -- --extra databricks`. Signing in to the
  workspace also uses the [Databricks CLI](https://docs.databricks.com/aws/en/dev-tools/cli/install).

</details>

<details>
<summary>Windows (native)</summary>

Omnigent runs natively on Windows in a degraded mode. The `install_oss.sh`
bootstrap is POSIX-only, so install with `uv` directly:

```powershell
uv tool install --python 3.12 omnigent
# or from the repo:
uv tool install --python 3.12 git+https://github.com/omnigent-ai/omnigent.git
```

What works on Windows: `omnigent server`, the web UI, and the SDK-based
harnesses (`omnigent run <agent.yaml>` with the claude-sdk / cursor / codex
harnesses). Agents run under a Windows **Job Object** for process-tree
containment.

What is **not** available on Windows (use Linux/macOS, or WSL, for these):

- the native `omnigent claude
