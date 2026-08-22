# PipedreamHQ/pipedream

Connect APIs, remarkably fast. Free for developers.

## features

- [Workflows](#workflows) - Workflows run automations. Workflows are sequences of steps - pre-built actions or custom [Node.js](https://pipedream.com/docs/code/nodejs/), [Python](https://pipedream.com/docs/code/python/), [Golang](https://pipedream.com/docs/code/go/), or [Bash](https://pipedream.com/docs/code/bash/) code - triggered by an event (HTTP request, timer, when a new row is added to a Google Sheets, and more).
- [Event Sources](#event-sources) - Sources trigger workflows. They emit events from services like GitHub, Slack, Airtable, RSS and [more](https://pipedream.com/apps). When you want to run a workflow when an event happens in any third-party app, you're using an event source.
- [Actions](#actions) - Actions are pre-built code steps that you can use in a workflow to perform common operations across Pipedream's 1,000+ API integrations. For example, you can use actions to send email, add a row to a Google Sheet, [and more](https://pipedream.com/apps).
- [Custom code](#code) - Most integrations require custom logic. Code is often the best way to express that logic, so Pipedream allows you to run any [Node.js](https://pipedream.com/docs/code/nodejs/), [Python](https://pipedream.com/docs/code/python/), [Golang](https://pipedream.com/docs/code/go/), or [Bash](https://pipedream.com/docs/code/bash/) code. You can import any package from the languages' package managers, connect to any Pipedream connected app, and more. Pipedream is "low-code" in the best way: you can use pre-built components when you're performing common actions, but you can write custom code when you need to.
- [Destinations](#destinations) - Deliver events asynchronously to common destinations like Amazon S3, Snowflake, HTTP and email.
- [Free](#pricing) - No fees for individual developers (see [limits](https://docs.pipedream.com/limits/))

## Demo

Click the image below to watch a brief demo on YouTube.

<p align="center">
  <br />
  <a href="https://bit.ly/3ytGgyR">
    <img src="./images/demo.png" width="800px" alt="Pipedream demo static image" />
  </a>
</p>

### Workflows

Workflows are sequences of linear [steps](https://pipedream.com/docs/workflows/steps) triggered by an event (like an HTTP request, or when a new row is added to a Google sheet). You can quickly develop complex automations using workflows and connect to any of our 1,000+ integrated apps.

[See our workflow quickstart](https://pipedream.com/docs/quickstart/) to get started.

### Event Sources

[Event Sources](https://pipedream.com/docs/sources/) watch for new data from services like GitHub, Slack, Airtable, RSS and [more](https://pipedream.com/apps). When a source finds a new event, it emits it, triggering any linked workflows.

You can also consume events emitted by sources using [Pipedream's REST API](https://pipedream.com/docs/api/rest/) or a private, real-time [SSE stream](https://pipedream.com/docs/api/sse/).

When a pre-built source doesn't exist for your use case, [you can build your own](https://pipedream.com/docs/components/quickstart/nodejs/sources/). Here is the simplest event source: it exposes an HTTP endpoint you can send any request to, and prints the contents of the request when invoked:

```javascript
export default {
  name: "http",
  version: "0.0.1",
  props: {
    http: "$.interface.http",
  },
  run(event) {
    console.log(event); // event contains the method, payload, etc.
  },
};
```

<a href="https://pipedream.com/sources/new?app=http"><img src="https://i.ibb.co/m0bBsSL/deploy-clean.png" height="35"></a>

You can find the code for all pre-built sources in [the `components` directory](https://github.com/PipedreamHQ/pipedream/tree/master/components). If you find a bug or want to contribute a feature, [see our contribution guide](https://pipedream.com/docs/components/guidelines/#process).

### Actions

[Actions](https://pipedream.com/docs/components/actions/) are pre-built code steps that you can use in a workflow to perform common operations across Pipedream'
