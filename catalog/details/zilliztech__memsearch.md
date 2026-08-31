# zilliztech/memsearch

A persistent, unified memory layer for all your AI agents (e.g. Claude Code, Codex, DSH), backed by Markdown and Milvus.

## features

- 🌐 **All Platforms, One Memory** — memories flow across [Claude Code](plugins/claude-code/README.md), [Codex](plugins/codex/README.md), [DeepSeek Harness](plugins/dsh/README.md), [OpenClaw](plugins/openclaw/README.md), and [OpenCode](plugins/opencode/README.md). A conversation in one agent becomes searchable context in all others — no extra setup
- 👥 **For Agent Users**, install a plugin and get persistent memory with zero effort; **for Agent Developers**, use the full [CLI](https://zilliztech.github.io/memsearch/cli/) and [Python API](https://zilliztech.github.io/memsearch/python-api/) to build memory and harness engineering into your own agents
- 📄 **Markdown is the source of truth** — inspired by [OpenClaw](https://github.com/openclaw/openclaw). Your memories are just `.md` files — human-readable, editable, version-controllable. Milvus is a "shadow index": a derived, rebuildable cache
- 🔍 **Progressive retrieval, hybrid search, smart dedup, live sync** — 3-layer recall (search → expand → transcript); dense vector + BM25 sparse + RRF reranking; SHA-256 content hashing skips unchanged content; file watcher auto-indexes in real time

---

## 🧑‍💻 For Agent Users

Pick your platform, install the plugin, and you're done. Each plugin captures conversations automatically and provides semantic recall with zero configuration.

<details open>
<summary><h3>For Claude Code Users</h3></summary>

```bash

## installation

/plugin marketplace add zilliztech/memsearch
/plugin install memsearch
# Restart Claude Code to activate the plugin
```

After restarting, just chat with Claude Code as usual. The plugin captures every conversation turn automatically.

**Verify it's working** — after a few conversations, check your memory files:

```bash
ls .memsearch/memory/          # you should see daily .md files
cat .memsearch/memory/$(date +%Y-%m-%d).md
```

**Recall memories** — two ways to trigger:

```
/memory-recall what did we discuss about Redis?
```
Or just ask naturally — Claude auto-invokes the skill when it senses the question needs history:
```
We discussed Redis caching before, what was the TTL we chose?
```

> 📖 [Claude Code Plugin docs](https://zilliztech.github.io/memsearch/platforms/claude-code/) · [Troubleshooting](https://zilliztech.github.io/memsearch/platforms/claude-code/troubleshooting/)

</details>

<details open>
<summary><h3>For Codex Users</h3></summary>

```bash
# Install
git clone --depth 1 https://github.com/zilliztech/memsearch.git
bash memsearch/plugins/codex/scripts/install.sh
codex --yolo  # needed for ONNX model network access
```

After installing, chat as usual. Hooks capture and summarize each turn.

**Verify it's working:**

```bash
ls .memsearch/memory/
```

**Recall memories** — use the skill:

```
$memory-recall what did we discuss about deployment?
```

> 📖 [Codex Plugin docs](https://zilliztech.github.io/memsearch/platforms/codex/)

</details>

<details open>
<summary><h3>For DeepSeek Harness Users</h3></summary>

```bash
# Install the published plugin into your DSH profile
uv tool install "memsearch[onnx]"
dsh plugin --profile web add @zilliz/memsearch-dsh
# Restart that DSH profile, or start a new session
```

After installing, use DSH normally. Completed turns are captured automatically, and relevant memories are injected before the first model step only when they are useful.

**Verify it's working:**

```bash
ls .memsearch/memory/
```

**Recall memories** — ask naturally or tell DSH to use the registered `memory-recall` skill:

```
Use memory-recall to find what we decided about the deployment architecture.
```

The web profile also adds a compact MemSearch dock where you can review skill candidates and browse supported files under `.memsearch/` without editing them.

> 📖 [DeepSeek Harness Plugin docs](https://zilliztech.github.io/memsearch/platforms/dsh/)

</details>

<details>
<summary><h3>For OpenClaw Users</h3></summary>

```bash
# Install from ClawHub
openclaw plugins install --force clawhub:memsearch
openclaw config set plugins.entries.memsearch.hooks.allowConversationAccess true
openclaw config set plugins.entries.memsearch.hooks.allowPromptInjection true
openclaw gateway restart
```

After installing, chat in TUI as usual. The plugin captures each turn automatically.

**Verify it's working** — memory files are stored in your agent's workspace:

```bash
# For the main agent:
ls ~/.openclaw/workspace/.memsearch/memory/
# For other agents (e.g. work):
ls ~/.openclaw/workspace-work/.memsearch/memory/
```

**Recall memories** — two ways to trigger:

```
/memory-recall what was the batch size limit we set?
```
Or just ask naturally — the LLM auto-invokes memory tools when it senses the question needs history:
```
We discussed batch size limits before, what did we decide?
```

> 📖 [OpenClaw Plugin docs](https://zilliztech.github.io/memsearch/platforms/openclaw/) · [Browse on ClawHub](https://clawhub.ai/plugins/memsearch)

</details>

<details>
<summary><h3>For OpenCode Users</h3></summary>

```json
// In ~/.config/opencode/opencode.json
{ "plugin": ["@zilliz/memsearch-opencode"] }
```

After installing, chat in TUI as usual. A background daemon captures conversations.

**Verify it's working:**

```bash
ls .memsearch/memory/    # daily .md files appear after a few conversations
```

**Recall memories** — two ways to trigger:

```
/memory-recall what did we discuss about authentication?
```
Or just ask natura

## configuration

All plugins share the same memsearch backend. Configure once, works everywhere.

#### Embedding

Defaults to **ONNX bge-m3** — runs locally on CPU, no API key, no cost. On first launch the model (~558 MB) is downloaded from HuggingFace Hub.

```bash
memsearch config set embedding.provider onnx     # default — local, free
memsearch config set embedding.provider openai   # needs OPENAI_API_KEY
memsearch config set embedding.provider ollama   # local, any model
```

> All providers and models: [Configuration — Embedding Provider](https://zilliztech.github.io/memsearch/home/configuration/#embedding-provider)

#### Milvus Backend

Just change `milvus_uri` (and optionally `milvus_token`) to switch between deployment modes:

**Milvus Lite** (default) — zero config, single file. Great for getting started:

```bash

## tools

uv tool install "memsearch[onnx]"
pipx install "memsearch[onnx]"
pip install "memsearch[onnx]"

# As a project dependency
uv add "memsearch[onnx]"
