# nextlevelbuilder/ui-ux-pro-max-skill

An AI skill that provides design intelligence for building professional UI/UX across multiple platforms.

## features

- **79 Searchable UI Styles (50 active)** - Glassmorphism, Claymorphism, Minimalism, Brutalism, Neumorphism, Bento Grid, Dark Mode, AI-Native UI, and more
- **192 Color Palettes** - Industry-specific palettes aligned 1:1 with the 192 product types
- **74 Font Pairings** - Curated typography combinations with Google Fonts imports
- **25 Chart Types** - Recommendations for dashboards and analytics
- **22 Tech Stacks** - React, Next.js, Astro, Vue, Nuxt.js, Nuxt UI, Svelte, SwiftUI, React Native, Flutter, HTML+Tailwind, shadcn/ui, Jetpack Compose, Angular, Laravel, Three.js, JavaFX, WPF, WinUI 3, UWP, Avalonia, Uno Platform
- **119 UX Guidelines** - Best practices, anti-patterns, accessibility rules, resilient text layout, compact labels, and cancellable interactions
- **192 Reasoning Rules** - Industry-specific design system generation (NEW in v2.0)

### Resilient Text and Compact UI

The guidance now covers common production failures around headings, long tokens,
chips, badges, and interrupted micro-interactions:

- Balanced heading wrapping is a progressive enhancement, not a guarantee that a
  specific word will remain on the last line. Designs must still work with natural
  wrapping across widths, fonts, and locales.
- Essential text must reflow without clipping at narrow widths, browser zoom, text
  scaling, and user spacing overrides. Long URLs and identifiers may wrap safely.
- Chip and tag collections should wrap or use an operable `+n` disclosure. A compact
  label should remain whole when practical; unavoidable truncation needs an accessible
  full-value path for keyboard, pointer, and touch users.
- Badge meaning cannot rely on color alone. Interactive chips need native semantics,
  visible focus, and programmatic state; live counts need meaningful context.
- Rapid interactions may cancel animation, but the final semantic state, focus, and
  content must remain correct. Timing is selected for the platform and component,
  with reduced-motion preferences respected.

### Style Taxonomy

The catalog contains **79 searchable styles** backed by stable IDs and aliases:

| Status | Count | Search behavior |
|--------|------:|-----------------|
| Active | 50 | Included in normal recommendations and shown by default in the gallery |
| Supplemental | 29 | Returned for exact or explicit variant/system intent; available through the gallery status filter |
| Deprecated | 9 | Excluded from normal ranking; legacy names redirect to a canonical style or landing pattern |

The active set covers 43 general visual families, 2 mobile-specific styles, 3 official platform/design systems, 1 platform material, and 1 core analytics style. Current official systems include Fluent 2, Shopify Polaris, and Adobe Spectrum; Liquid Glass is scoped as an Apple platform material, Material 3 Expressive remains a mobile Material variant, and Spectrum 2 is supplemental. Landing-page structures live in the separate 34-pattern landing dataset rather than competing with visual styles in BM25 ranking.

See [`styles.csv`](src/ui-ux-pro-max/data/styles.csv) for the full taxonomy and provenance-aware metadata.

## 💎 Basic vs. Premium Version Comparison

Many users ask about the differences between the open-source and premium versions. Here is a detailed breakdown to help you choose the right fit for your workflow.

### 🟢 Basic Version (This Repository)
* **Fully Open Source:** Perfect for individual developers, hobbyists, and standard projects.
* **Core UI/UX Intelligence:** Full access to 79 searchable UI styles (50 active), 192 product types, color palettes, and curated font pairings.
* **Smart Recommendations:** Built-in BM25 search engine for highly accurate design matching.
* **Cross-Platform Support:** Stack-specific guidelines supporting 22 major frameworks (React, Vue, Tailwind, iOS, Android, etc.).
* **Design System Generation:** Instantly generate tailored UI rules, patterns, and logic via CLI.

### 🟡 Premium Version
* **Extended Brand Design Skills:** 

## installation

### Using Claude Marketplace (Claude Code)

Install directly in Claude Code with two commands:

```
/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill
/plugin install ui-ux-pro-max@ui-ux-pro-max-skill
```

### Using CLI (Recommended)

```bash
# Install CLI globally
npm install -g ui-ux-pro-max-cli

# Go to your project
cd /path/to/your/project

# Install for your AI assistant
uipro init --ai claude      # Claude Code
uipro init --ai cursor      # Cursor
uipro init --ai windsurf    # Windsurf
uipro init --ai antigravity # Antigravity
uipro init --ai copilot     # GitHub Copilot
uipro init --ai kiro        # Kiro
uipro init --ai codex       # Codex CLI
uipro init --ai qoder       # Qoder
uipro init --ai roocode     # Roo Code
uipro init --ai gemini      # Gemini CLI
uipro init --ai trae        # Trae
uipro init --ai opencode    # OpenCode
uipro init --ai continue    # Continue
uipro init --ai codebuddy   # CodeBuddy
uipro init --ai droid       # Droid (Factory)
uipro init --ai kilocode    # KiloCode
uipro init --ai warp        # Warp
uipro init --ai augment     # Augment
uipro init --ai codewhale   # CodeWhale
uipro init --ai openclaw    # OpenClaw
uipro init --ai universal   # Universal / Agent Standard (.agents/skills/)
uipro init --ai all         # All assistants
```

The npm package is `ui-ux-pro-max-cli`; it still installs the `uipro` command. Older `uipro-cli` releases are stale and should not be used for current assets.

### Global Install (Available for All Projects)

```bash
uipro init --ai claude --global   # Install to ~/.claude/skills/
uipro init --ai cursor --global   # Install to ~/.cursor/skills/
uipro init --ai universal --global # Install to ~/.agents/skills/
```

## tools

```bash
uipro versions              # List available versions
uipro update                # Refresh skill files from installed CLI package
uipro update --global       # Refresh global skill files from installed CLI package
uipro init --offline        # Compatibility flag; installs bundled templates
uipro uninstall             # Remove skill (auto-detect platform)
uipro uninstall --ai claude # Remove specific platform
uipro uninstall --global    # Remove from global install
```

## requirements

Python 3.x is required for the search script (standard library only — the scripts install nothing and make no network calls).

Check if Python is installed:

```bash
python3 --version
```

If it is missing, install it yourself from [python.org](https://www.python.org/downloads/) or with your OS package manager (Homebrew, apt, winget). These install steps are for **you, the human user** — AI agents using this skill should never install software on your machine; they are instructed to ask you instead.
