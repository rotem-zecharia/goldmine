# reviewdog/reviewdog

🐶 Automated code review tool integrated with any code analysis tools regardless of programming language

## installation

```shell
# Install the latest version. (Install it into ./bin/ by default).
$ curl -sfL https://raw.githubusercontent.com/reviewdog/reviewdog/fd59714416d6d9a1c0692d872e38e7f8448df4fc/install.sh | sh -s

# Specify installation directory ($(go env GOPATH)/bin/) and version.
$ curl -sfL https://raw.githubusercontent.com/reviewdog/reviewdog/fd59714416d6d9a1c0692d872e38e7f8448df4fc/install.sh | sh -s -- -b $(go env GOPATH)/bin [vX.Y.Z]

# In alpine linux (as it does not come with curl by default)
$ wget -O - -q https://raw.githubusercontent.com/reviewdog/reviewdog/fd59714416d6d9a1c0692d872e38e7f8448df4fc/install.sh | sh -s [vX.Y.Z]
```

### Nightly releases

You can also use [nightly reviewdog release](https://github.com/reviewdog/nightly)
to try the latest reviewdog improvements every day!

```shell
$ curl -sfL https://raw.githubusercontent.com/reviewdog/nightly/30fccfe9f47f7e6fd8b3c38aa0da11a6c9f04de7/install.sh | sh -s -- -b $(go env GOPATH)/bin
```

### GitHub Action: [reviewdog/action-setup](https://github.com/reviewdog/action-setup)

```yaml
steps:
- uses: reviewdog/action-setup@d8edfce3dd5e1ec6978745e801f9c50b5ef80252 # v1.4.0
  with:
    reviewdog_version: latest # Optional. [latest,nightly,v.X.Y.Z]
```

### homebrew / linuxbrew
You can also install reviewdog using brew:

```shell
$ brew install reviewdog/tap/reviewdog
$ brew upgrade reviewdog/tap/reviewdog
```

### [Scoop](https://scoop.sh/) on Windows

```
> scoop install reviewdog
```

### Build with go install

```shell
$ go install github.com/reviewdog/reviewdog/cmd/reviewdog@latest
```

## Input Format

### 'errorformat'

reviewdog accepts any compiler or linter result from stdin and parses it with
scan-f like [**'errorformat'**](https://github.com/reviewdog/errorformat),
which is the port of Vim's [errorformat](https://vim-jp.org/vimdoc-en/quickfix.html#error-file-format)
feature.

For example, if the result format is `{file}:{line number}:{column number}: {message}`,
errorformat should be `%f:%l:%c: %m` and you can pass it as `-efm` arguments.

```shell
$ golint ./...
comment_iowriter.go:11:6: exported type CommentWriter should have comment or be unexported
$ golint ./... | reviewdog -efm="%f:%l:%c: %m" -diff="git diff FETCH_HEAD"
```

| name | description |
| ---- | ----------- |
| %f | file name |
| %l | line number |
| %c | column number |
| %m | error message |
| %% | the single '%' character |
| ... | ... |

Please see [reviewdog/errorformat](https://github.com/reviewdog/errorformat)
and [:h errorformat](https://vim-jp.org/vimdoc-en/quickfix.html#error-file-format)
if you want to deal with a more complex output. 'errorformat' can handle more
complex output like a multi-line error message.

You can also try errorformat on [the Playground](https://reviewdog.github.io/errorformat-playground/)!

With this 'errorformat' feature, reviewdog can support any tool output with ease.

### Available pre-defined 'errorformat'

But, you don't have to write 'errorformat' in many cases. reviewdog supports
pre-defined errorformat for major tools.

You can find available errorformat name by `reviewdog -list` and you can use it
with `-f={name}`.

```shell
$ reviewdog -list
golint          linter for Go source code                                       - https://github.com/golang/lint
govet           Vet examines Go source code and reports suspicious problems     - https://golang.org/cmd/vet/
sbt             the interactive build tool                                      - http://www.scala-sbt.org/
...
```

```shell
$ golint ./... | reviewdog -f=golint -diff="git diff FETCH_HEAD"
```

You can add supported pre-defined 'errorformat' by contributing to [reviewdog/errorformat](https://github.com/reviewdog/errorformat)

### Reviewdog Diagnostic Format (RDFormat)

reviewdog supports [Reviewdog Diagnostic Format (RDFormat)](./proto/rdf/) as a
generic diagnostic format and it supports both [rdjson](./proto/rdf/#rdjson) and
[rdjsonl](./proto/rdf/#rdjsonl) formats.

This rdformat supports r

## configuration

reviewdog can also be controlled via the .reviewdog.yml configuration file instead of "-f" or "-efm" arguments.

With .reviewdog.yml, you can run the same commands for both CI service and local
environment including editor integration with ease.

#### .reviewdog.yml

```yaml
runner:
  <tool-name>:
    cmd: <command> # (required)
    errorformat: # (optional if you use `format`)
      - <list of errorformat>
    format: <format-name> # (optional if you use `errorformat`. e.g. golint,rdjson,rdjsonl)
    name: <tool-name> # (optional. you can overwrite <tool-name> defined by runner key)
    level: <level> # (optional. same as -level flag. [info,warning,error])

  # examples
  golint:
    cmd: golint ./...
    errorformat:
      - "%f:%l:%c: %m"
    level: warning
  govet:
    cmd: go vet -all .
    format: govet
  your-awesome-linter:
    cmd: awesome-linter run
    format: rdjson
    name: AwesomeLinter
```

```shell
$ reviewdog -diff="git diff FETCH_HEAD"
project/run_test.go:61:28: [golint] error strings should not end with punctuation
project/run.go:57:18: [errcheck]        defer os.Setenv(name, os.Getenv(name))
project/run.go:58:12: [errcheck]        os.Setenv(name, "")
# You can use -runners to run only specified runners.
$ reviewdog -diff="git diff FETCH_HEAD" -runners=golint,govet
project/run_test.go:61:28: [golint] error strings should not end with punctuation
# You can use -conf to specify config file path.
$ reviewdog -conf=./.reviewdog.yml -reporter=github-pr-check
```

Output format for project config based run is one of the following formats.

- `<file>: [<tool name>] <message>`
- `<file>:<lnum>: [<tool name>] <message>`
- `<file>:<lnum>:<col>: [<tool name>] <message>`

## Reporters

reviewdog can report results both in the local environment and review services as
continuous integration.

### Reporter: Local (-reporter=local) [default]

reviewdog can find newly introduced findings by filtering linter results
using diff. You can pass the diff command as `-diff` arg.

```shell
$ golint ./... | reviewdog -f=golint -diff="git diff FETCH_HEAD"
```

### Reporter: GitHub PR Checks (-reporter=github-pr-check)

[![github-pr-check sample annotation with option 1](https://user-images.githubusercontent.com/3797062/64875597-65016f80-d688-11e9-843f-4679fb666f0d.png)](https://github.com/reviewdog/reviewdog/pull/275/files#annotation_6177941961779419)
[![github-pr-check sample](https://user-images.githubusercontent.com/3797062/40884858-6efd82a0-6756-11e8-9f1a-c6af4f920fb0.png)](https://github.com/reviewdog/reviewdog/pull/131/checks)

github-pr-check reporter reports results to [GitHub Checks](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks).

You can change the report level for this reporter by `level` field in [config
file](#reviewdog-config-file) or `-level` flag. You can control GitHub status
check results with this feature. (default: error)

| Level     | GitHub Status |
| --------- | ------------- |
| `info`    | neutral       |
| `warning` | neutral       |
| `error`   | failure       |

There are two options to use this reporter.

#### Option 1) Run reviewdog from GitHub Actions w/ secrets.GITHUB_TOKEN

Example: [.github/workflows/reviewdog.yml](.github/workflows/reviewdog.yml)

```yaml
- name: Run reviewdog
  env:
    REVIEWDOG_GITHUB_API_TOKEN: ${{ secrets.GITHUB_TOKEN }}
  run: |
    golint ./... | reviewdog -f=golint -reporter=github-pr-check
```

See [GitHub Actions](#github-actions) section too. You can also use public
reviewdog GitHub Actions.

#### Option 2) Install reviewdog GitHub Apps
reviewdog CLI sends a request to reviewdog GitHub App server and the server post
results as GitHub Checks, because Check API is only supported for GitHub App and
GitHub Actions.

1. Install reviewdog Apps. https://github.com/apps/reviewdog
2. Set `REVIEWDOG_TOKEN`.
  - Get token from `https://reviewdog.app/gh/{owner}/{repo-name}`.

``

## features

Example: [.github/workflows/reviewdog.yml](.github/workflows/reviewdog.yml)

```yaml
name: reviewdog
on: [pull_request]
jobs:
  reviewdog:
    name: reviewdog
    runs-on: ubuntu-latest
    steps:
      # ...
      - uses: reviewdog/action-setup@d8edfce3dd5e1ec6978745e801f9c50b5ef80252 # v1.4.0
        with:
          reviewdog_version: latest # Optional. [latest,nightly,v.X.Y.Z]
      - name: Run reviewdog
        env:
          REVIEWDOG_GITHUB_API_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          reviewdog -reporter=github-pr-check -runners=golint,govet
          # or
          reviewdog -reporter=github-pr-review -runners=golint,govet
```

<details>
<summary><strong>Example (github-check reporter):</strong></summary>

[.github/workflows/reviewdog](.github/workflows/reviewdog.yml)

Only `github-check` reporter can run on the push event too.

```yaml
name: reviewdog (github-check)
on:
  push:
    branches:
      - master
  pull_request:

jobs:
  reviewdog:
    name: reviewdog
    runs-on: ubuntu-latest
    steps:
      # ...
      - name: Run reviewdog
        env:
          REVIEWDOG_GITHUB_API_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          reviewdog -reporter=github-check -runners=golint,govet
```

</details>

#### Public Reviewdog GitHub Actions
You can use public GitHub Actions to start using reviewdog with ease! :tada: :arrow_forward: :tada:

- Common
  - [reviewdog/action-misspell](https://github.com/reviewdog/action-misspell) - Run [misspell](https://github.com/client9/misspell).
  - [EPMatt/reviewdog-action-prettier](https://github.com/EPMatt/reviewdog-action-prettier) - Run [Prettier](https://prettier.io/).
- Text
  - [reviewdog/action-alex](https://github.com/reviewdog/action-alex) - Run [alex](https://github.com/get-alex/alex) which catches insensitive, inconsiderate writing. (e.g. master/slave)
  - [reviewdog/action-languagetool](https://github.com/reviewdog/action-languagetool) - Run [languagetool](https://github.com/languagetool-org/languagetool).
  - [tsuyoshicho/action-textlint](https://github.com/tsuyoshicho/action-textlint) - Run [textlint](https://github.com/textlint/textlint)
  - [tsuyoshicho/action-redpen](https://github.com/tsuyoshicho/action-redpen) - Run [redpen](https://github.com/redpen-cc/redpen)
- Markdown
  - [reviewdog/action-markdownlint](https://github.com/reviewdog/action-markdownlint) - Run [markdownlint](https://github.com/DavidAnson/markdownlint)
- Docker
  - [reviewdog/action-hadolint](https://github.com/reviewdog/action-hadolint) - Run [hadolint](https://github.com/hadolint/hadolint) to lint `Dockerfile`.
- Env
  - [dotenv-linter/action-dotenv-linter](https://github.com/dotenv-linter/action-dotenv-linter) - Run [dotenv-linter](https://github.com/dotenv-linter/dotenv-linter) to lint `.env` files.
- Shell script
  - [reviewdog/action-shellcheck](https://github.com/reviewdog/action-shellcheck) - Run [shellcheck](https://github.com/koalaman/shellcheck).
  - [reviewdog/action-shfmt](https://github.com/reviewdog/action-shfmt) - Run [shfmt](https://github.com/mvdan/sh).
- Go
  - [reviewdog/action-staticcheck](https://github.com/reviewdog/action-staticcheck) - Run [staticcheck](https://staticcheck.io/).
  - [reviewdog/action-golangci-lint](https://github.com/reviewdog/action-golangci-lint) - Run [golangci-lint](https://github.com/golangci/golangci-lint) and supported linters individually by golangci-lint.
- JavaScript
  - [reviewdog/action-eslint](https://github.com/reviewdog/action-eslint) - Run [eslint](https://github.com/eslint/eslint).
  - [mongolyy/reviewdog-action-biome](https://github.com/mongolyy/reviewdog-action-biome) - Run [Biome](https://biomejs.dev/).
- TypeScript
  - [EPMatt/reviewdog-action-tsc](https://github.com/EPMatt/reviewdog-action-tsc) - Run [tsc](https://www.typescriptlang.org/docs/handbook/compiler-options.html).
- CSS
  - [reviewdog/action-stylelint](https://github.com/reviewdog/action-stylelint) - Run [stylelint](https://github.com/stylelint/style

## tools

$ REVIEWDOG_GITHUB_API_TOKEN="<token>" reviewdog -reporter=github-pr-review
# Or, to submit directly via API using github-pr-check reporter (requires GitHub App Account configured)
$ REVIEWDOG_SKIP_DOGHOUSE=true REVIEWDOG_GITHUB_API_TOKEN="<token>" reviewdog -reporter=github-pr-check
```

## Exit codes
By default (`-fail-level=none`) reviewdog will return `0` as exit code even if it finds errors.
reviewdog will exit with code 1 with `-fail-level=[any,info,warning,error]` flag if it finds at least 1 issue with severity greater than or equal to the given level.
This can be helpful when you are using it as a step in your CI pipeline and want to mark the step failed if any error found by linter.

You can also use `-level` flag to configure default report revel.

## Filter mode
reviewdog filter results by diff and you can control how reviewdog filter results by `-filter-mode` flag.
Available filter modes are as below.

### `added` (default)
Filter results by added/modified lines.
### `diff_context`
Filter results by diff context. i.e. changed lines +-N lines (N=3 for example).
### `file`
Filter results by added/modified file. i.e. reviewdog will report results as long as they are in added/modified file even if the results are not in actual diff.
### `nofilter`
Do not filter any results. Useful for posting results as comments as much as possible and check other results in console at the same time.

`-fail-on-error` also works with any filter-mode and can catch all results from any linters with `nofilter` mode.

Example:
```shell
$ reviewdog -reporter=github-pr-review -filter-mode=nofilter -fail-on-error
```

### Filter Mode Support Table
Note that not all reporters provide full support for filter mode due to API limitation.
e.g. `github-pr-review` reporter uses [GitHub Review
API](https://docs.github.com/en/rest/pulls/reviews) but this API don't support posting comments outside diff context,
so reviewdog will use [Check annotation](https://docs.github.com/en/rest/checks/runs) as fallback to post those comments [1]. 

| `-reporter` \ `-filter-mode` | `added` | `diff_context` | `file`                  | `nofilter` |
| ---------------------------- | ------- | -------------- | ----------------------- | ---------- |
| **`local`**                  | OK      | OK             | OK                      | OK |
| **`github-check`**           | OK      | OK             | OK                      | OK |
| **`github-pr-check`**        | OK      | OK             | OK                      | OK |
| **`github-pr-review`**       | OK      | OK             | Partially Supported [1] | Partially Supported [1] |
| **`github-pr-annotations`**  | OK      | OK             | OK                      | OK |
| **`gitlab-mr-discussion`**   | OK      | OK             | OK                      | Partially Supported [2] |
| **`gitlab-mr-commit`**       | OK      | Partially Supported [2] | Partially Supported [2] | Partially Supported [2] |
| **`gerrit-change-review`**   | OK      | OK? [3]        | OK? [3]                 | Partially Supported? [2][3] |
| **`bitbucket-code-report`**  | NO [4]  | NO [4]         | NO [4]                  | OK |
| **`gitea-pr-review`**        | OK      | OK             | Partially Supported [2] | Partially Supported [2] |

- [1] Report results that are outside the diff file with Check annotation as fallback if it's running in GitHub actions instead of Review API (comments). All results will be reported to console as well.
- [2] Report results that are outside the diff file to console.
- [3] It should work, but not been verified yet.
- [4] Not implemented at the moment

## Debugging

Use the `-tee` flag to show debug info.

```shell
reviewdog -filter-mode=nofilter -tee
```

## Articles
- [reviewdog — A code review dog who keeps your codebase healthy ](https://medium.com/@haya14busa/reviewdog-a-code-review-dog-who-keeps-your-codebase-healthy-d957c471938b)
- [reviewdog ♡ GitHub Check — improved automated review experience](https://medium.
