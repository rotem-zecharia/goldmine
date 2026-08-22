# portainer/portainer

Making Docker and Kubernetes management easy.

## installation

- [Deploy Portainer](https://docs.portainer.io/start/install-ce)
- [Documentation](https://docs.portainer.io)
- [Contribute to the project](https://docs.portainer.io/contribute/contribute)

## features

View [this](https://www.portainer.io/features) table to see all of the Portainer CE functionality and compare to Portainer Business.

## Getting help

Portainer CE is an open source project and is supported by the community. You can buy a supported version of Portainer at portainer.io

Learn more about Portainer's community support channels [here.](https://www.portainer.io/resources/get-help/get-support)

- Issues: https://github.com/portainer/portainer/issues
- Slack (chat): [https://portainer.io/slack](https://portainer.io/slack)

You can join the Portainer Community by visiting [https://www.portainer.io/join-our-community](https://www.portainer.io/join-our-community). This will give you advance notice of events, content and other related Portainer content.

## Reporting bugs and contributing

- Want to report a bug or request a feature? Please open [an issue](https://github.com/portainer/portainer/issues/new).
- Want to help us build **_portainer_**? Follow our [contribution guidelines](https://docs.portainer.io/contribute/contribute) to build it locally and make a pull request.

## tools

The frontend consumes a TypeScript API client (SDK functions and request/response types) that is generated from the Go API's Swagger annotations. Regenerate it after any API change — a new endpoint, a changed request/response shape, or a removed endpoint:

```bash
make generate-api
```

This runs the following pipeline:

```
Go Swagger annotations
  → dist/docs/swagger.yaml       (make docs-build, via swaggo/swag)
  → dist/docs/openapi.yaml       (swagger2openapi + validation)
  → app/react/portainer/generated-api/portainer/   (hey-api/openapi-ts)
```

The generator is configured in [`openapi-ts.config.ts`](./openapi-ts.config.ts), which controls the output path, plugins, and tag filters (for example, `deprecated` endpoints and `edge_agent`-tagged routes are excluded).

The generated files live in `app/react/portainer/generated-api/portainer/` and must **not** be edited by hand — your changes would be overwritten on the next run. Import the generated SDK functions and types instead of writing direct HTTP calls:

- `@api/sdk.gen` — SDK functions
- `@api/types.gen` — request/response types

See [Adding api docs](./CONTRIBUTING.md#adding-api-docs) for how to annotate handlers so they are picked up by the generator.

## Security

For information about reporting security vulnerabilities, please see our [Security Policy](SECURITY.md).

## Work for us

If you are a developer, and our code in this repo makes sense to you, we would love to hear from you. We are always on the hunt for awesome devs, either freelance or employed. Drop us a line to success@portainer.io with your details and/or visit our [careers page](https://apply.workable.com/portainer/).

## Privacy

**To make sure we focus our development effort in the right places we need to know which features get used most often. To give us this information we use [Matomo Analytics](https://matomo.org/), which is hosted in Germany and is fully GDPR compliant.**

When Portainer first starts, you are given the option to DISABLE analytics. If you **don't** choose to disable it, we collect anonymous usage as per [our privacy policy](https://www.portainer.io/legal/privacy-policy). **Please note**, there is no personally identifiable information sent or stored at any time and we only use the data to help us improve Portainer.

## limitations

Portainer supports "Current - 2 docker versions only. Prior versions may operate, however these are not supported.

## Licensing

Portainer is licensed under the zlib license. See [LICENSE](./LICENSE) for reference.

Portainer also contains code from open source projects. See [ATTRIBUTIONS.md](./ATTRIBUTIONS.md) for a list.
