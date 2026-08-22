# GoogleChrome/lighthouse

Automated auditing, performance metrics, and best practices for the web.

## tools

Lighthouse is integrated directly into the Chrome DevTools, under the "Lighthouse" panel.

**Installation**: install [Chrome](https://www.google.com/chrome/browser).

**Run it**: open Chrome DevTools, select the Lighthouse panel, and hit "Generate report".

<img width="550" alt="Lighthouse integration in Chrome DevTools." src="https://user-images.githubusercontent.com/2766281/204185043-9c49abe5-baee-4b26-b5ce-ece410661213.png">

## Using the Chrome extension

The Chrome extension was available prior to Lighthouse being available in Chrome Developer Tools, and offers similar functionality.

**Installation**: [install the extension](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) from the Chrome Web Store.

**Run it**: follow the [extension quick-start guide](https://developers.google.com/web/tools/lighthouse/#extension).

## Using the Node CLI

The Node CLI provides the most flexibility in how Lighthouse runs can be configured and reported. Users who want more advanced usage, or want to run Lighthouse in an automated fashion should use the Node CLI.

> [!NOTE]
> Lighthouse requires Node 22 (LTS) or later.

**Installation**:

```sh
npm install -g lighthouse
# or use yarn:
# yarn global add lighthouse
```

**Run it**: `lighthouse https://airhorner.com/`

By default, Lighthouse writes the report to an HTML file. You can control the output format by passing flags.

## configuration

<!-- To update the help output:
  node cli --help | pbcopy
-->

```
$ lighthouse --help

lighthouse <url> <options>

Logging:
  --verbose  Displays verbose logging  [boolean] [default: false]
  --quiet    Displays no progress, debug logs, or errors  [boolean] [default: false]

Configuration:
  --save-assets                  Save the trace contents & devtools logs to disk  [boolean] [default: false]
  --list-all-audits              Prints a list of all available audits and exits  [boolean] [default: false]
  --list-trace-categories        Prints a list of all required trace categories and exits  [boolean] [default: false]
  --additional-trace-categories  Additional categories to capture with the trace (comma-delimited).  [string]
  --config-path                  The path to the config JSON.
                                 An example config file: core/config/lr-desktop-config.js  [string]
  --preset                       Use a built-in configuration.
                                 WARNING: If the --config-path flag is provided, this preset will be ignored.  [string] [choices: "perf", "experimental", "desktop"]
  --chrome-flags                 Custom flags to pass to Chrome (space-delimited). For a full list of flags, see https://bit.ly/chrome-flags
                                 Additionally, use the CHROME_PATH environment variable to use a specific Chrome binary. Requires Chromium version 66.0 or later. If omitted, any detected Chrome Canary or Chrome stable will be used.  [string] [default: ""]
  --port                         The port to use for the debugging protocol. Use 0 for a random port  [number] [default: 0]
  --hostname                     The hostname to use for the debugging protocol.  [string] [default: "localhost"]
  --form-factor                  Determines how performance metrics are scored and if mobile-only audits are skipped. For desktop, use --preset=desktop instead.  [string] [choices: "mobile", "desktop"]
  --screenEmulation              Sets screen emulation parameters. See also --preset. Use --screenEmulation.disabled to disable. Otherwise set these 4 parameters individually: --screenEmulation.mobile --screenEmulation.width=360 --screenEmulation.height=640 --screenEmulation.deviceScaleFactor=2
  --emulatedUserAgent            Sets useragent emulation  [string]
  --max-wait-for-load            The timeout (in milliseconds) to wait before the page is considered done loading and the run should continue. WARNING: Very high values can lead to large traces and instability  [number]
  --enable-error-reporting       Enables error reporting, overriding any saved preference. --no-enable-error-reporting will do the opposite. More: https://github.com/GoogleChrome/lighthouse/blob/main/docs/error-reporting.md  [boolean]
  --gather-mode, -G              Collect artifacts from a connected browser and save to disk. (Artifacts folder path may optionally be provided). If audit-mode is not also enabled, the run will quit early.
  --audit-mode, -A               Process saved artifacts from disk. (Artifacts folder path may be provided, otherwise defaults to ./latest-run/)
  --only-audits                  Only run the specified audits  [array]
  --only-categories              Only run the specified categories. Available categories: accessibility, best-practices, performance, seo  [array]
  --skip-audits                  Run everything except these audits  [array]
  --disable-full-page-screenshot Disables collection of the full page screenshot, which can be quite large  [boolean]

Output:
  --output       Reporter for the results, supports multiple values. choices: "json", "html", "csv"  [array] [default: ["html"]]
  --output-path  The file path to output the results. Use 'stdout' to write to stdout.
                   If using JSON output, default is stdout.
                   If using HTML or CSV output, default is a file in the working directory with a name based on the test URL and date.
                   If using mu

## installation

```sh
# yarn should be installed first

git clone https://github.com/GoogleChrome/lighthouse

cd lighthouse
yarn
yarn build-all
```

### Run

```sh
node cli http://example.com
# append --chrome-flags="--no-sandbox --headless --disable-gpu" if you run into problems connecting to Chrome
```

> **Getting started tip**: `node --inspect-brk cli http://example.com` to open up Chrome DevTools and step
through the entire app. See [Debugging Node.js with Chrome
DevTools](https://medium.com/@paul_irish/debugging-node-js-nightlies-with-chrome-devtools-7c4a1b95ae27#.59rma3ukm)
for more info.

### Tests

```sh
# lint and test all files
yarn test

# run all unit tests
yarn unit

# run a given unit test (e.g. core/test/audits/byte-efficiency/uses-long-cache-ttl-test.js)
yarn mocha uses-long-cache-ttl

# watch for file changes and run tests
#   Requires http://entrproject.org : brew install entr
yarn watch

## run linting, unit, and smoke tests separately
yarn lint
yarn unit
yarn smoke

## run tsc compiler
yarn type-check
```

### Docs

Some of our docs have tests that run only in CI by default. To modify our documentation, you'll need to run `yarn build-pack && yarn test-docs` locally to make sure they pass.

**Additional Dependencies**
- `brew install jq`

## Lighthouse Integrations in Web Perf services

This section details services that have integrated Lighthouse data. If you're working on a cool project integrating Lighthouse and would like to be featured here, file an issue to this repo or tweet at us [@_____lighthouse](https://twitter.com/____lighthouse)!

* **[Web Page Test](https://www.webpagetest.org)** — An [open source](https://github.com/WPO-Foundation/webpagetest) tool for measuring and analyzing the performance of web pages on real devices. Users can choose to produce a Lighthouse report alongside the analysis of WebPageTest results.

* **[HTTPArchive](http://httparchive.org/)** - HTTPArchive tracks how the web is built by crawling 500k pages with Web Page Test, including Lighthouse results, and stores the information in BigQuery where it is [publicly available](https://discuss.httparchive.org/t/quickstart-guide-to-exploring-the-http-archive/682).

* **[Calibre](https://calibreapp.com)** - Calibre is a comprehensive performance monitoring platform running on Lighthouse. See the performance impact of your work before it hits production with GitHub Pull Request Reviews. Track the impact of Third Party scripts. Automate your performance system with a developer-first Node.js API. Try Calibre with a free 15-day trial.

* **[DebugBear](https://www.debugbear.com/)** - DebugBear is a website monitoring tool based on Lighthouse. See how your scores and metrics changed over time, with a focus on understanding what caused each change. DebugBear is a paid product with a free 30-day trial.

* **[Treo](https://treo.sh)** - Treo is Lighthouse as a Service. It provides regression testing, geographical regions, custom networks, and integrations with GitHub & Slack. Treo is a paid product with plans for solo-developers and teams.

* **[PageVitals](https://pagevitals.com)** - PageVitals combines Lighthouse, CrUX and field testing to monitor the performance of websites. See how your website performs over time and get alerted if it gets too slow. Drill down and find the real cause of any performance issue. PageVitals is a paid product with a free 14-day trial.

* **[Screpy](https://screpy.com)** - Screpy is a web analysis tool that can analyze all pages of your websites in one dashboard and monitor them with your team. It's powered by Lighthouse and it also includes some different analysis tools (SERP, W3C, Uptime, etc). Screpy has free and paid plans.

* **[Siteimprove Performance](https://siteimprove.com/en/performance/)** — Siteimprove Performance is a web Performance monitoring solution that enables a marketer, manager or decision maker to understand and optimize website load times. Get easy-to-use insights with a focus on quick and impactful w

## features

Lighthouse reports the performance metrics as they would be experienced by a typical mobile user on a 4G connection and a mid-tier ~$200 phone. Even if it loads quickly on your device and network, users in other environments will experience the site very differently.

Read more in our [guide to throttling](./docs/throttling.md).

### Why does the performance score change so much?

Lighthouse performance scores will change due to inherent variability in web and network technologies, even if there hasn't been a code change. Test in consistent environments, run Lighthouse multiple times, and beware of variability before drawing conclusions about a performance-impacting change.

Read more in our [guide to reducing variability](./docs/variability.md).
