# steel-dev/steel-browser

🔥 Open Source Browser API for AI Agents & Apps. Steel Browser is a batteries-included browser sandbox that lets you automate the web without worrying about infrastructure.

## installation

The easiest way to get started with Steel is by creating a [Steel Cloud](https://app.steel.dev) account. Otherwise, you can deploy this Steel browser instance to a cloud provider or run it locally.

## tools

> If you're looking for quick examples on how to use Steel, check out the [Cookbook](https://github.com/steel-dev/steel-cookbook).
>
> Alternatively you can play with the [REPL package](./repl/README.md) too `cd repl` and `npm run start`

There are two main ways to interact with the Steel browser API:
1. [Using Sessions](#sessions)
2. [Using the Quick Actions Endpoints](#quick-actions-api)

In these examples, we assume your custom Steel API endpoint is `http://localhost:3000`.

The full REST OpenAPI documentation can be found [on our site](https://docs.steel.dev/api-reference) and on your local Steel instance at `http://localhost:3000/documentation`.

#### Using the SDKs
If you prefer to use the our Python and Node SDKs, you can install the `steel-sdk` package for Node or Python.

These SDKs are built on top of the REST API and provide a more convenient way to interact with the Steel browser API. They are fully typed, and are compatible with both Steel Cloud and self-hosted Steel instances (changeable using the `baseURL` option on Node and `base_url` on Python).

For more details on installing and using the SDKs, please see the [Node SDK Reference](https://github.com/steel-dev/steel-node/blob/main/api.md) and the [Python SDK Reference](https://github.com/steel-dev/steel-python/blob/main/api.md).
