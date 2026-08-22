# nicobailon/surf-cli

The CLI for AI agents to control Chrome. Zero config, agent-agnostic, battle-tested.

## features

Browser automation for AI agents is harder than it looks. Most tools require complex setup, tie you to specific AI providers, or break on real-world pages.

Surf takes a different approach:

**Agent-Agnostic** - Pure CLI commands over Unix socket. Works with Claude Code, GPT, Gemini, Cursor, custom agents, shell scripts - anything that can run commands.

**Zero Config** - Install the extension, run commands. No MCP servers to configure, no relay processes, no subscriptions.

**Battle-Tested** - Built by reverse-engineering production browser extensions and methodically working through agent-hostile pages like Discord settings. Falls back gracefully when CDP fails.

**Smart Defaults** - Screenshots auto-resize to 1200px (saves tokens). Actions auto-capture screenshots (saves round-trips). Errors on restricted pages warn instead of fail.

**AI Without API Keys** - Query ChatGPT, Gemini, Perplexity, and Grok using your existing browser logins. No API keys needed.

**Network Capture** - Automatically logs all network requests while active. Filter, search, and replay API calls without manually setting up request interception.

## Comparison

| Feature | Surf | Manus | Claude Extension | DevTools MCP | dev-browser |
|---------|------|-------|------------------|--------------|-------------|
| Agent-agnostic | Yes | No (Manus only) | No (Claude only) | Partial | No (Claude skill) |
| Zero config | Yes | No (subscription) | No (subscription) | No (MCP setup) | No (relay server) |
| Self-hosted (local or Tailnet) | Yes | No (cloud) | Partial | Yes | Partial |
| CLI interface | Yes | No | No | No | No |
| Free | Yes | No | No | Yes | Yes |
| AI via browser cookies | Yes | No | No | No | No |

## installation

### Quick Start

```bash
# 1. Install globally
npm install -g surf-cli

# 2. Load extension in Chrome
#    - Open chrome://extensions
#    - Enable "Developer mode"
#    - Click "Load unpacked"
#    - Paste the path from: surf extension-path

# 3. Install native host (copy extension ID from chrome://extensions)
surf install <extension-id>

# 4. Restart Chrome and test
surf tab.list
```

### Multi-Browser Support

```bash
surf install <extension-id>                    # Chrome (default)
surf install <extension-id> --browser brave    # Brave
surf install <extension-id> --browser helium   # Helium
surf install <extension-id> --browser all      # All supported browsers
surf install <extension-id> --target linux     # WSLg/Linux browser from WSL2
```

Supported: `chrome`, `chromium`, `brave`, `edge`, `arc`, `helium`

**WSL2 with Windows Chrome**
When you run `surf install <extension-id>` inside WSL2, Surf detects WSL2 and installs a Windows-side native messaging manifest for Windows Chrome/Brave/Edge by default. The generated Windows wrapper launches the WSL2 host with `wsl.exe`, so `surf` commands run inside WSL2 still connect to the WSL socket.

If you use a Linux browser inside WSLg instead, install with:
```bash
surf install <extension-id> --target linux
```

Restart Windows Chrome after installing. If the extension reports `Access to the specified native messaging host is forbidden`, rerun `surf install <extension-id>` from the same WSL distro and confirm the extension ID was copied from `chrome://extensions`.

**Package Manager Installs (Nix, Homebrew, etc.)**
If surf is installed via a package manager that stores binaries in non-standard locations, set these environment variables before running `surf install`:
```bash
export SURF_NODE_PATH=/path/to/node
export SURF_HOST_PATH=/path/to/native/host.cjs
export SURF_EXTENSION_PATH=/path/to/extension/dist
```
See [Environment Variables](#environment-variables) for details.

### Uninstall

```bash
surf uninstall                  # Chrome only
surf uninstall --all            # All browsers + wrapper files
surf uninstall --target linux   # Remove WSLg/Linux-browser config from WSL2
```

### Remote Surf over Tailscale

Remote Surf runs the browser and native host on one Tailnet machine while the CLI runs on another. The listener is available only while the browser extension's native-messaging connection is alive. Tailnet reachability is not authorization: every remote client also needs its own Surf credential.

On the browser host, authorize a client before installing the listener:

```bash
surf remote authorize agent-macbook --output ~/agent-macbook.surf-credential.json
surf remote list
surf install <extension-id> --listen 100.101.102.103:4321
```

`authorize` creates a mode-0600 credential containing the client's Ed25519 private identity and the pinned host identity. Move it to that client through an existing secure channel, then remove the generated copy from the host if it is no longer needed there. The host keeps only the client's public identity in `~/.surf/remote/remote-clients.json`.

From the authorized client:

```bash
surf --remote 100.101.102.103:4321 \
  --remote-credential ~/.config/surf/agent-macbook.json \
  tab.list

## configuration

SURF_REMOTE=100.101.102.103:4321 \
SURF_REMOTE_CREDENTIAL=~/.config/surf/agent-macbook.json \
  surf tab.list
```

Surf performs mutual Ed25519 challenge-response with fresh nonces and checks authorization throughout the connection. A credential grants the same browser and host-file authority as a trusted local Surf user. Give each client its own credential, do not share it, and revoke it immediately if the client or file is lost:

```bash
surf remote revoke agent-macbook
surf remote list
```

`--remote <host>:<port>` takes precedence over `SURF_REMOTE`; `--remote-credential` takes precedence over `SURF_REMOTE_CREDENTIAL`. A selected remote endpoint overrides `SURF_SOCKET` and the default local socket. Local and remote requests share the same host scheduler: each tab has a FIFO lane, different tabs may execute concurrently, and browser-wide writers are exclusive. Disconnects and timeouts abort queued or in-flight work and retain admission until request-owned cleanup drains or the hard deadline is reached. Browser side effects that already completed are not rolled back.

`surf install --listen` persists the explicit Tailnet address in the native-host wrapper. Re-run `surf install` without `--listen` to remove it. The address must be a Tailscale IPv4 or IPv6 address with a port; Surf does not bind every interface. Remote listeners currently require a POSIX browser host and are not supported by Windows native-host wrappers.

Keep Tailscale policy restrictions as defense in depth. For example:

```json
{
  "acls": [
    {
      "action": "accept",
      "src": ["tag:surf-agent"],
      "dst": ["tag:surf-browser:4321"]
    }
  ]
}
```

Adapt tags and ports to your Tailnet. Surf authentication does not replace Tailnet policy, and Surf does not add a separate TLS or SSH tunnel.

**Operations and troubleshooting**

```bash
tailscale status
tailscale ping 100.101.102.103
surf doctor --remote 100.101.102.103:4321 \
  --remote-credential ~/.config/surf/agent-macbook.json
```

Use `tailscale status` and `tailscale ping` to confirm reachability, then use `doctor` to verify endpoint selection and authentication.

**Remote filesystem and transfer semantics**

Unprefixed paths and `local:` paths refer to the client. Only `remote:/absolute/path` refers directly to the browser host. For example:

```bash
surf --remote "$SURF_REMOTE" --remote-credential "$SURF_REMOTE_CREDENTIAL" \
  upload --ref e5 --files ./client-file.pdf
surf --remote "$SURF_REMOTE" --remote-credential "$SURF_REMOTE_CREDENTIAL" \
  screenshot --output local:./shot.png
surf --remote "$SURF_REMOTE" --remote-credential "$SURF_REMOTE_CREDENTIAL" \
  network.export --output remote:/var/tmp/network.har --har
```

Client-local inputs are staged privately on the host and removed after the request. Client-local outputs are downloaded with size/hash verification and atomic destination replacement. `surf js --file` and `perf-audit --output` are handled by the client itself. `network.export` defaults to a generated client-local `.json`, `.jsonl`, or `.har` path. Gemini edits default to client-local `edited.png`. Successful remote actions transfer their automatic screenshot to a generated client-local path; `--auto-capture` on failure remains a separate screenshot and console diagnostic.

The remote single-file boundary supports one `upload` file, one ChatGPT attachment, or one Gemini attachment/edit input, plus one screenshot, network export, or Gemini image output. Transfers are limited to 256 MiB per file, 512 MiB and 32 files per connection, with 256 KiB decoded chunks. Remote `record`, `aistudio.build`, smoke screenshot directories, directory transfer, and multi-file inputs are intentionally rejected. A `remote:` path bypasses transfer and gives the trusted client direct authority over that absolute host path.

## tools

```bash
surf <command> [args] [options]
surf --help                    # Basic help
surf --llm-context             # Compact reference for AI agents
surf --help-full               # All 50+ commands
surf <command> --help          # Command details
surf --find <query>            # Search commands
```

### Navigation

```bash
surf go "https://example.com"
surf back
surf forward
surf tab.reload --hard
```

### Reading Pages

```bash
surf read                           # Accessibility tree + visible text content
surf read --no-text                 # Accessibility tree only (no text)
surf read --depth 3                 # Limit tree depth (smaller output)
surf read --compact                 # Remove empty structural elements
surf read --depth 3 --compact       # Both (60% smaller output)
surf read --max-bytes 2000          # Cap visible text on a UTF-8 byte boundary
surf page.text                      # Raw text content only
surf page.html                      # Rendered document HTML
surf page.html --strip-scripts > artifact.html # Save a safe static Claude artifact
surf page.save --selector "#artifact" --strip-scripts --output artifact.html # Save one rendered element
surf page.state                     # Modals, loading state, scroll position
```

Use `surf page.html --strip-scripts` after the page loads when you need a static export of a Claude artifact or other rendered DOM. Use `--selector <css>` to export one element. Both commands target the active frame when `frame.switch` is active.

Element refs (`e1`, `e2`, `e3`...) are stable identifiers from the accessibility tree - semantic, predictable, and resilient to DOM changes.

### Semantic Locators

Find and interact with elements by role, text, or label - no refs or selectors needed:

```bash
# By ARIA role
surf locate.role button --name "Submit"           # Find button
surf locate.role button --name "Submit" --action click  # Find and click
surf locate.role textbox --action fill --value "hello"  # Find and fill
surf locate.role link --all                       # List all links

# By text content  
surf locate.text "Sign In" --action click         # Click element with text
surf locate.text "Accept" --exact                 # Exact match only

# By form label
surf locate.label "Email" --action fill --value "test@example.com"
```

### Iframe Support

Work with content inside iframes:

```bash
surf frame.list                     # List all frames
surf frame.switch --index 0         # Switch to first iframe
surf frame.switch --name "payment"  # Switch by frame name
surf frame.switch --selector "#checkout-frame"  # Switch by CSS selector

# Now all commands target the iframe
surf read                           # Read iframe content
surf click e5                       # Click in iframe
surf type "4242" --into "#card-number"
surf locate.role button --action click

surf frame.main                     # Return to main page
```

### Interaction

```bash
surf click e5                       # Click by element ref
surf click --selector ".btn"        # Click by CSS selector
surf click 100 200                  # Click by coordinates
surf type "hello" --submit          # Type at the current focus with CDP events
surf type "email@example.com" --ref e12  # Fill an element from page.read
surf type "hello" --into "#message"     # Fill a selector in the active frame
surf key Escape                     # Press key
surf scroll down 800                # Scroll down 800px
surf scroll bottom                  # Scroll to bottom
surf scroll.bottom                  # Dot command form also works
```

### Forms

Select options in dropdown menus:

```bash
surf select e5 "US"                         # Select by value
surf select "#country" "US"                 # Select by CSS selector
surf select e5 "opt1" "opt2"                # Multi-select
surf select e5 --by label "United States"   # Select by visible text
surf select e5 --by index 0                 # Select first option
```

### Element Inspection

Get c

## limitations

- Cannot automate `chrome://` pages or the Chrome Web Store (Chrome restriction)
- First CDP operation on a new tab takes ~100-500ms (debugger attachment)
- Some operations on restricted pages return warnings instead of results

## Linux Support (Experimental)

Surf should work on Linux with Chromium. Not yet tested in production.

```bash
