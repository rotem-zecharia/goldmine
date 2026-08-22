# eugeniughelbur/obsidian-second-brain

Persistent memory for Claude Code and 6 other CLI agents, stored as plain markdown in your Obsidian vault. Stop re-explaining your projects, decisions and people every session. 45 commands: hybrid sem

## installation

**After a meeting:** `/obsidian-save`
Claude pulls out every decision, person, task, and idea and saves each one to the right note. You do nothing.

**You recorded a voice memo:** `/obsidian-ingest meeting.m4a`
Claude transcribes it with a local Whisper install, attributes speakers where the transcript makes them identifiable, extracts every promise and action item, and distributes across entity pages, task boards, and the daily note.

**You screenshot a whiteboard:** `/obsidian-ingest photo.png`
Claude reads the image, extracts text and structure, creates concept notes, links to related projects. A photo becomes knowledge.

**You find a great video:** `/obsidian-ingest https://youtube.com/...`
Claude doesn't summarize into one note. It REWRITES your existing pages. People get updated. Contradictions get resolved. Patterns trigger new synthesis pages. One URL in. The vault is smarter.

**Before a big decision:** `/obsidian-challenge`
Claude searches your vault for past failures and reversed decisions on the same topic. Pushes back with your own words. Your vault holds you accountable.

**You want to see the big picture:** `/obsidian-visualize`
Claude generates a visual canvas of your entire vault. Hub nodes centered, color-coded by type, orphans highlighted. Open it in Obsidian and see the shape of your knowledge.

**You go to sleep:** The nightly agent runs 5 phases: closes the day, reconciles contradictions, synthesizes cross-source patterns, heals orphan notes, and rebuilds the index. You wake up to a smarter vault.

**You start a new day:** `/obsidian-daily`
Claude pulls your calendar events, overdue tasks, and overnight changes into today's note. Your morning starts informed.

**Someone shares an X post:** `/x-read https://x.com/...`
Grok with live X access fetches the post, the thread, and the replies. Returns verbatim text + TL;DR + key claims + reply sentiment + voices to watch. No more screenshots.

**You're planning today's content:** `/x-pulse "AI automation"`
Grok scans X for what's trending in your topic right now. Returns 3-5 emerging themes (with rep posts + key voices), gaps nobody is filling, hook formats that are working, and 3 specific post ideas you could write today.

**You need real research:** `/research "AI memory tools"`
Perplexity Sonar Pro pulls a deep dossier with citations: summary, key facts (every claim with a recency marker and source domain), timeline, key players, contrarian views, recommended further reading, open questions. Saved to your vault, auto-opens in Obsidian.

**You want vault-first deep research:** `/research-deep "AI memory tools"`
Scans your vault for what you already know. Identifies gaps. Spawns 3-5 targeted searches via Perplexity (web) and Grok (X discourse). Synthesizes a delta report: what's new, what's confirmed, contradictions to resolve, recommended vault updates. Vault baseline doesn't get re-researched. Only gaps get filled.

**You hit a great YouTube video:** `/youtube https://youtu.be/...`
Free transcript via youtube-transcript-api. Optional metadata + top comments via YouTube Data API v3. Gemini (free tier, Grok fallback) summarizes into TL;DR, Key Points, Notable Quotes (verbatim), Themes, Comment Sentiment, and Worth Following Up On. Saved as an AI-first note in your vault. Add `--visual` to also *watch* it: scene-change frame extraction (ffmpeg) that Claude reads with its own vision to capture on-screen text, code, diagrams, and demos the transcript misses.

**You never open Obsidian.** Everything happens through Claude.

---

## tools

Mostly no. The vault commands (`/obsidian-save`, `/obsidian-daily`, etc.) need no API keys. `/research` and `/research-deep` are also key-free now - with no Perplexity key they automatically fall back to free, key-less sources (Wikipedia, HackerNews, arXiv, Reddit, and more) and Claude synthesizes the dossier. The remaining research commands (`/x-read`, `/x-pulse`, `/notebooklm`, `/youtube`, `/podcast`) need their respective keys (xAI Grok, Perplexity, Google Gemini, optionally YouTube Data API v3 / OpenAI Whisper) and exit with a clear setup message when one is missing. The calendar command (`/obsidian-calendar`, all four modes) needs the Google Calendar MCP connector rather than an API key.

## features

Command reference: https://eugeniughelbur.github.io/obsidian-second-brain/ - every command, with the plain-language phrases that trigger it in English, Spanish, Portuguese and Simplified Chinese.

Retrieval benchmark: [scripts/eval/BENCHMARK.md](scripts/eval/BENCHMARK.md) - a reproducible 300-note synthetic corpus and three query sets, so the search numbers are something you can run yourself rather than something this README claims.

The rule on its own: [AI-FIRST.md](AI-FIRST.md) - the note spec as a 50-line block you can paste into any `CLAUDE.md` or `AGENTS.md`. Installs nothing, works without this project, keep the attribution line.

GitHub Issues: https://github.com/eugeniughelbur/obsidian-second-brain/issues. PRs welcome, see Contributing below.

---
