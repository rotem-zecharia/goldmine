# gruntwork-io/terratest

Terratest is a Go library that makes it easier to write automated tests for your infrastructure code.

## installation

```bash
go get github.com/gruntwork-io/terratest@latest
```

Requires Go 1.26 or later. To lock to a specific release instead of `@latest`, see [Pinning a Terratest version](https://terratest.gruntwork.io/docs/getting-started/version-pinning/).

## Stability and versioning

Starting with v1.0.0, Terratest follows [semantic versioning](https://semver.org/). Breaking changes to the public API
only happen in major releases (e.g. v2.0.0).

Symbols renamed or replaced in v1 are kept with `// Deprecated:` annotations pointing at the new name; removals happen
in v2. Migrating from v0.x: see the [v1 migration guide](https://terratest.gruntwork.io/docs/migrating-to-v1/overview/).

**v1 maintenance.** With v2 in development, the v1 line has entered maintenance: it receives security fixes only,
delivered on the `v1` branch, until 12 months after v2.0.0 reaches general availability. v2 ships under new `/v2`
module paths, so pinned v1 consumers are unaffected. Upgrade on your own schedule.

## More info

- [Terratest Website](https://terratest.gruntwork.io)
- [Getting started with Terratest](https://terratest.gruntwork.io/docs/getting-started/quick-start/)
- [Terratest Documentation](https://terratest.gruntwork.io/docs/)
- [Contributing to Terratest](https://terratest.gruntwork.io/docs/community/contributing/)
- [Commercial Support](https://gruntwork.io/support/)

## License

This code is released under the Apache 2.0 License. Please see [LICENSE](LICENSE) and [NOTICE](NOTICE) for more details.

Copyright &copy; 2025 Gruntwork, Inc.
