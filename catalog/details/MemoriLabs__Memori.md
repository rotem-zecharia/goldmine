# MemoriLabs/Memori

Memori is agent-native memory infrastructure. A LLM-agnostic layer that turns agent execution and conversation into structured, persistent state for production systems. Built for enterprise, Memori wo

## installation

### Installation

<details>
<summary><b>TypeScript SDK</b></summary>

```bash
npm install @memorilabs/memori
```
</details>

<details>
<summary><b>Python SDK</b></summary>

```bash
pip install memori
```
</details>

### Quickstart

Sign up at [app.memorilabs.ai](https://app.memorilabs.ai), get a Memori API key, and start building. Full docs: [memorilabs.ai/docs/memori-cloud/](https://memorilabs.ai/docs/memori-cloud/).

Set `MEMORI_API_KEY` and your LLM API key (e.g. `OPENAI_API_KEY`), then:

<details>
<summary><b>TypeScript SDK</b></summary>

```typescript
import { OpenAI } from 'openai';
import { Memori } from '@memorilabs/memori';

// Requires MEMORI_API_KEY and OPENAI_API_KEY in your environment
const client = new OpenAI();
const mem = new Memori().llm
  .register(client)
  .attribution('user_123', 'support_agent');

async function main() {
  await client.chat.completions.create({
    model: 'gpt-4o-mini',
    messages: [{ role: 'user', content: 'My favorite color is blue.' }],
  });
  // Conversations are persisted and recalled automatically in the background.

  const response = await client.chat.completions.create({
    model: 'gpt-4o-mini',
    messages: [{ role: 'user', content: "What's my favorite color?" }],
  });
  // Memori recalls that your favorite color is blue.
}
```
</details>

<details>
<summary><b>Python SDK</b></summary>

```python
from memori import Memori
from openai import OpenAI

## tools

client = OpenAI()
mem = Memori().llm.register(client)

mem.attribution(entity_id="user_123", process_id="support_agent")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "My favorite color is blue."}]
)
# Conversations are persisted and recalled automatically.

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "What's my favorite color?"}]
)
# Memori recalls that your favorite color is blue.
```
</details>

## Explore the Memories

Use the [Dashboard](https://app.memorilabs.ai) — Memories, Analytics, Playground, and API Keys.

> [!TIP]
> Want to use your own database? Check out docs for Memori BYODB here:
> [https://memorilabs.ai/docs/memori-byodb/](https://memorilabs.ai/docs/memori-byodb/).
> For disposable BYODB development databases, see the TiDB Zero provisioning
> guide: [docs/memori-byodb/databases/tidb.mdx](docs/memori-byodb/databases/tidb.mdx).

## LoCoMo Benchmark

Memori was evaluated on the LoCoMo benchmark for long-conversation memory and achieved **87% overall accuracy** while using an average of **721 tokens per query**. That is just **2.8% of the full-context footprint**, showing that structured memory can preserve reasoning quality without forcing large prompts into every request.

Compared with other retrieval-based memory systems, Memori outperformed Zep, LangMem, and Mem0 while reducing prompt size by roughly **67% vs. Zep** and lowering context cost by more than **36x vs. full-context prompting**.

Read the [benchmark overview](docs/memori-cloud/benchmark/overview.mdx), see the [results](docs/memori-cloud/benchmark/results.mdx), or download the [paper](https://arxiv.org/abs/2603.19935).

!["Memori's average accuracy along with the standard deviation"](images/benchmark.png)

## OpenClaw (Persistent Memory for Your Gateway)

By default, OpenClaw agents forget everything between sessions. The Memori plugin fixes that. It automatically captures structured memory from conversation and agent execution after each turn — including tool calls, decisions, and outcomes — and makes it available for agents to recall on demand.

No changes to your agent code or prompts are required. The plugin hooks into OpenClaw's lifecycle, so you get structured memory, agent-controlled recall, and Advanced Augmentation with a drop-in plugin.

```bash
openclaw plugins install @memorilabs/openclaw-memori
openclaw plugins enable openclaw-memori

openclaw memori init \
  --api-key "YOUR_MEMORI_API_KEY" \
  --entity-id "your-app-user-id" \
  --project-id "my-project"

openclaw gateway restart
```

For setup and configuration, see the [OpenClaw Quickstart](docs/memori-cloud/openclaw/quickstart.mdx). For architecture and lifecycle details, see the [OpenClaw Overview](docs/memori-cloud/openclaw/overview.mdx).

## Hermes Agent (Persistent Memory Provider)

Memori also ships as a Hermes Agent memory provider. It captures completed conversations in the background and gives Hermes explicit `memori_recall` and `memori_recall_summary` tools for agent-controlled recall.

```bash
pip install hermes-memori
hermes-memori install

hermes config set memory.provider memori
HERMES_HOME="${HERMES_HOME:-$HOME/.hermes}"
mkdir -p "$HERMES_HOME"
echo "MEMORI_API_KEY=YOUR_MEMORI_API_KEY" >> "$HERMES_HOME/.env"
echo "MEMORI_ENTITY_ID=your-app-user-id" >> "$HERMES_HOME/.env"
```

`MEMORI_PROJECT_ID` is optional; when omitted, the provider uses Hermes' active project context for scoping.

For setup and configuration, see the [Hermes Quickstart](docs/memori-cloud/hermes/quickstart.mdx). For architecture and lifecycle details, see the [Hermes Overview](docs/memori-cloud/hermes/overview.mdx).

## MCP (Connect Your Agent in One Command)

Your agent forgets everything between sessions. Memori fixes that. It remembers your stack, your conventions, and how you like things done so you stop repeating yourself.

Works for solo developers and teams. Your a
