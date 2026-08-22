# blacklanternsecurity/bbot

The recursive internet scanner for hackers. 🧡

## installation

```bash
# stable version
pipx install bbot

# bleeding edge (dev branch)
pipx install --pip-args '\--pre' bbot
```

_For more installation methods, including [Docker](https://hub.docker.com/r/blacklanternsecurity/bbot), see [Getting Started](https://www.blacklanternsecurity.com/bbot/Stable/)_

> **Upgrading from 2.x?** BBOT 3.0 contains breaking changes to the CLI, presets, modules, events, and Python API. See the [2.x → 3.0 Migration Guide](https://www.blacklanternsecurity.com/bbot/Stable/migration/3.0_breaking_changes/) ([source](docs/migration/3.0_breaking_changes.md)) before upgrading.

> **Speed tip:** BBOT's DNS resolver ([blastdns](https://github.com/blacklanternsecurity/blastdns)) spins up multiple threads per resolver in `/etc/resolv.conf`. Adding more unfiltered resolvers dramatically speeds up scans. See the [sample resolv.conf](docs/data/resolv-sample.conf) and [Tips and Tricks](https://www.blacklanternsecurity.com/bbot/Stable/scanning/tips_and_tricks/#speed-up-scans-with-more-dns-resolvers) for details.

## tools

### 1) Subdomain Finder

Passive API sources plus a recursive DNS brute-force with target-specific subdomain mutations.

```bash
# find subdomains of evilcorp.com
bbot -t evilcorp.com -p subdomain-enum

# passive sources only
bbot -t evilcorp.com -p subdomain-enum -rf passive
```

<!-- BBOT SUBDOMAIN-ENUM PRESET EXPANDABLE -->

<details>
<summary><b><code>subdomain-enum.yml</code></b></summary>

```yaml
description: Enumerate subdomains via APIs, brute-force

flags:
  # enable every module with the subdomain-enum flag
  - subdomain-enum

output_modules:
  # output unique subdomains to TXT file
  - subdomains

config:
  dns:
    threads: 25
    brute_threads: 1000
  # put your API keys here
  # modules:
  #   github:
  #     api_key: ""
  #   chaos:
  #     api_key: ""
  #   securitytrails:
  #     api_key: ""

```

</details>

<!-- END BBOT SUBDOMAIN-ENUM PRESET EXPANDABLE -->

BBOT consistently finds 20-50% more subdomains than other tools. The bigger the domain, the bigger the difference. To learn how this is possible, see [How It Works](https://www.blacklanternsecurity.com/bbot/Stable/how_it_works/).

![subdomain-stats-ebay](https://github.com/blacklanternsecurity/bbot/assets/20261699/de3e7f21-6f52-4ac4-8eab-367296cd385f)

### 2) Web Spider

```bash
# crawl evilcorp.com, extracting emails and other goodies
bbot -t evilcorp.com -p spider
```

<!-- BBOT SPIDER PRESET EXPANDABLE -->

<details>
<summary><b><code>spider.yml</code></b></summary>

```yaml
description: Recursive web spider

modules:
  - http

blacklist:
  # Prevent spider from invalidating sessions by logging out
  - "RE:/.*(sign|log)[_-]?out"

config:
  web:
    # how many links to follow in a row
    spider_distance: 2
    # don't follow links whose directory depth is higher than 4
    spider_depth: 4
    # maximum number of links to follow per page
    spider_links_per_page: 25

```

</details>

<!-- END BBOT SPIDER PRESET EXPANDABLE -->

### 3) Email Gatherer

```bash
# quick email enum with free APIs + scraping
bbot -t evilcorp.com -p email-enum

# pair with subdomain enum + web spider for maximum yield
bbot -t evilcorp.com -p email-enum subdomain-enum spider
```

<!-- BBOT EMAIL-ENUM PRESET EXPANDABLE -->

<details>
<summary><b><code>email-enum.yml</code></b></summary>

```yaml
description: Enumerate email addresses from APIs, web crawling, etc.

flags:
  - email-enum

output_modules:
  - emails

```

</details>

<!-- END BBOT EMAIL-ENUM PRESET EXPANDABLE -->

### 4) Web Scanner

```bash
# run a light web scan against www.evilcorp.com
bbot -t www.evilcorp.com -p web

# run a heavy web scan against www.evilcorp.com
bbot -t www.evilcorp.com -p web-heavy
```

<!-- BBOT WEB PRESET EXPANDABLE -->

<details>
<summary><b><code>web.yml</code></b></summary>

```yaml
description: Quick web scan

include:
  - iis-shortnames

flags:
  - web

```

</details>

<!-- END BBOT WEB PRESET EXPANDABLE -->

<!-- BBOT WEB-HEAVY PRESET EXPANDABLE -->

<details>
<summary><b><code>web-heavy.yml</code></b></summary>

```yaml
description: Aggressive web scan

include:
  # include the web preset
  - web

flags:
  - web-heavy

```

</details>

<!-- END BBOT WEB-HEAVY PRESET EXPANDABLE -->

### 5) Everything Everywhere All at Once

```bash
# everything everywhere all at once
bbot -t evilcorp.com -p kitchen-sink

# roughly equivalent to:
bbot -t evilcorp.com -p subdomain-enum cloud-enum code-enum email-enum spider web paramminer webbrute web-screenshots
```

<!-- BBOT KITCHEN-SINK PRESET EXPANDABLE -->

<details>
<summary><b><code>kitchen-sink.yml</code></b></summary>

```yaml
description: Everything everywhere all at once

include:
  - subdomain-enum
  - cloud-enum
  - code-enum
  - email-enum
  - spider
  - web
  - paramminer
  - webbrute
  - web-screenshots
  - baddns-heavy

config:
  modules:
    dnsbrute:
      recursive_mutations: true
    dnscommonsrv:
      recursive_mutations: true
    webbrute:
      avoid_wafs: False
    wayback:
      urls: True
      parameters: True
      arc

## features

- Support for Multiple Targets
- Web Screenshots
- Suite of Offensive Web Modules
- NLP-powered Subdomain Mutations
- Native Output to Neo4j (and more)
- Automatic dependency install with Ansible
- Search entire attack surface with custom YARA rules
- Python API + Developer Documentation

## Targets

BBOT accepts an unlimited number of targets via `-t`. You can specify targets either directly on the command line or in files (or both!):

```bash
bbot -t evilcorp.com evilcorp.org 1.2.3.0/24 -p subdomain-enum
```

Targets can be any of the following:

- DNS Name (`evilcorp.com`)
- IP Address (`1.2.3.4`)
- IP Range (`1.2.3.0/24`)
- Open TCP Port (`192.168.0.1:80`)
- URL (`https://www.evilcorp.com`)
- Email Address (`bob@evilcorp.com`)
- Organization (`ORG:evilcorp`)
- Username (`USER:bobsmith`)
- Filesystem (`FILESYSTEM:/tmp/asdf`)
- Mobile App (`MOBILE_APP:https://play.google.com/store/apps/details?id=com.evilcorp.app`)

For more information, see [Targets](https://www.blacklanternsecurity.com/bbot/Stable/scanning/#targets-t). To learn how BBOT handles scope, see [Scope](https://www.blacklanternsecurity.com/bbot/Stable/scanning/#scope).
