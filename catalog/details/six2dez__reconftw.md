# six2dez/reconftw

reconFTW is a tool designed to perform automated recon on a target domain by running the best set of tools to perform scanning and finding out vulnerabilities

## features

reconFTW is packed with features to make reconnaissance thorough and efficient. Below is a detailed breakdown of its capabilities, updated to reflect the latest functionality in the script and configuration.

## installation

reconFTW supports multiple installation methods to suit different environments. Ensure you have sufficient disk space (at least 10 GB recommended) and a stable internet connection.

## tools

- `subfinder`: `~/.config/subfinder/provider-config.yaml`
- GitHub tokens: `~/Tools/.github_tokens` (one per line)
- GitLab tokens: `~/Tools/.gitlab_tokens` (one per line)
- WHOISXML: set `WHOISXML_API` in `reconftw.cfg` or env var
- ASN enumeration (`asnmap`): set `PDCP_API_KEY` in env/config (`ASN_ENUM` skips if unset)
- Slack/Discord/Telegram: configure `notify` in `~/.config/notify/provider-config.yaml`
- SSRF server: set `COLLAB_SERVER` env/cfg if used
- Blind XSS server: set `XSS_SERVER` env/cfg if used

## requirements

- Disk: 10–20 GB free recommended (toolchain + data)
- Network: stable connection during installation and updates
- OS: Linux/macOS with Bash ≥ 4
- Extras: `shellcheck` and `shfmt` (optional) for `make lint`/`make fmt`

## configuration

The `reconftw.cfg` file controls the entire execution of reconFTW. It allows fine-grained customization of:

- **Tool Paths**: Set paths for tools, resolvers, and wordlists (`tools`, `resolvers`, `fuzz_wordlist`).
- **API Keys**: Configure keys for Shodan, WHOISXML, etc. via environment variables or `secrets.cfg` (see [SECURITY.md](SECURITY.md)).
- **Scanning Modes**: Enable/disable modules (e.g., `OSINT`, `SUBDOMAINS_GENERAL`, `VULNS_GENERAL`).
- **Performance**: Adjust threads, rate limits, and timeouts (e.g., `FFUF_THREADS`, `HTTPX_RATELIMIT`).
- **Adaptive Rate Limiting**: Automatically back off on 429/503 errors (`ADAPTIVE_RATE_LIMIT`, `MIN_RATE_LIMIT`, `MAX_RATE_LIMIT`).
- **Incremental Scanning**: Only scan new findings since last run (`INCREMENTAL_MODE`).
- **Notifications**: Set up Slack, Discord, or Telegram notifications (`NOTIFY_CONFIG`).
- **Ax (formerly Axiom)**: Configure distributed scanning and resolver paths (`AXIOM_FLEET_NAME`, `AXIOM_FLEET_COUNT`, `AXIOM_RESOLVERS_PATH`).
- **AI Reporting**: Configure model/profile/format and context controls (`AI_MODEL`, `AI_REPORT_PROFILE`, `AI_REPORT_TYPE`, `AI_MAX_CHARS_PER_FILE`).
- **Advanced Web Checks**: Toggle GraphQL introspection, parameter discovery, WebSocket testing, gRPC probing, and IPv6 scanning.
- **Automation & Data**: Control quick rescan heuristics, asset logging, chunk sizes, hotlists, and debug tracing (`QUICK_RESCAN`, `ASSET_STORE`, `CHUNK_LIMIT`, `HOTLIST_TOP`, `SHOW_COMMANDS`).
- **Disk & Logging**: Pre-flight disk check (`MIN_DISK_SPACE_GB`), log rotation (`MAX_LOG_FILES`, `MAX_LOG_AGE_DAYS`), structured JSON logging (`STRUCTURED_LOGGING`).
- **Caching**: Configure cache expiry for wordlists and resolvers (`CACHE_MAX_AGE_DAYS`).
- **DNS Resolver Safety**: Missing resolver files fail fast, resolver downloads use configurable retry/timeout knobs (`RESOLVER_DOWNLOAD_*`), and DNS brute/resolve timeout defaults to disabled (`DNS_*_TIMEOUT=0`) with heartbeat progress.
- **Secrets**: Use `secrets.cfg` for local overrides or environment variables for CI/Docker (see [SECURITY.md](SECURITY.md)).

**Example Configuration**:
