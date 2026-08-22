# HKUDS/Vibe-Trading

"Vibe-Trading: Your Personal Trading Agent"

## features

<div align="center">
<table align="center" width="94%" style="width:94%; margin-left:auto; margin-right:auto;">
  <tr>
    <td align="center" width="50%" valign="top">
      <img src="assets/feature-self-improving-trading-agent.png" height="130" alt="Self-improving trading agent"/><br>
      <h3>🔍 Self-Improving Trading Agent</h3>
      <div align="left">
        • Natural-language market research<br>
        • Strategy drafts and file/web analysis<br>
        • Memory-backed workflows
      </div>
    </td>
    <td align="center" width="50%" valign="top">
      <img src="assets/feature-multi-agent-trading-teams.png" height="130" alt="Multi-agent trading teams"/><br>
      <h3>🐝 Multi-Agent Trading Teams</h3>
      <div align="left">
        • Investment, quant, crypto, and risk teams<br>
        • Streaming progress and persisted reports<br>
        • Workers grounded with fetched market data
      </div>
    </td>
  </tr>
  <tr>
    <td align="center" width="50%" valign="top">
      <img src="assets/feature-cross-market-data-backtesting.png" height="130" alt="Cross-market data and backtesting"/><br>
      <h3>📊 Cross-Market Data & Backtesting</h3>
      <div align="left">
        • A / HK / US / Canada / India / Korea equities, crypto, futures, and forex<br>
        • Data fallback and composite backtests<br>
        • PIT data, validation, and run cards
      </div>
    </td>
    <td align="center" width="50%" valign="top">
      <img src="assets/feature-shadow-account.png" height="130" alt="Shadow Account"/><br>
      <h3>👥 Shadow Account</h3>
      <div align="left">
        • Broker-journal behavior diagnostics<br>
        • Rule-based Shadow Account comparisons<br>
        • Exportable audit reports and strategy code
      </div>
    </td>
  </tr>
</table>
</div>

## installation

```bash
pip install vibe-trading-ai
```

Then run a first research task:

```bash
vibe-trading init
vibe-trading run -p "Backtest a BTC-USDT 20/50 moving-average strategy for 2024 and summarize return and drawdown"
```

> **Upgrading from an older version?** 0.1.10 moved to LangChain 1.x. If imports break after `pip install -U vibe-trading-ai` over a pre-0.1.10 install (e.g. langgraph fails to import), recreate the venv or run `pip install --force-reinstall vibe-trading-ai`. A fresh install is unaffected.

> **Package name vs commands:** The PyPI package is `vibe-trading-ai`. Once installed, you get three commands:
>
> | Command | Purpose |
> |---------|---------|
> | `vibe-trading` | Interactive CLI / TUI |
> | `vibe-trading serve` | Launch FastAPI web server |
> | `vibe-trading-mcp` | Start MCP server (for Claude Desktop, OpenClaw, Cursor, etc.) |

```bash
vibe-trading init              # interactive .env setup
vibe-trading                   # launch CLI
vibe-trading serve --port 8899 # launch web UI
vibe-trading-mcp               # start MCP server (stdio)
```

## requirements

- An **LLM API key** from any supported provider — or run locally with **Ollama** (no key needed)
- **Python 3.11+** for Path B
- **Docker** for Path A
- OpenAI Codex can also be used with ChatGPT OAuth: set `LANGCHAIN_PROVIDER=openai-codex`, then run `vibe-trading provider login openai-codex`. This does not use `OPENAI_API_KEY`.
- GitHub Copilot can be used with an active Copilot subscription instead of a separately billed LLM API key. See [GitHub Copilot SDK provider](#github-copilot-sdk-provider).

> **Supported LLM providers:** OpenRouter, Requesty, OpenAI, Anthropic (native Messages API), DeepSeek, Gemini, Groq, DashScope/Qwen, Zhipu, Moonshot/Kimi, MiniMax, SiliconFlow (CN + Global), Xiaomi MIMO, Novita AI, iFlytek Spark, Z.ai, NVIDIA NIM, ModelScope, GitHub Copilot, Ollama (local). When no `*_BASE_URL` is set, each provider falls back to its canonical endpoint, so just a key is enough. See `.env.example` for config.

> **Tip:** All markets work without any API keys thanks to automatic fallback. yfinance/Yahoo (HK/US/Canada), OKX (crypto), mootdx (A-shares, TCP-direct, no IP throttle), and AKShare (A-shares, US, HK, futures, forex) are all free. Tushare token is optional — mootdx is the preferred no-token A-share fallback, with AKShare as a broader backup.

## tools

docker compose up --build
```

Open `http://localhost:8899`. Backend + frontend in one container.

> [!NOTE]
> **OpenAI Codex OAuth with Docker:** the browser login needs a terminal so you
> can paste the callback URL. Run it through Compose, which allocates an
> interactive terminal automatically:
>
> ```bash
> docker compose exec vibe-trading vibe-trading provider login openai-codex
> ```
>
> If you use `docker exec` directly, pass `-it` before the container name.

Docker publishes the backend on `127.0.0.1:8899` by default and runs the app as a non-root container user. If you intentionally expose the API beyond your own machine, set a strong `API_AUTH_KEY` and send `Authorization: Bearer <key>` from clients.

> [!NOTE]
> **Using Ollama with Docker:** the container reaches a host-side Ollama via `host.docker.internal`, not `localhost` (inside the container `localhost` is the container itself). `docker-compose.yml` defaults `OLLAMA_BASE_URL` to `http://host.docker.internal:11434`; export `OLLAMA_BASE_URL` (or set it in a top-level `.env`) to point elsewhere. This relies on the `host-gateway` mapping in `extra_hosts`, which requires **Docker Engine ≥ 20.10 / Compose v2** (provided automatically on Docker Desktop).

Your data survives updates: persistent memory, the cross-session search index, user-created skills, shadow accounts, broker connector config, web sessions, backtest runs, swarm history, and uploads all live in named Docker volumes, so `git pull && docker compose up --build` keeps them. They are deleted only by `docker compose down -v`.

## configuration

Copy `agent/.env.example` to `agent/.env` and uncomment the provider block you want. Each provider needs 3-4 variables:

| Variable | Required | Description |
|----------|:--------:|-------------|
| `LANGCHAIN_PROVIDER` | Yes | Provider name (`openrouter`, `deepseek`, `groq`, `ollama`, etc.) |
| `<PROVIDER>_API_KEY` | Yes* | API key (`OPENROUTER_API_KEY`, `DEEPSEEK_API_KEY`, etc.) |
| `<PROVIDER>_BASE_URL` | Yes | API endpoint URL |
| `LANGCHAIN_MODEL_NAME` | Yes | Model name (e.g. `deepseek-v4-pro`) |
| `LANGCHAIN_REASONING_EFFORT` | No | Reasoning effort (`none`, `low`, `medium`, `high`, or `max`) |
| `LANGCHAIN_USE_RESPONSES_API` | No | Responses transport override: literal `true` uses `/v1/responses` when the endpoint supports it; native adapters retain their own transport; all other values use Chat Completions |
| `TUSHARE_TOKEN` | No | Tushare Pro token for A-share data (falls back to AKShare) |
| `TIMEOUT_SECONDS` | No | LLM call timeout, default 120s |
| `API_AUTH_KEY` | Recommended for network deployments | Bearer token required when the API is reachable from non-local clients |
| `VIBE_TRADING_ENABLE_SHELL_TOOLS` | No | Explicit opt-in for shell-capable tools in remote API/MCP-SSE style deployments |
| `VIBE_TRADING_ALLOWED_FILE_ROOTS` | No | Extra comma-separated roots for document and broker-journal imports |
| `VIBE_TRADING_ALLOWED_RUN_ROOTS` | No | Extra comma-separated roots for generated-code run directories |
| `VIBE_TW_STOCK_DB` | No | Path to a Taiwan-market SQLite snapshot; the read-only `taiwan_stock_data` tool registers only when it is schema-valid |
| `VIBE_TRADING_EXTRA_CORS_ORIGINS` | No | Comma-separated origins **added** to the loopback CORS defaults (`CORS_ORIGINS` replaces them instead) |
| `CONTENT_FILTER_WARNING_THRESHOLD` | No | Content-filter warning ratio threshold (default 0.05 = 5%). When the ratio of LLM responses blocked by content moderation exceeds this, the run card warns you to switch providers. |

<sub>* Ollama does not require an API key. OpenAI Codex uses ChatGPT OAuth and stores tokens via `oauth-cli-kit`, not in `agent/.env`. GitHub Copilot authentication is handled by the official SDK.</sub>

**Free data (no key needed):** A-shares via AKShare, HK/US/Canada equities via Yahoo/yfinance, crypto via OKX, 100+ crypto exchanges via CCXT. The system automatically selects the best available source for each market.

## limitations

> We ship in phases. Items move to [Issues](https://github.com/HKUDS/Vibe-Trading/issues) when work begins.

| Phase | Feature | Status |
|-------|---------|--------|
| **Trust Layer** | Reproducible run cards are emitted and shown in Run Detail; v1 adds tool traces and citations | v0 Shipped |
| **Hypothesis Registry** | Durable research hypotheses with lifecycle status, data sources, skills, run-card links, and invalidation notes | Backend MVP Shipped |
| **Research Autopilot** | Manual-first research loop: hypothesis → deterministic backtest → evidence report | Phase 1–3 Shipped |
| **Data Bridge** | Bring-your-own data: local CSV/Parquet/SQL connectors with schema mapping | Local loader Shipped |
| **Options Lab** | Vol surface, Greeks dashboard, payoff/scenario explorer | Analytic payoff/scenario tool **Shipped**; surface/dashboard Planned |
| **Portfolio Studio** | Risk x-ray, constraints, turnover-aware optimizer, rebalance notes | Turnover-aware optimizer **Shipped 0.1.11**; rest Planned |
| **Alpha Zoo** | 462 pre-built alphas (Qlib 158 + Kakushadze 101 + GTJA 191 + academic + fundamental) with one-line bench, agent integration, and Web UI | **Shipped 0.1.8**, extended through 0.1.12 |
| **Strategy Development Manager** | Register papers / broker research as factors & strategies with a persistent store + automated IC/Sharpe decay lifecycle | **Shipped 0.1.11** |
| **Correlation Regime** | Edge-density + hysteresis regime timeline layered on `/correlation` — spot when markets fuse into one bloc | **Shipped 0.1.12** |
| **Research Delivery** | Scheduled briefs and live research sessions through Slack / Telegram / email-style IM channels | Scheduler + IM Runtime Shipped |
| **Community** | Shareable skills, presets, and strategy cards | Exploring |

---
