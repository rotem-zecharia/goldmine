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
