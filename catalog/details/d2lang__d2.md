# d2lang/d2

D2 is a modern diagram scripting language that turns text to diagrams.

## installation

The most convenient way to use D2 is to just run it as a CLI executable to
produce SVGs from `.d2` files.

```sh
# First, install D2
curl -fsSL https://d2lang.com/install.sh | sh -s --

echo 'x -> y -> z' > in.d2
d2 --watch in.d2 out.svg
```

A browser window will open with `out.svg` and live-reload on changes to `in.d2`.

## Install

The easiest way to install is with our install script:

```sh
curl -fsSL https://d2lang.com/install.sh | sh -s --
```

You can run the install script with `--dry-run` to see the commands that will be used
to install without executing them.

Or if you have Go installed you can install from source though you won't get the manpage:

```sh
go install github.com/d2lang/d2@latest
```

You can also install a release from source which will include manpages.
See [./docs/INSTALL.md#source-release](./docs/INSTALL.md#source-release).

To uninstall with the install script:

```sh
curl -fsSL https://d2lang.com/install.sh | sh -s -- --uninstall
```

For detailed installation docs, see [./docs/INSTALL.md](./docs/INSTALL.md).
We demonstrate alternative methods and examples for each OS.

As well, the functioning of the install script is described in detail to alleviate any
concern of its use. We recommend using your OS's package manager directly instead for
improved security but the install script is by no means insecure.

## D2 as a library

In addition to being a runnable CLI tool, D2 can also be used to produce diagrams from
Go programs.

For examples, see [./docs/examples/lib](./docs/examples/lib).

## Themes

D2 includes a variety of official themes to style your diagrams beautifully right out of
the box. See [./d2themes](./d2themes) to browse the available themes and make or
contribute your own creation.

## Fonts

D2 ships with "Source Sans Pro" as the font in renders. If you wish to use a different
one, please see [./d2renderers/d2fonts](./d2renderers/d2fonts).

## Export file types

D2 currently supports SVG, PNG and PDF exports. More coming soon.

## Language tooling

D2 is designed with language tooling in mind. D2's parser can parse multiple errors from a
broken program, has an autoformatter, syntax highlighting, and we have plans for LSP's and
more. Good language tooling is necessary for creating and maintaining large diagrams.

The extensions for VSCode and Vim can be found in the [Related](#related) section.

## Plugins

D2 is designed to be extensible and composable. The plugin system allows you to
change out layout engines and customize the rendering pipeline. Plugins can either be
bundled with the build or separately installed as a standalone binary.

**Layout engines**:

- [Dagro](https://github.com/d2lang/dagro) (default, bundled): A native Go port of the
  Dagre directed graph layout engine that produces layered/hierarchical layouts. Based
  on Graphviz's DOT algorithm.
- [elk-go](https://github.com/d2lang/elk-go) (bundled): A native Go port of the ELK
  directed graph layout engine, particularly suited for node-link diagrams with an
  inherent direction and ports.
- [TALA](https://github.com/terrastruct/TALA) (binary): Novel layout engine designed
  specifically for software architecture diagrams. Requires separate install, visit the
  Github page for more.

D2 intends to integrate with a variety of layout engines, e.g. `dot`, as well as
single-purpose layout types like sequence diagrams. You can choose whichever layout engine
you like and works best for the diagram you're making.

Sketch-mode rendering uses [rough-go](https://github.com/d2lang/rough-go), a native Go
compatibility port of the Rough.js 4.6.6 rendering surface used by D2.

LaTeX labels use [mathjax-go](https://github.com/d2lang/mathjax-go), a native Go port of
the MathJax 3.2.2 TeX-to-SVG pipeline.

## Comparison

For a comparison against other popular text-to-diagram tools, see
[https://text-to-diagram.com](https://text-to-diagram.com).

## Contributing

Contributions are welcome! See [./docs/CONTRIBUTING.md](./docs/CONTRIBUTI
