# browser-use/browser-use

Agents that use the browser.

## installation

## Path 1: Fully Hosted Cloud

Scale browser automation with our hosted agent, stealth browsers, and infrastructure for profiles, recordings, and data policies.

[Get started with the API ↗](https://docs.browser-use.com/cloud/agent/quickstart)

New Google, GitHub, or Microsoft signups get **$15 cloud credit**.

<br/>

## Path 2: CLI

Paste this prompt into Claude Code, Codex, Hermes, OpenClaw, or your favorite agent.

```text
Install or upgrade browser-use to the latest stable version with uv using Python 3.12, run `browser-use skill install` to register the skill, and connect it to my browser. If setup or connection fails, follow https://github.com/browser-use/browser-harness/blob/main/install.md.
```

<br/>

## Path 3: Python Library

Run the Browser Use agent locally from Python, with your choice of model and a local or cloud browser:

**1. Install Browser Use (Python >= 3.11):**

With [uv](https://docs.astral.sh/uv/getting-started/installation/) installed, run `uv init --python 3.12` first if you're starting a new project.

```bash
uv add browser-use
```

**2. Add your [OpenAI API key](https://platform.openai.com/api-keys) to `.env`:**

```bash
# .env
OPENAI_API_KEY=your-key

## tools

```

For either optional Browser Use service, get a [Browser Use API key](https://cloud.browser-use.com/new-api-key).

**3. Save this as `agent.py`:**

```python
import asyncio

from browser_use import Agent, Browser, ChatBrowserUse, ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

async def main():
    llm = ChatOpenAI(model='gpt-5.6-luna', reasoning_effort='xhigh')
    # llm = ChatBrowserUse(model='bu-2-0')  # Use BU2 instead; requires BROWSER_USE_API_KEY
    agent = Agent(
        task="Find the number of stars of the browser-use repo",
        llm=llm,
        # browser=Browser(use_cloud=True),  # Use a cloud browser; requires BROWSER_USE_API_KEY
    )
    history = await agent.run()
    print(history.final_result())

if __name__ == "__main__":
    asyncio.run(main())
```

To use BU2, replace the `ChatOpenAI` line with the commented `ChatBrowserUse` line. The cloud-browser option works with either model.

**4. Run it:**

```bash
uv run agent.py
```

The agent opens a browser, looks up the repository, and prints its answer.

[Python library docs ↗](https://docs.browser-use.com/open-source/introduction)

<br/>

# Browser Use toolsets for Claude

Maintained by Browser Use. Compatible with Claude.

Use Claude's browser toolset with Browser Use as the driver. Browser Use
implements all 31 browser actions and can control a local browser, a Browser
Use Cloud browser, or an existing remote browser over CDP.
Bash is included in the Browser Use integration for processing data and writing files.

<img src="examples/integrations/toolsets-for-claude/architecture.svg" alt="Claude uses Browser Use browser actions and Bash through the Anthropic SDK. The browser can be local or remote; Bash runs on the SDK host." width="100%">

Requires an Anthropic SDK version that includes `anthropic.tools.browser`.
Bash requires a Linux or macOS host with `/bin/bash`; use WSL on Windows.
The snippet below runs inside an async function; see the quickstart for a complete script.

```python
import os

from anthropic import AsyncAnthropic
from browser_use.integrations.toolsets_for_claude import Bash, BrowserUse

task = 'Open example.com and report its page title.'
driver = BrowserUse()  # Or BrowserUse(use_cloud=True)
bash = Bash(output_dir='outputs')

async with driver, AsyncAnthropic() as client:
    runner = client.beta.messages.tool_runner(
        model=os.environ['ANTHROPIC_MODEL'],
        max_tokens=32_768,
        max_iterations=100,
        tools=[driver, bash],
        messages=[{'role': 'user', 'content': task}],
    )
    result = await runner.until_done()
```

[Quickstart ↗](examples/integrations/toolsets-for-claude) · [Integration docs ↗](https://docs.browser-use.com/open-source/customize/integrations/toolsets-for-claude)

<br/>

# Browser Use Benchmark v2

<img alt="Browser Use Benchmark v2 - Mean rubric score by model and cost per task" src="static/hard_benchmark_v2.jpg" width="100%">

This [very hard benchmark](https://github.com/browser-use/benchmark) targets the hardest browser tasks. On easier tasks, even smaller models can achieve very high success rates. Results shown are from a 60-task subset of BU Bench V2.

## Integrations, hosting, custom tools, MCP, and more on our [Docs ↗](https://docs.browser-use.com)

<br/>

# FAQ

<details>
<summary><b>Should I use the fully hosted cloud, CLI, or Python library?</b></summary>

- **[Fully Hosted Cloud](#path-1-fully-hosted-cloud):** Send tasks through the API and let Browser Use run the agent, browser, and infrastructure.
- **[CLI](#path-2-cli):** Give an existing agent (Claude Code, Codex, Hermes, OpenClaw, Pi, Cursor, etc.) browser access. You can use it interactively or in scripts.
- **[Python Library](#path-3-python-library):** Run the open source agent in your own application, with custom tools, structured output, and your choice of model.

The CLI and Python library can each connect to a local or cloud browser. A cloud browser hosts the browser; the fully hosted API runs the age
