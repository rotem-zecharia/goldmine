# botpress/botpress

The open-source hub to build & deploy GPT/LLM Agents ⚡️

## tools

| **Package**                                                          | **Description**                                         | **Docs**                                                               | **Code**               |
| -------------------------------------------------------------------- | ------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------- |
| [`@botpress/cli`](https://www.npmjs.com/package/@botpress/cli)       | Build, Deploy and Manage Bots, Integrations and Plugins | [Docs](https://www.botpress.com/docs/for-developers/sdk/cli-reference) | [Code](./packages/cli) |
| [`@botpress/client`](https://www.npmjs.com/package/@botpress/client) | Type-safe clients to consume the Botpress APIs          | [Docs](<>)                                                             | [Code](<>)             |
| [`@botpress/sdk`](https://www.npmjs.com/package/@botpress/sdk)       | SDK used by to build integrations                       | [Docs](<>)                                                             | [Code](<>)             |

## Local Development

## requirements

The development environment requires the following tools to be installed:

- [`git`](https://git-scm.com/): Git is a free and open source distributed version control system.
- [`node`](https://nodejs.org/en/): Node.js® is a JavaScript runtime built on Chrome's V8 JavaScript engine.
- [`pnpm`](https://pnpm.io/): PNPM is a fast, disk space efficient package manager.

#### Windows-specific prerequisites

- [Microsoft Visual C++ Redistributable for Visual Studio 2015-2022](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist#visual-studio-2015-2017-2019-and-2022)

### Building from sources

```sh
# Clone the repository
git clone https://github.com/botpress/botpress.git
cd botpress

## installation

pnpm install

# Build all packages
pnpm run build

# Run Checks
pnpm run check
```

## Licensing

All packages in this repository are open-source software and licensed under the [MIT License](LICENSE). By contributing in this repository, you agree to release your code under this license as well.

Let's build the future of chatbot development together! 🤖🚀
