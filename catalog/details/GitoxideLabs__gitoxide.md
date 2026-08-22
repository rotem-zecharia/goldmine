# GitoxideLabs/gitoxide

An idiomatic, lean, fast & safe pure Rust implementation of Git

## features

> Can `gix` do what I need it to do?

The above can be hard to answer and this paragraph is here to help with feature discovery.

Look at [`crate-status.md`](https://github.com/GitoxideLabs/gitoxide/blob/main/crate-status.md) for a rather exhaustive document that contains
both implemented and planned features.

Further, the [`gix` crate documentation with the `git2` search term](https://docs.rs/gix/latest/gix?search=git2) helps to find all currently
known `git2` equivalent method calls. Please note that this list is definitely not exhaustive yet, but might help if you are coming from `git2`.

What follows is a high-level list of features and those which are planned:

* [x] clone
* [x] fetch
* [ ] push
* [x] blame (*plumbing*)
* [x] status
* [x] blob and tree-diff
* [ ] merge
    - [x] blobs
    - [x] trees
    - [ ] commits
* [x] commit
    - [ ] hooks
* [x] commit-graph traversal
* [ ] rebase
* [x] worktree checkout and worktree stream
* [ ] reset
* [x] reading and writing of objects
* [x] reading and writing of refs
* [x] reading and writing of `.git/index`
* [x] reading and writing of git configuration
* [x] pathspecs
* [x] revspecs
* [x] `.gitignore` and `.gitattributes`

### Crates

Follow linked crate name for detailed status. Please note that all crates follow [semver] as well as the [stability guide].

[semver]: https://semver.org

### Production Grade

* **Stability Tier 1**
  - [gix-lock](https://github.com/GitoxideLabs/gitoxide/blob/main/gix-lock/README.md)

* **Stability Tier 2**
  - [gix-tempfile](https://github.com/GitoxideLabs/gitoxide/blob/main/gix-tempfile/README.md)

### Stabilization Candidates

Crates that seem feature complete and need to see some more use before they can be released as 1.0.
Documentation is complete and was reviewed at least once.

* [gix-mailmap](https://github.com/GitoxideLabs/gitoxide/blob/main/crate-status.md#gix-mailmap)
* [gix-chunk](https://github.com/GitoxideLabs/gitoxide/blob/main/crate-status.md#gix-chunk)
* [gix-ref](https://github.com/GitoxideLabs/gitoxide/blob/main/crate-status.md#gix-ref)
* [gix-config](https://github.com/GitoxideLabs/gitoxide/blob/main/crate-status.md#gix-config)
* [gix-config-value](https://github.com/GitoxideLabs/gitoxide/blob/main/crate-status.md#gix-config-value)
* [gix-glob](https://github.com/GitoxideLabs/gitoxide/blob/main/crate-status.md#gix-glob)
* [gix-actor](https://github.com/GitoxideLabs/gitoxide/blob/main/crate-status.md#gix-actor)
* [gix-hash](https://github.com/GitoxideLabs/gitoxide/blob/main/crate-status.md#gix-hash)

### Initial Development

These crates may be missing some features and thus are somewhat incomplete, but what's there
is usable to some extent.

* **usable** _(with rough but complete docs, possibly incomplete functionality)_
  * [gix](https://github.com/GitoxideLabs/gitoxide/blob/main/crate-status.md#gix) (**⬅ entrypoint**)
  * [gix-object](https://github.com/GitoxideLabs/gitoxide/blob/main/crate-status.md#gix-object)
  * [gix-validate](https://github.com/GitoxideLabs/gitoxide/blob/main/crate-status.md#gix-validate)
  * [gix-url](https://github.com/GitoxideLabs/gitoxide/blob/main/crate-status.md#gix-url)
  * [gix-packetline](https://github.com/GitoxideLabs/gitoxide/blob/main/crate-status.md#gix-packetline)
  * [gix-packetline-blocking](https://github.com/GitoxideLabs/gitoxide/blob/main/crate-status.md#gix-packetline)
  * [gix-transport](https://github.com/GitoxideLabs/gitoxide/blob/main/crate-status.md#gix-transport)
  * [gix-protocol](https://github.com/GitoxideLabs/gitoxide/blob/main/crate-status.md#gix-protocol)
  * [gix-pack](https://github.com/GitoxideLabs/gitoxide/blob/main/crate-status.md#gix-pack)
  * [gix-odb](https://github.com/GitoxideLabs/gitoxide/blob/main/crate-status.md#gix-odb)
  * [gix-commitgraph](https://github.com/GitoxideLabs/gitoxide/blob/main/crate-status.md#gix-commitgraph)
  * [gix-diff](https://github.com/GitoxideLabs/gitoxide/blob/main/crate-status.md#gix-diff)
  * [gix-traverse](https://github.com/

## installation

### Download a Binary Release

Using `cargo binstall`, one is able to fetch [binary releases][releases]. You can install it via `cargo install cargo-binstall`, assuming
the [rust toolchain][rustup] is present.

Then install gitoxide with `cargo binstall gitoxide`.

See the [releases section][releases] for manual installation and various alternative builds that are _slimmer_ or _smaller_, depending
on your needs, for _Linux_, _MacOS_ and _Windows_.

[releases]: https://github.com/GitoxideLabs/gitoxide/releases

### Install with Homebrew

For macOS and Linux, `gitoxide` can be installed from [Homebrew](https://brew.sh):

```sh
brew install gitoxide
```

### Download from Arch Linux repository

For Arch Linux you can download `gitoxide` from `community` repository:

```sh
pacman -S gitoxide
```

### Download from Exherbo Linux Rust repository

For Exherbo Linux you can download `gitoxide` from the [Rust](https://gitlab.exherbo.org/exherbo/rust/-/tree/master/packages/dev-scm/gitoxide) repository:

```sh
cave resolve -x repository/rust
cave resolve -x gitoxide
```

### From Source via Cargo

`cargo` is the Rust package manager which can easily be obtained through [rustup]. With it, you can build your own binary
effortlessly and for your particular CPU for additional performance gains.

The minimum supported Rust version is [documented in the Cargo package](https://github.com/GitoxideLabs/gitoxide/blob/main/gix/Cargo.toml#L12-L14),
the latest stable one will work as well.

There are various build configurations, all of them are [documented here](https://docs.rs/crate/gitoxide/latest). The documentation should also be useful
for packagers who need to tune external dependencies.

```sh
# A way to install `gitoxide` with just Rust and a C compiler installed.
# If there are problems with SSL certificates during clones, try to omit `--locked`.
cargo install gitoxide --locked --no-default-features --features max-pure

# The default installation, 'max', is the fastest, but also needs `cmake` to build successfully.
# Installing it is platform-dependent.
cargo install gitoxide

# For smaller binaries and even faster build times that are traded for a less fancy CLI implementation,

## tools

Once installed, there are two binaries:

* **ein**
  * high level commands, _porcelain_, for every-day use, optimized for a pleasant user experience
* **gix**
  * low level commands, _plumbing_, for use in more specialized cases and to validate newly written code in real-world scenarios

## Project Goals

Project goals can change over time as we learn more, and they can be challenged.

 * **a pure-rust implementation of git**
   * including *transport*, *object database*, *references*, *cli* and *tui*
   * a simple command-line interface is provided for the most common git operations, optimized for
     user experience. A *simple-git* if you so will.
   * be the go-to implementation for anyone who wants to solve problems around git, and become
     *the* alternative to `GitPython` and *libgit2* in the process.
   * become the foundation for a distributed alternative to GitHub, and maybe even for use within GitHub itself
 * **learn from the best to write the best possible idiomatic Rust**
   * *libgit2* is a fantastic resource to see what abstractions work, we will use them
   * use Rust's type system to make misuse impossible
 * **be the best performing implementation**
   * use Rust's type system to optimize for work not done without being hard to use
   * make use of parallelism from the get go
   * _sparse checkout_ support from day one
 * **assure on-disk consistency**
   * assure reads never interfere with concurrent writes
   * assure multiple concurrent writes don't cause trouble
 * **take shortcuts, but not in quality**
   * binaries may use `anyhow::Error` exhaustively, knowing these errors are solely user-facing.
   * libraries use light-weight custom errors implemented using `quick-error` or `thiserror`.
   * internationalization is nothing we are concerned with right now.
   * IO errors due to insufficient amount of open file handles don't always lead to operation failure
 * **Cross platform support, including Windows**
   * With the tools and experience available here there is no reason not to support Windows.
   * [Windows is tested on CI](https://github.com/GitoxideLabs/gitoxide/blob/df66d74aa2a8cb62d8a03383135f08c8e8c579a8/.github/workflows/rust.yml#L34)
     and failures do prevent releases.

## Non-Goals

Project non-goals can change over time as we learn more, and they can be challenged.

 * **replicate `git` command functionality perfectly**
   * `git` is `git`, and there is no reason to not use it. Our path is the one of simplicity to make
     getting started with git easy.
 * **be incompatible to git**
   * the on-disk format must remain compatible, and we will never contend with it.
 * **use async IO everywhere**
   * for the most part, git operations are heavily reliant on memory mapped IO as well as CPU to decompress data,
     which doesn't lend itself well to async IO out of the box.
   * Use `blocking` as well as `gix-features::interrupt` to bring operations into the async world and to control
     long running operations.
   * When connecting or streaming over TCP connections, especially when receiving on the server, async seems like a must
     though, but behind a feature flag.

## Contributions

If what you have seen so far sparked your interest to contribute, then let us say: We are happy to have you and help you to get started.

We recommend running `just test` during the development process to assure CI is green before pushing.

A backlog for work ready to be picked up is [available in the Project's Kanban board][project-board], which contains instructions on how
to pick a task. If it's empty or you have other questions, feel free to [start a discussion][discussions] or reach out to @Byron [privately][keybase].

For additional details, also take a look at the [collaboration guide]. If an AI agent communicates through your account,
please follow the [agent impersonation policy].

[agent impersonation policy]: https://github.com/GitoxideLabs/gitoxide/blob/main/CONTRIBUTING.md#prevent-agent-imp

## limitations

Please take a look at the [`SHORTCOMINGS.md` file](https://github.com/GitoxideLabs/gitoxide/blob/main/SHORTCOMINGS.md) for details.

## Credits

* **itertools** _(MIT Licensed)_
  * We use the `izip!` macro in code
* **flate2** _(MIT Licensed)_
  * We use the high-level `flate2` library to implement decompression and compression, which builds on the high-performance `zlib-rs` crate.

## 🙏 Special Thanks 🙏

At least for now this section is exclusive to highlight the incredible support that [Josh Triplett](https://github.com/joshtriplett) has provided to me
in the form of advice, sponsorship and countless other benefits that were incredibly meaningful. Going full time with `gitoxide` would hardly have been
feasible without his involvement, and I couldn't be more grateful 😌.

## License

This project is licensed under either of

 * Apache License, Version 2.0, ([LICENSE-APACHE](LICENSE-APACHE) or
   http://www.apache.org/licenses/LICENSE-2.0)
 * MIT license ([LICENSE-MIT](LICENSE-MIT) or
   http://opensource.org/licenses/MIT)

at your option.

## Fun facts

* Originally @Byron was really fascinated by [this problem](https://github.com/gitpython-developers/GitPython/issues/765#issuecomment-396072153)
  and believes that with `gitoxide` it will be possible to provide the fastest solution for it.
* @Byron has been absolutely blown away by `git` from the first time he experienced git more than 13 years ago, and
  tried to implement it in [various shapes](https://github.com/gitpython-developers/GitPython/pull/1028) and [forms](https://github.com/byron/gogit)
  multiple [times](https://github.com/Byron/gitplusplus). Now with Rust @Byron finally feels to have found the right tool for the job!
