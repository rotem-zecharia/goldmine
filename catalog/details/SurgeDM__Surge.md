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

## Support the Project

We are just two CS students building Surge in between classes and exams. We love working on this, but maintaining a project of this scale takes time and resources. That's where you come in!

If Surge saves you time, consider supporting the development! Donations go directly toward:

- **Publishing the Extension:** Paying the Chrome Web Store fee so you can finally install the extension officially (no more sideloading!).
- **Dev Tools:** Licenses for tools like **GoReleaser Pro** to help us automate our builds.
- **Debrid Integration:** Covering subscription costs so we can test and build native Debrid support.

[**☕ Buy us a coffee**](https://www.buymeacoffee.com/surge.downloader)

_Totally optional-your stars, issues, and contributions already mean the world to us! :)_

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

### 1. Interactive TUI Mode

Just run `surge` to enter the dashboard. This is where you can visualize progress, manage the queue, and see speed graphs. If you encounter any issues, press `?` to open the bug reporting wizard. You can also press `Shift + A` or use your terminal's paste shortcut to automatically parse a copied browser 'cURL' command straight into a new download.

```bash
# Start the TUI
surge

# Start the TUI without the local HTTP API server
surge --no-server

# Start TUI with downloads queued
surge https://example.com/file1.zip https://example.com/file2.zip

# Combine URLs and batch file
surge https://example.com/file.zip --batch urls.txt
```

`--no-server` keeps the TUI fully local and skips the embedded HTTP API. CLI control commands such as `surge add`, `surge pause`, and browser-extension requests will not be able to target that instance.

### 2. Server Mode (Headless)

Great for servers, Raspberry Pis, or background processes.

```bash
# Start the server
surge server

# Start the server with a download
surge server https://url.com/file.zip

# Start with explicit API token
surge server --token <token>
```

### 3. Auto-Start Service

Surge provides an official way to manage it as a system service (daemon). This is the recommended way for servers and reproducible deployments.

```bash
