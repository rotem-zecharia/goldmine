# go-kratos/kratos

Your ultimate Go microservices framework for the cloud-native era.

## features

- API-first development with Protobuf and generated HTTP/gRPC code.
- Unified [transport](https://go-kratos.dev/docs/component/transport/overview) layer for [HTTP](https://go-kratos.dev/docs/component/transport/http) and [gRPC](https://go-kratos.dev/docs/component/transport/grpc).
- Composable [middleware](https://go-kratos.dev/docs/component/middleware/overview) for recovery, logging, validation, tracing, metrics, auth, and more.
- Pluggable [registry](https://go-kratos.dev/docs/component/registry), [configuration](https://go-kratos.dev/docs/component/config), and [encoding](https://go-kratos.dev/docs/component/encoding) components.
- Standard-library `log/slog` based logging with OpenTelemetry extensions in contrib packages.
- Consistent metadata, errors, validation, OpenAPI, and code-generation workflows.
- A contrib ecosystem for optional integrations such as registries, config stores, middleware, encodings, and observability.

## requirements

- [Go](https://go.dev/dl/) 1.25 or later
- [protoc](https://github.com/protocolbuffers/protobuf)
- [protoc-gen-go](https://github.com/protocolbuffers/protobuf-go)

## installation

```shell
go install github.com/go-kratos/kratos/cmd/kratos/v3@latest
kratos upgrade
```

## Create a Service

```shell
kratos new helloworld
cd helloworld
go mod tidy
kratos run
```

Visit `http://localhost:8000/helloworld/kratos` after the service starts.

For a fuller generated service flow:

```shell
kratos proto add api/helloworld/helloworld.proto
kratos proto client api/helloworld/helloworld.proto
kratos proto server api/helloworld/helloworld.proto -t internal/service
go generate ./...
kratos run
```

## tools

```go
package main

import (
	"github.com/go-kratos/kratos/v3"
	"github.com/go-kratos/kratos/v3/transport/grpc"
	"github.com/go-kratos/kratos/v3/transport/http"
)

func main() {
	httpSrv := http.NewServer(http.Address(":8000"))
	grpcSrv := grpc.NewServer(grpc.Address(":9000"))

	app := kratos.New(
		kratos.Name("helloworld"),
		kratos.Version("v1.0.0"),
		kratos.Server(httpSrv, grpcSrv),
	)
	if err := app.Run(); err != nil {
		panic(err)
	}
}
```

## v3 Migration

Kratos v3 reduces core dependencies and makes previously implicit behavior explicit. Review the [v2 to v3 migration guide](docs/migration/v2-to-v3.md) before upgrading production services.

## Further Reading

- [Documentation](https://go-kratos.dev/docs/getting-started/start)
- [Examples](https://github.com/go-kratos/examples)
- [Project Layout](https://github.com/go-kratos/kratos-layout)
- [v2 to v3 Migration Guide](docs/migration/v2-to-v3.md)
- [Community Contribution Guide](https://go-kratos.dev/docs/community/contribution)

## Development

```shell
make test
make lint
```

## Community

- [Documentation](https://go-kratos.dev/en)
- [WeChat Group](https://github.com/go-kratos/kratos/issues/682)
- [Discord Group](https://discord.gg/BWzJsUJ)
- [Discussions](https://github.com/go-kratos/kratos/discussions)

## Security

If you discover a security vulnerability in Kratos, please contact go-kratos@googlegroups.com. Security reports are handled privately before disclosure.

## Contributors

Thank you for contributing to Kratos. The contribution guide is available in the [Kratos documentation](https://go-kratos.dev/docs/community/contribution).

<a href="https://github.com/go-kratos/kratos/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=go-kratos/kratos" alt="Kratos contributors">
</a>

## Acknowledgments

The following projects influenced Kratos design:

- [go-kit/kit](https://github.com/go-kit/kit)
- [go-micro](https://github.com/asim/go-micro)
- [google/go-cloud](https://github.com/google/go-cloud)
- [go-zero](https://github.com/zeromicro/go-zero)
- [beego](https://github.com/beego/beego)

## License

Kratos is open-sourced software licensed under the [MIT license](./LICENSE).
