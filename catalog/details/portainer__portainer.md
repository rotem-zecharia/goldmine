# portainer/portainer

Making Docker and Kubernetes management easy.

## installation

- [Deploy Portainer](https://docs.portainer.io/start/install-ce)
- [Documentation](https://docs.portainer.io)
- [Contribute to the project](https://docs.portainer.io/contribute/contribute)

## features

View [this](https://www.portainer.io/features) table to see all of the Portainer CE functionality and compare to Portainer Business.

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

## limitations

Portainer supports "Current - 2 docker versions only. Prior versions may operate, however these are not supported.
