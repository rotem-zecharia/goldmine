# webdriverio/webdriverio

Next-gen browser and mobile automation test framework for Node.js

## installation

To get started, create a codespace for this repository by clicking this 👇

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=2296970)

A codespace will open in a web-based version of Visual Studio Code. The [dev container](.devcontainer/devcontainer.json) is fully configured with the software needed for this project.

**Note**: Dev containers are an open spec that is supported by [GitHub Codespaces](https://github.com/codespaces) and [other tools](https://containers.dev/supporting).

### Getting started with Gitpod

You can also just click on:

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/webdriverio/webdriverio)

to get a ready-to-use development environment for you to start working on this code base.

If you're looking for issues to help out with, check out [the issues labeled "good first pick"](https://github.com/webdriverio/webdriverio/issues?q=is%3Aopen+is%3Aissue+label%3A"good+first+pick"). You can also reach out to our [Matrix Channel](https://discord.webdriver.io) if you have questions on where to start contributing.

## :office: WebdriverIO for Enterprise

Available as part of the Tidelift Subscription.

The maintainers of WebdriverIO and thousands of other packages are working with Tidelift to deliver commercial support and maintenance for the open-source dependencies you use to build your applications. Save time, reduce risk, and improve code health, while paying the maintainers of the exact dependencies you use. [Learn more.](https://tidelift.com/subscription/pkg/npm-webdriverio?utm_source=npm-webdriverio&utm_medium=referral&utm_campaign=enterprise&utm_term=repo)

## :package: Packages

This repository contains some of the core packages of the WebdriverIO project. There are many wonderful [curated resources](https://github.com/webdriverio-community/awesome-webdriverio) the WebdriverIO community has put together.

**Did you build a WebdriverIO service or reporter?** That's awesome! Please add it to our configuration wizard and docs (e.g. like in [this example commit](https://github.com/webdriverio/webdriverio/commit/3cb5937b968dfe93cf78871589019736a6c98d9e)) as well as to our [awesome-webdriverio](https://github.com/webdriverio-community/awesome-webdriverio) list. Thank you! 🙏 ❤️

### Core

- [webdriver](https://github.com/webdriverio/webdriverio/tree/main/packages/webdriver) - A Node.js bindings implementation for the W3C WebDriver and Mobile JSONWire Protocol
- [webdriverio](https://github.com/webdriverio/webdriverio/blob/main/packages/webdriverio) - Next-gen browser and mobile automation test framework for Node.js
- [@wdio/cli](https://github.com/webdriverio/webdriverio/tree/main/packages/wdio-cli) - A WebdriverIO testrunner command line interface

### Helper

- [@wdio/config](https://github.com/webdriverio/webdriverio/blob/main/packages/wdio-config) - A helper utility to parse and validate WebdriverIO options
- [@wdio/logger](https://github.com/webdriverio/webdriverio/tree/main/packages/wdio-logger) - A helper utility for logging WebdriverIO packages
- [@wdio/protocols](https://github.com/webdriverio/webdriverio/tree/main/packages/wdio-protocols) - Utility package providing information about automation protocols
- [@wdio/repl](https://github.com/webdriverio/webdriverio/tree/main/packages/wdio-repl) - A WDIO helper utility to provide a repl interface for WebdriverIO
- [@wdio/reporter](https://github.com/webdriverio/webdriverio/tree/main/packages/wdio-reporter) - A WebdriverIO utility to help report all events
- [@wdio/runner](https://github.com/webdriverio/webdriverio/tree/main/packages/wdio-runner) - A WebdriverIO service that runs tests in arbitrary environments
- [@wdio/utils](https://github.com/webdriverio/webdriverio/tree/main/packages/wdio-utils) - A WDIO helper utility to provide several utility functions used across the project
- [@wdio/globals](https://gith

## tools

Adapters that bring the WebdriverIO DevTools UI to test suites running outside WebdriverIO. These are not WDIO services — they integrate directly with their host runner.

- [@wdio/nightwatch-devtools](https://github.com/webdriverio/devtools/tree/main/packages/nightwatch-devtools) - Nightwatch.js adapter for WebdriverIO DevTools — same visual debugging UI with zero test code changes
- [@wdio/selenium-devtools](https://github.com/webdriverio/devtools/tree/main/packages/selenium-devtools) - Selenium WebDriver adapter for WebdriverIO DevTools — runner-agnostic (Mocha, Jest, Cucumber, or plain Node scripts)

### Runner

- [@wdio/local-runner](https://github.com/webdriverio/webdriverio/tree/main/packages/wdio-local-runner) - A WebdriverIO runner to run tests locally
- [@wdio/browser-runner](https://github.com/webdriverio/webdriverio/tree/main/packages/wdio-browser-runner) - A WebdriverIO runner to run unit or component tests in the browser

### Framework Adapters

- [@wdio/cucumber-framework](https://github.com/webdriverio/webdriverio/tree/main/packages/wdio-cucumber-framework) - Adapter for [Cucumber](https://cucumber.io/) testing framework
- [@wdio/jasmine-framework](https://github.com/webdriverio/webdriverio/tree/main/packages/wdio-jasmine-framework) - Adapter for [Jasmine](https://jasmine.github.io/) testing framework
- [@wdio/mocha-framework](https://github.com/webdriverio/webdriverio/tree/main/packages/wdio-mocha-framework) - Adapter for [Mocha](https://mochajs.org/) testing framework.

### Others

- [create-wdio](https://github.com/webdriverio/webdriverio/tree/main/packages/create-wdio) - A CLI and utility to install and setup a WebdriverIO
- [eslint-plugin-wdio](https://github.com/webdriverio/webdriverio/tree/main/packages/eslint-plugin-wdio) - Eslint rules for WebdriverIO
- [@wdio/smoke-test-reporter](https://github.com/webdriverio/webdriverio/tree/main/packages/wdio-smoke-test-reporter) - A WebdriverIO utility to smoke test reporters for internal testing purposes
- [@wdio/smoke-test-service](https://github.com/webdriverio/webdriverio/tree/main/packages/wdio-smoke-test-service) - A WebdriverIO utility to smoke test services for internal testing purposes
- [@wdio/webdriver-mock-service](https://github.com/webdriverio/webdriverio/tree/main/packages/wdio-webdriver-mock-service) - A WebdriverIO service to stub all endpoints for internal testing purposes

### Infrastructure Packages

These packages are not released to NPM and used to work on this codebase.

- [@wdio/compiler](https://github.com/webdriverio/webdriverio/tree/main/infra/compiler) - Esbuild script to
compile the source code all of all packages
- [@wdio/lerna-patch](https://github.com/webdriverio/webdriverio/tree/main/infra/lernaPatch) - This sub-package is being used to patch Lerna to not run `pnpm install` after it prepared all packages for release

## :handshake: Project Governance

This project is maintained by [awesome people](/AUTHORS.md) following a common [set of rules](/GOVERNANCE.md) and treating each other with [respect and appreciation](/CODE_OF_CONDUCT.md).

## :man_cook: :woman_cook: Backers

[Become a backer](https://opencollective.com/webdriverio) and show your support for our open-source project.

<a href="https://opencollective.com/webdriverio"><img src="https://opencollective.com/webdriverio/tiers/baker.svg?avatarHeight=36&width=600"></a>

## :money_with_wings: Sponsors

Does your company use WebdriverIO? Ask your manager or marketing team if your company would be interested in supporting our project. Support will allow the maintainers to dedicate more time to maintenance and new features for everyone. Also, your company's logo will show [on GitHub](https://github.com/webdriverio/webdriverio#readme) - who doesn't want a little extra exposure? [Here's the info](https://opencollective.com/webdriverio).

<a href="https://opencollective.com/webdriverio"><img src="https://opencollective.com/webdriverio/tiers/gold-sponsor.svg?avatarHeight=36&width=600"><
