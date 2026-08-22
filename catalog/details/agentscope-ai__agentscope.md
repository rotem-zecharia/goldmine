# agentscope-ai/agentscope

Build and run agents you can see, understand and trust.

## installation

### Installation

> AgentScope requires **Python 3.11** or higher.

#### From PyPI

```bash
uv pip install agentscope
```

#### From source

```bash
# Pull the source code from GitHub
git clone -b main https://github.com/agentscope-ai/agentscope.git

# Install the package in editable mode
cd agentscope

uv pip install -e .
```

## Agent

The SDK layer — compose an agent from a rich set of building blocks:

| Building block | What's inside |
|---|---|
| [**ReAct**](https://docs.agentscope.io/latest/en/building-blocks/agent/overview) | Reasoning-acting loop with structured output, realtime interruption & resume, and batched (sequential / concurrent) tool acting |
| [**Toolkit**](https://docs.agentscope.io/latest/en/building-blocks/tool/overview) | Agentic tool management over Python tools, MCP servers, and skills; ships with built-in coding tools (shell, file edit, search) and task/plan tools |
| [**Model**](https://docs.agentscope.io/latest/en/building-blocks/model/overview) | LLM, embedding, and TTS across major providers (OpenAI, Anthropic, Gemini, DashScope, DeepSeek, Moonshot, xAI, Ollama) |
| [**Context**](https://docs.agentscope.io/latest/en/building-blocks/context/overview) | Automatic compaction, tool-result offload, and context injection (system prompt, RAG, memory) via built-in middleware |
| [**Event System**](https://docs.agentscope.io/latest/en/building-blocks/message-and-event) | Unified event bus streaming reasoning, tool calls, and multimodal content (text, image, audio) to the frontend |
| [**Permission & HITL**](https://docs.agentscope.io/latest/en/building-blocks/permission-system/overview) | Fine-grained control over tools and resources, confirmation, bypass mode |
| [**Middleware**](https://docs.agentscope.io/latest/en/building-blocks/middleware) | Composable hooks across the loop — reply, reasoning, acting, model calling, permission checking, context compression, system prompt |
| [**Memory**](https://docs.agentscope.io/latest/en/building-blocks/long-term-memory) | Agentic memory with switchable backends (ReMe, Mem0) |
| [**Workspace / Sandbox**](https://docs.agentscope.io/latest/en/building-blocks/workspace/overview) | Isolated tool & code execution — local, Docker, Apple Container, Bubblewrap, E2B, OpenSandbox, Daytona, K8s |

Start your first agent with AgentScope 2.0 in console:

```python
from agentscope.agent import Agent
from agentscope.console import launch_console
from agentscope.tool import Toolkit, Bash, Grep, Glob, Read, Write, Edit
from agentscope.credential import DashScopeCredential
from agentscope.model import DashScopeChatModel

import os, asyncio


async def main() -> None:
    agent = Agent(
        name="Friday",
        system_prompt="You're a helpful assistant named Friday.",
        model=DashScopeChatModel(
            credential=DashScopeCredential(
              api_key=os.environ["DASHSCOPE_API_KEY"]
            ),
            model="qwen3.6-plus",
        ),
        toolkit=Toolkit(
            tools=[
                Bash(),
                Grep(),
                Glob(),
                Read(),
                Write(),
                Edit(),
            ]
        ),
    )

    # Chat with the agent in the terminal — streamed output, tool-call
    # confirmation and Ctrl+C interruption are all handled for you
    await launch_console(agent)

asyncio.run(main())
```

## Agent Service — All You Need to Build Your App

AgentScope ships a batteries-included **agent service** — a FastAPI backend with a pre-built Web UI (`examples/web_ui`) that turns your agents into a multi-tenant, multi-session application, with rich capabilities out of the box:

| Capability | What you get |
|---|---|
| [**Serving**](https://docs.agentscope.io/latest/en/deploy/agent-service) | Multi-tenancy, multi-session isolation, FastAPI backend, pre-built Web UI |
| [**Agent Team**](https://docs.agentscope.io/latest/en/deploy/agent-team) | Leader–worker orchestration, built-in team tools, task planning |
| [*
