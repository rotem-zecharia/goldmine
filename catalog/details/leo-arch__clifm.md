# leo-arch/clifm

💾 The shell-like, command-line terminal file manager

## features

<details>
<summary>Click here to expand</summary>

In addition to common file operations, such as copy, move, remove, etc., **clifm** provides the following features:
- Specific
  - [Really CLI-based](https://github.com/leo-arch/clifm/wiki/Introduction#main-design-and-goals). No GUI nor TUI at all, but just a command-line
  - It can run on the kernel built-in console and even on a SSH or any other remote session
  - Highly compatible with old VT102-only terminal emulators like Rxvt and Rxvt-based ones: even on a terminal with only 8 colors and no Unicode support, **clifm** will just work. [It can run even on an old DEC-VT100 terminal!](https://github.com/leo-arch/clifm/wiki/Extra#clifm-running-on-a-dec-vt100-terminal-1978)
  - [High performance](https://github.com/leo-arch/clifm/wiki/Performance). Incredibly lightweight and fast even on really old hardware
  - [Short (and even one-character) commands](https://github.com/leo-arch/clifm/wiki/Introduction#commands-short-summary)
  - [Entry list numbers (ELNs)](https://github.com/leo-arch/clifm/wiki/Common-Operations#elns) for filenames
  - [Extended color codes](https://github.com/leo-arch/clifm/wiki/Customization#colors) for file types and file extensions
  - [File counter](https://github.com/leo-arch/clifm/wiki/Introduction#interface) for directories and symlinks to directories
  - Support for files attributes, extended attributes, birth time, BSD flags, and Solaris doors.
  - Privacy: Zero data collection and no connection to the outside world at all
  - Security: [Secure environment](https://github.com/leo-arch/clifm/wiki/Specifics#security) and [secure commands](https://github.com/leo-arch/clifm/wiki/Specifics#security). See also the [stealth mode section](https://github.com/leo-arch/clifm/wiki/Specifics#stealth-mode)
- Navigation and file operations
  - [Bookmarks](https://github.com/leo-arch/clifm/wiki/Common-Operations#bookmarks)
  - [File selection](https://github.com/leo-arch/clifm/wiki/Common-Operations#selection) (supports both glob and regular expressions, and works even across multiple instances of the program)
  - [File opener](https://github.com/leo-arch/clifm/wiki/Specifics#file-opener) (supports regular expressions and is able to discern between GUI and non-GUI environments)
  - [File previews](https://github.com/leo-arch/clifm/wiki/Advanced#files-preview) (including [image previews](https://github.com/leo-arch/clifm/tree/master/misc/tools/imgprev))
  - [File tags](https://github.com/leo-arch/clifm/wiki/Common-Operations#tagging-files)
  - [File filters](https://github.com/leo-arch/clifm/wiki/Advanced#files-filters) (including support for [`.hidden` files](https://github.com/leo-arch/clifm/wiki/Advanced#1b-hidden-files))
  - [File search](https://github.com/leo-arch/clifm/wiki/Common-Operations#searching) (supports both glob and regular expressions)
  - [File templates](https://github.com/leo-arch/clifm/wiki/Introduction#n-new)
  - [Filenames sanitizer](https://github.com/leo-arch/clifm/wiki/Introduction#bb-bleach)
  - [A Freedesktop-compliant trash system](https://github.com/leo-arch/clifm/wiki/Common-Operations#trashing-files)
  - [copy(-as), move(-as)](https://github.com/leo-arch/clifm/wiki/Introduction#c-l-e-edit-m-md-r), [interactive rename](https://github.com/leo-arch/clifm/wiki/Introduction#c-l-e-edit-m-md-r), and [open-with](https://github.com/leo-arch/clifm/wiki/Introduction#ow) functions
  - [Bulk operations](https://github.com/leo-arch/clifm/wiki/Advanced#bulk-operations): rename, create, remove, and create symbolic links in bulk
  - [File encryption/decryption (plugin)](https://github.com/leo-arch/clifm/wiki/Advanced#plugins)
  - [Archiving and compression](https://github.com/leo-arch/clifm/wiki/Advanced#archives) support (including Zstandard and ISO 9660)
  - [Symlinks editor](https://github.com/leo-arch/clifm/wiki/Introduction#l-le)
  - File permissions/ownership editor via the [`pc`](https://github.com/leo-arch/clifm/wiki/Introduction#pc) and [`oc

## installation

### From a package manager

<details>
<summary>Packaging status <a href="https://repology.org/project/clifm/versions"><img src="https://repology.org/badge/tiny-repos/clifm.svg" alt="Packaging status"></a></summary>
<a href="https://repology.org/project/clifm/versions">
    <img src="https://repology.org/badge/vertical-allrepos/clifm.svg?columns=3" alt="Packaging status">
</a>
</details>

If running on Linux, [binary packages](https://software.opensuse.org//download.html?project=home%3Aarchcrack&package=clifm) are available for most major distributions via the OpenSUSE Build System.

### From source (Linux/BSD)

**Note**: Dependencies are most likely already satisfied, but, in any case, consult the [dependencies section](https://github.com/leo-arch/clifm/wiki/Introduction#1-satisfy-dependencies).

```sh
git clone https://github.com/leo-arch/clifm.git
cd clifm
sudo make install
```

For more information/supported platforms, consult the [installation page](https://github.com/leo-arch/clifm/wiki/Introduction#installation).

---

## 💡 Getting started

To start using **clifm**, _you don't need to learn anything new_: the usual shell commands will just work. However, there is much more than just shell commands... \
✓ The `help` command gives you a quick introduction to **clifm**: once in the command prompt, enter `help` or `?`. \
✓ Type `cmd<TAB>` to get the list of available commands and a brief description. \
✓ Type `help <TAB>` to get the list of available _help topics_. Select the one you want and press <kbd>Enter</kbd>. \
✓ To jump into the **COMMANDS** section in the [manpage](https://github.com/leo-arch/clifm/blob/master/misc/clifm.1.pdf), simply enter `cmd` or press <kbd>F2</kbd>. \
✓ Press <kbd>F1</kbd> to access the full manpage and <kbd>F3</kbd> to access the keybindings help-page. \
✓ To get help about some specific command, just enter `CMD -h`. For instance, `s -h`.

You can also take a look at our [FAQ](https://github.com/leo-arch/clifm/wiki/FAQ) and these [basic usage-examples](https://github.com/leo-arch/clifm/wiki/Common-Operations#basic-usage-examples). \
For a complete description, please consult our [Wiki](https://github.com/leo-arch/clifm/wiki).

> [!TIP]
> Start **clifm** and just press a number (technically, an ELN or [Entry List Number](https://github.com/leo-arch/clifm/wiki/Common-Operations#elns)).

---

## 📰 What's new?

Consult the [changelog file](https://github.com/leo-arch/clifm/blob/master/CHANGELOG).

---

## Support

**Clifm** runs on Linux, Termux (Android), FreeBSD, NetBSD, OpenBSD, DragonFly, MacOS, Solaris/Illumos, Haiku, and Cygwin/MinGW, on x86, ARM, PowerPC, and RISC-V architectures.

---

## License
This project is licensed GPL version 2 (or later).
See the [LICENSE file](https://github.com/leo-arch/clifm/blob/master/LICENSE) for details.

---

## Contributing
Contributions are kindly welcome! Please see our [contribution guidelines](https://github.com/leo-arch/clifm/wiki/CONTRIBUTING) for details.

---

## Community

Visit the [Discussions section](https://github.com/leo-arch/clifm/discussions) of this repo and let us know what you think: ideas, comments, observations and questions are always useful.

---

## Developer
[Leo Abramovich](https://github.com/leo-arch) <<leo.clifm@outlook.com>>.

Special thanks to [all those who have contributed to this project](https://github.com/leo-arch/clifm/graphs/contributors).
