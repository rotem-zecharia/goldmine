# dpearson2699/swift-ios-skills

Agent Skills for iOS 26+, Swift 6.3, SwiftUI, and modern Apple frameworks

## installation

### Recommended: any agent via [skills CLI](https://github.com/vercel-labs/skills)

The skills CLI is the recommended install method.

Interactive install (recommended):

```sh
npx skills add dpearson2699/swift-ios-skills
```

Running the default command opens the skills CLI UI so you can choose which skills to install and which agent(s) to install them for.

Install everything for any coding agent:

```sh
npx skills add dpearson2699/swift-ios-skills --all
```

Use `--all` when you want the full set of 86 skills installed automatically for any coding agent.

Install specific skills directly:

```sh
npx skills add dpearson2699/swift-ios-skills --skill <skill-name> --skill <skill-name>
```

Check for updates to installed skills:

```sh
npx skills check
```

Update installed skills to the latest versions:

```sh
npx skills update
```

Use these after installing through the skills CLI.

### Claude Code (via plugin marketplace)

Add the marketplace (one-time):

```sh
/plugin marketplace add dpearson2699/swift-ios-skills
```

Install everything:

```sh
/plugin install all-ios-skills@swift-ios-skills
```

Or install a themed bundle (bundles limit how many skills load into the context window — if you want everything, use `all-ios-skills` above instead of installing multiple bundles):

```sh
/plugin install swiftui-skills@swift-ios-skills
/plugin install swift-core-skills@swift-ios-skills
/plugin install ios-app-framework-skills@swift-ios-skills
/plugin install ios-data-framework-skills@swift-ios-skills
/plugin install ios-ai-ml-skills@swift-ios-skills
/plugin install ios-engineering-skills@swift-ios-skills
/plugin install ios-hardware-skills@swift-ios-skills
/plugin install ios-platform-skills@swift-ios-skills
/plugin install ios-gaming-skills@swift-ios-skills
/plugin install apple-kit-skills@swift-ios-skills
```

### OpenAI Codex

```sh
$skill-installer install https://github.com/dpearson2699/swift-ios-skills/tree/main/skills/<skill-name>
```

### Claude Web App / Claude Desktop

1. Download the skill folder(s) you want from this repo
2. Zip each skill folder
3. Go to **Settings > Capabilities** and enable "Code execution and file creation"
4. Go to **Customize > Skills**, click **+**, then **Upload a skill**
5. Upload the zip

### ChatGPT

1. Download the skill folder(s) you want from this repo
2. Zip each skill folder
3. Click your profile icon in ChatGPT and select **Skills**
4. Click **New skill** and select **Upload from your computer**
5. Upload the zip

## Plugin Bundles (Claude Code)

| Plugin | Skills included |
|--------|----------------|
| **all-ios-skills** | All 86 skills |
| **apple-kit-skills** | 39 skills spanning Apple Kit frameworks plus CarPlay |
| **swiftui-skills** | focus-engine, swiftui-animation, swiftui-gestures, swiftui-layout-components, swiftui-liquid-glass, swiftui-navigation, swiftui-patterns, swiftui-performance, swiftui-uikit-interop, swiftui-webkit |
| **swift-core-skills** | core-data, swift-api-design-guidelines, swift-architecture, swift-codable, swift-charts, swift-concurrency, swift-formatstyle, swift-language, swift-testing, swiftdata |
| **ios-app-framework-skills** | activitykit, adattributionkit, alarmkit, app-clips, app-intents, avkit, carplay, mapkit, paperkit, pdfkit, photokit, push-notifications, storekit, tipkit, widgetkit |
| **ios-data-framework-skills** | cloudkit, contacts-framework, eventkit, financekit, healthkit, musickit, passkit, weatherkit |
| **ios-ai-ml-skills** | apple-on-device-ai, coreml, natural-language, speech-recognition, vision-framework |
| **ios-engineering-skills** | app-store-optimization, app-store-review, authentication, background-processing, cryptokit, debugging-instruments, device-integrity, ios-accessibility, ios-ettrace-performance, ios-localization, ios-memgraph-analysis, ios-networking, swift-security, swiftlint, ios-simulator, metrickit |
| **ios-hardware-skills** | accessorysetupkit, core-bluetooth, core-motion, core-nfc, dockkit, pencilkit, realitykit,
