# grpc-ecosystem/go-grpc-middleware

Golang gRPC Middlewares: interceptor chaining, auth, logging, retries and more.

## requirements

- **[Go](https://golang.org)**: Any one of the **three latest major** [releases](https://golang.org/doc/devel/release.html) are supported.

## Structure of this repository

The main interceptors are available in the subdirectories of the [`interceptors` directory](interceptors) e.g. [`interceptors/validator`](interceptors/validator), [`interceptors/auth`](interceptors/auth) or [`interceptors/logging`](interceptors/logging).

Some interceptors or utilities of interceptors requires opinionated code that depends on larger amount of dependencies. Those are places in `providers` directory as separate Go module, with separate versioning. For example [`providers/prometheus`](providers/prometheus) offer metrics middleware (there is no "interceptor/metrics" at the moment). The separate module, might be a little bit harder to discover and version in your `go.mod`, but it allows core interceptors to be ultra slim in terms of dependencies.

The [`interceptors` directory](interceptors) also holds generic interceptors that accepts [`Reporter`](interceptors/reporter.go) interface which allows creating your own middlewares with ease.

As you might notice this repository contains multiple modules with different versions ([Go Module specifics](https://github.com/golang/go/wiki/Modules#faqs--multi-module-repositories)). Refer to [versions.yaml](versions.yaml) for current modules. We have main module of version 2.x.y and providers modules of lower versions. Since main module is v2, it's module path ends with `v2`:

```
go get github.com/grpc-ecosystem/go-grpc-middleware/v2/<package>
```

For providers modules and packages, since they are v1, no version is added to the path e.g.

```
go get github.com/grpc-ecosystem/go-grpc-middleware/providers/prometheus
```

## Changes compared to v1

[go-grpc-middleware v1](https://pkg.go.dev/github.com/grpc-ecosystem/go-grpc-middleware) was created near 2015 and became a popular choice for gRPC users. However, many have changed since then. The main changes of v2 compared to v1:

- Path for separate, multiple Go modules in "providers". This allows to add in future specific providers for certain middlewares if needed. This allows interceptors to be extended without the dependency hell to the core framework (e.g. if use some other metric provider, do you want to import prometheus?). This allows greater extensibility.
- Loggers are removed. The [`interceptors/logging`](interceptors/logging) got simplified and writing adapter for each logger is straightforward. For convenience, we will maintain examples for popular providers in [`interceptors/logging/examples`](interceptors/logging/examples), but those are meant to be copied, not imported.
- `grpc_opentracing` interceptor was removed. This is because tracing instrumentation evolved. OpenTracing is deprecated and OpenTelemetry has now a [superior tracing interceptor](https://go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc).
- `grpc_ctxtags` interceptor was removed. Custom tags can be added to logging fields using `logging.InjectFields`. Proto option to add logging field was clunky in practice and we don't see any use of it nowadays, so it's removed.
- One of the most powerful interceptor was imported from https://github.com/grpc-ecosystem/go-grpc-prometheus (repo is now deprecated). This consolidation allows easier maintenance, easier use and consistent API.
- Chain interceptors was removed, because `grpc` implemented one.
- Moved to the new proto API (google.golang.org/protobuf).
- All "deciders", so functions that decide what to do based on gRPC service name and method (aka "fullMethodName") are removed (!). Use [`github.com/grpc-ecosystem/go-grpc-middleware/v2/interceptors/selector`](interceptors/selector) interceptor to select what method, type or service should use what interceptor.
- No more snake case package names. We have now single word meaningful package names. If you have collision in package names we recommend adding grpc pre
