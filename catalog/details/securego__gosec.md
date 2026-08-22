# securego/gosec

Go security checker

## features

- **Pattern-based rules** for detecting common security issues
  in Go code
- **SSA-based analyzers** for type conversions, slice bounds,
  and crypto issues
- **Taint analysis** for tracking data flow from user input to
  dangerous functions (SQL injection, command injection, path
  traversal, SSRF, XSS, log injection, SMTP injection, SSTI,
  unsafe deserialization, open redirect)

## installation

gosec requires Go 1.25 or newer.

```bash
go install github.com/securego/gosec/v2/cmd/gosec@latest
```

## tools

Gosec can be configured to only run a subset of rules, to
exclude certain file paths, and produce reports in different
formats. By default all rules will be run against the supplied
input files. To recursively scan from the current directory you
can supply `./...` as the input argument.

## configuration

A number of global settings can be provided in a configuration
file as follows:

```JSON
{
    "global": {
        "nosec": "enabled",
        "audit": "enabled"
    }

## requirements

gosec loads packages using Go modules. In most projects,
dependencies are resolved automatically during scanning.

If dependencies are missing, run:

```bash
go mod tidy
go mod download
```
