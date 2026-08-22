# openstatusHQ/openstatus

🫖 Status page with uptime monitoring & API monitoring as code 🫖

## features

- **Status pages + monitoring in one tool** — no need to wire up a separate monitoring service
- **28 global regions** checking in parallel across 3 cloud providers
- **Flat pricing, unlimited members** — no per-seat or per-subscriber charges
- **Open source & self-hostable** — AGPL-3.0, private-locations run in a single 8.5MB Docker image
- **Monitoring as code** — YAML config, CLI, GitHub Actions, Terraform
- **Incident communication** — subscriber notifications via email, RSS, and webhooks

### Status pages

Beautiful, customizable status pages with custom domains, password protection, maintenance windows, and subscriber notifications via email and RSS. Build trust and keep your users informed during incidents.

### Uptime Monitoring

Monitor your servers, websites and APIs from 28 regions across multiple cloud providers globally. Get notified via Slack, Discord, PagerDuty, email, and more when your services are down or slow.

## Recognitions

<a href="https://trendshift.io/repositories/1780" target="_blank"><img src="https://trendshift.io/api/badge/repositories/1780" alt="openstatus | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
<a href="https://news.ycombinator.com/item?id=37740870"><img alt="Featured on Hacker News" src="https://hackerbadge.now.sh/api?id=37740870" style="width: 250px; height: 55px;" width="250" height="55" /></a>
<a href="https://www.producthunt.com/posts/openstatus-2?utm_source=badge-top-post-badge&utm_medium=badge" target="_blank"><img alt="openstatus - #2 Product of the Day on Product Hunt" src="https://api.producthunt.com/widgets/embed-image/v1/top-post-badge.svg?post_id=openstatus-2&theme=light&period=daily" style="width: 250px; height: 55px;" width="250" height="55" /></a>

## Tooling

Everything the dashboard does is reachable from your terminal, your infrastructure code, and your AI assistant — all sharing a single API key.

- **[API](https://www.openstatus.dev/tooling/api)** — typed JSON-over-HTTP (ConnectRPC) with a [Node SDK](https://github.com/openstatusHQ/sdk-node)
- **[CLI](https://www.openstatus.dev/tooling/cli)** — interactive for humans, `--json` for agents, YAML monitoring as code
- **[Terraform](https://www.openstatus.dev/tooling/terraform)** — monitors, notifications, and status pages as HCL
- **[MCP server](https://www.openstatus.dev/tooling/mcp-server)** — connect Claude, ChatGPT, Cursor, or any MCP client to your workspace

## installation

### With Docker (Recommended)

The fastest way to get started for both development and self-hosting:

```sh

## configuration

cp .env.docker.example .env.docker

# 2. Start all services
docker compose up -d

# 3. Access the application
open http://localhost:3002  # Dashboard
open http://localhost:3003  # Status Pages
```

Full guide: [DOCKER.md](DOCKER.md)

### Self-Hosting with Coolify

We provide pre-built Docker images for easy deployment:

```bash
ghcr.io/openstatushq/openstatus-server:latest
ghcr.io/openstatushq/openstatus-dashboard:latest
ghcr.io/openstatushq/openstatus-workflows:latest
ghcr.io/openstatushq/openstatus-private-location:latest
ghcr.io/openstatushq/openstatus-status-page:latest
ghcr.io/openstatushq/openstatus-checker:latest
```

[Complete Coolify Deployment Guide](./COOLIFY_DEPLOYMENT.md)
