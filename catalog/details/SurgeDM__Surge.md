# SurgeDM/Surge

Blazing fast TUI download manager built in Go for power users

## features

Most browsers open a single connection for a download. Surge opens multiple (up to 32), splits the file, and downloads chunks in parallel. But we take it a step further:

- **Blazing Fast:** Designed to maximize your bandwidth utilization and download files as quickly as possible.
- **Multiple Mirrors:** Download from multiple sources simultaneously. Surge distributes workers across all available mirrors and automatically handles failover.
- **Sequential Download:** Option to download files in strict order (Streaming Mode). Ideal for media files that you want to preview while downloading.
- **Daemon Architecture:** Surge runs a single background "engine." You can open 10 different terminal tabs and queue downloads; they all funnel into one efficient manager.
- **Beautiful TUI:** Built with Bubble Tea & Lipgloss, featuring customizable palettes and full theme engine support.

For a deep dive into how we make downloads faster (like work stealing and slow worker handling), check out our **[Optimization Guide](docs/OPTIMIZATIONS.md)**.

---

## installation

Surge is available on multiple platforms. Choose the method that works best for you.

| Platform / Method                  | Command / Instructions                                                           | Notes                                        |
| :--------------------------------- | :------------------------------------------------------------------------------- | :------------------------------------------- |
| **Prebuilt Binary**          | [Download from Releases](https://github.com/SurgeDM/Surge/releases/latest) | Easiest method. Just download and run.       |
| **Arch Linux (AUR)**         | `yay -S surge`                                                                 | Managed via AUR.                             |
| **macOS / Linux (Homebrew)** | `brew install SurgeDM/tap/surge`                                      | Recommended for Mac/Linux users.             |
| **Nix / NixOS**              | `nix run github:SurgeDM/Surge`                                        | Via Nix flake. NixOS config: `inputs.surge.packages.${pkgs.system}.default` |
| **Windows**         | `winget install surge-downloader.surge`<br />or<br />`scoop install surge` | Recommended for Windows users.               |
| **Dockerfile**               | [See instructions](#4-server-mode-with-docker-compose)                              | Run Surge in server mode with Docker Compose |
| **Go Install**               | `go install github.com/SurgeDM/Surge@latest`                          | Requires Go 1.25+                           |

---

## tools

Surge has two main modes: **TUI (Interactive)** and **Server (Headless)**.

For a full reference, see the **[Themes Guide](docs/THEMES.md)**, **[Settings &amp; Configuration Guide](docs/SETTINGS.md)** and the **[CLI Usage Guide](docs/USAGE.md)**.
