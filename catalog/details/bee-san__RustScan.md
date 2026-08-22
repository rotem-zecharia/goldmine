# bee-san/RustScan

🤖 The Modern Port Scanner 🤖

## installation

You can install RustScan's binary from our [releases page](https://github.com/RustScan/RustScan/releases).

We would prefer you to install with a package manager so it is tested and works for your system.

RustScan is in many repositories already. Install it with whatever tools you wish:

[![Packaging status](https://repology.org/badge/vertical-allrepos/rustscan.svg)](https://repology.org/project/rustscan/versions)

RustScan only officially supports Cargo installations, if you want to use that please install Rust and then `cargo install rustscan`

Example installations include:

MacOS:

```
  brew install rustscan
```

Arch:

```
  pacman -S rustscan
```

## features

- Scans all 65k ports in **3 seconds**.
- Full scripting engine support. Automatically pipe results into Nmap, or use our scripts (or write your own) to do whatever you want.
- Adaptive learning. RustScan improves the more you use it. No bloated machine learning here, just basic maths.
- The usuals you would expect. IPv6, CIDR, file input and more.
- Automatically pipes ports into Nmap.

## tools

We have 2 usage guides. [Basic Usage][usage-1] and [Things you may want to do][usage-2].

We also have documentation about our config file [here][config-file-here].
