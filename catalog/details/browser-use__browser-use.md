# browser-use/browser-use

🌐 Make websites accessible for AI agents. Automate tasks online with ease.

## installation

If you want to use Browser Use in your agent (Claude Code, Codex, Cursor, Hermes, OpenClaw, etc.), paste this prompt, and it sets everything up itself:

```text
Install or upgrade browser-use to the latest stable version with uv using Python 3.12, run `browser-use skill install` to register the skill, and connect it to my browser. If setup or connection fails, follow https://github.com/browser-use/browser-harness/blob/main/install.md.
```

Then tell your agent what you want done.

<br/>

# Python library: the easiest way to automate the web

Want to automate the web at scale, from your own code, and with any LLM? Use the Python library:

**1. Install Browser Use (Python >= 3.11):**

```bash
uv add browser-use
# or: pip install browser-use
```

**2. Add your LLM API key to `.env`**. Get one from [Browser Use Cloud](https://cloud.browser-use.com/new-api-key?utm_source=github&utm_medium=readme-quickstart-api-key), or bring your own provider key:

```bash
# .env
BROWSER_USE_API_KEY=your-key

## tools

# ANTHROPIC_API_KEY=your-key
```

**3. Run your first agent:**

```python
import asyncio

from browser_use import Agent, ChatBrowserUse

async def main():
    agent = Agent(
        task="Find the number of stars of the browser-use repo",
        llm=ChatBrowserUse(model='openai/gpt-5.5'),
        # llm=ChatBrowserUse(model='bu-2-0-mini-preview'),  # Browser Use's optimized model
        # llm=ChatOpenAI(model='gpt-5.5'),
        # llm=ChatAnthropic(model='claude-opus-4-8'),  # Sonnet also works well
    )
    history = await agent.run()

if __name__ == "__main__":
    asyncio.run(main())
```

Check out the [library docs](https://docs.browser-use.com/open-source/introduction) and the [cloud docs](https://docs.cloud.browser-use.com?utm_source=github&utm_medium=readme-cloud-docs) for more!

<br/>

# Open Source vs Cloud

<picture>
  <source media="(prefers-color-scheme: light)" srcset="static/accuracy_by_model_light.png">
  <source media="(prefers-color-scheme: dark)" srcset="static/accuracy_by_model_dark.png">
  <img alt="BU Bench V1 - LLM Success Rates" src="static/accuracy_by_model_light.png" width="100%">
</picture>

We benchmark Browser Use across 100 real-world browser tasks. Full benchmark is open source: **[browser-use/benchmark](https://github.com/browser-use/benchmark)**.

Browser Use is also **#1 on the [Odysseys leaderboard](https://odysseysbench.com/leaderboard)** with an 87.4% average, ahead of computer-use agents from OpenAI, Anthropic, Google, and Microsoft. Odysseys measures the agent's performance on 200 long-horizon web tasks.

**Use the Open-Source Agent**
- Free, and runs on your own machine
- Deep code-level integration and control: pick your LLM, customize the agent's behavior
- We recommend pairing it with our [cloud browsers](https://docs.browser-use.com/open-source/customize/browser/remote) for leading stealth, proxy rotation, and scaling

**Use the [Fully-Hosted Cloud Agent](https://cloud.browser-use.com?utm_source=github&utm_medium=readme-hosted-agent) (recommended)**
- Much more powerful agent for complex tasks (see plot above)
- Easiest way to start and scale
- Best stealth with proxy rotation and captcha solving
- 1000+ integrations (Gmail, Slack, Notion, and more)
- Persistent filesystem and memory
- Rerunnable scripts fetch live data, even when sites change ([guide](https://docs.browser-use.com/cloud/agent/scripts))

```sh
curl -X POST https://api.browser-use.com/api/v4/runs \
  -H "X-Browser-Use-API-Key: $BROWSER_USE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"task": "Your task"}'
```

<br/>

## Integrations, hosting, custom tools, MCP, and more on our [Docs ↗](https://docs.browser-use.com)

<br/>

# FAQ

<details>
<summary><b>Should I use the CLI vs. the Python library?</b></summary>

**Use the CLI** if you already have an agent (Claude Code, Codex, Cursor, Hermes, OpenClaw, etc.) that you want to complete browser tasks for you. The agent installs the skill once (see [Quickstart](#quickstart)) and can then control the browser. Examples:
- "Upload this video to YouTube"
- "Compare these three laptops and give me a table with prices"
- "Fill in this job application with my resume"

**Use the Python library** when you are building software that automates the web. Examples:
- Run many tasks on a schedule or in parallel (scraping, monitoring, QA)
- Embed a browser agent into your own product
- Custom tools, custom system prompts, structured output, fine-grained browser control

Rule of thumb: one-off tasks through an agent → CLI. Repeatable automation in code → Python library.
</details>

<details>
<summary><b>What's the best model to use?</b></summary>

We optimized **ChatBrowserUse()** specifically for browser automation tasks. On avg it completes tasks 3-5x faster than other models with SOTA accuracy.

For pricing and other LLM providers, see our [supported models documentation](https://docs.browser-use.com/supported-models).
</details>

<details>
<summary><b>Can I use Claude / GPT
