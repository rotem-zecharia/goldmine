# sergebulaev/linkedin-skills

Claude skills for LinkedIn. 11 Claude Code and Codex skills that write human-sounding LinkedIn posts, craft comments that get noticed, analyze your feed, and build a publishing cadence, all from your 

## installation

Pick whichever way you use Claude Code or Codex:

### Codex CLI

```bash
codex plugin marketplace add sergebulaev/linkedin-skills
codex plugin add linkedin-skills@linkedin-skills
```

To test a local clone before publishing changes:

```bash
git clone https://github.com/sergebulaev/linkedin-skills.git
cd linkedin-skills
codex plugin marketplace add .
codex plugin add linkedin-skills@linkedin-skills
```

### claude.ai (web)

1. Open https://claude.ai/code
2. Go to **Skills** in the sidebar
3. Click **Add from GitHub**
4. Paste: `sergebulaev/linkedin-skills`
5. Done. The skills activate automatically when you ask about LinkedIn.

### Claude Desktop (Mac / Windows)

1. Open Claude Desktop
2. Click **Customize**
3. Click the **+** next to **Personal plugins** → **Create plugin** → **Add marketplace**
4. Choose **Add from a repository** and paste: `sergebulaev/linkedin-skills`
5. Install the plugin
6. Done. Start a new conversation and ask Claude to write a LinkedIn post.

### OpenClaw

1. Open your OpenClaw working directory
2. Clone the skills into it:
   ```bash
   git clone https://github.com/sergebulaev/linkedin-skills.git
   ```
3. In OpenClaw settings, add this to your system prompt:
   ```
   You have LinkedIn marketing skills in ./linkedin-skills/.
   For any LinkedIn task, read the relevant skills/*/SKILL.md first.
   Use lib/url_parser.py for URL parsing,
       lib/apify_client.py for reading posts / comments / engagers,
       lib/publora_client.py for publishing actions.
   ```
4. Done. Ask OpenClaw to write a LinkedIn post or comment.

### Claude Code (CLI / VS Code / JetBrains)

```
/plugin marketplace add sergebulaev/linkedin-skills
/plugin install linkedin-skills@linkedin-skills
```

Or clone the repo and open it as your working directory:

```bash
git clone https://github.com/sergebulaev/linkedin-skills.git
cd linkedin-skills
```

### Hermes Agent

Hermes Agent (Nous Research) follows the agentskills.io open standard and loads `skills/*/SKILL.md` directly. Clone the bundle into your Hermes skills folder:

```bash
git clone https://github.com/sergebulaev/linkedin-skills.git ~/.hermes/skills/linkedin-skills
```

Coming from OpenClaw? `hermes claw migrate` imports these skills automatically. Then call `/<skill-name>` from any of your Hermes chat surfaces.

### Any agent (skills CLI)

One command that works across Claude Code, Codex, Cursor, and any other agent that reads SKILL.md files:

```bash
npx skills add sergebulaev/linkedin-skills
```

> **Found this useful? [Star the repo](https://github.com/sergebulaev/linkedin-skills).** Curated Claude Code and Codex directories rank and gate by star count, so a star is what makes these skills findable for the next person. It is the only thing we ask. No signup, no email.

## What you can do

Once installed, just ask Claude Code or Codex for help with LinkedIn. The right skill activates automatically.

**Write a post:**
> "Write me a LinkedIn post about why AI agencies are replacing traditional ones. Make it viral."

**Comment on someone's post:**
> "Comment on this post: https://linkedin.com/posts/... — I want to add a thoughtful take."

**Check a draft before publishing:**
> "Audit this post draft for AI tells and algorithm issues: [paste your text]"

**Reverse-engineer a viral post:**
> "What hook formula does this post use? https://linkedin.com/posts/..."

**Plan your week:**
> "Create a 7-day LinkedIn content plan. I'm a B2B SaaS founder targeting VPs of Marketing."

**Rewrite your profile:**
> "Optimize my LinkedIn profile for inbound leads: https://linkedin.com/in/yourname"

**Remove AI tells from any text:**
> "Humanize this text: [paste AI-generated draft]"

Every skill shows you a draft first and waits for your OK before doing anything. Nothing gets posted without your approval.

## The 11 skills

| Skill | What it does |
|---|---|
| **Post Writer** | Drafts viral-ready posts using 20 proven 2026 hook formulas (anaphora, R.I.P. obituary, year-over-year pivot, cur

## tools

Four of the skills (Comment Drafter, Reply Handler, Hook Extractor, Engagement Monitor) can read post bodies, comment threads, your own recent comments, and the people who liked or commented on any post. Without an Apify token they fall back to asking you to paste the relevant text. With one, they fetch automatically.

[Apify](https://console.apify.com/sign-up) free tier ships with $5/month of credit, which goes a long way at $1-$5 per 1,000 results. The skills use four no-cookies actors:

| Use case | Actor | Cost |
|---|---|---|
| Post body by URL | `supreme_coder/linkedin-post` | $1 / 1,000 |
| Comments + replies on a post | `apimaestro/linkedin-post-comments-replies-engagements-scraper-no-cookies` | $5 / 1,000 |
| Your own recent comments | `apimaestro/linkedin-profile-comments` | $5 / 1,000 |
| Likers + commenters on any post | `scraping_solutions/linkedin-posts-engagers-likers-and-commenters-no-cookies` | $5 / 1,000 |

Setup: drop `APIFY_TOKEN=apify_api_...` into your `.env`. The thin client at `lib/apify_client.py` exposes `fetch_post`, `fetch_post_comments`, `fetch_user_recent_comments`, and `fetch_post_engagers`.

A typical creator running daily comment ops + a weekly engager-analytics sweep stays under $2/month, well inside the free tier.

## Optional: auto-post with Publora

By default, skills draft content for you to copy-paste into LinkedIn. If you want Claude Code or Codex to publish directly to your LinkedIn (and optionally to X, Threads, Instagram), connect Publora. It takes about 2 minutes.

### What is Publora?

[Publora](https://publora.com) is a publishing API that handles LinkedIn's quirks (3 different URL formats, reaction type mismatches, thread flattening bugs). The free tier gives you 15 posts/month.
