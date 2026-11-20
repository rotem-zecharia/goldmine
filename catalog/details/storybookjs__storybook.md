# storybookjs/storybook

Storybook is the industry standard workshop for building, documenting, and testing UI components in isolation

## installation

Run this command at the root of an existing project to install and configure Storybook:

```sh
npm create storybook@latest
```

Or paste this prompt into your agent:

```text
Set up Storybook for me with npm create storybook@latest and follow its instructions precisely
```

Visit [Storybook's website](https://storybook.js.org/?ref=readme) to learn more about Storybook, or follow the [installation guide](https://storybook.js.org/docs/get-started/install?ref=readme) for other package managers and manual setup.

### Documentation

Documentation can be found on [Storybook's docs site](https://storybook.js.org/docs?ref=readme). To learn Storybook step by step, follow the [tutorials](https://storybook.js.org/tutorials/?ref=readme).

## tools

View the [Storybook Showcase](https://storybook.js.org/showcase?ref=readme) to see how leading teams use Storybook.

Use [storybook.new](https://storybook.new) to quickly create an example project in Stackblitz.

## AI

Storybook makes building UI with agents faster, better and cheaper. Your agent reuses the components you already have, writes stories for what it builds, tests its work by running stories, and gives you a visual review to check the result.

### Skills and the CLI

Run this command in the root of your project to install Storybook's skills:

```sh
npx storybook automigrate skills
```

Skills are short instruction files in your repository that tell your agent what to do at each step of a UI change. Most AI agents support skills. Your agent learns how to interact with Storybook by reading skill files, and then calls the `storybook tools` command to get work done:

| Command                           |                                                                             |
| --------------------------------- | --------------------------------------------------------------------------- |
| `storybook tools docs list`       | List all components and docs entries                                        |
| `storybook tools docs show`       | Show the props and usage examples of a component                            |
| `storybook tools stories changed` | List the stories that are new, modified, or affected by uncommitted changes |
| `storybook tools test run`        | Run story tests, with accessibility checks if set up                        |
| `storybook tools review create`   | Publish a review of the stories that a change affects                       |

See [Connect your agent](https://storybook.js.org/docs/ai/connect?ref=readme) to get started, and the [CLI options](https://storybook.js.org/docs/api/cli-options?ref=readme#tools) for all the tools. If you want your agent to call Storybook through MCP tools instead of CLI commands, the [MCP addon](code/addons/mcp/) serves the same tools from your dev server.

These features are available for React, Next, TanStack, Vue, Angular, Svelte, Web Components and multiple community frameworks. Check the [supported frameworks](https://storybook.js.org/docs/ai/connect?ref=readme#supported-frameworks) for more details.

### Published Storybooks

When you [publish your Storybook with Chromatic](https://storybook.js.org/docs/sharing/publish-storybook?ref=readme#publish-storybook-with-chromatic), Chromatic also publishes its MCP server, at your published Storybook's URL followed by `/mcp`:

```
https://<branch>--<app-id>.chromatic.com/mcp
```

Agents that connect to the MCP server can look up your components, with their props and usage examples, without running Storybook. This lets the teams that build with your design system reuse its components from their own repositories. Chromatic MCP hosting is entirely free. See [Use a published Storybook](https://storybook.js.org/docs/ai/published-storybook?ref=readme) and [Chromatic's setup guide](https://chromatic.com/docs/storybook-mcp/) for more details.

## Projects

### Supported Frameworks

| Framework                                                   | Version                                                                                                                                                                        | Downloads                                                                                                                                                |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [React](code/frameworks/react-vite)                      
