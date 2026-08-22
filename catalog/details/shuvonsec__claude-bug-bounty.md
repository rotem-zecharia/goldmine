# shuvonsec/claude-bug-bounty

AI-powered bug bounty hunting from your terminal - recon, 20 vuln classes, autonomous hunting, and report generation. All inside Claude Code.

## installation

```bash
# 1. Install Ollama (runs AI locally, no internet needed after download)
curl -fsSL https://ollama.ai/install.sh | sh
ollama pull qwen2.5:14b          # ~9 GB, one-time download

# 2. Install BugHunter
git clone https://github.com/shuvonsec/claude-bug-bounty.git
cd claude-bug-bounty
./install.sh --agent standalone   # creates system-wide 'bughunter' command

# 3. Hunt
bughunter setup       # choose Ollama, then choose one of its installed models
bughunter recon target.com
```

### Groq setup (free cloud, fastest option)

```bash
export GROQ_API_KEY="your-key-here"     # free at console.groq.com
./install.sh --agent standalone
bughunter setup       # choose Groq
bughunter hunt target.com
```

---

## Quick Start

**Option A — standalone (no subscription, works for everyone)**

```bash
git clone https://github.com/shuvonsec/claude-bug-bounty.git
cd claude-bug-bounty
./install.sh --agent standalone   # creates system-wide 'bughunter' command
bughunter setup                   # pick a free AI provider
bughunter recon target.com
bughunter hunt  target.com
bughunter validate "my finding"
bughunter report
```

**Option B — Claude Code plugin** *(requires Claude Code)*

```bash
git clone https://github.com/shuvonsec/claude-bug-bounty.git
cd claude-bug-bounty
chmod +x install_tools.sh && ./install_tools.sh   # subfinder · httpx · nuclei · katana · ffuf
chmod +x install.sh      && ./install.sh          # skills + commands → ~/.claude/
```

```bash
claude
/recon target.com        # map the attack surface
/hunt target.com         # test for vulnerabilities
/validate                # run the 7-Question Gate
/report                  # write the submission
```

**Option C — let Claude install it** *(Claude Code only)*

Open your terminal, run `claude`, then paste:

```text
Install the Claude Bug Bounty toolkit from https://github.com/shuvonsec/claude-bug-bounty
into ~/tools/. Clone the repo, run ./install_tools.sh then ./install.sh.
Verify /recon /hunt /validate /report are available.
```

---

## tools

### Core Workflow

| Command | What It Does |
|:---|:---|
| `/recon target.com` | Subdomain enum · live host probing · URL crawl · nuclei sweep |
| `/hunt target.com` | Tests IDOR · auth bypass · SSRF · XSS · SQLi · logic flaws and more |
| `/validate` | 7-Question Gate — kills weak findings before you waste time reporting |
| `/report` | Generates an H1 · Bugcrowd · Intigriti · Immunefi submission in 60s |
| `/autopilot target.com` | Full loop, autonomous — scope → recon → hunt → validate → report |

### Recon & Enumeration

| Command | What It Does |
|:---|:---|
| `/surface target.com` | Ranked attack surface from recon data + memory |
| `/scope-aggregate <program>` | All in-scope assets across H1 · Bugcrowd · Intigriti · YWH · Immunefi |
| `/cloud-recon --keyword <name>` | Public S3 · Azure · GCP buckets + CloudFlare-bypass origin IPs |
| `/param-discover <url>` | Hidden HTTP parameters via Arjun · x8 |
| `/secrets-hunt --js-bundle <dir>` | Leaked credentials in source, JS bundles, or a GitHub org |
| `/takeover --recon <dir>` | Subdomain takeover candidates via dnsReaper · subjack |
| `/scan-cves <host>` | Focused nuclei high/critical sweep + optional log4j-scan |
| `/bypass-403 <url>` | Header · method · encoding tricks against 403/401 |
| `/portscan <host>` | Open ports + non-web services (Redis · Docker API · DBs · RDP) via naabu/smap |
| `/screenshot -l urls.txt` | Screenshot live hosts into an HTML gallery — triage + PoC evidence |


### Scanners (Web + LLM)

| Command | What It Does |
|:---|:---|
| `/cors <url>` | CORS misconfig — origin reflection · null · credentialed |
| `/crlf <url>` | CRLF / response-splitting + host-header injection |
| `/nosqli <url>` | NoSQL injection (operator bypass · `$where` timing) |
| `/jwt-scan <token>` | Offline JWT toolkit — alg:none · RS256→HS256 · secret crack |
| `/oob <target>` | Out-of-band listener (interactsh) for blind SSRF/XXE/SQLi |
| `/sast <path>` | Semgrep security packs over fetched JS/source → ranked sinks |
| `/domxss <url>` | Confirms DOM XSS in headless Chromium — reports only when the payload executes |
| `/llm-redteam <endpoint>` | LLM red-team corpus — prompt injection · jailbreak · exfil |

### Smart Contract (Web3)

| Command | What It Does |
|:---|:---|
| `/web3-audit <contract.sol>` | 10-class smart contract audit with Foundry PoC template |
| `/token-scan <contract>` | Rug pull scanner — mint authority · LP lock · honeypot · bonding curve |

### Session & Utility

| Command | What It Does |
|:---|:---|
| `/pickup target.com` | Resume from last session — untested endpoints first |
| `/intel target.com` | CVEs + disclosed reports relevant to this target |
| `/chain` | Bug A found → finds bugs B and C that chain with it |
| `/scope <asset>` | Checks if a domain or URL is in scope before you test it |
| `/triage` | Quick 2-minute go/no-go check |
| `/remember` | Logs the current finding or technique to hunt memory |
| `/memory-gc` | Inspect or rotate hunt-memory JSONL files (10 MB cap, 3 backups) |
| `/arsenal [tool]` | Lists installed external tools or prints an install hint |

---

## What It Finds

<details>
<summary><b>26 Web2 Vulnerability Classes</b></summary>
<br>

| Vulnerability | Typical Payout |
|:---|:---|
| IDOR / BOLA | $500 – $5K |
| Auth Bypass | $1K – $10K |
| XSS (Stored / Reflected / DOM) | $500 – $5K |
| SSRF | $1K – $15K |
| Business Logic | $500 – $10K |
| Race Conditions | $500 – $5K |
| SQL Injection | $1K – $15K |
| OAuth / OIDC | $500 – $5K |
| File Upload → RCE | $500 – $10K |
| GraphQL Auth Bypass | $1K – $10K |
| LLM / Prompt Injection | $500 – $10K |
| API Misconfiguration (mass assignment · JWT · CORS) | $500 – $5K |
| Account Takeover | $1K – $20K |
| SSTI | $2K – $10K |
| Subdomain Takeover | $200 – $5K |
| Cloud / Infra Exposure | $500 – $20K |
| HTTP Request Smuggling | $5K – $30K |
| Cache Poisoning | $1K – $10K |
| MFA / 2FA Bypass | $1K – $10K |
| SAML / SSO Attack | $2K – $20K |
| Error Disclosure / Debug Endpoints | $200 –
