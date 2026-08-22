# XiaomiMiMo/MiMo-Code

MiMo Code: Where Models and Agents Co-Evolve

## installation

```bash
# One-line install (macOS / Linux)
curl -fsSL https://mimo.xiaomi.com/install | bash

# One-line install (Windows PowerShell)
powershell -ep Bypass -c "irm https://mimo.xiaomi.com/install.ps1 | iex"

# Or install via npm (all platforms)
npm install -g @mimo-ai/cli

# Run
mimo
```

The first launch guides you through configuration automatically. Supported options:
- **Xiaomi MiMo Platform** — OAuth login
- **Codex (ChatGPT Pro/Plus)** — OpenAI OAuth login
- **Import from Claude Code** — migrate existing authentication in one step
- **Provider list** — connect catalog providers by API key, or OAuth where supported (e.g. xAI/Grok)
- **Custom Provider** — add any OpenAI-compatible API in the TUI

<details>
<summary><strong>WSL: clipboard issues</strong></summary>

If you encounter garbled text when copying on WSL, install `xsel`:
```bash
sudo apt install xsel
```
</details>

<details>
<summary><strong>macOS: rendering issues in the default terminal</strong></summary>

MiMoCode does not support the built-in macOS Terminal (Terminal.app). If the interface is misaligned, flickers, or has other rendering issues, use [iTerm2](https://iterm2.com/) or the VS Code integrated terminal instead:

```bash
brew install --cask iterm2
```
</details>

<details>
<summary><strong>TUI lag and visual animation issues</strong></summary>

If the TUI lags when run directly over SSH, render it locally and run only the MiMoCode server on the remote host. Start the server from the remote project directory:

```bash
# Remote host
mimo serve --port 4096

# Local host: create the SSH port forward
ssh -N -L 4096:127.0.0.1:4096 user@remote-host

# Local host: connect from another terminal
mimo attach http://127.0.0.1:4096
```

If decorative animation is causing the lag, run `/vivid`, or configure **Vivid visuals** in the `ctrl+p` command palette, to switch between Vivid and Minimal visuals as needed.

</details>

<details>
<summary><strong>Windows: garbled CJK (Chinese/Japanese/Korean) output in the shell</strong></summary>

On Windows with a non-UTF-8 system locale (e.g. zh-CN, whose active code page is 936/GBK),
command output containing CJK characters may appear garbled (mojibake). MiMoCode forces
UTF-8 output for spawned PowerShell/cmd subprocesses. If you still encounter garbled output
in cases this does not yet cover, enable Windows' system-wide UTF-8 support:

**Settings → Time & language → Language & region → Administrative language settings →
Change system locale → check "Beta: Use Unicode UTF-8 for worldwide language support" →
reboot.**

This switches the active code page (ACP) to UTF-8 (65001) for all programs, so subprocesses
no longer inherit the legacy code page. Note it is a system-wide Beta toggle and may cause
some older non-Unicode programs to display incorrectly, so treat it as a workaround.
</details>

---

## MiMo Ecosystem

Beyond MiMoCode, Xiaomi MiMo models also work in other agents and coding tools like Cursor, Cline, and Zed.

**[awesome-mimo-agent](https://github.com/XiaomiMiMo/awesome-mimo-agent)** collects setup guides for using MiMo in those tools — worth a look if you want to try MiMo elsewhere. Contributions welcome: open a PR to add your own setup.

---

## features

### Multiple Agents

| Agent | Description |
|--------|------|
| **build** | Default. Full tool permissions for development |
| **plan** | Read-only analysis mode for code exploration and solution design |
| **compose** | Orchestration mode for specs-driven development and skill-driven workflows |

Press `Tab` to switch between primary agents. Subagents are created by the system as needed. After the first message the mode locks: Build and Plan can still switch between each other, but Compose is isolated once entered — keeping the skill/tool set fixed from session start significantly improves tool-call reliability.

For frontier models (Fable/Sol-class), the recommended way to run compose-style work is the **build** agent with the `/compose-next` skill — see [Compose Mode](#compose-mode).

### Persistent Memory

Cross-session memory powered by SQLite FTS5 full-text search:

- **Project memory** (`MEMORY.md`) — persistent project knowledge, rules, and architecture decisions
- **Session checkpoint** (`checkpoint.md`) — structured state snapshots maintained automatically by the checkpoint-writer subagent
- **Scratch notes** (`notes.md`) — temporary note area for agents
- **Task progress** (`tasks/<id>/progress.md`) — per-task logs

Memory is injected automatically when a session resumes, so the agent does not need to relearn project context.

### Intelligent Context Management

- **Automatic checkpoints** — decides when to save session state based on the model context window
- **Context reconstruction** — when context approaches the limit, rebuilds it from the latest checkpoint, project memory, task progress, and retained recent messages so the agent can continue the current task
- **Budgeted injection** — uses a token budget to control how much checkpoint, memory, and notes content enters context, with importance ranking
- **Adjustable compaction point** — `/context-limit` (or `compaction.max_context`) makes a model compact earlier than its own window, per model

<details>
<summary><strong>Compacting earlier than the model window (<code>/context-limit</code>)</strong></summary>

Compaction normally fires just below the model's context window. Run `/context-limit` to
pick a smaller working budget for the current model — `200K` / `300K` / `500K` / `1M` or a
custom value — stored per model as `compaction.max_context`:

```jsonc
{
  "compaction": {
    "max_context": {
      "openai/gpt-5.6": "272K", // token count, "300K", "1M", or "50%" of the window
      "anthropic/*": "300K" // wildcards allowed, longest pattern wins
    }
  }
}
```

The value is always clamped to what the provider actually accepts, so it can only lower the
compaction point, never raise it. `0` restores the model's own window.

Why you might want it:

- **Cost tiers.** OpenAI prices GPT-5.6 prompts above 272K input at 2x input and 1.5x output
  for the whole request.
- **The advertised window is not always what you get.** The same model can have a different
  usable window depending on how you reach it — a ChatGPT/Codex subscription, a direct API
  key, or a reseller such as OpenRouter — so a catalog figure of 1M does not mean your route
  serves 1M.
- **Quality and latency.** Very long contexts are slower and, past a point, not better.

`mimo models <provider>` prints, per model, the window MiMoCode resolved and the token count
where it will compact. The prompt footer uses that same number as its denominator
(`33.0K/260K↓ (13%)` — the `↓` means a budget is in force), and `/status` breaks it down.

</details>

### Task Tracking

A tree-shaped task system (`T1`, `T1.1`, `T1.2`, …) that integrates automatically with the checkpoint system, so task progress is preserved when sessions resume.

### Subagent System

The primary agent can create subagents on demand. Subagents share the current session context and can work in parallel, with lifecycle tracking, cancellation, and background execution.

### Goal / Stop Condition

The `/goal` command sets a stopping conditio

## configuration

# Remote host
apt install -y pulseaudio pulseaudio-utils sox
export PULSE_SERVER=tcp:127.0.0.1:4713
# Verify: pactl info
```
</details>

<details>
<summary><strong>Non-MiMo voice providers (OpenRouter, internal API, etc.)</strong></summary>

Voice input can route through other OpenAI-compatible providers via the `voice` config field. The ASR model (`mimo-v2.5-asr`) is only available on MiMo's platform; voice control mode (`mimo-v2.5`) is available on OpenRouter and compatible relay platforms.

**OpenRouter (voice control only):**

Use `/connect` to sign in to OpenRouter, then add to your config:
```jsonc
{
  "voice": {
    "control_model": "openrouter/xiaomi/mimo-v2.5"
  }
}
```

**Internal / self-hosted relay (both ASR and voice control):**
```jsonc
{
  "provider": {
    "internal": {
      "options": {
        "baseURL": "https://your-api-gateway.example.com/v1",
        "apiKey": "sk-..."
      },
      "models": {
        "xiaomi/mimo-v2.5-asr": { "name": "MiMo-V2.5-ASR" },
        "xiaomi/mimo-v2.5": { "name": "MiMo-V2.5" }
      }
    }
  },
  "voice": {
    "asr_model": "internal/xiaomi/mimo-v2.5-asr",
    "control_model": "internal/xiaomi/mimo-v2.5"
  }
}
```

Custom providers must register at least one model in their `models` field to be recognized. The model names in `voice.*_model` are sent directly to the API — they don't need to match the registered model keys exactly.

> **Note:** Models registered under a custom provider will appear in the model selection list. Don't use ASR-only models (e.g. `mimo-v2.5-asr`) as your primary coding model.

</details>

### Dream & Distill

- **`/dream`** — scans recent session traces, extracts persistent knowledge into project memory, and removes outdated entries
- **`/distill`** — discovers repeated manual workflows in recent work and packages high-confidence candidates into reusable skills, subagents, or commands

---

## Configuration

MiMoCode uses JSON/JSONC config files with published JSON Schemas for autocompletion and validation.

### File Locations

| File | Project-level | Global |
|------|--------------|--------|
| Main config | `.mimocode/mimocode.jsonc` (also `.json`) | `~/.config/mimocode/mimocode.jsonc` (also `.json`) |
| TUI config | `.mimocode/tui.json` | `~/.config/mimocode/tui.json` |
| Auth credentials | — | `~/.local/share/mimocode/auth.json` |

> On Windows, XDG paths fall under `%LOCALAPPDATA%\mimocode\`. You can override all paths with `MIMOCODE_HOME`.

### JSON Schemas

MiMoCode auto-injects a `$schema` field when it first loads your config, so your editor gets completions and validation out of the box:

| Config | Schema URL |
|--------|-----------|
| `mimocode.jsonc` / `mimocode.json` | `https://mimo.xiaomi.com/mimocode/config.json` |
| `tui.json` | `https://mimo.xiaomi.com/mimocode/tui.json` |

<details>
<summary><strong>VS Code / Cursor: trust the schema domain</strong></summary>

Add to your `settings.json` so the editor can download schemas for autocompletion:

```json
{
  "json.schemaDownload.trustedDomains": {
    "https://mimo.xiaomi.com/": true
  }
}
```

</details>

<details>
<summary><strong>Data directories</strong></summary>

Beyond config files, MiMoCode stores runtime data under XDG paths (or `$MIMOCODE_HOME`):

| Directory | Default (Linux) | Contents |
|-----------|----------------|----------|
| data | `~/.local/share/mimocode/` | SQLite database, auth credentials (`auth.json`), memory, logs |
| state | `~/.local/state/mimocode/` | TUI preferences (`kv.json`), recent models (`model.json`) |
| cache | `~/.cache/mimocode/` | Language servers, cached model catalog, skills |

To remove stored credentials, delete `auth.json` from the data directory. On macOS, XDG data defaults to `~/Library/Application Support/mimocode/`.

</details>

### Custom OpenAI-Compatible Endpoints

If your provider is not in the built-in model catalog, configure it directly with its base URL, API key, and model ID:

```jsonc
{
  "$schema": "https://mimo.xiaomi.com/mi
