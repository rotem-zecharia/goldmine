# xberg-io/xberg

A polyglot document intelligence framework with a Rust core. Extract text, metadata, images, and structured data from 101 formats (115 file extensions) plus code intelligence for 371 code languages. 1

## installation

### Language Packages

<details open>
<summary><strong>Python</strong></summary>

```sh
pip install xberg
```

See [Python README](https://github.com/xberg-io/xberg/tree/main/packages/python) for full documentation.

</details>

<details>
<summary><strong>Node.js / TypeScript</strong></summary>

```sh
npm install @xberg-io/xberg
```

See [Node.js README](https://github.com/xberg-io/xberg/tree/main/crates/xberg-node) for full documentation.

</details>

<details>
<summary><strong>Rust</strong></summary>

```sh
cargo add xberg
```

See [Rust README](https://github.com/xberg-io/xberg/tree/main/crates/xberg) for full documentation.

</details>

<details>
<summary><strong>Go</strong></summary>

```sh
go get github.com/xberg-io/xberg/packages/go@latest
```

> ⚠️ The repository root is not a Go module — `go get github.com/xberg-io/xberg` will fail.
> Always target the `/packages/go` subdirectory as shown above.

See [Go README](https://github.com/xberg-io/xberg/tree/main/packages/go) for full documentation.

</details>

<details>
<summary><strong>Java</strong></summary>

Available on Maven Central as `io.xberg:xberg`. See [Java README](https://github.com/xberg-io/xberg/tree/main/packages/java) for the dependency snippet.

</details>

<details>
<summary><strong>C#</strong></summary>

```sh
dotnet add package Xberg
```

See [C# README](https://github.com/xberg-io/xberg/tree/main/packages/csharp) for full documentation.

</details>

<details>
<summary><strong>Ruby</strong></summary>

```sh
gem install xberg
```

See [Ruby README](https://github.com/xberg-io/xberg/tree/main/packages/ruby) for full documentation.

</details>

<details>
<summary><strong>PHP</strong></summary>

```sh
composer require xberg-io/xberg
```

See [PHP README](https://github.com/xberg-io/xberg/tree/main/packages/php) for full documentation.

</details>

<details>
<summary><strong>Elixir</strong></summary>

Add `{:xberg, "~> 1.0"}` to your `mix.exs` dependencies. See [Elixir README](https://github.com/xberg-io/xberg/tree/main/packages/elixir) for full documentation.

</details>

<details>
<summary><strong>WebAssembly</strong></summary>

```sh
npm install @xberg-io/xberg-wasm
```

See [WebAssembly README](https://github.com/xberg-io/xberg/tree/main/crates/xberg-wasm) for full documentation.

</details>

<details>
<summary><strong>Kotlin (Android)</strong></summary>

Available on Maven Central as `io.xberg:xberg-android`. See [Kotlin README](https://github.com/xberg-io/xberg/tree/main/packages/kotlin-android) for the dependency snippet.

</details>

<details>
<summary><strong>Swift</strong></summary>

Add via Swift Package Manager. See [Swift README](https://github.com/xberg-io/xberg/tree/main/packages/swift) for full documentation.

</details>

<details>
<summary><strong>Dart / Flutter</strong></summary>

```sh
dart pub add xberg
```

See [Dart README](https://github.com/xberg-io/xberg/tree/main/packages/dart) for full documentation.

</details>

<details>
<summary><strong>Zig</strong></summary>

Add via `zig fetch`. See [Zig README](https://github.com/xberg-io/xberg/tree/main/packages/zig) for full documentation.

</details>

<details>
<summary><strong>C/C++ (FFI)</strong></summary>

Build from source as part of this workspace. See [C (FFI) README](https://github.com/xberg-io/xberg/tree/main/crates/xberg-ffi) for full documentation.

</details>

### CLI & Deployment

<details>
<summary><strong>CLI Tool</strong></summary>

```sh
brew install xberg-io/tap/xberg
```

12 commands: `extract`, `batch`, `detect`, `formats`, `version`, `cache` (stats/clear/manifest/warm), `serve`, `mcp`, `api`, `embed`, `chunk`, `completions`.

See [CLI usage guide](https://docs.xberg.io/cli/usage/) for detailed documentation.

</details>

<details>
<summary><strong>Docker</strong></summary>

```sh
docker pull ghcr.io/xberg-io/xberg:latest
```

Run in API, CLI, or MCP modes. See [Docker guide](https://docs.xberg.io/guides/docker/) for examples.

</details>

<details>
<summary><strong>REST 

## features

<details>
<summary><strong>Full feature list</strong></summary>

### Supported File Formats (100 formats · 120 file extensions)

100 formats across 120 file extensions in 8 major categories with intelligent format detection and comprehensive metadata extraction.

#### Office Documents

| Category | Formats | Capabilities |
|----------|---------|--------------|
| **Word Processing** | `.docx`, `.docm`, `.doc`, `.dotx`, `.dotm`, `.dot`, `.odt`, `.pages`, `.wpd`, `.wp`, `.wp5`, `.wp6` | Full text, tables, images, metadata, styles |
| **Spreadsheets** | `.xlsx`, `.xlsm`, `.xlsb`, `.xls`, `.xla`, `.xlam`, `.xltm`, `.xltx`, `.xlt`, `.ods`, `.numbers` | Sheet data, formulas, cell metadata, charts |
| **Presentations** | `.pptx`, `.pptm`, `.ppt`, `.ppsx`, `.potx`, `.potm`, `.pot`, `.odp`, `.key` | Slides, speaker notes, images, metadata |
| **PDF** | `.pdf` | Text, tables, images, metadata, OCR support |
| **eBooks** | `.epub`, `.fb2` | Chapters, metadata, embedded resources |
| **Database** | `.dbf` | Table data extraction, field type support |
| **Hangul** | `.hwp`, `.hwpx` | Korean document format, text extraction |

#### Images (OCR-Enabled)

| Category | Formats | Features |
|----------|---------|----------|
| **Raster** | `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.bmp`, `.tiff`, `.tif` | OCR, table detection, EXIF metadata, dimensions, color space |
| **Advanced** | `.jp2`, `.jpx`, `.jpm`, `.mj2`, `.jbig2`, `.jb2`, `.pnm`, `.pbm`, `.pgm`, `.ppm` | OCR via pure-Rust JPEG2000 decoder, JBIG2 support, table detection |
| **HEIC family** | `.heic`, `.heics`, `.heif`, `.avif`, `.avcs` | EXIF metadata, optional pixel decoding |
| **Vector** | `.svg` | DOM parsing, embedded text, graphics metadata |

#### Audio & Video

| Category | Formats | Features |
|----------|---------|----------|
| **Audio** | `.mp3`, `.mpga`, `.m4a`, `.wav`, `.webm` | Whisper transcription |
| **Video audio track** | `.mp4`, `.mpeg`, `.webm` | Audio-track transcription only |

#### Web & Data

| Category | Formats | Features |
|----------|---------|----------|
| **Markup** | `.html`, `.htm`, `.xhtml`, `.xml`, `.svg` | DOM parsing, metadata (Open Graph, Twitter Card), link extraction |
| **Structured Data** | `.json`, `.yaml`, `.yml`, `.toml`, `.csv`, `.tsv` | Schema detection, nested structures, validation |
| **Text & Markdown** | `.txt`, `.md`, `.markdown`, `.djot`, `.mdx`, `.rst`, `.org`, `.rtf` | CommonMark, GFM, Djot, MDX, reStructuredText, Org Mode |

#### Email & Archives

| Category | Formats | Features |
|----------|---------|----------|
| **Email** | `.eml`, `.msg`, `.pst` | Headers, body (HTML/plain), attachments, threading |
| **Archives** | `.zip`, `.tar`, `.tgz`, `.gz`, `.7z` | File listing, nested archives, metadata, recursive extraction |

#### Academic & Scientific

| Category | Formats | Features |
|----------|---------|----------|
| **Citations** | `.bib`, `.ris`, `.nbib`, `.enw` | Structured parsing: RIS, PubMed/MEDLINE, EndNote XML, BibTeX/BibLaTeX |
| **Scientific** | `.tex`, `.latex`, `.typ`, `.typst`, `.jats`, `.ipynb` | LaTeX, Typst, Jupyter notebooks, PubMed JATS |
| **Publishing** | `.fb2`, `.docbook`, `.dbk`, `.docbook4`, `.docbook5`, `.opml` | FictionBook, DocBook XML, OPML outlines |

### Code Intelligence (371 Languages)

Extract structure from 371 programming languages via tree-sitter:

| Feature | Description |
|---------|-------------|
| **Structure Extraction** | Functions, classes, methods, structs, interfaces, enums |
| **Import/Export Analysis** | Module dependencies, re-exports, wildcard imports |
| **Symbol Extraction** | Variables, constants, type aliases, properties |
| **Docstring Parsing** | Google, NumPy, Sphinx, JSDoc, RustDoc, and 10+ formats |
| **Syntax-Aware Chunking** | Split code by semantic boundaries for RAG pipelines |
| **Diagnostics** | Parse errors with line/column positions |

Powered by [tree-sitter-language-pack](https://github.com/xberg-io/tree-sitter-language-pack).

### Output Formats (6)

| Format
