# Arindam200/awesome-ai-apps

A collection of projects showcasing RAG, agents, workflows, and other AI use cases

## features

### 🧩 Starter Agents

**Quick-start agents for learning and extending different AI frameworks.** _20 projects_

- [AutoGen Tool-Calling Starter](starter_ai_agents/autogen_starter): Microsoft AutoGen `AssistantAgent` with a custom tool, powered by Nebius Token Factory
- [AWS Strands Agent Starter](starter_ai_agents/aws_strands_starter): Weather report agent using AWS Strands SDK
- [CAMEL AI Model Benchmark](starter_ai_agents/camel_ai_starter): Performance benchmarking tool comparing various AI models
- [CrewAI Research Crew](starter_ai_agents/crewai_starter): Multi-agent research team example
- [Docker cagent Multi-Agent Starter](starter_ai_agents/cagent_starter): Open-source customizable multi-agent runtime by Docker
- [DSPy Optimization Starter](starter_ai_agents/dspy_starter): DSPy framework for building and optimizing AI systems
- [Google Agent Development Kit Starter](starter_ai_agents/google_adk_starter): Google Agent Development Kit starter template
- [Hacker News Trend Analyst (Agno)](starter_ai_agents/agno_starter): Agno-based agent for trend analysis on Hacker News
- [Hugging Face smolagents Starter](starter_ai_agents/smolagents_starter): Hugging Face smolagents code-first web-search agent
- [KAOS Kubernetes Multi-Agent Starter](starter_ai_agents/kaos_starter): Kubernetes-native multi-agent system with MCP tools and in-cluster LLM
- [LangChain Tool-Calling Starter](starter_ai_agents/langchain_starter): LangChain tool-calling agent with `create_tool_calling_agent` + `AgentExecutor`, powered by Nebius
- [LangGraph ReAct Agent Starter](starter_ai_agents/langgraph_starter): LangGraph prebuilt ReAct agent (`create_react_agent`) with custom tools, powered by Nebius
- [Letta Stateful Memory Agent](starter_ai_agents/letta_starter): Stateful agent with persistent long-term memory across sessions
- [LlamaIndex Task Manager](starter_ai_agents/llamaindex_starter): LlamaIndex-powered task assistant
- [Mastra Tool-Calling Starter](starter_ai_agents/mastra_starter): TypeScript-first agent with a custom tool powered by Nebius Token Factory
- [Microsoft Agent Framework Starter](starter_ai_agents/microsoft_agents_starter): Multi-agent travel planning demos built on Microsoft Agent Framework
- [OpenAI Agents SDK Starter](starter_ai_agents/openai_agents_sdk): OpenAI Agents SDK with email helper and haiku writer examples
- [PydanticAI Weather Bot](starter_ai_agents/pydantic_starter): Real-time weather information agent
- [Sayna Realtime Voice Agent](starter_ai_agents/sayna_starter): Real-time voice infrastructure with multi-provider STT/TTS (Deepgram, ElevenLabs, Azure, Google) and WebSocket streaming
- [Semantic Kernel Starter](starter_ai_agents/semantic_kernel_starter): Microsoft Semantic Kernel `ChatCompletionAgent` with plugin-based tool calling

### 🪶 Simple Agents

**Straightforward, practical use-cases for everyday AI applications.** _18 projects_

- [Agno Agent Examples](simple_ai_agents/agno_ai_examples): Simple to multi-agent examples with web search and a knowledge base
- [Agno Agent UI](simple_ai_agents/agno_ui_agent): Interactive UI for web and finance agents
- [AI Agent Registry Explorer](simple_ai_agents/agent_discovery_agent): Find and compare AI agents across NANDA, MCP, Virtuals, A2A, and ERC-8004 registries
- [Calendar Assistant](simple_ai_agents/cal_scheduling_agent): Calendar scheduling integration with Cal.com
- [Cost-Aware Model Router (RouteLLM)](simple_ai_agents/llm_router): Intelligent model routing with RouteLLM (GPT-4o-mini vs Nebius Llama) for cost optimization
- [Email-to-Calendar Assistant](simple_ai_agents/email_to_calendar_scheduler): AI-powered Gmail reader and Google Calendar manager
- [Financial Reasoning Agent](simple_ai_agents/reasoning_agent): Step-by-step financial reasoning demonstration
- [Human-in-the-Loop Agent](simple_ai_agents/human_in_the_loop_agent): HITL actions for safe AI task execution
- [LangChain Operations Agent Collection](simple_ai_agents/langchain_simple_agents): Nebius-powered inc

## requirements

- **Python 3.10+** (Python 3.11+ recommended for newer projects)
- **Git** for cloning the repository
- **Package Manager**: `pip` or `uv` (recommended for faster installs)
- **API Keys**: Most projects require API keys (see individual project READMEs)

## installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Arindam200/awesome-ai-apps.git
   cd awesome-ai-apps
   ```

2. **Choose a project** and navigate to its directory

   ```bash
   cd starter_ai_agents/agno_starter  # Example: Start with Agno starter
   ```

3. **Set up environment variables**

   ```bash
   cp .env.example .env  # Copy example environment file
   # Edit .env with your API keys
   ```

4. **Install dependencies**

   ```bash
   # Using pip
   pip install -r requirements.txt

   # OR using uv (recommended - faster)
   uv sync
   # or
   uv pip install -e .
   ```

5. **Run the project**

   ```bash
   python main.py
   # or for Streamlit apps
   streamlit run app.py
   ```

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

- 💡 **Add new projects**: Submit your own AI agent examples
- 🔧 **Fix issues**: Contribute code improvements and bug fixes
- 📝 **Improve documentation**: Help make projects more accessible
- 🐛 **Report bugs** or suggest improvements via [GitHub Issues](https://github.com/Arindam200/awesome-ai-apps/issues)

**Before contributing:**

- Read our [Contributing Guidelines](CONTRIBUTING.md) for detailed information
- Check existing issues to avoid duplicates
- Follow the project structure and naming conventions
- Ensure your project includes a comprehensive README.md

**Important:** This project follows a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to abide by its terms.

## 📜 License

This repository is licensed under the [MIT License](./LICENSE). Feel free to use and modify the examples for your projects.

## 👥 Core Maintainers

This project is actively maintained by:

<p align="center">
  <a href="https://github.com/Arindam200" title="Arindam Majumder">
    <img src="https://avatars.githubusercontent.com/u/109217591?s=128&v=4" width="72" height="72" alt="Arindam Majumder" style="border-radius: 50%;" />
  </a>
  &nbsp;&nbsp;&nbsp;
  <a href="https://github.com/shivaylamba" title="Shivay Lamba">
    <img src="https://avatars.githubusercontent.com/u/19529592?s=128&v=4" width="72" height="72" alt="Shivay Lamba" style="border-radius: 50%;" />
  </a>
  &nbsp;&nbsp;&nbsp;
  <a href="https://github.com/Astrodevil" title="Astrodevil">
    <img src="https://avatars.githubusercontent.com/u/73425223?s=128&v=4" width="72" height="72" alt="Astrodevil" style="border-radius: 50%;" />
  </a>
</p>

<p align="center">
  <sub>
    <a href="https://github.com/Arindam200">Arindam Majumder</a>
    &nbsp;·&nbsp;
    <a href="https://github.com/shivaylamba">Shivay Lamba</a>
    &nbsp;·&nbsp;
    <a href="https://github.com/Astrodevil">Astrodevil</a>
  </sub>
</p>

For any questions, suggestions, or contributions, feel free to reach out to the maintainers.

## Thank You for the Support! 🙏

[![Star History Chart](https://star-history.dera.page/svg?repos=Arindam200/awesome-ai-apps&type=Date)](https://star-history.dera.page/#Arindam200/awesome-ai-apps&Date)
