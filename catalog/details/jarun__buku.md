# jarun/buku

:bookmark: Personal mini-web in text

## features

- Store bookmarks with auto-fetched title, tags and description
- Auto-import from Firefox, Google Chrome, Chromium, Vivaldi, Vivaldi Beta (Internal), Brave, and MS Edge
- Open bookmarks and search results in browser
- Browse cached page from the Wayback Machine
- Text editor integration
- Lightweight, clean interface, custom colors
- Powerful search options (regex, substring...)
- Continuous search with on the fly mode switch
- Portable, merge-able database to sync between systems
- Import/export bookmarks from/to HTML, XBEL, Markdown, RSS/Atom or Orgfile
- Smart tag management using redirection (>>, >, <<)
- Multi-threaded full DB refresh
- Manual encryption support
- Shell completion scripts, man page with handy examples
- Privacy-aware (no unconfirmed user data collection)
- Can be used as a Python library ([_API documentation_](https://buku.readthedocs.io/en/latest/?badge=latest))
- Has a compation Web-application ([Bukuserver](https://github.com/jarun/buku/wiki/Bukuserver-%28WebUI%29)) with an HTTP-based API (for personal use only)

## installation

#### Dependencies

| Feature | Dependency |
| --- | --- |
| Lang, SQLite | Python 3.10+ |
| HTTPS | certifi, urllib3 |
| Encryption | cryptography |
| HTML | beautifulsoup4, html5lib |

To copy URL to clipboard `buku` uses `xsel` (or `xclip`) on Linux, `pbcopy` (default installed) on OS X, `clip` (default installed) on Windows, `termux-clipboard` on Termux (terminal emulation for Android), `wl-copy` on Wayland. If X11 is missing, GNU Screen or tmux copy-paste buffers are recognized.

#### From a package manager

To install buku with all its dependencies from PyPI, run:

    # pip3 install buku

You can also install `buku` from your package manager. If the version available is dated try an alternative installation method.

<details><summary>Packaging status (expand)</summary>
<p>
<br>
<a href="https://repology.org/project/buku/versions"><img src="https://repology.org/badge/vertical-allrepos/buku.svg" alt="Packaging status"></a>
</p>
Unlisted packagers:
<p>
<br>
● <a href="https://pypi.org/project/buku/">PyPI</a> (<code>pip3 install buku</code>)<br>
● Termux (<code>pip3 install buku</code>)<br>
</p>
</details>

#### Release packages

Auto-generated packages (with only the cli component) for Arch Linux, CentOS, Debian, Fedora, openSUSE Leap and Ubuntu are available with the [latest stable release](https://github.com/jarun/buku/releases/latest).

NOTE: CentOS may not have the python3-beautifulsoup4 package in the repos. Install it using pip3.

#### From source

If you have git installed, clone this repository. Otherwise download the [latest stable release](https://github.com/jarun/buku/releases/latest) or [development version](https://github.com/jarun/buku/archive/master.zip) (*risky*).

Install the dependencies. For example, on Ubuntu:

    $ apt-get install ca-certificates python3-urllib3 python3-cryptography python3-bs4

Install the cli component to default location (`/usr/local`):

    $ sudo make install

To remove, run:

    $ sudo make uninstall

`PREFIX` is supported, in case you want to install to a different location.

#### Running standalone

`buku` is a standalone utility. From the containing directory, run:

    $ chmod +x buku.py
    $ ./buku.py

### Shell completion

Shell completion scripts for Bash, Fish and Zsh can be found in respective subdirectories of [auto-completion/](https://github.com/jarun/buku/blob/master/auto-completion). Please refer to your shell's manual for installation instructions.

## tools

#### Command-line options

```
usage: buku [OPTIONS] [KEYWORD [KEYWORD ...]]

Bookmark manager like a text-based mini-web.

POSITIONAL ARGUMENTS:
      KEYWORD              search keywords

GENERAL OPTIONS:
      -a, --add URL [+|-] [tag, ...]
                           bookmark URL with comma-separated tags
                           (prepend tags with '+' or '-' to use fetched tags)
      -u, --update [...]   update fields of an existing bookmark
                           accepts indices and ranges
                           refresh title and desc if no edit options
                           if no arguments:
                           - update results when used with search
                           - otherwise refresh all titles and desc
      -w, --write [editor|index]
                           edit and add a new bookmark in editor
                           else, edit bookmark at index in EDITOR
                           edit last bookmark, if index=-1
                           if no args, edit new bookmark in EDITOR
      -d, --delete [...]   remove bookmarks from DB
                           accepts indices or a single range
                           if no arguments:
                           - delete results when used with search
                           - otherwise delete all bookmarks
      --retain-order       prevents reordering after deleting a bookmark
      -h, --help           show this information and exit
      -v, --version        show the program version and exit

EDIT OPTIONS:
      --url keyword        bookmark link
      --tag [+|-] [...]    comma-separated tags
                           clear bookmark tagset, if no arguments
                           '+' appends to, '-' removes from tagset
      --title [...]        bookmark title; if no arguments:
                           -a: do not set title, -u: clear title
      -c, --comment [...]  notes or description of the bookmark
                           clears description, if no arguments
      --immutable N        disable web-fetch during auto-refresh
                           N=0: mutable (default), N=1: immutable
      --swap N M           swap two records at specified indices

SEARCH OPTIONS:
      -s, --sany [...]     find records with ANY matching keyword
                           this is the default search option
      -S, --sall [...]     find records matching ALL the keywords
                           special keywords -
                           "blank": entries with empty title/tag
                           "immutable": entries with locked title
      --deep               match substrings ('pen' matches 'opens')
      --markers            search for keywords in specific fields
                           based on (optional) prefix markers:
                           '.' - title, '>' - description, ':' - URL,
                           '#' - tags (comma-separated, PARTIAL matches)
                           '#,' - tags (comma-separated, EXACT matches)
                           '*' - any field (same as no prefix)
      -r, --sreg expr      run a regex search
      -t, --stag [tag [,|+] ...] [- tag, ...]
                           search bookmarks by tags
                           use ',' to find entries matching ANY tag
                           use '+' to find entries matching ALL tags
                           excludes entries with tags after ' - '
                           list all tags, if no search keywords
      -x, --exclude [...]  omit records matching specified keywords
      --random [N]         output random bookmarks out of the selection (default 1)
      --order fields [...] comma-separated list of fields to order the output by
                           (prepend with '+'/'-' to choose sort direction)

ENCRYPTION OPTIONS:
      -l, --lock [N]       encrypt DB in N (default 8) # iterations
      -k, --unlock [N]     decrypt DB in N (default 8) # iterations

POWER TOYS:
      --ai                 auto-import bookmar
