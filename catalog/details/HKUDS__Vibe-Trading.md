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

## 💡 What Is Vibe-Trading?

Vibe-Trading is an open-source research workspace for turning finance questions into runnable analysis. It connects natural-language prompts to market-data loaders, strategy generation, backtest engines, reports, exports, and persistent research memory.

It is designed for research, simulation, and backtesting — and, when you choose, autonomous trading through a broker you authorize yourself (e.g. Robinhood Agentic Trading). It holds no funds and never trades outside the limits you set, and you can halt it instantly.

---

## ✨ What You Can Do

| Task | Output |
|------|--------|
| **Ask a trading question** | Market research with tools, data, documents, and reusable session context. |
| **Backtest a strategy idea** | Strategy code, metrics, benchmark context, validation artifacts, and run cards. |
| **Review your own trades** | Broker-journal parsing, behavior diagnostics, rule extraction, and Shadow Account comparisons. |
| **Read documents & charts** | Parse PDF / DOCX / XLSX / PPTX / images with pluggable OCR (`read_document`), and read chart screenshots semantically with a vision model (`analyze_image`). |
| **Read institutional filings & fund books** | SEC 13F manager books with quarter-over-quarter position diffs, ETF constituents across markets, event-contract implied probability, and arXiv / OpenAlex factor extraction — all read-only, on free public sources. |
| **Improve repeated research** | Persistent memory and editable skills turn useful routines into reusable workflows. |
| **Run analyst teams** | Multi-agent research reviews for investment, quant, crypto, macro, and risk workflows. |
| **Put research into IM channels** | Run the same session runtime through WebSocket, Telegram, Slack, Discord, Matrix, WhatsApp, Signal, QQ/NapCat, WeChat/WeCom, Feishu/Lark, DingTalk, Teams, email, and Mochat with CLI, REST, and Web UI controls. |
| **Ship usable artifacts** | Reports, TradingView Pine Script, TDX, MetaTrader 5, MCP tools, and later research sessions. |
| **Bench a pre-built alpha zoo** | One-line IC + alive/reversed/dead categorisation across 462 alphas (Qlib 158 + Kakushadze 101 + GTJA 191 + academic + PIT-safe funda

## installation

### One-line install (PyPI)

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

### Or choose a path

| Path | Best for | Time |
|------|----------|------|
| **A. Docker** | Try it now, zero local setup | 2 min |
| **B. Local install** | Development, full CLI access | 5 min |
| **C. MCP plugin** | Plug into your existing agent | 3 min |
| **D. ClawHub** | One command, no cloning | 1 min |

## requirements

- An **LLM API key** from any supported provider — or run locally with **Ollama** (no key needed)
- **Python 3.11+** for Path B
- **Docker** for Path A
- OpenAI Codex can also be used with ChatGPT OAuth: set `LANGCHAIN_PROVIDER=openai-codex`, then run `vibe-trading provider login openai-codex`. This does not use `OPENAI_API_KEY`.
- GitHub Copilot can be used with an active Copilot subscription instead of a separately billed LLM API key. See [GitHub Copilot SDK provider](#github-copilot-sdk-provider).

> **Supported LLM providers:** OpenRouter, Requesty, OpenAI, Anthropic (native Messages API), DeepSeek, Gemini, Groq, DashScope/Qwen, Zhipu, Moonshot/Kimi, MiniMax, SiliconFlow (CN + Global), Xiaomi MIMO, Novita AI, iFlytek Spark, Z.ai, NVIDIA NIM, ModelScope, GitHub Copilot, Ollama (local). When no `*_BASE_URL` is set, each provider falls back to its canonical endpoint, so just a key is enough. See `.env.example` for config.

> **Tip:** All markets work without any API keys thanks to automatic fallback. yfinance/Yahoo (HK/US/Canada), OKX (crypto), mootdx (A-shares, TCP-direct, no IP throttle), and AKShare (A-shares, US, HK, futures, forex) are all free. Tushare token is optional — mootdx is the preferred no-token A-share fallback, with AKShare as a broader backup.

### GitHub Copilot SDK provider

The official GitHub Copilot SDK ships as an optional extra, so install it alongside Vibe-Trading with `pip install "vibe-trading-ai[copilot]"`; installing the Copilot CLI is optional. Authenticate with any one of these supported methods:

```bash
gh auth login                         # use GitHub CLI credentials
# or run `copilot` and sign in         # stores credentials in the OS keychain
# or export COPILOT_GITHUB_TOKEN=gho_xxx
```

Then configure `agent/.env`:

```dotenv
LANGCHAIN_PROVIDER=copilot
LANGCHAIN_MODEL_NAME=claude-sonnet-5
# COPILOT_GITHUB_TOKEN=gho_xxx         # optional; recommended for Docker/CI
```

Start Vibe-Trading normally. Its preflight reports whether the SDK can authenticate:

```bash
vibe-trading
```

Authentication priority is `COPILOT_GITHUB_TOKEN`, `GH_TOKEN`, `GITHUB_TOKEN`, stored Copilot CLI credentials, then `gh` credentials. Vibe-Trading does not copy or persist SDK credentials. Host keychain credentials are not automatically available inside Docker, so containers should receive `COPILOT_GITHUB_TOKEN`.

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

### 🎯 Recommended Models

Vibe-Trading is a tool-heavy agent — skills, backtests, memory, and swarms all flow through tool calls. Model choice directly decides whether the agent *uses* its tools or fabricates answers from training data.

| Tier | Examples | When to use |
|------|----------|-------------|
| **Best** | `anthropic/claude-opus-4.7`, `anthropic/claude-sonnet-4.6`, `openai/gpt-5.5-pro`, `google/gemini-3.5-flash` | Complex swarms (3+ agents), long research sessions, paper-grade analysis |
| **Sweet spot** (default) | `deepseek-v4-pro`, `deepseek/deepseek-v4-pro`, `x-ai/grok-4.20`, `z-ai/glm-5.1`, `moonshotai/kimi-k2.6`, `qwen/qwen3-max-thinking` | Daily driver — reliable tool-calling at ~1/10 the cost |
| **Avoid for agent use** | `*-nano`, `*-flash-lite`, `*-coder-next`, small / distilled variants | Tool-calling is unreliable — the agent will appear to "answer from memory" instead of loading skills or running backtests |

The default `agent/.env.example` ships with DeepSeek official API + `deepseek-v4-pro`; OpenRouter users can use `deepseek/deepseek-v4-pro`.

---

## 🖥 CLI Reference

The interactive TUI (`vibe-trading`) now uses a terminal-native transcript: a startup banner, prompt rule, previous-turn recap, live activity rail, Markdown/table rendering, and run timing all stay in the CLI. Non-interactive invocations such as `vibe-trading run`, pipes, and `--json` remain script-friendly.

```bash
vibe-trading               # interactive TUI
vibe-trading run -p "..."  # single run
vibe-trading serve         # API server
vibe-trading alpha list    # browse 462 pre-b

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

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Good first issues** are tagged with [`good first issue`](https://github.com/HKUDS/Vibe-Trading/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) — pick one and get started.

Want to contribute something bigger? Check the [Roadmap](#-roadmap) above and open an issue to discuss before starting.

---

## Contributors

Thanks to everyone who has contributed to Vibe-Trading!

Recent v0.1.14 cycle contributors and credits:

- @Shizoqua — a 13-PR correctness sweep across nearly every subsystem: grounding auto-recovers identity and price evidence within a bounded budget (#1092), swarm isolates worker artifacts between retries (#1053), rejects raw `ok`/`success` tool-result envelopes (#1052) and truncates oversized results with the shared notice (#1110), MCP gains offset paging for SEC filings and statements (#1138), routes `load_skill` through the registry so oversized skills page (#1137) and carries market-data provenance on `get_market_data` (#1131), plus `excess_return` consistency (#1058), Wilder-EWM RSI (#1056), the FTS5 tokenizer floor (#1071), non-finite prediction-market fields (#1136), in-flight delivery protection (#1140) and preserved backtest validation evidence (#1139)
- @shadowinlife — the run-analysis surface, four pages in one cycle: Options Lab (#1096), the Factor Research panel with its new IC correlation matrix (#1099), positions structure visualization (#1097) and the tearsheet tab (#1091); plus evidence-gated Strategy Discovery Phase 1 (#978) and Phase 2 decay monitoring (#1007), per-market volume units in market-data provenance (#1065) and baostock volume normalized to board lots (#1067)
- @pengpengyi92 — five quantlib numerics fixes: `xirr` and money-weighted return survive long-horizon discount underflow (#1119), zero-volatility options discount their forward value (#1066), the fixed-income curve keeps decay inside the requested bounds (#1076), event studies anchor to the prior session (#1078) and cross-validation aligns label ends to the prior observation (#1079)
- @cgycorey — reasoning effort honoured in chat completions (#1025), the per-task
