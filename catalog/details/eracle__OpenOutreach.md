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

## ⚙️ Local Installation (Development)

For contributors or if you prefer running directly on your machine.

## requirements

- [Git](https://git-scm.com/)
- [Python](https://www.python.org/downloads/) (3.12+)

### 1. Clone & Set Up
```bash
git clone https://github.com/eracle/OpenOutreach.git
cd OpenOutreach

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

## 📖 How the Pipeline Works

`find` does one thing at a time until your goal is met, asking the deals what they need — there is no queue table and nothing is scheduled in advance. Each pass walks one ordered list and stops at the first thing it can do, so priority *is* that order:

| # | Step | What it does |
|---|------|-------------|
| 1 | **check a lookup** | Polls an in-flight work-email job: hit → `RESOLVED`, miss → `NO_EMAIL_BETTERCONTACT`, still running → ask again later on the same job. |
| 2 | **rank the pool** | Promotes the qualified leads the model is confident about. |
| 3 | **buy an address** | Free hub-cache hit resolves immediately; otherwise fires a paid provider job and parks the deal at `FINDING_EMAIL`. |
| 4 | **top up** | Discovers and qualifies more leads. |

Only step 3 costs money, and its only gate is whether you configured a provider. **Steps 2 and 4 are ungated on purpose**: searching the index is free and qualifying costs one call against your own LLM key, so there is nothing to ration — and what bounds the paid step is the number you typed, since one credit is one verified address.

The run ends when the goal is met, or when **nothing can advance right now** — every lead is waiting on a lookup that is not due yet, or the search has drained. There is no timeout to configure, because each thing being waited on carries its own.

**Discover → qualify → gate → resolve → export.** One LLM pass turns your campaign into opening search keywords; from there the keyword vocabulary grows by counting the words that appear in profiles the LLM has accepted, and the walk keeps firing the most promising set. Qualification runs the GP + LLM loop over the stored firmographic text and writes the `reason`. The GP confidence gate promotes `QUALIFIED → READY_TO_FIND_EMAIL`, **rationing the paid lookup** so only the best-fit leads 
