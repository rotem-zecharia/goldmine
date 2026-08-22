# MervinPraison/PraisonAI

PraisonAI 🦞 — Hire a 24/7 AI Workforce. Stop writing boilerplate and start shipping autonomous self-improving agents that research, plan, code, and execute tasks. Deployed in 5 lines of code with buil

## tools

agent = Agent(name="builder", instructions="You build things.",
              tools_run_on="docker")   # docker | e2b | modal | daytona | flyio
                                       # tenki | sandlock | ssh | novita | subprocess

# B. The WHOLE agent moves — model calls, loop and tools
agent = Agent(name="teacher", instructions="You teach.", run_on="anthropic")  # hosted
agent = Agent(name="builder", instructions="You build.", run_on="docker")     # self-hosted
agent.start("Write a Python script that prints the first 10 primes, then run it")
```

Ask any object where it runs, and it will tell you:

```python
>>> Agent(name="builder", instructions="x", tools_run_on="docker")
Agent(name='builder', thinks_on='this machine', tools_run_on='a Docker container')

>>> agent.where_does_it_run()
Thinking (the AI model calls) happens on this machine.
Tools run on a Docker container.
Your own tools (check_db) still run on this machine -- only shell, file and
code tools move. They read and write this machine's files.
```

Naming a place that cannot do the job is a typo, not a preference, so it says so:

```python
>>> Agent(name="x", instructions="i", run_on="e2b")
TypeError: Agent(run_on='e2b') is not valid: run_on= places the whole agent
-- model calls, loop and tools -- on a managed runtime, and 'e2b' runs
commands but cannot host an agent loop.
  To run only the tools there:  Agent(tools_run_on='e2b')
```

To run one block of code somewhere else, name the place on that call:

```python
agent.execute_code_sync("print(6 * 7)", run_in="sandlock")   # kernel-enforced
```

See what is running and reclaim strays:

```bash
praisonai managed ps          # list running sandboxes
praisonai managed stop --all  # reclaim them
```

Sandboxes shut themselves down when idle (`auto_shutdown`, `idle_timeout_s`), and a post-setup snapshot is reused so the next run skips the image pull and dependency install. Commit a `.praisonai/environment.yaml` and the environment travels with the repo.

> 📖 [20 runnable examples](examples/python/managed-agents/) · manage sessions with `praisonai managed sessions list <agent-id>` or `praisonai managed sessions resume <session-id> "<prompt>"`

<sub>Stack framing adapted from [The Five-Layer Agent Stack](https://mer.vin/2026/07/five-layer-agent-stack-match-bug-to-right-layer/) and [Agent Harnesses vs Orbs](https://mer.vin/2026/08/agent-harnesses-vs-orbs-why-remote-sandboxes-beat-local-agent-loops/).</sub>

---

## 🌌 The PraisonAI Ecosystem

Start simple with the core SDK, or expand to full visual builders and dashboards when you're ready.

*   **Core SDK (`praisonaiagents`)**: For pure Python development. `pip install praisonaiagents`
*   💻 **PraisonAI CLI (`praisonai`)**: For terminal-based developers. `pip install praisonai`
*   🦞 **Claw Dashboard**: Connect agents directly to Telegram, Slack, or Discord. `pip install "praisonai[claw]"`
*   🔗 **Flow Visual Builder**: Drag-and-drop workflow creation. `pip install "praisonai[flow]"`
*   🤖 **PraisonAI UI**: Clean chat interface. `pip install "praisonai[ui]"`

### JavaScript SDK

```bash
npm install praisonai
```

## features

Powered by 100+ LLMs (OpenAI, Anthropic, Gemini & local models).

<p align="center">
<img src="https://img.shields.io/badge/OpenAI-412991?style=flat&logo=openai&logoColor=white" alt="OpenAI" />
<img src="https://img.shields.io/badge/Anthropic-191919?style=flat&logo=anthropic&logoColor=white" alt="Anthropic" />
<img src="https://img.shields.io/badge/Google_Gemini-4285F4?style=flat&logo=google&logoColor=white" alt="Google Gemini" />
<img src="https://img.shields.io/badge/DeepSeek-566AB2?style=flat" alt="DeepSeek" />
<img src="https://img.shields.io/badge/Azure-0078D4?style=flat&logo=microsoftazure&logoColor=white" alt="Azure" />
<img src="https://img.shields.io/badge/Ollama-000000?style=flat" alt="Ollama" />
<img src="https://img.shields.io/badge/Groq-F05237?style=flat" alt="Groq" />
<img src="https://img.shields.io/badge/Mistral-FF7000?style=flat" alt="Mistral" />
<img src="https://img.shields.io/badge/Cerebras-F05A28?style=flat" alt="Cerebras" />
<img src="https://img.shields.io/badge/Cohere-39594D?style=flat" alt="Cohere" />
<img src="https://img.shields.io/badge/OpenRouter-6467F2?style=flat" alt="OpenRouter" />
<img src="https://img.shields.io/badge/Perplexity-20808D?style=flat" alt="Perplexity" />
<img src="https://img.shields.io/badge/Fireworks-FF6B35?style=flat" alt="Fireworks" />
<img src="https://img.shields.io/badge/AWS_Bedrock-FF9900?style=flat&logo=amazonaws&logoColor=white" alt="AWS Bedrock" />
<img src="https://img.shields.io/badge/xAI_Grok-000000?style=flat" alt="xAI Grok" />
<img src="https://img.shields.io/badge/Vertex_AI-4285F4?style=flat&logo=googlecloud&logoColor=white" alt="Vertex AI" />
<img src="https://img.shields.io/badge/HuggingFace-FFD21E?style=flat&logo=huggingface&logoColor=black" alt="HuggingFace" />
<img src="https://img.shields.io/badge/Together_AI-000000?style=flat" alt="Together AI" />
<img src="https://img.shields.io/badge/Databricks-FF3621?style=flat&logo=databricks&logoColor=white" alt="Databricks" />
<img src="https://img.shields.io/badge/Replicate-262626?style=flat" alt="Replicate" />
<img src="https://img.shields.io/badge/Cloudflare-F38020?style=flat&logo=cloudflare&logoColor=white" alt="Cloudflare" />
</p>

<details>
<summary><strong>View all 24 providers with examples</strong></summary>

| Provider | Example |
|----------|:-------:|
| OpenAI | [Example](examples/python/providers/openai/openai_gpt4_example.py) |
| Anthropic | [Example](examples/python/providers/anthropic/anthropic_claude_example.py) |
| Google Gemini | [Example](examples/python/providers/google/google_gemini_example.py) |
| Ollama | [Example](examples/python/providers/ollama/ollama-agents.py) |
| Groq | [Example](examples/python/providers/groq/kimi_with_groq_example.py) |
| DeepSeek | [Example](examples/python/providers/deepseek/deepseek_example.py) |
| xAI Grok | [Example](examples/python/providers/xai/xai_grok_example.py) |
| Mistral | [Example](examples/python/providers/mistral/mistral_example.py) |
| Cohere | [Example](examples/python/providers/cohere/cohere_example.py) |
| Perplexity | [Example](examples/python/providers/perplexity/perplexity_example.py) |
| Fireworks | [Example](examples/python/providers/fireworks/fireworks_example.py) |
| Together AI | [Example](examples/python/providers/together/together_ai_example.py) |
| OpenRouter | [Example](examples/python/providers/openrouter/openrouter_example.py) |
| HuggingFace | [Example](examples/python/providers/huggingface/huggingface_example.py) |
| Azure OpenAI | [Example](examples/python/providers/azure/azure_openai_example.py) |
| AWS Bedrock | [Example](examples/python/providers/aws/aws_bedrock_example.py) |
| Google Vertex | [Example](examples/python/providers/vertex/vertex_example.py) |
| Databricks | [Example](examples/python/providers/databricks/databricks_example.py) |
| Cloudflare | [Example](examples/python/providers/cloudflare/cloudflare_example.py) |
| AI21 | [Example](examples/python/providers/ai21/ai21_example.py) |
| Replicate | [Example](examples/pyt

## configuration

agent = Agent(
    tools=MCP(
        command="npx",
        args=["-y", "@modelcontextprotocol/server-brave-search"],
        env={"BRAVE_API_KEY": "your-key"}
    )
)
```

> 📖 [Full MCP docs](https://docs.praison.ai/docs/mcp/transports) — stdio, HTTP, WebSocket, SSE transports
