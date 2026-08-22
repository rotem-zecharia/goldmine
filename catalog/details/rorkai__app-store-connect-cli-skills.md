# rorkai/app-store-connect-cli-skills

Skills to automate app store deployed and everything related to it using the asc cli

## installation

Install the skills with `asc`:

```bash
asc install-skills
```

Or install them directly from GitHub with the Agent Skills installer:

```bash
npx skills add rorkai/app-store-connect-cli-skills
```

### Claude Code plugin

This repository is also a Claude Code marketplace. Add it once, then install the `asc` plugin:

```bash
claude plugin marketplace add rorkai/app-store-connect-cli-skills
claude plugin install asc@rorkai
```

### Codex plugin

The repository includes a Codex plugin manifest and can be listed by a Codex plugin marketplace.
Codex currently installs plugins from configured marketplaces, so use the Agent Skills installer
until `asc` has a public marketplace listing:

```bash
npx skills add rorkai/app-store-connect-cli-skills --agent codex
```

## Available Skills

## tools

Guidance for running `asc` commands (canonical verbs, flags, pagination, output, auth).

**Use when:**
- You need the correct `asc` command or flag combination
- You want JSON-first output and pagination tips for automation
- You need Apple Ads command, auth, ad-account, org, payload, or pagination guidance

**Example:**

```bash
Find the right asc command to list all builds for app 123456789 as JSON and paginate through everything.
```

### asc-apple-ads

Apple Ads auth and account discovery, Platform API v1 campaigns, targeting, reports, assets, guarded mutations, raw calls, and v5 migration.

**Use when:**
- You need to read or change Apple Ads resources with `asc ads`
- You need Apple Ads OAuth, profile, ad-account context, or `ASC_ADS_*` guidance
- You need a safe read-first plan before mutating a live Ads account
- You need to migrate deprecated `asc ads v5` automation to Platform API v1

**Example:**

```bash
Discover my Apple Ads ad account, query campaigns through Platform API v1, and draft a paused test plan before creating anything.
```

### asc-workflow

Define and run repo-local automation graphs using `asc workflow` and `.asc/workflow.json`.

**Use when:**
- You are migrating from lane-based automation to repo-local workflows
- You need multi-step orchestration with machine-parseable JSON output for CI/agents
- You need hooks (`before_all`, `after_all`, `error`), conditionals (`if`), and private helper sub-workflows
- You want validation (`asc workflow validate`) with cycle/reference checks before execution

**Example:**

```bash
Create an asc workflow that stages a release, validates it, and only submits when CONFIRM_RELEASE=true.
```

### asc-app-create-ui

Create a new App Store Connect app via browser automation when no API exists.

**Use when:**
- You need to create an app record (name, bundle ID, SKU, primary language)
- You are comfortable logging in to App Store Connect in a real browser

**Example:**

```bash
Create a new App Store Connect app for com.example.myapp with SKU MYAPP123 and primary language English (U.S.).
```

### asc-xcode-build

Build, archive, generate export options, export, and manage Xcode version/build numbers before uploading.

**Use when:**
- You need to create an IPA or PKG for upload
- You're setting up CI/CD build pipelines
- You need to generate or customize ExportOptions.plist
- You need a modern `release-testing` IPA for registered devices
- You're troubleshooting encryption compliance issues

**Example:**

```bash
Archive and export my macOS app as a PKG I can upload to App Store Connect.
```

### asc-ad-hoc-distribution

Prepare and publish verified private iOS installs for registered devices with
the experimental `asc distribute` workflow.

**Use when:**
- You need to ship a build outside TestFlight to a controlled device list
- You want a read-only plan before additive signing and storage mutations
- You need to resume or live-verify a private S3-compatible distribution run

**Example:**

```bash
Plan a private release-testing install from this Xcode archive, show me the exact effects, and apply only after I approve the plan hash.
```

### asc-screenshot-resize

Resize and validate App Store screenshots using the current size catalog from `asc screenshots sizes` and macOS `sips`.

**Use when:**
- You need to inspect the screenshot dimensions Apple currently accepts
- You need to remove alpha or resize screenshots before upload
- You want local validation against an App Store screenshot device type

**Example:**

```bash
Validate these iPhone screenshots, resize only the invalid files, and verify the results before upload.
```

### asc-shots-pipeline

Agent-first screenshot pipeline using xcodebuild/simctl, AXe, JSON plans, `asc screenshots frame` (experimental), and `asc screenshots upload`.

**Use when:**
- You need a repeatable simulator screenshot automation flow
- You want AXe-based UI driving before capture
- You need a staged pipeline (capture -> frame -> upload)
- 
