# steipete/CodexBar

Show usage stats for OpenAI Codex and Claude Code, without having to login.

## requirements

- macOS 14+ (Sonoma)

## tools

Provider toggles and API keys live in the resolved CodexBar config file. New installs use
`~/.config/codexbar/config.json`; existing `~/.codexbar/config.json` installs still load from the legacy path. You can
script the same provider list that Settings → Providers uses:

```bash
codexbar config providers
codexbar config enable --provider grok
codexbar config disable --provider cursor
```

For API-key providers, store a key without opening Settings:

```bash
printf '%s' "$ELEVENLABS_API_KEY" | codexbar config set-api-key --provider elevenlabs --stdin
```

`set-api-key` trims the piped value, stores it with restrictive config-file permissions, and enables the provider by default. Use `--no-enable` to only save the key, or `--api-key <key>` for one-off local scripts where shell history is not a concern.
See [CLI configuration](docs/cli-configuration.md) for the full flow.

## features

- Multi-provider menu bar with per-provider toggles (Settings → Providers).
- Provider-specific usage meters with reset countdowns.
- Optional Codex web dashboard enrichments (code review remaining, usage breakdown, credits history).
- Inline spend and usage charts for API-backed providers such as OpenAI, Claude Admin API, OpenRouter, LiteLLM, z.ai, MiniMax, Mistral, and AWS Bedrock.
- Configurable cost-usage scans for Codex + Claude, plus reused chart UI for supported provider histories. Codex history uses a WAL-enabled SQLite store capped at 25,000 retained session entries and 256 MiB.
- A persistent Settings → Usage & Spend view for local 7/30-day estimates, grouped by native currency and limited to providers that expose cost history.
- Provider status polling with incident badges in the menu and icon overlay.
- Merge Icons mode to combine providers into one status item + switcher.
- Display controls for provider icons, labels, bars, reset-time style, and highest-usage auto-selection.
- Fresh installs default to Adaptive refresh. Existing users keep every valid stored choice, while legacy unset or
  invalid preferences resolve to 5 minutes. Manual and fixed 1m, 2m, 5m, 15m, and 30m alternatives remain available.
- Bundled CLI (`codexbar`) for scripts and CI (including `codexbar cost --provider codex`, `claude`, or `both` for local cost usage); macOS and Linux CLI builds available.
- WidgetKit widgets for supported providers.
- Localized app and website with a shared 21-language catalog, automatic website detection, persistent pickers, and RTL support.
- Optional session quota notifications and weekly-reset confetti.
- Privacy-first: on-device parsing by default; browser cookies are opt-in and reused (no passwords stored).

## installation

- Clone the repo and open it in Xcode or run the scripts directly.
- Launch once, then toggle providers in Settings → Providers.
- Install/sign in to provider sources you rely on (CLIs, browser cookies, OAuth/device flow, API keys, or local app/config files).
- Optional: set OpenAI cookies (Automatic or Manual) for Codex dashboard extras.
