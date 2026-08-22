# AlexsJones/llmfit

Hundreds of models & providers. One command to find what runs on your hardware.

## installation

### Windows
```sh
scoop install llmfit
```

If Scoop is not installed, follow the [Scoop installation guide](https://scoop.sh/).

### macOS / Linux

#### Homebrew

Prebuilt binary (recommended, works on all macOS/Linux versions):
```sh
brew install AlexsJones/llmfit/llmfit
```

Or from the homebrew-core formula, which builds from source on macOS versions without a bottle:
```sh
brew install llmfit
```

#### MacPorts
```sh
port install llmfit
```

#### Quick install
```sh
curl -fsSL https://llmfit.axjns.dev/install.sh | sh
```

Downloads the latest release binary from GitHub and installs it to `/usr/local/bin` (or `~/.local/bin` if no sudo).

**Install to `~/.local/bin` without sudo:**
```sh
curl -fsSL https://llmfit.axjns.dev/install.sh | sh -s -- --local
```

### uv / pip
To install or update llmfit:
```sh
uv tool install -U llmfit
```

To run without installing:
```sh
uvx llmfit
```

You can also install llmfit as a Python package in the normal way with tools such as pip or uv.

### Docker / Podman
```sh
docker run ghcr.io/alexsjones/llmfit
```
This prints JSON from `llmfit recommend` command. The JSON could be further queried with `jq`.
```
podman run ghcr.io/alexsjones/llmfit recommend --use-case coding | jq '.models[].name'
```
To launch the interactive TUI instead, pass the global `--tui` flag:
```sh
docker run --rm -it ghcr.io/alexsjones/llmfit --tui
```

### From source
```sh
git clone https://github.com/AlexsJones/llmfit.git
cd llmfit
cargo build --release
# binary is at target/release/llmfit
```

---

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

## How it works

llmfit detects your hardware (RAM, CPU, GPU/VRAM, backend), then scores every model in its catalog across four dimensions: memory fit, estimated speed, quality, and context. Speed estimates come from a memory-bandwidth model grounded in runtime sampling and real community measurements — and every estimate ships its inputs, so `llmfit info` shows exactly what a number assumes and how to verify it on your machine.

Full detail, including the estimation formulas and the model database: [How llmfit works](docs/how-it-works.md).

---

## Contributing

Contributions are welcome, especially new models.

### Before submitting a PR

Please run `cargo fmt` before pushing your changes. Most CI check failures are caused by unformatted code:

```sh
cargo fmt
```

Guides for adding models — locally (no rebuild) or to the built-in catalog: [Custom models](docs/custom-models.md).

---

## Alternatives

If you're looking for a different approach, check out [llm-checker](https://github.com/Pavelevich/llm-checker) -- a Node.js CLI tool with Ollama integration that can pull and benchmark models directly. It takes a more hands-on approach by actually running models on your hardware via Ollama, rather than estimating from specs. Good if you already have Ollama installed and want to test real-world performance. Note that it doesn't support MoE (Mixture-of-Experts) architectures -- all models are treated as dense, so memory estimates for models like Mixtral or DeepSeek-V3 will reflect total parameter count rather than the smaller active subset.

---

## Code signing

llmfit's Windows release binaries are digitally signed (Authenticode) via [SignPath.io](https://about.signpath.io/), with a free code signing certificate provided by the [SignPath Foundation](https://signpath.org/).

Signing happens automatically in the [release pipeline](.github/workflows/release.yml): only artifacts built by GitHub Actions from this repository are submitted for signing, and signing requests are approved by the project maintainer ([@AlexsJones](https://github.com/AlexsJones)).

**Code signing policy:** see the [SignPath Foundation code signing policy and terms](https://signpath.org/terms).

**Privacy:** this program will not transfer any information to other networked systems unless specifically requested by the user or the person installing or operating it. llmfit only contacts external services when you explicitly use the corresponding feature (e.g. model downloads, runtime provider queries, or the community leaderboard).

---

## License

MIT
