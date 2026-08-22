# eracle/OpenOutreach

Open-source AI agent for B2B lead generation — describe your product, it finds the people who fit and explains why each one does, then exports a CSV your cold-email tool can send. Self-hosted CLI.

## installation

```bash
uvx openoutreach find 10
```

or, if you would rather install it:

```bash
pip install openoutreach && openoutreach find 10
```

The interactive onboarding walks you through the inputs above on first run — four steps: product/objective → LLM key (live-verified) → BetterContact key → your email, country and the legal notice. `find` does it for you if it hasn't happened yet; `openoutreach init` does it deliberately, prints the campaign it created and stops before spending anything. Either way every answer can come from the environment instead (`OPENOUTREACH_*`), which is what makes a headless install possible. Everything lives in `~/.openoutreach/data`, so stopping and starting loses nothing: the number you ask for is *more than you already have*, so running it again continues where it left off. No browser, no daemon manager, no container.

**The three verbs:**

```bash
openoutreach init                # set up the pipeline and the campaign, print it, stop
openoutreach find 10             # ten more qualified leads — free, and cannot spend
openoutreach find 10 --emails    # ...and buy an address for whatever is ready
openoutreach find 10 emails      # ten more *with* a work email (one credit each)
openoutreach find 0              # no work — just print what the campaign already has
openoutreach find 1 --open       # ...and open each new profile in your browser as it lands
openoutreach find 1 --debug      # ...and show the discovery walk's reasoning as it goes
openoutreach status              # what is configured, blocked and counted
```

Running it on a server instead? A Docker image is published to GitHub Container Registry for exactly that — see the **[Docker Guide](./docs/docker.md)**.

---

## requirements

- [Git](https://git-scm.com/)
- [Python](https://www.python.org/downloads/) (3.12+)

## features

| Feature                            | Description                                                                                                          |
|------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| 🧠 **Autonomous Lead Discovery**   | No contact lists needed — an LLM turns your product + objective into opening keywords, and the walk grows them by counting the words that appear in profiles it already accepted. |
| 📝 **A Reason Per Lead**           | Every qualified lead carries the LLM's written rationale for choosing it. It exports alongside the row, so the tool downstream can merge it — and so you can tell a bad ICP from a bad model. |
| 🔒 **Licensed Discovery**          | Firmographic profiles come from a licensed provider (BetterContact Lead Finder) — no scraping, no browser, no account. |
| 🎯 **Pay Only For What Resolves**  | Search against the licensed source is free; a confidence gate rations the paid lookups, billed only on a verified hit. Cost scales with qualified leads, not with how much you searched. |
| 📤 **Export That Just Imports**    | CSV in the exact column names Instantly and Smartlead expect, so a file imports without column mapping. One record schema, one translation layer, no privileged path for our own sender. |
| 💾 **Built-in CRM**               | Django Admin — browse Leads, Companies and Deals, and read every verdict. Everything is local and everything exports. |
| 🔄 **Stateful Pipeline**          | Tracks deal states in a local DB — fully resumable, nothing scheduled in advance, no queue table.                   |
| ⚡ **One-Command Install**          | `uvx openoutreach find 10` — a Python CLI with interactive onboarding, no browser and no container. A Docker image exists for running it on a server. |
| 🤖 **Built For Agents**            | One bounded call: ask for an amount, get the rows on stdout and an exit code that means *I got what you asked for*. No daemon to supervise, no file to discover, nothing to poll. `--json` for the whole outcome. |

---
