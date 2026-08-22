# six2dez/reconftw

reconFTW is a tool designed to perform automated recon on a target domain by running the best set of tools to perform scanning and finding out vulnerabilities

## features

reconFTW is packed with features to make reconnaissance thorough and efficient. Below is a detailed breakdown of its capabilities, updated to reflect the latest functionality in the script and configuration.

### OSINT

- **Domain Information**: WHOIS lookup for domain registration details ([whois](https://github.com/rfc1036/whois)).
- **Email and Password Leaks**: Searches for leaked emails and credentials ([emailfinder](https://github.com/Josue87/EmailFinder) and [LeakSearch](https://github.com/JoelGMSec/LeakSearch)).
- **Microsoft 365/Azure Mapping**: Identifies Microsoft 365 and Azure tenants ([msftrecon](https://github.com/Arcanum-Sec/msftrecon)).
- **Metadata Extraction**: Extracts metadata from indexed office documents ([metagoofil](https://github.com/opsdisk/metagoofil)).
- **API Leaks**: Detects exposed APIs in public sources ([porch-pirate](https://github.com/MandConsultingGroup/porch-pirate), [SwaggerSpy](https://github.com/UndeadSec/SwaggerSpy) and [postleaksNg](https://github.com/six2dez/postleaksNG)).
- **Google Dorking**: Automated Google dork queries for sensitive information ([dorks_hunter](https://github.com/six2dez/dorks_hunter) and [xnldorker](https://github.com/xnl-h4ck3r/xnldorker)).
- **GitHub Analysis**: Scans GitHub organizations for repositories and secrets with selectable engines ([enumerepo](https://github.com/trickest/enumerepo), [trufflehog](https://github.com/trufflesecurity/trufflehog), [gitleaks](https://github.com/gitleaks/gitleaks), [titus](https://github.com/praetorian-inc/titus), [noseyparker](https://github.com/praetorian-inc/noseyparker)).
- **GitHub Actions Audit (Optional)**: Audits workflow artifacts and CI/CD exposure with [gato](https://github.com/praetorian-inc/gato).
- **Third-Party Misconfigurations**: Identifies misconfigured third-party services ([misconfig-mapper](https://github.com/intigriti/misconfig-mapper)).
- **Mail Hygiene**: Reviews SPF/DMARC configuration to flag spoofing or deliverability issues.
- **Cloud Storage Enumeration**: Surveys buckets across major providers for exposure ([cloud_enum](https://github.com/initstring/cloud_enum)).
- **Spoofable Domains**: Checks for domains vulnerable to spoofing ([spoofcheck](https://github.com/MattKeeley/Spoofy)).

### Subdomains

- **Passive Enumeration**: Uses APIs and public sources for subdomain discovery ([subfinder](https://github.com/projectdiscovery/subfinder) and [github-subdomains](https://github.com/gwen001/github-subdomains)).
- **Certificate Transparency**: Queries certificate transparency logs ([crt](https://github.com/cemulus/crt)).
- **NOERROR Discovery**: Identifies subdomains with DNS NOERROR responses ([dnsx](https://github.com/projectdiscovery/dnsx), more info [here](https://www.securesystems.de/blog/enhancing-subdomain-enumeration-ents-and-noerror/)).
- **Bruteforce**: Performs DNS bruteforcing with customizable wordlists ([puredns](https://github.com/d3mondev/puredns) and custom wordlists).
- **Permutations**: Generates subdomain permutations using AI, regex and tools ([Gotator](https://github.com/Josue87/gotator) as the single permutation engine, plus [regulator](https://github.com/cramppet/regulator) and [subwiz](https://github.com/hadriansecurity/subwiz)).
- **Web Scraping**: Extracts subdomains from passive URL sources and live web metadata ([urlfinder](https://github.com/projectdiscovery/urlfinder), [waymore](https://github.com/xnl-h4ck3r/waymore), [httpx](https://github.com/projectdiscovery/httpx), [csprecon](https://github.com/edoardottt/csprecon)).
- **DNS Records**: Resolves DNS records for subdomains ([dnsx](https://github.com/projectdiscovery/dnsx)).
- **Google Analytics**: Identifies subdomains via Analytics IDs ([AnalyticsRelationships](https://github.com/Josue87/AnalyticsRelationships)).
- **TLS Handshake**: Discovers subdomains via TLS ports ([tlsx](https://github.com/projectdiscovery/tlsx)).
- **Recursive Search**: Performs recursive passive or bruteforce enumeration combined ([dsieve](http

## installation

reconFTW supports multiple installation methods to suit different environments. Ensure you have sufficient disk space (at least 10 GB recommended) and a stable internet connection.

### Quickstart

1) Clone and install

```yaml
git clone https://github.com/six2dez/reconftw
cd reconftw
./install.sh --verbose
```

2) Run a scan (full + resume)

```bash
./reconftw.sh -d example.com -r
```

3) Minimal run (passive-only footprint)

```bash
./reconftw.sh -d example.com -p
```

> Tip: re-run `./install.sh --tools` later to refresh the toolchain without reinstalling system packages.

### Local Installation (PC/VPS/VM)

1. **Prerequisites**:

   - **Golang**: Latest version (`install_golang` enabled by default in `reconftw.cfg`).
   - **System Permissions**: If not running as root, configure sudo to avoid prompts:
     ```bash
     sudo echo "${USERNAME} ALL=(ALL:ALL) NOPASSWD: ALL" | sudo tee -a /etc/sudoers.d/reconFTW
     ```

2. **Steps**:

   ```bash
   git clone https://github.com/six2dez/reconftw
   cd reconftw
   ./install.sh
   ./reconftw.sh -d target.com -r
   ```

3. **Notes**:
- The `install.sh` script installs dependencies, tools, and configures paths (`GOROOT`, `GOPATH`, `PATH`).
- Set `install_golang=false` in `reconftw.cfg` if Golang is already configured.
- For existing setups, run `./install.sh --tools` to refresh Go binaries, pipx packages, and repositories without touching system packages.
- Check the [Installation Guide](https://github.com/six2dez/reconftw/wiki/0.-Installation-Guide) for detailed instructions.

### Docker

1. **Pull the Image**:

   ```bash
   docker pull six2dez/reconftw:main
   ```

2. **Run the Container**:

   ```bash
   docker run -it --rm \
     -v "${PWD}/OutputFolder/:/reconftw/Recon/" \
     six2dez/reconftw:main -d example.com -r
   ```

   For a list of targets, bind the list file into the container and reference the in-container path:

   ```bash
   docker run -it --rm \
     -v "${PWD}/domains.txt:/reconftw/domains.txt:ro" \
     -v "${PWD}/OutputFolder/:/reconftw/Recon/" \
     six2dez/reconftw:main -l /reconftw/domains.txt -r
   ```

3. **View Results**:

   - Results are saved in the `OutputFolder` directory on the host (not inside the container).

4. **Customization**:
   - Modify the Docker image or build your own; see the [Docker Guide](https://github.com/six2dez/reconftw/wiki/4.-Docker).
   - To skip Ax tooling in custom builds, pass `--build-arg INSTALL_AXIOM=false`.
   - Mount your notify config at `~/.config/notify/provider-config.yaml` inside the container if you use notifications.

5. **Secrets at Runtime**:

   Pass API keys and secrets via environment variables — never bake them into the image:

   ```bash
   docker run -it --rm \
     -e SHODAN_API_KEY="your-key" \
     -e PDCP_API_KEY="your-projectdiscovery-key" \
     -e COLLAB_SERVER="your-server" \
     -e XSS_SERVER="your-server" \
     -v "${PWD}/OutputFolder/:/reconftw/Recon/" \
     six2dez/reconftw:main -d example.com -r
   ```

   See [SECURITY.md](SECURITY.md) for full secrets management guidance.

6. **Health Check**:

   The Docker image includes a built-in `HEALTHCHECK` that runs `./reconftw.sh --health-check` every 60 seconds. You can also run it manually:

   ```bash
   docker exec <container-id> ./reconftw.sh --health-check
   ```

### Terraform + Ansible

- Deploy reconFTW on AWS using Terraform and Ansible.
- Follow the guide in [Terraform/README.md](Terraform/README.md) for setup instructions.

---

## 🛠️ Troubleshooting

- Bash 4+ on macOS: The scripts auto-relaunch under Homebrew Bash. If you see a message about Bash < 4, run `brew install bash`, open a new terminal, and re-run `./install.sh`.
- timeout on macOS: macOS provides `gtimeout` via `brew install coreutils`. The scripts now detect and use it automatically.
- Network hiccups: Installers hide most command output. If something fails, re-run with `upgrade_tools=true` in `reconftw.cfg`, execute `./install.sh --tools`, or install the missing too

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

```bash
#############################################
#			reconFTW config file			#
#############################################

# General values
tools=$HOME/Tools   # Path installed tools
if [[ -z "${SCRIPTPATH:-}" ]]; then
	if [[ -n "${BASH_SOURCE[0]:-}" ]]; then
		SCRIPTPATH="$( cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 ; pwd -P )" # Get current script's path
	else
		SCRIPTPATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )" # Get current script's path
	fi
fi
_detected_shell="${SHELL:-/bin/bash}"
profile_shell=".$(basename "${_detected_shell}")rc" # Get current shell profile
if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
	reconftw_version="$(git rev-parse --abbrev-ref HEAD)-$(git describe --tags 2>/dev/null || git rev-parse --short HEAD)"
else
	reconftw_version="standalone"
fi # Fetch current reconftw version
DATA_DIR="${SCRIPTPATH}/data"
WORDLISTS_DIR="${DATA_DIR}/wordlists"
PATTERNS_DIR="${DATA_DIR}/patterns"
generate_resolvers=false # Generate custom resolvers with dnsvalidator
update_resolvers=true # Fetch and rewrite resolvers from trickest/resolvers before DNS resolution
resolvers_url="https://raw.githubusercontent.com/trickest/resolvers/main/resolvers.txt"
resolvers_trusted_url="https://gist.githubusercontent.com/six2dez/ae9ed7e5c786461868abd3f2344401b6/raw/trusted_resolvers.txt"
RESOLVER_DOWNLOAD_CONNECT_TIMEOUT=10 # Seconds to wait for resolver download TCP connection
RESOLVER_DOWNLOAD_MAX_TIME=120 # Hard cap in seconds for resolver downloads
RESOLVER_DOWNLOAD_RETRY=2 # Retry count for resolver downloads
RESOLVER_DOWNLOAD_RETRY_DELAY=2 # Delay in seconds between resolver download retries
fuzzing_remote_list="https://raw.githubusercontent.com/six2dez/OneListForAll/main/onelistforallmicro.txt" # Used to send to Ax (if used) on fuzzing
proxy_url="http://127.0.0.1:8080/" # Proxy url
install_golang=tr
