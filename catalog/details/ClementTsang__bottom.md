# ClementTsang/bottom

Yet another cross-platform graphical process/system monitor.

## features

As (yet another) process/system visualization and management application, bottom supports the typical features:

- Graphical visualization widgets for:
  - [CPU usage](https://bottom.pages.dev/nightly/usage/widgets/cpu-graph/) over time, at an average and per-core level
  - [RAM and swap usage](https://bottom.pages.dev/nightly/usage/widgets/memory-graph/) over time
  - [Network I/O usage](https://bottom.pages.dev/nightly/usage/widgets/network-graph/) over time
  - [Temperature](https://bottom.pages.dev/nightly/usage/widgets/temperature-graph/) over time
  - [Disk I/O usage](https://bottom.pages.dev/nightly/usage/widgets/disk-io-graph/) over time

  with support for zooming in/out the current time interval displayed.

- Widgets for displaying info about:
  - [Disk capacity/usage](https://bottom.pages.dev/nightly/usage/widgets/disk/)
  - [Temperature sensors](https://bottom.pages.dev/nightly/usage/widgets/temperature-table/)
  - [Battery usage](https://bottom.pages.dev/nightly/usage/widgets/battery/)

- [A process widget](https://bottom.pages.dev/nightly/usage/widgets/process/) for displaying, sorting, and searching info about processes, as well as support for:
  - [Kill signals](https://bottom.pages.dev/nightly/usage/widgets/process/#process-termination)
  - [Tree mode](https://bottom.pages.dev/nightly/usage/widgets/process/#tree-mode)

- [Cross-platform support](https://github.com/ClementTsang/bottom#support) for Linux, macOS, and Windows, with more planned in the future.

- [Customizable behaviour](https://bottom.pages.dev/nightly/configuration/command-line-options/) that can be controlled with command-line options or a config file, such as:
  - Custom and built-in colour themes
  - Customizing widget behaviour
  - Changing the layout of widgets
  - Filtering out entries in some widgets

- And more:
  - [An htop-inspired basic mode](https://bottom.pages.dev/nightly/usage/basic-mode/)
  - [Expansion to focus on just one widget](https://bottom.pages.dev/nightly/usage/general-usage/#expansion)

You can find more details in [the documentation](https://bottom.pages.dev/nightly/usage/general-usage/).

## Support

### Official

bottom _officially_ supports the following operating systems and corresponding architectures:

- macOS (`x86_64`, `aarch64`)
- Linux (`x86_64`, `i686`, `aarch64`)
- Windows (`x86_64`, `i686`)

These platforms are tested to work for the most part and issues on these platforms will be fixed if possible.
Furthermore, binaries are built and tested using the most recent version of stable Rust at the time.

For more details on supported platforms and known problems, check out [the documentation](https://bottom.pages.dev/nightly/support/official/).

### Unofficial

bottom may work on a number of platforms that aren't officially supported. Note that unsupported platforms:

- Might not be tested in CI to build or pass tests (see [here](./.github/workflows/ci.yml) for checked platforms).
- Might not be properly tested by maintainers prior to a stable release.
- May only receive limited support, such as missing features or bugs that may not be fixed.

Note that some unsupported platforms may eventually be officially supported (e.g., FreeBSD).

A non-comprehensive list of some currently unofficially-supported platforms that may compile/work include:

- FreeBSD (`x86_64`)
- Linux (`armv6`, `armv7`, `powerpc64le`, `riscv64gc`, `loongarch64`)
- Android (`arm64`)
- Windows (`arm64`)
- NetBSD (`x86_64`)

For more details on unsupported platforms and known problems, check out [the documentation](https://bottom.pages.dev/nightly/support/unofficial/).

## installation

### Cargo

Installation via `cargo` can be done by installing the [`bottom`](https://crates.io/crates/bottom) crate:

```bash
# You might need to update the stable version of Rust first.
# Other versions might work, but this is not guaranteed.
rustup update stable

# Install the binary from crates.io.
cargo install bottom --locked

# If you use another channel by default, you can specify
# the what channel to use like so:
cargo +stable install bottom --locked

# --locked may be omitted if you wish to not use the
# locked crate versions in Cargo.lock. However, be

## requirements

cargo install bottom
```

Alternatively, you can use `cargo install` using the repo as the source.

```bash
# You might need to update the stable version of Rust first.
# Other versions might work, but this is not guaranteed.
rustup update stable

## tools

You can run bottom using `btm`.

- For help on flags, use `btm -h` for a quick overview or `btm --help` for more details.
- For info on key and mouse bindings, press `?` inside bottom or refer to the [documentation page](https://bottom.pages.dev/nightly/).

You can find more information on usage in the [documentation](https://bottom.pages.dev/nightly/).

## configuration

bottom accepts a number of command-line arguments to change the behaviour of the application as desired.
Additionally, bottom will automatically generate a configuration file on the first launch, which can be changed.

More details on configuration can be found [in the documentation](https://bottom.pages.dev/nightly/configuration/config-file/).

## Troubleshooting

If some things aren't working, give the [troubleshooting page](https://bottom.pages.dev/nightly/troubleshooting)
a look. If things still aren't working, then consider asking [a question](https://github.com/ClementTsang/bottom/discussions)
or filing a [bug report](https://github.com/ClementTsang/bottom/issues/new/choose) if you think it's a bug.

## Documentation

The main documentation page can be found at <https://bottom.pages.dev>, using Cloudflare Pages. If needed, a mirror hosted using
Github Pages is also available at <https://clementtsang.github.io/bottom>.

## Contribution

Whether it's reporting bugs, suggesting features, maintaining packages, or submitting a PR, contribution is always welcome! Please read
[CONTRIBUTING.md](./CONTRIBUTING.md) for details on how to contribute to bottom.

### Contributors

Thanks to all contributors:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="http://shilangyu.github.io"><img src="https://avatars3.githubusercontent.com/u/29288116?v=4?s=100" width="100px;" alt="Marcin Wojnarowski"/><br /><sub><b>Marcin Wojnarowski</b></sub></a><br /><a href="https://github.com/ClementTsang/bottom/commits?author=shilangyu" title="Code">💻</a> <a href="#platform-shilangyu" title="Packaging/porting to new platform">📦</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://neosmart.net/"><img src="https://avatars3.githubusercontent.com/u/606923?v=4?s=100" width="100px;" alt="Mahmoud Al-Qudsi"/><br /><sub><b>Mahmoud Al-Qudsi</b></sub></a><br /><a href="https://github.com/ClementTsang/bottom/commits?author=mqudsi" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://andys8.de"><img src="https://avatars0.githubusercontent.com/u/13085980?v=4?s=100" width="100px;" alt="Andy"/><br /><sub><b>Andy</b></sub></a><br /><a href="https://github.com/ClementTsang/bottom/commits?author=andys8" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/HarHarLinks"><img src="https://avatars0.githubusercontent.com/u/2803622?v=4?s=100" width="100px;" alt="Kim Brose"/><br /><sub><b>Kim Brose</b></sub></a><br /><a href="https://github.com/ClementTsang/bottom/commits?author=HarHarLinks" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://svenstaro.org"><img src="https://avatars0.githubusercontent.com/u/1664?v=4?s=100" width="100px;" alt="Sven-Hendrik Haase"/><br /><sub><b>Sven-Hendrik Haase</b></sub></a><br /><a href="https://github.com/ClementTsang/bottom/commits?author=svenstaro" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://liberapay.com/Artem4/"><img src="https://avatars0.githubusercontent.com/u/5614476?v=4?s=100" width="100px;" alt="Artem Polishchuk"/><br /><sub><b>Artem Polishchuk</b></sub></a><br /><a href="#platform-tim77" title="Packaging/porting to new platform">📦</a> <a href="https://github.com/ClementTsang/bottom/commits?author=tim77" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://ruby-journal.com/"><img src="https://avatars2.githubusercontent.com/u/135605?v=4?s=100" width="100px;" alt="Trung Lê"/><br /><sub><b>Trung Lê</b></sub></a><br /><a href="#platform-runlevel5" title="Packaging/porting to new platform">📦</a> <a href="#infra-runlevel5" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a></td>
    </tr>
    <tr>

