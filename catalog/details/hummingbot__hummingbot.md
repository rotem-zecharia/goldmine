# hummingbot/hummingbot

Open source software that helps you create and deploy high-frequency crypto trading bots

## installation

### Condor (AI harness)

**[Condor](https://github.com/hummingbot/condor)** is the AI harness for building and running agentic strategies and bot instances. It connects LLM-powered decision-making to deterministic trade execution via the Hummingbot API, controlled through Telegram or its web dashboard. See **[condor.hummingbot.org](https://condor.hummingbot.org/)** to get started.

### `hbot` CLI

The recommended way to run the Hummingbot client directly is the **`hbot` command-line interface**, installed from
source. `hbot` runs, controls, and monitors a trading bot non-interactively: start/stop a bot, author
and tune configs, and read trades, PnL, logs, and status — all scriptable, as compact Markdown with
stable exit codes. See the **[hbot CLI guide](hummingbot/cli/README.md)** for the full reference.

Requires [Anaconda or Miniconda](https://www.anaconda.com/download).

```bash
# Clone the repository
git clone https://github.com/hummingbot/hummingbot.git
cd hummingbot

## configuration

make install

# Activate the environment
conda activate hummingbot
hbot --help
```

To use `hbot` outside the conda environment, run `make link-cli` to add it to your host PATH.

On first use, `hbot` prompts for a keystore password that encrypts your exchange API keys — set `HBOT_PASSWORD` or pass `--password-stdin` to run non-interactively (e.g. in scripts or agent workflows).

Then create a config and run the `simple_pmm` **paper trading script** — it simulates trading against live Binance market data, so no API keys are required:

```bash
hbot create simple_pmm --name conf_paper_bot.yml \
     --set exchange=binance_paper_trade --set trading_pair=BTC-USDT
hbot start conf_paper_bot.yml                          # run it (one bot per install)
hbot status                                            # check on it
hbot stop                                              # stop gracefully
```

To trade **live**, connect your exchange API keys and run a **strategy controller** like `pmm_mister` — a reusable V2 strategy whose settings can be tuned live while the bot runs:

```bash
hbot connect binance                                   # store API keys (encrypted)
hbot create pmm_mister --name conf_my_bot.yml \
     --set connector_name=binance --set trading_pair=BTC-USDT --set total_amount_quote=100
hbot start conf_my_bot.yml                             # run it (one bot per install)
```

Full command reference and ontology: **[hbot CLI guide](hummingbot/cli/README.md)**.

### Docker

Prefer containers? `hbot` works the same way — install [Docker Compose](https://docs.docker.com/compose/install/), then:

```bash
git clone https://github.com/hummingbot/hummingbot.git
cd hummingbot
make setup            # answer `y` to "Include Gateway?" to add the DEX middleware
make deploy           # start the container (interactive client by default)
make link-cli         # put the `hbot` command on your host PATH (dispatches into the container)

hbot --help           # same commands as the source install above
```

`make link-cli` installs a small wrapper that runs `hbot` inside the container, so every command
above is identical whether you installed from source or Docker. (Or skip it and use
`docker exec -it hummingbot hbot <command>`.) To dedicate the container to `hbot` instead of the
interactive client, uncomment `command: tail -f /dev/null` in `docker-compose.yml` before
`make deploy` — see [Running in Docker](hummingbot/cli/README.md#running-in-docker).

### Interactive Client (TUI)

The classic full-screen client is the Docker default:
`make deploy`, then `docker attach hummingbot` — or run it from source with
`make install && make run`. With Gateway included it starts in development mode
(unencrypted HTTP); for production HTTPS use the `DEV=false` flag and run `gateway generate-certs`.
See [Development vs Production Modes](https://hummingbot.org/gateway/installation/#development-vs-production-modes).

---

For comprehensive installation instructions and troubleshooting, visit our [Installation](https://hummingbot.org/installation/) documentation.

## Strategies

Hummingbot offers several frameworks for building and running algorithmic trading strategies — see the [Strategies docs](https://hummingbot.org/strategies/) for a full overview:

* **[Scripts](./scripts)**: Single-file Python strategies — the easiest way to build and customize your own bot. Example: [`simple_pmm.py`](./scripts/simple_pmm.py), a basic market making script.
* **[Controllers](./controllers)**: Reusable V2 strategies whose configs can be backtested, deployed, and tuned live while running. Example: [`pmm_mister.py`](./controllers/generic/pmm_mister.py), a full-featured market making controller.
* **[Executors](./hummingbot/strategy_v2/executors)**: Self-contained building blocks that manage order lifecycles for common patterns — position, DCA, grid, arbitrage, XEMM, TWAP, and LP. Example: [`position_executor`](./hummingbot/strategy_v2/executors/position_executor), which m
