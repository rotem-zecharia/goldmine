# BurntSushi/ripgrep

ripgrep recursively searches directories for a regex pattern while respecting your gitignore

## tools

This example searches the entire
[Linux kernel source tree](https://github.com/BurntSushi/linux)
(after running `make defconfig && make -j8`) for `[A-Z]+_SUSPEND`, where
all matches must be words. Timings were collected on a system with an Intel
i9-12900K 5.2 GHz.

Please remember that a single benchmark is never enough! See my
[blog post on ripgrep](https://blog.burntsushi.net/ripgrep/)
for a very detailed comparison with more benchmarks and analysis.

| Tool | Command | Line count | Time |
| ---- | ------- | ---------- | ---- |
| ripgrep (Unicode) | `rg -n -w '[A-Z]+_SUSPEND'` | 536 | **0.082s** (1.00x) |
| [hypergrep](https://github.com/p-ranav/hypergrep) | `hgrep -n -w '[A-Z]+_SUSPEND'` | 536 | 0.167s (2.04x) |
| [git grep](https://www.kernel.org/pub/software/scm/git/docs/git-grep.html) | `git grep -P -n -w '[A-Z]+_SUSPEND'` | 536 | 0.273s (3.34x) |
| [The Silver Searcher](https://github.com/ggreer/the_silver_searcher) | `ag -w '[A-Z]+_SUSPEND'` | 534 | 0.443s (5.43x) |
| [ugrep](https://github.com/Genivia/ugrep) | `ugrep -r --ignore-files --no-hidden -I -w '[A-Z]+_SUSPEND'` | 536 | 0.639s (7.82x) |
| [git grep](https://www.kernel.org/pub/software/scm/git/docs/git-grep.html) | `LC_ALL=C git grep -E -n -w '[A-Z]+_SUSPEND'` | 536 | 0.727s (8.91x) |
| [git grep (Unicode)](https://www.kernel.org/pub/software/scm/git/docs/git-grep.html) | `LC_ALL=en_US.UTF-8 git grep -E -n -w '[A-Z]+_SUSPEND'` | 536 | 2.670s (32.70x) |
| [ack](https://github.com/beyondgrep/ack3) | `ack -w '[A-Z]+_SUSPEND'` | 2677 | 2.935s (35.94x) |

Here's another benchmark on the same corpus as above that disregards gitignore
files and searches with a whitelist instead. The corpus is the same as in the
previous benchmark, and the flags passed to each command ensure that they are
doing equivalent work:

| Tool | Command | Line count | Time |
| ---- | ------- | ---------- | ---- |
| ripgrep | `rg -uuu -tc -n -w '[A-Z]+_SUSPEND'` | 447 | **0.063s** (1.00x) |
| [ugrep](https://github.com/Genivia/ugrep) | `ugrep -r -n --include='*.c' --include='*.h' -w '[A-Z]+_SUSPEND'` | 447 | 0.607s (9.62x) |
| [GNU grep](https://www.gnu.org/software/grep/) | `grep -E -r -n --include='*.c' --include='*.h' -w '[A-Z]+_SUSPEND'` | 447 | 0.674s (10.69x) |

Now we'll move to searching on single large file. Here is a straight-up
comparison between ripgrep, ugrep and GNU grep on a file cached in memory
(~13GB, [`OpenSubtitles.raw.en.gz`](https://object.pouta.csc.fi/OPUS-OpenSubtitles/v2018/mono/en.txt.gz), decompressed):

| Tool | Command | Line count | Time |
| ---- | ------- | ---------- | ---- |
| ripgrep (Unicode) | `rg -w 'Sherlock [A-Z]\w+'` | 7882 | **1.042s** (1.00x) |
| [ugrep](https://github.com/Genivia/ugrep) | `ugrep -w 'Sherlock [A-Z]\w+'` | 7882 | 1.339s (1.28x) |
| [GNU grep (Unicode)](https://www.gnu.org/software/grep/) | `LC_ALL=en_US.UTF-8 egrep -w 'Sherlock [A-Z]\w+'` | 7882 | 6.577s (6.31x) |

In the above benchmark, passing the `-n` flag (for showing line numbers)
increases the times to `1.664s` for ripgrep and `9.484s` for GNU grep. ugrep
times are unaffected by the presence or absence of `-n`.

Beware of performance cliffs though:

| Tool | Command | Line count | Time |
| ---- | ------- | ---------- | ---- |
| ripgrep (Unicode) | `rg -w '[A-Z]\w+ Sherlock [A-Z]\w+'` | 485 | **1.053s** (1.00x) |
| [GNU grep (Unicode)](https://www.gnu.org/software/grep/) | `LC_ALL=en_US.UTF-8 grep -E -w '[A-Z]\w+ Sherlock [A-Z]\w+'` | 485 | 6.234s (5.92x) |
| [ugrep](https://github.com/Genivia/ugrep) | `ugrep -w '[A-Z]\w+ Sherlock [A-Z]\w+'` | 485 | 28.973s (27.51x) |

And performance can drop precipitously across the board when searching big
files for patterns without any opportunities for literal optimizations:

| Tool | Command | Line count | Time |
| ---- | ------- | ---------- | ---- |
| ripgrep | `rg '[A-Za-z]{30}'` | 6749 | **15.569s** (1.00x) |
| [ugrep](https://github.com/Genivia/ugrep) | `ugrep -E '[A-Za-z]{30}'` | 6749 | 21.857s (1.40x) |
| [GNU grep](https://www.gnu.org

## features

* It can replace many use cases served by other search tools
  because it contains most of their features and is generally faster. (See
  [the FAQ](FAQ.md#posix4ever) for more details on whether ripgrep can truly
  replace grep.)
* Like other tools specialized to code search, ripgrep defaults to
  [recursive search](GUIDE.md#recursive-search) and does [automatic
  filtering](GUIDE.md#automatic-filtering). Namely, ripgrep won't search files
  ignored by your `.gitignore`/`.ignore`/`.rgignore` files, it won't search
  hidden files and it won't search binary files. Automatic filtering can be
  disabled with `rg -uuu`.
* ripgrep can [search specific types of files](GUIDE.md#manual-filtering-file-types).
  For example, `rg -tpy foo` limits your search to Python files and `rg -Tjs
  foo` excludes JavaScript files from your search. ripgrep can be taught about
  new file types with custom matching rules.
* ripgrep supports many features found in `grep`, such as showing the context
  of search results, searching multiple patterns, highlighting matches with
  color and full Unicode support. Unlike GNU grep, ripgrep stays fast while
  supporting Unicode (which is always on).
* ripgrep has optional support for switching its regex engine to use PCRE2.
  Among other things, this makes it possible to use look-around and
  backreferences in your patterns, which are not supported in ripgrep's default
  regex engine. PCRE2 support can be enabled with `-P/--pcre2` (use PCRE2
  always) or `--auto-hybrid-regex` (use PCRE2 only if needed). An alternative
  syntax is provided via the `--engine (default|pcre2|auto)` option.
* ripgrep has [rudimentary support for replacements](GUIDE.md#replacements),
  which permit rewriting output based on what was matched.
* ripgrep supports [searching files in text encodings](GUIDE.md#file-encoding)
  other than UTF-8, such as UTF-16, latin-1, GBK, EUC-JP, Shift_JIS and more.
  (Some support for automatically detecting UTF-16 is provided. Other text
  encodings must be specifically specified with the `-E/--encoding` flag.)
* ripgrep supports searching files compressed in a common format (brotli,
  bzip2, gzip, lz4, lzma, xz, or zstandard) with the `-z/--search-zip` flag.
* ripgrep supports
  [arbitrary input preprocessing filters](GUIDE.md#preprocessor)
  which could be PDF text extraction, less supported decompression, decrypting,
  automatic encoding detection and so on.
* ripgrep can be configured via a
  [configuration file](GUIDE.md#configuration-file).

In other words, use ripgrep if you like speed, filtering by default, fewer
bugs and Unicode support.

## installation

The binary name for ripgrep is `rg`.

**[Archives of precompiled binaries for ripgrep are available for Windows,
macOS and Linux.](https://github.com/BurntSushi/ripgrep/releases)** Linux and
Windows binaries are static executables. Users of platforms not explicitly
mentioned below are advised to download one of these archives.

If you're a **macOS Homebrew** or a **Linuxbrew** user, then you can install
ripgrep from homebrew-core:

```
$ brew install ripgrep
```

If you're a **MacPorts** user, then you can install ripgrep from the
[official ports](https://www.macports.org/ports.php?by=name&substr=ripgrep):

```
$ sudo port install ripgrep
```

If you're a **Windows Chocolatey** user, then you can install ripgrep from the
[official repo](https://chocolatey.org/packages/ripgrep):

```
$ choco install ripgrep
```

If you're a **Windows Scoop** user, then you can install ripgrep from the
[official bucket](https://github.com/ScoopInstaller/Main/blob/master/bucket/ripgrep.json):

```
$ scoop install ripgrep
```

If you're a **Windows Winget** user, then you can install ripgrep from the
[winget-pkgs](https://github.com/microsoft/winget-pkgs/tree/master/manifests/b/BurntSushi/ripgrep)
repository:

```
$ winget install BurntSushi.ripgrep.MSVC
```

If you're an **Arch Linux** user, then you can install ripgrep from the official repos:

```
$ sudo pacman -S ripgrep
```

If you're a **Gentoo** user, you can install ripgrep from the
[official repo](https://packages.gentoo.org/packages/sys-apps/ripgrep):

```
$ sudo emerge sys-apps/ripgrep
```

If you're a **Fedora** user, you can install ripgrep from official
repositories.

```
$ sudo dnf install ripgrep
```

If you're an **openSUSE** user, ripgrep is included in **openSUSE Tumbleweed**
and **openSUSE Leap** since 15.1.

```
$ sudo zypper install ripgrep
```

If you're a **CentOS Stream 10** user, you can install ripgrep from the
[EPEL](https://docs.fedoraproject.org/en-US/epel/getting-started/) repository:

```
$ sudo dnf config-manager --set-enabled crb
$ sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-10.noarch.rpm
$ sudo dnf install ripgrep
```

If you're a **Red Hat 10** user, you can install ripgrep from the
[EPEL](https://docs.fedoraproject.org/en-US/epel/getting-started/) repository:

```
$ sudo subscription-manager repos --enable codeready-builder-for-rhel-10-$(arch)-rpms
$ sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-10.noarch.rpm
$ sudo dnf install ripgrep
```

If you're a **Rocky Linux 10** user, you can install ripgrep from the
[EPEL](https://docs.fedoraproject.org/en-US/epel/getting-started/) repository:

```
$ sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-10.noarch.rpm
$ sudo dnf install ripgrep
```

If you're a **Nix** user, you can install ripgrep from
[nixpkgs](https://github.com/NixOS/nixpkgs/blob/master/pkgs/by-name/ri/ripgrep/package.nix):

```
$ nix-env --install ripgrep
```

If you're a **Flox** user, you can install ripgrep as follows:

```
$ flox install ripgrep
```

If you're a **Guix** user, you can install ripgrep from the official
package collection:

```
$ guix install ripgrep
```

If you're a **Debian** user (or a user of a Debian derivative like **Ubuntu**),
then ripgrep can be installed using a binary `.deb` file provided in each
[ripgrep release](https://github.com/BurntSushi/ripgrep/releases).

```
$ curl -LO https://github.com/BurntSushi/ripgrep/releases/download/14.1.1/ripgrep_14.1.1-1_amd64.deb
$ sudo dpkg -i ripgrep_14.1.1-1_amd64.deb
```

If you run Debian stable, ripgrep is [officially maintained by
Debian](https://tracker.debian.org/pkg/rust-ripgrep), although its version may
be older than the `deb` package available in the previous step.

```
$ sudo apt-get install ripgrep
```

If you're an **Ubuntu Cosmic (18.10)** (or newer) user, ripgrep is
[available](https://launchpad.net/ubuntu/+source/rust-ripgrep) using the same
packaging as Debian:

```
$ sudo apt-get in
