# soxoj/maigret

🕵️‍♂️ Collect a dossier on a person by username from 3000+ sites

## features

- Supports 3,000+ sites ([see full list](https://github.com/soxoj/maigret/blob/main/sites.md)). A default run checks the 500 highest-ranked sites by traffic; pass `-a` to scan everything, or `--tags` to narrow by category/country.
- Embeddable in Python projects — import `maigret` and run searches programmatically (see [library usage](https://maigret.readthedocs.io/en/latest/library-usage.html)).
- [Extracts](https://github.com/soxoj/socid_extractor) all available information about the account owner from profile pages and site APIs, including links to other accounts.
- Performs recursive search using discovered usernames and other IDs.
- Allows filtering by tags (site categories, countries).
- Detects and partially bypasses blocks, censorship, and CAPTCHA.
- Fetches an [auto-updated site database](https://maigret.readthedocs.io/en/latest/settings.html#database-auto-update) from GitHub each run (once per 24 hours), and falls back to the built-in database if offline.
- Works with Tor and I2P websites; able to check domains.
- Ships with a [web interface](#web-interface) for browsing results as a graph and downloading reports in every format from a single page.
- Optional [AI analysis mode](#ai-analysis) (`--ai`) that turns raw findings into a short investigation summary using an OpenAI-compatible API.

For the complete feature list, see the [features documentation](https://maigret.readthedocs.io/en/latest/features.html).

### Used by

Professional OSINT and social-media analysis tools built on Maigret:

<a href="https://github.com/SocialLinks-IO/sociallinks-api"><img height="60" alt="Social Links API" src="https://github.com/user-attachments/assets/789747b2-d7a0-4d4e-8868-ffc4427df660"></a>
<a href="https://sociallinks.io/products/sl-crimewall"><img height="60" alt="Social Links Crimewall" src="https://github.com/user-attachments/assets/0b18f06c-2f38-477b-b946-1be1a632a9d1"></a>
<a href="https://usersearch.ai/"><img height="60" alt="UserSearch" src="https://github.com/user-attachments/assets/66daa213-cf7d-40cf-9267-42f97cf77580"></a>

## Demo

### Video

<a href="https://asciinema.org/a/Ao0y7N0TTxpS0pisoprQJdylZ">
  <img src="https://asciinema.org/a/Ao0y7N0TTxpS0pisoprQJdylZ.svg" alt="asciicast" width="600">
</a>

### Reports

[PDF report](https://raw.githubusercontent.com/soxoj/maigret/main/static/report_alexaimephotographycars.pdf), [HTML report](https://htmlpreview.github.io/?https://raw.githubusercontent.com/soxoj/maigret/main/static/report_alexaimephotographycars.html)

![HTML report screenshot](https://raw.githubusercontent.com/soxoj/maigret/main/static/report_alexaimephotography_html_screenshot.png)

![XMind 8 report screenshot](https://raw.githubusercontent.com/soxoj/maigret/main/static/report_alexaimephotography_xmind_screenshot.png)

[Full console output](https://raw.githubusercontent.com/soxoj/maigret/main/static/recursive_search.md)

## installation

Already ran the [In one minute](#one-minute) steps? You're set. Below are alternative methods.

Don't want to install anything? Use the [community Telegram bot](https://sites.google.com/view/maigret-bot-link).

### Windows

Download `maigret_standalone.exe` from [Releases](https://github.com/soxoj/maigret/releases). You can launch it two ways:

- **Double-click it** — Maigret will ask for a username, run a default search, and wait at the end so the report links stay visible.
- **Run it from a terminal** — open Command Prompt (press `Win+R`, type `cmd`, hit Enter) or PowerShell to pass extra options:

```cmd
cd %USERPROFILE%\Downloads
maigret_standalone.exe USERNAME
maigret_standalone.exe USERNAME --html       :: also save an HTML report
maigret_standalone.exe --help                :: list all options
```

Video guide: https://youtu.be/qIgwTZOmMmM.

<a id="cloud-shells"></a>
### Cloud Shells

Run Maigret in the browser via cloud shells or Jupyter notebooks:

<a href="https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/soxoj/maigret&tutorial=cloudshell-tutorial.md"><img src="https://user-images.githubusercontent.com/27065646/92304704-8d146d80-ef80-11ea-8c29-0deaabb1c702.png" alt="Open in Cloud Shell" height="50"></a>
<a href="https://repl.it/github/soxoj/maigret"><img src="https://replit.com/badge/github/soxoj/maigret" alt="Run on Replit" height="50"></a>

<a href="https://colab.research.google.com/gist/soxoj/879b51bc3b2f8b695abb054090645000/maigret-collab.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" height="45"></a>
<a href="https://mybinder.org/v2/gist/soxoj/9d65c2f4d3bec5dd25949197ea73cf3a/HEAD"><img src="https://mybinder.org/badge_logo.svg" alt="Open In Binder" height="45"></a>

### Snap (Linux)

<a href="https://snapcraft.io/maigret"><img src="https://snapcraft.io/static/images/badges/en/snap-store-black.svg" alt="Get it from the Snap Store" height="50"></a>

```bash
sudo snap install maigret

## tools

maigret username
```

Available for amd64 and arm64, no Python required. The snap is strictly confined and can write inside your home directory, so run it from there. For USB drives, connect the interface once with `sudo snap connect maigret:removable-media`.
