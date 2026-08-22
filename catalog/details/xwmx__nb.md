# xwmx/nb

CLI and local web plain text note‑taking, bookmarking, and archiving with linking, tagging, filtering, search, Git versioning & syncing, Pandoc conversion, + more, in a single portable script.

## installation

#### Dependencies

##### Required

- [Bash](https://en.wikipedia.org/wiki/Bash_(Unix_shell))
  - `nb` works perfectly with Zsh, fish, and any other shell
    set as your primary login shell,
    the system just needs to have Bash available on it.
- [Git](https://git-scm.com/)
- A text editor with command line support, such as:
  - [Vim](https://en.wikipedia.org/wiki/Vim_\(text_editor\)),
  - [Emacs](https://en.wikipedia.org/wiki/Emacs),
  - [Visual Studio Code](https://code.visualstudio.com/),
  - [Sublime Text](https://www.sublimetext.com/),
  - [Helix](https://helix-editor.com/),
  - [micro](https://github.com/zyedidia/micro),
  - [nano](https://en.wikipedia.org/wiki/GNU_nano),
  - [Atom](https://atom.io/),
  - [TextMate](https://macromates.com/),
  - [MacDown](https://macdown.uranusjr.com/),
  - [some of these](https://github.com/topics/text-editor),
  - [and many of these.](https://en.wikipedia.org/wiki/List_of_text_editors)

##### Optional

`nb` leverages standard command line tools
and works in standard Linux / Unix environments.
`nb` also checks the environment for some additional optional tools and
uses them to enhance the experience whenever they are available.

Recommended:

- [`bat`](https://github.com/sharkdp/bat)
- [`ncat`](https://nmap.org/ncat/) or [`socat`](https://www.kali.org/tools/socat/)
- [`pandoc`](https://pandoc.org/)
- [`rg`](https://github.com/BurntSushi/ripgrep)
- [`tig`](https://github.com/jonas/tig)
- [`w3m`](https://en.wikipedia.org/wiki/W3m)

Also supported for various enhancements:

[Ack](https://beyondgrep.com/),
[`afplay`](https://ss64.com/osx/afplay.html),
[`asciidoctor`](https://asciidoctor.org/),
[The Silver Searcher (`ag`)](https://github.com/ggreer/the_silver_searcher),
[`catimg`](https://github.com/posva/catimg),
[Chafa](https://github.com/hpjansson/chafa),
[Chromium](https://www.chromium.org) / [Chrome](https://www.google.com/chrome/),
[`eza`](https://github.com/eza-community/eza),
[`ffplay`](https://ffmpeg.org/ffplay.html),
[ImageMagick](https://imagemagick.org/),
[`glow`](https://github.com/charmbracelet/glow),
[GnuPG](https://en.wikipedia.org/wiki/GNU_Privacy_Guard),
[`highlight`](http://www.andre-simon.de/doku/highlight/en/highlight.php),
[`imgcat`](https://www.iterm2.com/documentation-images.html),
[`joshuto`](https://github.com/kamiyaa/joshuto),
[kitty's `icat` kitten](https://sw.kovidgoyal.net/kitty/kittens/icat.html),
[`lowdown`](https://kristaps.bsd.lv/lowdown),
[`lsd`](https://github.com/lsd-rs/lsd),
[Links](https://en.wikipedia.org/wiki/Links_(web_browser)),
[Lynx](https://en.wikipedia.org/wiki/Lynx_(web_browser)),
[`mdcat`](https://github.com/swsnr/mdcat),
[`mdless`](https://github.com/ttscoff/mdless),
[`mdv`](https://github.com/axiros/terminal_markdown_viewer),
[Midnight Commander (`mc`)](https://en.wikipedia.org/wiki/Midnight_Commander),
[`mpg123`](https://en.wikipedia.org/wiki/Mpg123),
[MPlayer](https://en.wikipedia.org/wiki/MPlayer),
[`ncat`](https://nmap.org/ncat/),
[`netcat`](https://netcat.sourceforge.net/),
[note-link-janitor](https://github.com/andymatuschak/note-link-janitor)
(via [plugin](https://github.com/xwmx/nb/blob/master/plugins/backlink.nb-plugin)),
[`pdftotext`](https://en.wikipedia.org/wiki/Pdftotext),
[Pygments](https://pygments.org/),
[Ranger](https://ranger.github.io/),
[readability-cli](https://gitlab.com/gardenappl/readability-cli),
[`rga` / ripgrep-all](https://github.com/phiresky/ripgrep-all),
[`sc-im`](https://github.com/andmarti1424/sc-im),
[`socat`](https://www.kali.org/tools/socat/),
[`termvisage`](https://github.com/AnonymouX47/termvisage),
[`termpdf.py`](https://github.com/dsanson/termpdf.py),
[Tidy-Viewer (`tv`)](https://github.com/alexhallam/tv),
[`timg`](https://github.com/hzeller/timg),
[vifm](https://vifm.info/),
[`viu`](https://github.com/atanunq/viu),
[VisiData](https://www.visidata.org/)

#### macOS / Homebrew

```bash
brew install xwmx/taps/nb
```

Installing `nb` with Homebrew also installs
the recommended dependencies above
and comp

## features

<div align="center">
  <a href="#-notes"><code>📝</code>&nbsp;Notes</a>&nbsp;·
  <a href="#adding">Adding</a>&nbsp;·
  <a href="#listing--filtering">Listing</a>&nbsp;·
  <a href="#editing">Editing</a>&nbsp;·
  <a href="#viewing">Viewing</a>&nbsp;·
  <a href="#deleting">Deleting</a>&nbsp;·
  <a href="#-bookmarks"><code>🔖</code>&nbsp;Bookmarks</a>&nbsp;·
  <a href="#-todos"><code>✅</code>&nbsp;Todos</a>&nbsp;·
  <a href="#%EF%B8%8F-tasks"><code>✔️</code>&nbsp;Tasks</a>&nbsp;·
  <a href="#-tagging"><code>🏷</code>&nbsp;Tagging</a>&nbsp;·
  <a href="#-linking"><code>🔗</code>&nbsp;Linking</a>&nbsp;·
  <a href="#-browsing"><code>🌍</code>&nbsp;Browsing</a>&nbsp;·
  <a href="#-images"><code>🌄</code>&nbsp;Images</a>&nbsp;·
  <a href="#-zettelkasten"><code>🗂</code>&nbsp;Zettelkasten</a>&nbsp;·
  <a href="#-folders"><code>📂</code>&nbsp;Folders</a>&nbsp;·
  <a href="#-pinning"><code>📌</code>&nbsp;Pinning</a>&nbsp;·
  <a href="#-search"><code>🔍</code>&nbsp;Search</a>&nbsp;·
  <a href="#-moving--renaming"><code>↔</code>&nbsp;Moving&nbsp;&&nbsp;Renaming</a>&nbsp;·
  <a href="#-revision-history"><code>🗒</code>&nbsp;History</a>&nbsp;·
  <a href="#-notebooks"><code>📚</code>&nbsp;Notebooks</a>&nbsp;·
  <a href="#-git-sync"><code>🔄</code>&nbsp;Git&nbsp;Sync</a>&nbsp;·
  <a href="#%EF%B8%8F-import--export"><code>↕️</code>&nbsp;Import&nbsp;/&nbsp;Export</a>&nbsp;·
  <a href="#%EF%B8%8F-set--settings"><code>⚙️</code><code>set</code>&<code>settings</code></a>&nbsp;·
  <a href="#-color-themes"><code>🎨</code>&nbsp;Color&nbsp;Themes</a>&nbsp;·
  <a href="#-plugins"><code>🔌</code>&nbsp;Plugins</a>&nbsp;·
  <a href="#-selectors"><code>:/</code>&nbsp;Selectors</a>&nbsp;·
  <a href="#01-metadata"><code>01</code>&nbsp;Metadata</a>&nbsp;·
  <a href="#-interactive-shell"><code>❯</code>&nbsp;Shell</a>&nbsp;·
  <a href="#shortcut-aliases">Shortcuts</a>&nbsp;·
  <a href="#-help"><code>?</code>&nbsp;Help</a>&nbsp;·
  <a href="#-variables"><code>$</code>&nbsp;Variables</a>&nbsp;·
  <a href="#specifications">Specifications</a>&nbsp;·
  <a href="#tests">Tests</a>
</div>

<p align="center"></p><!-- spacer -->

<div align="center">
  <a href="#nb">&nbsp;↑&nbsp;</a>
</div>

<p align="center"></p><!-- spacer -->

To get started, simply run:

```bash
nb
```

`nb` sets up your initial `home` notebook the first time it runs.

By default, notebooks and notes are global (at `~/.nb`),
so they are always available to `nb`
regardless of the current working directory.
`nb` also supports [local notebooks](#global-and-local-notebooks).

### 📝 Notes

#### Adding

<p>
  <sup>
    <a href="#overview">↑</a> ·
    <a href="#add"><code>nb add</code></a>,
    <a href="#browse"><code>nb browse add</code></a>
  </sup>
</p>

Use [`nb add`](#add) (shortcuts: [`nb a`](#add), [`nb +`](#add))
to create new notes:

```bash
# create a new note in your text editor
nb add

# create a new note with the filename "example.md"
nb add example.md

# create a new note containing "This is a note."
nb add "This is a note."

# create a new note with piped content
echo "Note content." | nb add

# create a new password-protected, encrypted note titled "Secret Document"
nb add --title "Secret Document" --encrypt

# create a new note in the notebook named "example"
nb example:add "This is a note."

# create a new note in the folder named "sample"
nb add sample/
```

[`nb add`](#add) with no arguments or input will open the new, blank note
in your environment's preferred text editor.
You can change your editor using
the `$EDITOR` environment variable
or [`nb set editor`](#editor).

`nb` files are [Markdown](https://daringfireball.net/projects/markdown/)
files by default. The default file type can be changed to
whatever you like
using [`nb set default_extension`](#default_extension).

[`nb add`](#add) has intelligent argument parsing
and behaves differently depending on the types of arguments it receives.
When a filename with extension is specified,
a new note with that filename is opened in the editor:

```bash
nb a

## configuration

nb q -t tag1 -t tag2

# search for items tagged with "#tag1" OR "#tag2", arguments
nb q \#tag1 --or \#tag2
```

Files can be created with any file type by specifying the extension either
in the filename (`example.md`),
the extension by itself (`.md`),
or via the [`--type <type>`](#add) option (`--type md`):

```bash
# open a new Org file in the editor
nb add example.org

# open a new reStructuredText file in the editor
nb add --type rst

# open a new JavaScript file in the editor
nb add .js
```

Combining a type argument with piped clipboard content provides
a very convenient way to save code snippets using a clipboard utility such as
`pbpaste`,
`xclip`,
or [`pb`](https://github.com/xwmx/pb):

```bash
# save the clipboard contents as a JavaScript file in the current notebook
pb | nb add .js

# save the clipboard contents as a Rust file in the "rust" notebook
# using the shortcut alias `nb a`
pb | nb a rust: .rs

# save the clipboard contents as a Haskell file named "example.hs" in the
# "snippets" notebook using the shortcut alias `nb +`
pb | nb + snippets: example.hs
```

Use [`nb show`](#show) and [`nb browse`](#browse) to view code snippets
with automatic syntax highlighting and
use [`nb edit`](#edit) to open in your editor.

The [`clip` plugin](#clip) can also be used to
create notes from clipboard content.

Piping,
[`--title <title>`](#add),
[`--tags <tag-list>`](#add),
[`--content <content>`](#add),
and content passed in an argument
can be combined as needed
to create notes with content from multiple input methods and sources
using a single command:

```bash
❯ pb | nb add "Argument content." \
    --title   "Sample Title"      \
    --tags    tag1,tag2           \
    --content "Option content."
Added: [12] sample_title.md "Sample Title"

❯ nb show 12 --print
# Sample Title

#tag1 #tag2

Argument content.

Option content.

Clipboard content.
```

For a full list of options available for [`nb add`](#add), run
[`nb help add`](#add).

##### Password-Protected Encrypted Notes and Bookmarks

Password-protected notes and [bookmarks](#-bookmarks) are
created with the [`-e`](#add) / [`--encrypt`](#add) flag and
encrypted with AES-256 using OpenSSL by default.
GPG is also supported and can be configured with
[`nb set encryption_tool`](#encryption_tool).

Each protected note and bookmark is
encrypted individually with its own password.
When an encrypted item is viewed, edited, or opened,
`nb` will simply prompt for the item's password before proceeding.
After an item is edited,
`nb` automatically re-encrypts it and saves the new version.

Encrypted notes can be decrypted
using the OpenSSL and GPG command line tools directly, so
you aren't dependent on `nb` to decrypt your files.

##### Templates

Create a note based on a template by assigning a template string
or path to a template file with [`add --template <template>`](#add):

<!-- {% raw %} -->
```bash
# create a new note based on a template specified by path
nb add --template /path/to/example/template

# create a new note based on a template defined as a string
nb add --template "{{title}} • {{content}}"
```
<!-- {% endraw %} -->

`nb` template tags are enclosed in double curly brackets.
Supported tags include:

<dl>
  <dt><code>&#x007B;{title}}</code></dt>
  <dd>The note title, as specified with
  <a href="#add"><code>add --title &#60;title></code></a></dd>
  <dt><code>&#x007B;&#x007B;tags}}</code></dt>
  <dd>A list of hashtags, as specified with
  <a href="#add"><code>add --tags &#60;tag1>,&#60;tag2></code></a></dd>
  <dt><code>&#x007B;{content}}</code></dt>
  <dd>The note content, as specified with
  <a href="#add"><code>add &#60;content></code></a>,
  <a href="#add"><code>add --content &#60;content></code></a>,
  and piped content.</dd>
  <dt><code>&#x007B;{date}}</code></dt>
  <dd>The ouput of the system's <code>date</code> command. Use the
  <a href="https://man7.org/linux/man-pages/man1/date.1.html"><code>date</code>
  command options</a> to control formatting, e.g.,
  

## tools

<div align="center">
  <a href="#add">add</a>&nbsp;·
  <a href="#archive">archive</a>&nbsp;·
  <a href="#bookmark">bookmark</a>&nbsp;·
  <a href="#browse">browse</a>&nbsp;·
  <a href="#completions">completions</a>&nbsp;·
  <a href="#copy">copy</a>&nbsp;·
  <a href="#count">count</a>&nbsp;·
  <a href="#delete">delete</a>&nbsp;·
  <a href="#do">do</a>&nbsp;·
  <a href="#edit">edit</a>&nbsp;·
  <a href="#env">env</a>&nbsp;·
  <a href="#folders">folders</a>&nbsp;·
  <a href="#export">export</a>&nbsp;·
  <a href="#git">git</a>&nbsp;·
  <a href="#help">help</a>&nbsp;·
  <a href="#history">history</a>&nbsp;·
  <a href="#import">import</a>&nbsp;·
  <a href="#init">init</a>&nbsp;·
  <a href="#list">list</a>&nbsp;·
  <a href="#ls">ls</a>&nbsp;·
  <a href="#move">move</a>&nbsp;·
  <a href="#notebooks">notebooks</a>&nbsp;·
  <a href="#open">open</a>&nbsp;·
  <a href="#peek">peek</a>&nbsp;·
  <a href="#pin">pin</a>&nbsp;·
  <a href="#plugins">plugins</a>&nbsp;·
  <a href="#remote">remote</a>&nbsp;·
  <a href="#run">run</a>&nbsp;·
  <a href="#search">search</a>&nbsp;·
  <a href="#settings">settings</a>&nbsp;·
  <a href="#shell">shell</a>&nbsp;·
  <a href="#show">show</a>&nbsp;·
  <a href="#status">status</a>&nbsp;·
  <a href="#subcommands-1">subcommands</a>&nbsp;·
  <a href="#sync">sync</a>&nbsp;·
  <a href="#tasks">tasks</a>&nbsp;·
  <a href="#todo">todo</a>&nbsp;·
  <a href="#unarchive">unarchive</a>&nbsp;·
  <a href="#undo">undo</a>&nbsp;·
  <a href="#unpin">unpin</a>&nbsp;·
  <a href="#unset">unset</a>&nbsp;·
  <a href="#update">update</a>&nbsp;·
  <a href="#use">use</a>&nbsp;·
  <a href="#version">version</a>
</div>

<p align="center"></p><!-- spacer -->

<div align="center">
  <a href="#overview">&nbsp;↑&nbsp;</a>
</div>

#### `add`

[↑](#-help) · See also:
[Adding](#adding),
[`bookmark`](#bookmark),
[`browse`](#browse),
[`delete`](#delete),
[`edit`](#edit),
[`folders`](#folders),
[`import`](#import),
[`show`](#show),
[`todo`](#todo)

```text
Usage:
  nb add [<notebook>:][<folder-path>/][<filename>] [<content>]
         [-b | --browse] [-c <content> | --content <content>] [--edit]
         [-e | --encrypt] [-f <filename> | --filename <filename>]
         [--folder <folder-path>] [--no-template] [--tags <tag1>,<tag2>...]
         [--template <template>] [-t <title> | --title <title>] [--type <type>]
  nb add bookmark [<bookmark-options>...]
  nb add folder [<name>]
  nb add todo [<todo-options>...]

Options:
  -b, --browse                Add using a terminal or GUI web browser.
  -c, --content <content>     The content for the new note.
  --edit                      Open the note in the editor before saving when
                              content is piped or passed as an argument.
  -e, --encrypt               Encrypt the note with a password.
  -f, --filename <filename>   The filename for the new note.
  --folder <folder-path>      Add within the folder located at <folder-path>.
  --no-template               Skip the template when one is assigned.
  --tags <tag1>,<tag2>...     A comma-separated list of tags.
  --template <template>       A string template or path to a template file.
  -t, --title <title>         The title for a new note. If `--title` is
                              present, the filename is derived from the
                              title, unless `--filename` is specified.
  --type <type>               The file type for the new note, as a file
                              extension.

Description:
  Create a new note or folder.

  If no arguments are passed, a new blank note file is opened with `$EDITOR`,
  currently set to: example

  If a non-option argument is passed, `nb` will treat it as a <filename≥
  if a file extension is found. If no file extension is found,  `nb` will
  treat the string as <content> and will create a new note without opening the
  editor. `nb add` can also create a new note with piped content.

  `nb` creates Markdown files by default. To create a note with a
  different file type, us
