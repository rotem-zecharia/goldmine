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
