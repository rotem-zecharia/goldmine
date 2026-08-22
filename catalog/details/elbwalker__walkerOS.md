# elbwalker/walkerOS

Open-source tag manager for developers

## features

- **Config-as-code** - version control your tracking, review it in PRs, deploy
  with confidence
- **Declarative tagging** - tag your UI in HTML, not scattered JavaScript
- **Consent-native** - events queue until consent is given, then flush correctly
  to every destination
- **Schema validation** - catch bad events at collection time, not weeks later
  in a dashboard
- **One layer, many destinations** - send to your warehouse and ad platforms
  from a single event definition
- **Warehouse-native** - events land clean and structured in your data
  warehouse, ready to query
- **MIT licensed** - self-host anywhere, no vendor lock-in

## How it works

![walkerOS Architecture](https://raw.githubusercontent.com/elbwalker/walkerOS/main/website/static/diagrams/walkeros_readme.png)

- **Sources:** Where events come from (browser, dataLayer, Express, AWS Lambda,
  GCP Functions, and more)
- **Collector:** The processing engine (consent, validation, mapping, routing,
  enrichment)
- **Destinations:** Where events go (GA4, Google Ads, Meta CAPI, BigQuery, and
  more)

## installation

Choose one based on your workflow and integration possibilities:

| Mode           | Description                                                  | Best For                                |
| -------------- | ------------------------------------------------------------ | --------------------------------------- |
| **Integrated** | Import directly into your TypeScript application             | React/Next.js apps, TypeScript projects |
| **Bundled**    | Build a standalone script from JSON config with npx walkeros | Static sites, Docker deployments, CI/CD |

**Integrated** (import into your app):

```typescript
import { startFlow } from '@walkeros/collector';

const { elb } = await startFlow({
  destinations: {
    console: {
      code: {
        type: 'console',
        config: {},
        push: (event) => console.log('Event:', event.name),
      },
    },
  },
});

await elb('page view', { title: 'Home' });
// -> logs: Event: page view
```

Wire a real source and destination once you are ready:

```typescript
import { startFlow } from '@walkeros/collector';
import { sourceBrowser } from '@walkeros/web-source-browser';
import { destinationGtag } from '@walkeros/web-destination-gtag';

await startFlow({
  sources: {
    browser: {
      code: sourceBrowser,
      config: { settings: { pageview: true } },
    },
  },
  destinations: {
    ga4: {
      code: destinationGtag,
      config: {
        settings: { ga4: { measurementId: 'G-XXX' } },
      },
    },
  },
});
```

**Bundled** (build from JSON config):

```json
{
  "version": 4,
  "flows": {
    "default": {
      "config": {
        "platform": "web",
        "bundle": {
          "packages": {
            "@walkeros/collector": {},
            "@walkeros/web-source-browser": {},
            "@walkeros/web-destination-gtag": {}
          }
        }
      },
      "sources": {
        "browser": {
          "package": "@walkeros/web-source-browser",
          "config": { "settings": { "pageview": true } }
        }
      },
      "destinations": {
        "ga4": {
          "package": "@walkeros/web-destination-gtag",
          "config": {
            "settings": { "ga4": { "measurementId": "G-XXX" } }
          }
        }
      }
    }
  }
}
```

Then: `npx walkeros bundle flow.json`

- **[Operating Modes](https://www.walkeros.io/docs/getting-started/modes/)**
- **[Quickstart guide for React](https://www.walkeros.io/docs/getting-started/quickstart/react)**
- **[Full Documentation](https://www.walkeros.io/docs/)** - Complete guides and
  API reference
- **[Destinations](https://www.walkeros.io/docs/destinations/)** - GA4, Meta,
  BigQuery, and more
- **[React Demo](https://github.com/elbwalker/walkerOS/tree/main/apps/demos/react)**
- **[Storybook](https://storybook.walkeros.io/)**

## AI-ready via MCP

walkerOS exposes a Model Context Protocol (MCP) interface. AI agents can read
your event schema, suggest tracking definitions, and generate integration code -
making your event layer programmable, not just configurable.

In Claude Code, one plugin installs both MCP servers and the walkerOS skills:

```
/plugin marketplace add elbwalker/walkerOS
/plugin install walkeros@elbwalker
```

For any other MCP client, add the servers to its configuration:

```json
{
  "mcpServers": {
    "walkeros-flow": {
      "command": "npx",
      "args": ["@walkeros/mcp"]
    },
    "walkeros-source-browser": {
      "command": "npx",
      "args": ["@walkeros/mcp-source-browser"]
    }
  }
}
```

Loading a flow, validating it, and simulating an event all run locally, no
account needed. See the [MCP docs](https://www.walkeros.io/docs/apps/mcp).

Coming from Google Tag Manager? See
[walkerOS vs. GTM](https://www.walkeros.io/docs/comparisons/gtm).

## Contributing

⭐️ Help us grow and star us. See our
[Contributing Guidelines](https://www.walkeros.io/docs/contributing) to get
involved.

## Support

Need help? Start a
[discussion](https://github.com/elbwalker/walkerOS/discussions), or reach ou
