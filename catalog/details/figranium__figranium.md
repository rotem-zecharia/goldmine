# figranium/figranium

Stack blocks visually to build complex browser workflows and execute them via API

## features

<div align="center">
  <a href="https://swiftproxy.net/?ref=figranium" target="_blank">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="partner-assets/swiftproxy_white.png">
      <source media="(prefers-color-scheme: light)" srcset="partner-assets/swiftproxy.png">
      <img src="partner-assets/swiftproxy.png" width="220" alt="Swiftproxy">
    </picture>
  </a>
</div>

## installation

This starts the app on `http://localhost:11345` and the VNC viewer on `http://localhost:54311`.

## configuration

| Variable | Purpose | Default |
|----------|---------|---------|
| `SESSION_SECRET` | Signs session cookies. Required. | — |
| `ALLOWED_IPS` | Comma list for basic IP allowlisting. | none (open) |
| `TRUST_PROXY` | Honor `X-Forwarded-*` when behind a reverse proxy. | `0` |
| `ALLOW_PRIVATE_NETWORKS` | Allow scraping local/private IPs (SSRF risk). | `false` |
| `VITE_DEV_PORT` | Port for front-end dev server. | `5173` |
| `VITE_BACKEND_PORT` | Backend port for proxying + scripts. | `11345` |
| `DB_TYPE` | Optional database type overriding disk storage. Set to `postgres` to use PostgreSQL. | — |
| `DB_POSTGRESDB_HOST` | Hostname for the PostgreSQL database (required if DB_TYPE is postgres). | — |
| `DB_POSTGRESDB_PORT` | Port for the PostgreSQL database (required if DB_TYPE is postgres). | — |
| `DB_POSTGRESDB_USER` | Username for the PostgreSQL database (required if DB_TYPE is postgres). | — |
| `DB_POSTGRESDB_PASSWORD` | Password for the PostgreSQL database (required if DB_TYPE is postgres). | — |
| `USE_CLOAK_ENGINE` | Set to `true` to run the browser engine on CloakBrowser (stealth-patched Chromium) instead of the default Playwright stealth stack. | `false` |
| `CLOAKBROWSER_LICENSE_KEY` | CloakBrowser license key for the latest binary (read natively by cloakbrowser; `npx cloakbrowser login` writes `~/.cloakbrowser/license.key`). Without a key the free legacy binary is used. | — |

Proxy rotation also respects `data/proxies.json` (see below), and `data/allowed_ips.json` works as an alternate allowlist format.

## tools

Figranium exposes a comprehensive REST API for integration with agents (like OpenClaw) or custom automation scripts. All endpoints are hosted locally, typically on port `11345`.

**Authentication:** 
If enabled, provide the `x-api-key` header or `Authorization: Bearer <key>`. For internal network use, this may be optional depending on your settings.

## limitations

- [x] **Settings shortcuts** — the System tab already exposes API key regeneration, user agent selection, and layout preferences so operators can tune them without leaving the UI.
- [x] **Storage cleanup** — the Settings data tab lets you clear captures and cookies, and the backend exposes `/api/clear-screenshots` and `/api/clear-cookies`.
- [x] **IP rotation tooling** — build a settings workflow for importing proxies and automatically rotating them.
- [x] **API key workflow** — the API key panel already supports regenerating and copying keys via `/api/settings/api-key`, so secure API access is ready without extra setup.
- [x] **Task proxy rotation toggle** — the “Rotate Proxies” option in each task ties into the Settings rotation controls, enabling rotation per execution.
- [x] **Spatial editor transition** — transition to a spatial editor like that of activepieces (top priority).
- [ ] **Action key combos** — add modifier shortcuts (e.g., Ctrl+Click, Shift+Scroll) so tasks can more closely mirror real user interactions.
- [ ] **Click-and-drag block** — add an action that does drag gestures (selecting text, moving items) so tasks can simulate click-and-drag flows.
- [x] **Recording controls** — Task editor now exposes a “Disable automated recording” switch in the general settings panel so workflows can skip video capture on a per-task basis.
- [x] **File downloads** — add explicit support for agent tasks to download files (PDFs, CSVs, etc.) directly from target pages, then surface those downloads in the UI so users can preview or export them without sifting through captures.
- [x] **Stateless mode** — Tasks now have a “Stateless execution” toggle alongside the recording controls so each run starts with no cookies or local storage, ensuring nothing persists between executions for that workflow.
- [ ] **Adblocking filters** — add controls so execution contexts can enable built-in ad/malware filtering (e.g., via hosts file overrides or request blocking) to reduce noise on sensitive sites.
- [ ] **Extraction response mode** — add a Settings switch so users can choose whether the API returns HTML+data (for debugging) or data-only payloads when extraction scripts run.
- [ ] **Folder organization** — group tasks, assets, and captures into named folders so operators can browse, filter, and download collections per workflow.
- [ ] **Stable capture retention** — add filtering, pinning, and archiving in captures tab so teams can keep compliance records.
- [ ] **Workspace templates** — allow saving and sharing workspace presets (layout + default proxies/agents) so new team members can onboard with pre-configured setups.
- [ ] **Geo-targeted exits** — allow choosing proxy regions for tasks so you can pin the apparent location before running a job.
- [x] **Complete anti-detection coverage** — follow browserscan.net's anti-detection checklist (fingerprints, headers, fonts, WebRTC, etc.) so automated runs mimic real browsers across task executions.
- [ ] **Session recording redaction** — add toggles to redact sensitive fields (passwords, credit cards) from recordings/logs before storing them.
- [ ] **Two-factor authentication** — add optional TOTP/second-factor support to Settings/Auth so operators can lock down the UI with 2FA.
- [ ] **Automatic self-healing selectors** — add selector fallback and recovery logic so tasks can repair broken locators after layout changes without manual intervention.
- [ ] **AI-assisted fixing** — add an “AI auto-fix” helper that suggests layout, selector, and proxy tweaks after failed runs, letting teams approve or discard the proposed changes without switching contexts.
- [ ] **Companion app** — build a lightweight companion app that mirrors critical dashboard notifications (failures, capture completions, proxy issues) so operators can stay informed without opening the full UI.
- [x] **Community presets hub** — build a marketplace where users can publish task/workspace presets, browse and download others’ sub
