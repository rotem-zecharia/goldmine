# boyter/scc

Sloc, Cloc and Code: scc is a very fast accurate code counter with complexity calculations and COCOMO estimates written in pure Go

## installation

#### Go Install

You can install `scc` by using the standard go toolchain.

To install the latest stable version of scc:

`go install github.com/boyter/scc/v3@latest`

To install a development version:

`go install github.com/boyter/scc/v3@master`

Note that `scc` needs go version >= 1.25.

#### Snap

A [snap install](https://snapcraft.io/scc) exists thanks to [Ricardo](https://feliciano.tech/).

`$ sudo snap install scc`

*NB* Snap installed applications cannot run outside of `/home` <https://askubuntu.com/questions/930437/permission-denied-error-when-running-apps-installed-as-snap-packages-ubuntu-17> so you may encounter issues if you use snap and attempt to run outside this directory.

#### Homebrew

Or if you have [Homebrew](https://brew.sh/) installed

`$ brew install scc`

#### Fedora

Fedora Linux users can use a [COPR repository](https://copr.fedorainfracloud.org/coprs/lihaohong/scc/):

`$ sudo dnf copr enable lihaohong/scc && sudo dnf install scc`

#### MacPorts

On macOS, you can also install via [MacPorts](https://www.macports.org)

`$ sudo port install scc`

#### Scoop

Or if you are using [Scoop](https://scoop.sh/) on Windows

`$ scoop install scc`

#### Chocolatey

Or if you are using [Chocolatey](https://chocolatey.org/) on Windows

`$ choco install scc`

#### WinGet

Or if you are using [WinGet](https://github.com/microsoft/winget-cli) on Windows

`winget install --id benboyter.scc --source winget`

#### FreeBSD

On FreeBSD, scc is available as a package

`$ pkg install scc`

Or, if you prefer to build from source, you can use the ports tree

`$ cd /usr/ports/devel/scc && make install clean`

### Run in Docker

Go to the directory you want to run scc from.

Run the command below to run the latest release of scc on your current working directory:

```bash
docker run --rm -it -v "$PWD:/pwd:ro" --network none ghcr.io/boyter/scc:master scc /pwd
```

#### Manual

Binaries for Windows, GNU/Linux and macOS for both i386 and x86_64 machines are available from the [releases](https://github.com/boyter/scc/releases) page.

#### GitLab

<https://about.gitlab.com/blog/2023/02/15/code-counting-in-gitlab/>

#### Other

If you would like to assist with getting `scc` added into apt/chocolatey/etc... please submit a PR or at least raise an issue with instructions.

### Background

Read all about how it came to be along with performance benchmarks,

- <https://boyter.org/posts/sloc-cloc-code/>
- <https://boyter.org/posts/why-count-lines-of-code/>
- <https://boyter.org/posts/sloc-cloc-code-revisited/>
- <https://boyter.org/posts/sloc-cloc-code-performance/>
- <https://boyter.org/posts/sloc-cloc-code-performance-update/>

Some reviews of `scc`

- <https://nickmchardy.com/2018/10/counting-lines-of-code-in-koi-cms.html>
- <https://www.feliciano.tech/blog/determine-source-code-size-and-complexity-with-scc/>
- <https://metaredux.com/posts/2019/12/13/counting-lines.html>

Setting up `scc` in GitLab

- <https://about.gitlab.com/blog/2023/02/15/code-counting-in-gitlab/>

A talk given at the first GopherCon AU about `scc` (press S to see speaker notes)

- <https://boyter.org/static/gophercon-syd-presentation/>
- <https://www.youtube.com/watch?v=jd-sjoy3GZo>

For performance see the [Performance](https://github.com/boyter/scc#performance) section

Other similar projects,

- [SLOCCount](https://www.dwheeler.com/sloccount/) the original sloc counter
- [cloc](https://github.com/AlDanial/cloc), inspired by SLOCCount; implemented in Perl for portability
- [gocloc](https://github.com/hhatto/gocloc) a sloc counter in Go inspired by tokei
- [loc](https://github.com/cgag/loc) rust implementation similar to tokei but often faster
- [loccount](https://gitlab.com/esr/loccount) Go implementation written and maintained by ESR
- [polyglot](https://github.com/vmchale/polyglot) ATS sloc counter
- [tokei](https://github.com/XAMPPRocky/tokei) fast, accurate and written in rust
- [sloc](https://github.com/flosse/sloc) coffeescript code counter
- [stto](https:/

## tools

Command line usage of `scc` is designed to be as simple as possible.
Full details can be found in `scc --help` or `scc -h`. Note that the below reflects the state of master not a release, as such
features listed below may be missing from your installation.

```text
$ scc -h
Sloc, Cloc and Code. Count lines of code in a directory with complexity estimation.
Version 4.0.0 (beta)
Ben Boyter <ben@boyter.org> + Contributors
https://github.com/boyter/scc

Usage:
  scc [flags] [files or directories]

Examples:
  Count the current directory:
    scc

  Count a specific folder or file:
    scc myproject/
    scc main.go

  Count several paths at once:
    scc src/ docs/ README.md

  Show a per-file breakdown instead of the per-language summary:
    scc --by-file

  Output as CSV or JSON (e.g. for further processing):
    scc --format csv
    scc --format json -o counts.json

  Count an unrecognised extension as a known language:
    scc --count-as jsp:html

  Count files matching a path pattern as a new category (glob by default):
    scc --count-as-pattern '*_spec.rb:Ruby Spec:Ruby'

  Generate a self-contained HTML infographic report:
    scc --report
    scc --report=out.html --report-title "myrepo" --report-skip cocomo

  Use a project config file (./.sccconfig) or a global one (precedence: global < project < CLI):
    export SCC_CONFIG_PATH=~/.sccconfig
    scc --config team.sccconfig

  Tune the COCOMO cost estimate, or turn it off (see https://en.wikipedia.org/wiki/COCOMO):
    scc --avg-wage 75000 --cocomo-project-type semi-detached
    scc --no-cocomo

Flags:
      --avg-wage int                        average wage value used for basic COCOMO calculation (default 56286)
      --binary                              disable binary file detection
      --buckets int                         time-bucket resolution for the git timeline reports (default 60)
      --by-author                           render the author rollup report (bus factor and last-toucher attribution over recent git history)
      --by-file                             display output for every file
  -m, --character                           calculate max and mean characters per line
      --ci                                  enable CI output settings where stdout is ASCII
      --cocomo-project-type string          change COCOMO model type [organic, semi-detached, embedded, "custom,1,1,1,1"] (default "organic")
      --cognitive                           calculate cognitive (nesting-weighted) complexity
      --config string                       load this file as the global config source; overrides SCC_CONFIG_PATH, honored even with --no-config
      --cost-comparison                     show both COCOMO and LOCOMO estimates side by side
      --count-as string                     count extension as language [e.g. jsp:htm,chead:"C Header" maps extension jsp to html and chead to C Header]
      --count-as-pattern stringArray        count files matching a path pattern as a new named category backed by a base language [repeatable; pattern is glob by default, prefix with re: for regex; e.g. *_spec.rb:"Ruby Spec":Ruby or re:\.test\.js$:"JavaScript Tests":JavaScript]
      --count-ignore                        set to allow .gitignore and .ignore files to be counted
      --count-unsupported                   count files with an unrecognised language under an "Unknown" category as plain text
      --coupling                            render the change-coupling report (file pairs that change together over recent git history)
      --coupling-for string                 blast-radius view: given a file path, show what tends to change with it over recent git history
      --coupling-weighted                   weight coupling by file complexity so pairs of complex files rank above generated/data-file churn (implies --coupling)
      --currency-symbol string              set currency symbol (default "$")
      --debug                               enable debug output
      

## configuration

--ignore-file /home/me/.config/git/ignore
```

```
export SCC_CONFIG_PATH=~/.config/scc/global.sccconfig
scc   # now applies your global ignore on every run
```

### Configuration Files

`scc` can read default flags from a configuration file to avoid creating shell aliases. 
The format is an *opts-list* in the style of ripgrep and bat: the file is simply a list of the same command-line flags 
you would otherwise type, and anything valid on the command line is valid in the file, with the exception
of output flags.

Format rules:

- One flag per line is the recommended style, but multiple whitespace-separated tokens per line are allowed (`--exclude-dir vendor`).
- Lines use the normal `--` prefix, e.g. `--no-cocomo`.
- `#` begins a comment. Whole-line and inline trailing comments are stripped.
- Blank lines are ignored.
- Tokenization is quote-aware, so both `--exclude-dir vendor` and `--count-as 'jsp:html'` work. Quotes (single or double) are the only grouping mechanism; to include a literal quote, switch quote style (`--count-as "a'b"`).
- Backslash is an ordinary literal, not an escape character, so a Windows path such as `--exclude-dir C:\build\out` survives verbatim.
- A line whose first token does not start with `-` (a bare positional such as `src/`) is skipped with a warning, so a config file cannot inject extra count targets.

Example `.sccconfig`:

```
# count the way I like it
--no-cocomo
--exclude-dir vendor,node_modules
--format wide          # default to the wider table
```

#### Sources and discovery

There are two configuration tiers:

- **Global** — there is no fixed default location and no per-run home-directory stat. The global source is consulted only when set explicitly via the `SCC_CONFIG_PATH` environment variable or the `--config <path>` flag. `--config` which overrides `SCC_CONFIG_PATH`.
- **Project** — a file named `.sccconfig` in the current working directory (`./.sccconfig`), found with a single stat and **no walk-up**. `cd project && scc` picks up `project/.sccconfig`; running `scc` from a subdirectory does **not** pick up an ancestor's `.sccconfig`. Path arguments do not move the anchor — `scc ./project` still reads `./.sccconfig`, not `./project/.sccconfig`.

To read the repository root's `.sccconfig` from a subdirectory, pass `--find-root-config`, which walks back from the current directory to the git/hg root. It is off by default and affects config discovery only - it changes which `.sccconfig` is read, not which directory is counted. Outside a repository it degrades to `./.sccconfig`.

#### Precedence

Lowest to highest, later wins: **global config < project config < command line**. Scalar and boolean flags follow last-wins, so the command line always overrides config.

Slice flags (`--exclude-dir`, `--exclude-file`, `--exclude-ext`, `--include-ext`, `--not-match`) **union** instead of overriding:

```
config: --exclude-dir vendor
CLI:    --exclude-dir dist
result: vendor, dist
```

The three slice flags that ship with built-in defaults — `--exclude-dir` (`.git`, `.hg`, `.svn`), `--exclude-file` (the lockfile set) and `--generated-markers` — keep those defaults as a non-removable safety net: a config or CLI value is *added* to the defaults rather than replacing them, so putting `vendor` in `.sccconfig` never stops `scc` skipping `.git`.

#### Config can never write a file

A configuration file can change how `scc` counts and formats, including selecting a stdout format such as `--format json`, but it can **never** cause `scc` to write a file. The file-output flags — `--output` / `-o`, `--report` and `--format-multi` — are honoured only from the command line; the same flags supplied by config are ignored (output goes to stdout, the default). This is because a project `.sccconfig` is auto-discovered, so a cloned repository could otherwise silently overwrite one of your files. Only the command line can make `scc` write to disk.

#### Control flags

| Flag | Effect |
|------|--------|
| `--no-config`

## features

`scc` uses a small state machine in order to determine what state the code is when it reaches a newline `\n`. As such it is aware of and able to count

- Single Line Comments
- Multi Line Comments
- Strings
- Multi Line Strings
- Blank lines

Because of this it is able to accurately determine if a comment is in a string or is actually a comment.

It also attempts to count the complexity of code. This is done by checking for branching operations in the code. For example, each of the following `for if switch while else || && != ==` if encountered in Java would increment that files complexity by one.

### Complexity Estimates

Let's take a minute to discuss the complexity estimate itself.

The complexity estimate is really just a number that is only comparable to files in the same language. It should not be used to compare languages directly without weighting them. The reason for this is that its calculated by looking for branch and loop statements in the code and incrementing a counter for that file.

Because some languages don't have loops and instead use recursion they can have a lower complexity count. Does this mean they are less complex? Probably not, but the tool cannot see this because it does not build an AST of the code as it only scans through it.

Generally though the complexity there is to help estimate between projects written in the same language, or for finding the most complex file in a project `scc --by-file -s complexity` which can be useful when you are estimating on how hard something is to maintain, or when looking for those files that should probably be refactored.

As for how it works.

It's my own definition, but tries to be an approximation of cyclomatic complexity <https://en.wikipedia.org/wiki/Cyclomatic_complexity> although done only on a file level.

The reason it's an approximation is that it's calculated almost for free from a CPU point of view (since its a cheap lookup when counting), whereas a real cyclomatic complexity count would need to parse the code. It gives a reasonable guess in practice though even if it fails to identify recursive methods. The goal was never for it to be exact.

In short when scc is looking through what it has identified as code if it notices what are usually branch conditions it will increment a counter.

The conditions it looks for are compiled into the code and you can get an idea for them by looking at the JSON inside the repository. See <https://github.com/boyter/scc/blob/master/languages.json#L3869> for an example of what it's looking at for a file that's Java.

The increment happens for each of the matching conditions and produces the number you see.

### Unique Lines of Code (ULOC)

ULOC stands for Unique Lines of Code and represents the unique lines across languages, files and the project itself. This idea was taken from
<https://cmcenroe.me/2018/12/14/uloc.html> where the calculation is presented using standard Unix tools `sort -u *.h *.c | wc -l`. This metric is
there to assist with the estimation of complexity within the project. Quoting the source

> In my opinion, the number this produces should be a better estimate of the complexity of a project. Compared to SLOC, not only are blank lines discounted, but so are close-brace lines and other repetitive code such as common includes. On the other hand, ULOC counts comments, which require just as much maintenance as the code around them does, while avoiding inflating the result with license headers which appear in every file, for example.

You can obtain the ULOC by supplying the `-u` or `--uloc` argument to `scc`.

It has a corresponding metric `DRYness %` which is the percentage of ULOC to CLOC or `DRYness = ULOC / SLOC`. The
higher the number the more DRY (don't repeat yourself) the project can be considered. In general a higher value
here is a better as it indicates less duplicated code. The DRYness metric was taken from a comment by minimax <https://lobste.rs/s/has9r7/uloc_unique_lines_code>

To obtain the 
