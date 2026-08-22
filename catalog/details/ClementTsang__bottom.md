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

## installation

cargo install bottom --locked

## requirements

cargo install bottom
```

Alternatively, you can use `cargo install` using the repo as the source.

```bash

## tools

You can run bottom using `btm`.

- For help on flags, use `btm -h` for a quick overview or `btm --help` for more details.
- For info on key and mouse bindings, press `?` inside bottom or refer to the [documentation page](https://bottom.pages.dev/nightly/).

You can find more information on usage in the [documentation](https://bottom.pages.dev/nightly/).

## configuration

bottom accepts a number of command-line arguments to change the behaviour of the application as desired.
Additionally, bottom will automatically generate a configuration file on the first launch, which can be changed.

More details on configuration can be found [in the documentation](https://bottom.pages.dev/nightly/configuration/config-file/).
