# atenreiro/opensquat

openSquat is an open-source tool that detects look-alike domains impersonating your brand, by scanning newly registered domains daily.

## features

> **"A powerful swiss army knife for brand protection"**
> — [WhoisXML API Blog](https://www.whoisxmlapi.com/blog/orchestrating-open-source-software-and-whois-newly-registered-domain-data-feeds-to-fight-the-typosquatting-plague), August 2022

> **"A handy tool for collecting information on newly registered domains."** — ranked Top 5 phishing detection tool
> — [SOCRadar Blog](https://socradar.io/blog/top-5-tools-for-phishing-domain-detection/), July 2022

> **"openSquat provides essential protection against domain squatting and phishing attacks through automated monitoring and detection."**
> — [Prince Yadav, TutorialsPoint](https://www.tutorialspoint.com/article/opensquat-ndash-domain-squatting-and-phishing-watchdog), March 2026

### Academic Citation

> **"OpenSquat identified 103 squatting domains, 960 active phishing websites, and 53 domains with suspicious certificates."**
> — Sharma et al., [Journal of Information Security and Cybercrimes Research (JISCR)](https://journals.nauss.edu.sa/index.php/JISCR/article/download/2805/1349), Vol. 7, Issue 1, June 2024

---

## 🔓 Open-Core Model

openSquat follows an **open-core model**:

- **Core detection engine** — Open source and community-driven
- **Advanced capabilities** — Delivered through commercial intelligence services

This model enables transparency and community collaboration while supporting the scale, reliability, and operational requirements of enterprise use.

---

## ✨ Key Features

- 📅 **Daily NRD feeds** — Automatic newly registered domain updates
- 🔍 **Similarity detection** — Levenshtein distance algorithm
- 🔓 **Three operating modes** — **Community** (free feed), **Premium Feed** (paid feed, same local pipeline), or **Premium API** (hosted lookalike service). The two Premium modes share a single openSquat API key — see [Premium and API Modes](#-premium-and-api-modes).
- 🛡️ **VirusTotal integration** — Check domain reputation
- 🌐 **Quad9 DNS validation** — Identify malicious domains
- 📜 **Certificate Transparency** — Monitor SSL/TLS certificates
- 📊 **Multiple output formats** — TXT, JSON, CSV

---

## installation

### Install via pip (recommended)

```bash
pip install opensquat
opensquat -k keywords.txt
```

### Or clone the repository

```bash
git clone https://github.com/atenreiro/opensquat
cd opensquat
pip install -r requirements.txt
python3 opensquat.py -k keywords.txt
```

> **Repo users:** in all the examples below, replace `opensquat` with `python3 opensquat.py` to run from a cloned checkout.

### See it in action

<p align="center">
  <img src="screenshots/openSquat_v2.3.0.png" alt="openSquat 2.3.0 scanning the daily NRD feed for lookalikes of google, facebook, amazon and paypal" width="650"/>
</p>

---

## requirements

- **Python 3.10+**
- Dependencies: `confusable_homoglyphs`, `homoglyphs`, `colorama`, `requests`, `dnspython`, `beautifulsoup4`

---

## tools

### Basic Commands

```bash
# Default run
opensquat

## configuration

opensquat -h

# Use custom keywords file
opensquat -k my_keywords.txt
```

### Validation Options

```bash
# DNS validation via Quad9
opensquat --dns

# Check Certificate Transparency logs
opensquat --ct

# Scan for open ports (80/443)
opensquat --portcheck

# Cross-reference phishing databases
opensquat --phishing results.txt
```

### Output Formats

```bash
# Save as JSON
opensquat -o results.json -t json

# Save as CSV
opensquat -o results.csv -t csv
```

### Confidence Levels

| Level | Flag | Description |
|-------|------|-------------|
| 0 | `-c 0` | Very high (fewer results, high accuracy) |
| 1 | `-c 1` | High (default) |
| 2 | `-c 2` | Medium |
| 3 | `-c 3` | Low |
| 4 | `-c 4` | Very low (more results, more false positives) |

> **Note:** On the API side (`--api`), the five confidence levels map to four fuzziness values (`exact`, `low`, `auto`, `high`) — `-c 3` and `-c 4` both map to `high`. See [Premium and API Modes](#-premium-and-api-modes) for the full mapping and how to override with `--api-fuzziness`.

---
