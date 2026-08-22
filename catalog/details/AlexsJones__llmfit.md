# AlexsJones/llmfit

Hundreds of models & providers. One command to find what runs on your hardware.

## tools

```sh
llmfit          # interactive TUI: your hardware, every model, ranked
```

The TUI shows your detected specs at the top and every model scored for fit, speed, quality, and context. See the [TUI guide](docs/tui.md) for navigation, planning, simulation, downloads, the community leaderboard, and benchmarking.

For scripts, agents, and classic terminal output:

```sh
llmfit fit                    # table of all models ranked by fit
llmfit recommend --json       # top picks as JSON (agent/script consumption)
llmfit info "<model>"         # one model: fit analysis, estimate basis, verify commands
llmfit bench                  # measure real tok/s/TTFT against your running provider
llmfit doctor                 # hardware detection report for bug reports
```

Full reference: [CLI & automation](docs/cli.md).

---
