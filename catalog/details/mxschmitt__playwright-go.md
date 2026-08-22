# mxschmitt/playwright-go

Playwright for Go a browser automation library to control Chromium, Firefox and WebKit with a single API.

## installation

```shell
go get -u github.com/mxschmitt/playwright-go
```

Install the Playwright driver and browsers (add `--with-deps` to also install the OS dependencies). **Note** that you should replace the version number `0.xxxx.x` with the version used in your current `go.mod`. Each minor version upgrade requires a specific Playwright driver version.

```shell
go run github.com/mxschmitt/playwright-go/cmd/playwright@v0.xxxx.x install --with-deps

## tools

[https://pkg.go.dev/github.com/mxschmitt/playwright-go](https://pkg.go.dev/github.com/mxschmitt/playwright-go)

## features

* **Resilient locators** — find elements the way a user sees the page with `GetByRole`, `GetByLabel`, `GetByPlaceholder`, `GetByText` and `GetByTestId` instead of brittle CSS paths.
* **Auto-wait** — actions such as `Click` and `Fill` wait for the element to be actionable, and web-first assertions created via `playwright.NewPlaywrightAssertions()` retry until the condition is met. No arbitrary sleeps.
* **Full isolation** — every `BrowserContext` is the equivalent of a brand new browser profile at near-zero overhead. Save the authentication state once with `context.StorageState()` and reuse it everywhere.
* **Trace Viewer** — record a trace via `context.Tracing()` and inspect DOM snapshots, network traffic and console logs afterwards with `playwright show-trace`.
* **Network interception** — stub and mock requests with `page.Route()`, or monitor all traffic of a page.
* **Emulation** — mobile devices, geolocation, permissions, color scheme, locale and timezone.
* **Beyond the DOM** — scenarios that span multiple pages, domains and iframes, shadow-piercing selectors, native mouse and keyboard input, file uploads and downloads.
