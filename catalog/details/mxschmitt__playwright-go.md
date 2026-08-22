# mxschmitt/playwright-go

Playwright for Go a browser automation library to control Chromium, Firefox and WebKit with a single API.

## installation

```shell
go get -u github.com/mxschmitt/playwright-go
```

Install the Playwright driver and browsers (add `--with-deps` to also install the OS dependencies). **Note** that you should replace the version number `0.xxxx.x` with the version used in your current `go.mod`. Each minor version upgrade requires a specific Playwright driver version.

```shell
go run github.com/mxschmitt/playwright-go/cmd/playwright@v0.xxxx.x install --with-deps
# Or
go install github.com/mxschmitt/playwright-go/cmd/playwright@v0.xxxx.x
playwright install --with-deps
```

Alternatively, you can download the driver and browsers from your code. If your operating system lacks the browser dependencies you still need to install them manually, because installing system dependencies requires privileges.

```go
err := playwright.Install()
```

## Documentation

[https://playwright.dev/docs/intro](https://playwright.dev/docs/intro)

The guides, concepts and API semantics are shared across all Playwright languages — only the code samples on that site are written in JavaScript.

## tools

[https://pkg.go.dev/github.com/mxschmitt/playwright-go](https://pkg.go.dev/github.com/mxschmitt/playwright-go)

## Example

The following example crawls the current top voted items from [Hacker News](https://news.ycombinator.com).

```go
package main

import (
	"fmt"
	"log"

	"github.com/mxschmitt/playwright-go"
)

func main() {
	pw, err := playwright.Run()
	if err != nil {
		log.Fatalf("could not start playwright: %v", err)
	}
	browser, err := pw.Chromium.Launch()
	if err != nil {
		log.Fatalf("could not launch browser: %v", err)
	}
	page, err := browser.NewPage()
	if err != nil {
		log.Fatalf("could not create page: %v", err)
	}
	if _, err = page.Goto("https://news.ycombinator.com"); err != nil {
		log.Fatalf("could not goto: %v", err)
	}
	entries, err := page.Locator(".athing").All()
	if err != nil {
		log.Fatalf("could not get entries: %v", err)
	}
	for i, entry := range entries {
		title, err := entry.Locator("td.title > span > a").TextContent()
		if err != nil {
			log.Fatalf("could not get text content: %v", err)
		}
		fmt.Printf("%d: %s\n", i+1, title)
	}
	if err = browser.Close(); err != nil {
		log.Fatalf("could not close browser: %v", err)
	}
	if err = pw.Stop(); err != nil {
		log.Fatalf("could not stop Playwright: %v", err)
	}
}
```

## features

* **Resilient locators** — find elements the way a user sees the page with `GetByRole`, `GetByLabel`, `GetByPlaceholder`, `GetByText` and `GetByTestId` instead of brittle CSS paths.
* **Auto-wait** — actions such as `Click` and `Fill` wait for the element to be actionable, and web-first assertions created via `playwright.NewPlaywrightAssertions()` retry until the condition is met. No arbitrary sleeps.
* **Full isolation** — every `BrowserContext` is the equivalent of a brand new browser profile at near-zero overhead. Save the authentication state once with `context.StorageState()` and reuse it everywhere.
* **Trace Viewer** — record a trace via `context.Tracing()` and inspect DOM snapshots, network traffic and console logs afterwards with `playwright show-trace`.
* **Network interception** — stub and mock requests with `page.Route()`, or monitor all traffic of a page.
* **Emulation** — mobile devices, geolocation, permissions, color scheme, locale and timezone.
* **Beyond the DOM** — scenarios that span multiple pages, domains and iframes, shadow-piercing selectors, native mouse and keyboard input, file uploads and downloads.

## Docker

Refer to the [Dockerfile.example](./Dockerfile.example) to build your own Docker image.
