# sergebulaev/linkedin-skills

Claude skills for LinkedIn. 11 Claude Code and Codex skills that write human-sounding LinkedIn posts, craft comments that get noticed, analyze your feed, and build a publishing cadence, all from your 

## installation

Pick whichever way you use Claude Code or Codex:

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
