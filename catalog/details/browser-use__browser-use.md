# browser-use/browser-use

🌐 Make websites accessible for AI agents. Automate tasks online with ease.

## installation

If you want to use Browser Use in your agent (Claude Code, Codex, Cursor, Hermes, OpenClaw, etc.), paste this prompt, and it sets everything up itself:

```text
Install or upgrade browser-use to the latest stable version with uv using Python 3.12, run `browser-use skill install` to register the skill, and connect it to my browser. If setup or connection fails, follow https://github.com/browser-use/browser-harness/blob/main/install.md.
```

Then tell your agent what you want done.

<br/>

## tools

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
