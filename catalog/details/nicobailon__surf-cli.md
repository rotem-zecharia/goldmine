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

## installation

```bash

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

## tools

```bash
surf <command> [args] [options]
surf --help                    # Basic help
surf --llm-context             # Compact reference for AI agents
surf --help-full               # All 50+ commands
surf <command> --help          # Command details
surf --find <query>            # Search commands
```

## limitations

- Cannot automate `chrome://` pages or the Chrome Web Store (Chrome restriction)
- First CDP operation on a new tab takes ~100-500ms (debugger attachment)
- Some operations on restricted pages return warnings instead of results
