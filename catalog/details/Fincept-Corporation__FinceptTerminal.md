# Fincept-Corporation/FinceptTerminal

FinceptTerminal is a modern finance application offering advanced market analytics, investment research, and economic data tools, designed for interactive exploration and data-driven decision-making i

## installation

<!-- DOWNLOAD-TABLE-START -->
Latest release: **v4.4.1** — [View all releases](https://github.com/Fincept-Corporation/FinceptTerminal/releases/tag/v4.4.1)

| Platform | Download | Run |
|----------|----------|-----|
| **Windows x64** | [FinceptTerminal-Windows-x64-setup.exe](https://github.com/Fincept-Corporation/FinceptTerminal/releases/download/v4.4.1/FinceptTerminal-4.4.1-windows-x64-setup.exe) | Run installer → launch `FinceptTerminal.exe` |
| **Linux x64 (AppImage)** | [FinceptTerminal-Linux-x64.run](https://github.com/Fincept-Corporation/FinceptTerminal/releases/download/v4.4.1/FinceptTerminal-4.4.1-linux-x64-setup.run) | `chmod +x` → run installer |
| **Linux x64 (Debian/Ubuntu)** | [FinceptTerminal-Linux-x64.deb](https://github.com/Fincept-Corporation/FinceptTerminal/releases/download/v4.4.1/FinceptTerminal-4.4.1-linux-x64.deb) | `sudo apt install ./FinceptTerminal-*.deb` |
| **Linux x64 (Fedora/RHEL)** | [FinceptTerminal-Linux-x64.rpm](https://github.com/Fincept-Corporation/FinceptTerminal/releases/download/v4.4.1/FinceptTerminal-4.4.1-linux-x64.rpm) | `sudo dnf install ./FinceptTerminal-*.rpm` |
| **macOS Apple Silicon** | [FinceptTerminal-macOS-arm64.dmg](https://github.com/Fincept-Corporation/FinceptTerminal/releases/download/v4.4.1/FinceptTerminal-4.4.1-macos-arm64-setup.dmg) | Open DMG → drag to Applications |
<!-- DOWNLOAD-TABLE-END -->

**Build from source** — Linux/macOS: `git clone … && ./setup.sh`. Windows and manual builds, the pinned toolchain (**CMake 3.27.7 · Ninja 1.11.1 · Qt 6.8.3 · Python 3.11.9**) and troubleshooting live in **[docs/GETTING_STARTED.md](docs/GETTING_STARTED.md)**. Versions are pinned — newer or older ones are unsupported.

> Looking for the Enterprise build? It has its own signed installers for Windows, macOS and Linux, behind an Enterprise login — [get them here](https://fincept.in/enterprise).

---

## What's in the open build

- **Analytics** — DCF, portfolio optimisation, VaR/Sharpe, derivatives pricing, fixed income, alternatives, plus an 18-module QuantLib suite
- **AI** — 37 trader/investor, economic and geopolitics agents; bring your own key (OpenAI, Anthropic, Gemini, Groq, DeepSeek, OpenRouter, Ollama)
- **Data** — 100+ connectors: FRED, IMF, World Bank, DBnomics, AkShare, Polygon, Kraken, Yahoo Finance, government APIs
- **Trading** — crypto and equity feeds, paper-trading engine, 16 broker integrations
- **Automation** — visual node editor, MCP tools, AI Quant Lab (ML, factor discovery, RL)
- **Global intelligence** — maritime tracking, geopolitical analysis, relationship mapping

Native C++20 · Qt6 · embedded Python 3.11 · single binary · no Node.js, no browser runtime.

---

## How this repo is maintained

This repo **stays public and will not be deleted**. Everything already released stays released.

It now ships **one release a month** rather than continuous development, because the team's daily work is on Enterprise. Issues and pull requests are still reviewed, and fixes land on the monthly cycle. Security reports go to [support@fincept.in](mailto:support@fincept.in).

---

## Contributing

New data connectors, AI agents, analytics modules, C++ screens and documentation are all welcome.

[Contributing guide](docs/CONTRIBUTING.md) · [C++ guide](docs/CPP_CONTRIBUTOR_GUIDE.md) · [Python guide](docs/PYTHON_CONTRIBUTOR_GUIDE.md) · [Architecture](docs/ARCHITECTURE.md) · [Report a bug](https://github.com/Fincept-Corporation/FinceptTerminal/issues) · [Request a feature](https://github.com/Fincept-Corporation/FinceptTerminal/discussions)

---

## Also from Fincept

- **[Fincept Data API](https://docs.fincept.in)** — 500+ REST endpoints, 423,000+ instruments, 2,000+ sources. Free tier included with any account.
- **[Quantcept](https://quantcept.io)** — open-source, AI-powered command-line finance terminal (Apache-2.0).

---

## License

**AGPL-3.0-or-later** — full text in [LICENSE](LICENSE).

Free for personal use, learning and academic research. AGPL-3.0 is **strong copyleft,
