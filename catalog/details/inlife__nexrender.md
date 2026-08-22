# inlife/nexrender

📹 Data-driven render automation for After Effects

## features

* data-driven, dynamic, personalized video rendering
* automated video management, processing, and delivery
* network-oriented project structure, render farm
* highly modular nature, extensive plugin support
* works only in cli mode, never launches After Effects GUI application
* does not require licenses for Adobe After Effects on any worker machine
* free to use and open source

## installation

You can download binaries directly from the [releases](https://github.com/inlife/nexrender/releases) section,
or install them using npm, whichever option works better for you.

However, please note: the npm version of the binaries doesn't include all optional `plugin` packages that are covered in the usage section.
If you wish to install them as well, please do so by providing each one individually:

```
npm i -g @nexrender/cli @nexrender/action-copy @nexrender/action-encode ...
```

## tools

We will be using `nexrender-cli` binary for this example. It's recommended to download/install it if you haven't already.

>⚠ If using WSL check out [wsl support](#wsl)
