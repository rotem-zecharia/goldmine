# atenreiro/opensquat

openSquat is an open-source tool that detects look-alike domains impersonating your brand, by scanning newly registered domains daily.

## features

> **"A powerful swiss army knife for brand protection"**
> — [WhoisXML API Blog](https://www.whoisxmlapi.com/blog/orchestrating-open-source-software-and-whois-newly-registered-domain-data-feeds-to-fight-the-typosquatting-plague), August 2022

> **"A handy tool for collecting information on newly registered domains."** — ranked Top 5 phishing detection tool
> — [SOCRadar Blog](https://socradar.io/blog/top-5-tools-for-phishing-domain-detection/), July 2022

> **"openSquat provides essential protection against domain squatting and phishing attacks through automated monitoring and detection."**
> — [Prince Yadav, TutorialsPoint](https://www.tutorialspoint.com/article/opensquat-ndash-domain-squatting-and-phishing-watchdog), March 2026

## installation

```bash
pip install opensquat
opensquat -k keywords.txt
```

## requirements

- **Python 3.10+**
- Dependencies: `confusable_homoglyphs`, `homoglyphs`, `colorama`, `requests`, `dnspython`, `beautifulsoup4`

---

## tools

```bash

## configuration

opensquat -h
