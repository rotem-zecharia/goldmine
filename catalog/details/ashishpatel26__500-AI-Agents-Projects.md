# ashishpatel26/500-AI-Agents-Projects

The 500 AI Agents Projects is a curated collection of AI agent use cases across various industries. It showcases practical applications and provides links to open-source projects for implementation, i

## installation

Pick a framework and run an agent in under 5 minutes:

```bash
# Clone the repo
git clone https://github.com/ashishpatel26/500-AI-Agents-Projects.git
cd 500-AI-Agents-Projects

# Run any agent from the agents/ directory
cd agents/01-web-research-agent
pip install -r requirements.txt
cp .env.example .env        # add your API key
python agent.py
```

> All agents in `agents/` are self-contained with their own `requirements.txt` and `.env.example`. No monorepo setup needed.

---

## 🗺️ Navigation Guide

| I want to... | Go to |
|---|---|
| Run a working agent right now | [`agents/`](agents/) |
| Browse by AI framework | [Framework-wise Use Cases](#-browse-by-framework) |
| Browse by industry | [Industry Use Cases](#-industry-use-cases) |
| Understand which framework to use | [Framework Comparison](#-framework-comparison) |
| Add my own agent | [Contributing](CONTRIBUTION.md) |
| Learn with a course | [`crewai_mcp_course/`](crewai_mcp_course/) |

---

## 📊 Framework Comparison

Choosing a framework? Here's when to use each:

| Framework | Best For | Complexity | Multi-Agent | Streaming | Local LLM |
|---|---|---|---|---|---|
| **LangGraph** | Stateful workflows, RAG pipelines, complex graphs | ⭐⭐⭐ | ✅ | ✅ | ✅ |
| **CrewAI** | Role-based teams, business automation, rapid prototyping | ⭐⭐ | ✅ | ✅ | ✅ |
| **AutoGen** | Code generation, research, self-healing workflows | ⭐⭐⭐ | ✅ | ✅ | ✅ |
| **Agno** | Lightweight single agents, tool integration, fast iteration | ⭐ | ✅ | ✅ | ✅ |
| **LlamaIndex** | Document Q&A, enterprise RAG, data pipelines | ⭐⭐ | ⚠️ | ✅ | ✅ |

**Quick decision guide:**
- Just starting out → **Agno** or **CrewAI**
- Need stateful graphs + RAG → **LangGraph**
- Building code-writing / research agents → **AutoGen**
- Enterprise document pipelines → **LlamaIndex**

---

## 🏭 Industry Use Cases

![Industry Mind Map](images/industry_usecase1.png)

| Use Case | Industry | Description | Code |
|---|---|---|---|
| **HIA (Health Insights Agent)** | Healthcare | Analyses medical reports and provides health insights | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/harshhh28/hia) |
| **AI Health Assistant** | Healthcare | Diagnoses and monitors diseases using patient data | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/ahmadvh/AI-Agents-for-Medical-Diagnostics) |
| **Automated Trading Bot** | Finance | Automates stock trading with real-time market analysis | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/MingyuJ666/Stockagent) |
| **Agent Wallet SDK** | Finance | Non-custodial smart contract wallet SDK for AI agents with enforced spend limits | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/up2itnow0822/agent-wallet-sdk) |
| **Virtual AI Tutor** | Education | Provides personalized education tailored to users | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/hqanhh/EduGPT) |
| **24/7 AI Chatbot** | Customer Service | Handles customer queries around the clock | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/NirDiamant/GenAI_Agents/blob/main/all_agents_tutorials/customer_support_agent_langgraph.ipynb) |
| **Product Recommendation Agent** | Retail | Suggests products based on user preferences and history | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/microsoft/RecAI) |
| **Self-Driving Delivery Agent** | Transportation | Optimizes routes and autonomously delivers packages | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/sled-group/driVLMe) |
| **Factory Process Monitoring Agent** | Manufacturing | Monitors production lines and ensures quality control | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/yuchenxia/llm4ias) |
| **Property Pricing Ag
