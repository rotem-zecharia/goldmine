# yamadashy/repomix

📦 Repomix is a powerful tool that packs your entire repository into a single, AI-friendly file. Perfect for when you need to feed your codebase to Large Language Models (LLMs) or other AI tools like C

## features

- **AI-Optimized**: Formats your codebase in a way that's easy for AI to understand and process.
- **Token Counting**: Provides token counts for each file and the entire repository, useful for LLM context limits.
- **Simple to Use**: You need just one command to pack your entire repository.
- **Customizable**: Easily configure what to include or exclude.
- **Git-Aware**: Automatically respects your `.gitignore`, `.ignore`, and `.repomixignore` files.
- **Security-Focused**: Incorporates [Secretlint](https://github.com/secretlint/secretlint) to detect files matching known credential formats and leave them out of the output.
- **Code Compression**: The `--compress` option uses [Tree-sitter](https://github.com/tree-sitter/tree-sitter) to extract key code elements, reducing token count while preserving structure.

## installation

### Using the CLI Tool `>_`

You can try Repomix instantly in your project directory without installation:

```bash
npx repomix@latest
```

Or install globally for repeated use:

```bash
# Install using npm
npm install -g repomix

# Alternatively using yarn
yarn global add repomix

# Alternatively using bun
bun add -g repomix

# Alternatively using Homebrew (macOS/Linux)
brew install repomix

# Then run in any project directory
repomix
```

That's it! Repomix will generate a `repomix-output.xml` file in your current directory, containing your entire
repository in an AI-friendly format.

You can then send this file to an AI assistant with a prompt like:

```
This file contains all the files in the repository combined into one.
I want to refactor the code, so please review it first.
```

![Repomix File Usage 1](website/client/src/public/images/docs/repomix-file-usage-1.png)

When you propose specific changes, the AI might be able to generate code accordingly. With features like Claude's
Artifacts, you could potentially output multiple files, allowing for the generation of multiple interdependent pieces of
code.

![Repomix File Usage 2](website/client/src/public/images/docs/repomix-file-usage-2.png)

Happy coding! 🚀

### Using The Website 🌐

Want to try it quickly? Visit the official website at [repomix.com](https://repomix.com). Simply enter your repository
name, fill in any optional details, and click the **Pack** button to see your generated output.

#### Available Options

The website offers several convenient features:

- Customizable output format (XML, Markdown, or Plain Text)
- Instant token count estimation
- Much more!

### Using The Browser Extension 🧩

Get instant access to Repomix directly from any GitHub repository! Our Chrome extension adds a convenient "Repomix" button to GitHub repository pages.

![Repomix Browser Extension](website/client/src/public/images/docs/browser-extension.png)

#### Install
- Chrome Extension: [Repomix - Chrome Web Store](https://chromewebstore.google.com/detail/repomix/fimfamikepjgchehkohedilpdigcpkoa)
- Firefox Add-on: [Repomix - Firefox Add-ons](https://addons.mozilla.org/firefox/addon/repomix/)

#### Features
- One-click access to Repomix for any GitHub repository
- More exciting features coming soon!

### Using The VSCode Extension ⚡️

A community-maintained VSCode extension called [Repomix Runner](https://marketplace.visualstudio.com/items?itemName=DorianMassoulier.repomix-runner) (created by [massdo](https://github.com/massdo)) lets you run Repomix right inside your editor with just a few clicks. Run it on any folder, manage outputs seamlessly, and control everything through VSCode's intuitive interface. 

Want your output as a file or just the content? Need automatic cleanup? This extension has you covered. Plus, it works smoothly with your existing repomix.config.json.

Try it now on the [VSCode Marketplace](https://marketplace.visualstudio.com/items?itemName=DorianMassoulier.repomix-runner)!
Source code is available on [GitHub](https://github.com/massdo/repomix-runner).

## tools

If you're using Python, you might want to check out `Gitingest`, which is better suited for Python ecosystem and data
science workflows:
https://github.com/cyclotruc/gitingest

## 📊 Usage

To pack your entire repository:

```bash
repomix
```

To pack a specific directory:

```bash
repomix path/to/directory
```

To pack specific files or directories
using [glob patterns](https://github.com/mrmlnc/fast-glob?tab=readme-ov-file#pattern-syntax):

```bash
repomix --include "src/**/*.ts,**/*.md"
```

To exclude specific files or directories:

```bash
repomix --ignore "**/*.log,tmp/"
```

To pack a remote repository:

```bash
repomix --remote https://github.com/yamadashy/repomix

# You can also use GitHub shorthand:
repomix --remote yamadashy/repomix

# You can specify the branch name, tag, or commit hash:
repomix --remote https://github.com/yamadashy/repomix --remote-branch main

# Or use a specific commit hash:
repomix --remote https://github.com/yamadashy/repomix --remote-branch 935b695

# Another convenient way is specifying the branch's URL
repomix --remote https://github.com/yamadashy/repomix/tree/main

# Commit's URL is also supported
repomix --remote https://github.com/yamadashy/repomix/commit/836abcd7335137228ad77feb28655d85712680f1

```

To pack files from a file list (pipe via stdin):

```bash
# Using find command
find src -name "*.ts" -type f | repomix --stdin

# Using git to get tracked files
git ls-files "*.ts" | repomix --stdin

# Using grep to find files containing specific content
grep -l "TODO" **/*.ts | repomix --stdin

# Using ripgrep to find files with specific content
rg -l "TODO|FIXME" --type ts | repomix --stdin

# Using ripgrep (rg) to find files
rg --files --type ts | repomix --stdin

# Using sharkdp/fd to find files
fd -e ts | repomix --stdin

# Using fzf to select from all files
fzf -m | repomix --stdin

# Interactive file selection with fzf
find . -name "*.ts" -type f | fzf -m | repomix --stdin

# Using ls with glob patterns
ls src/**/*.ts | repomix --stdin

# From a file containing file paths
cat file-list.txt | repomix --stdin

# Direct input with echo
echo -e "src/index.ts\nsrc/utils.ts" | repomix --stdin
```

The `--stdin` option allows you to pipe a list of file paths to Repomix, giving you ultimate flexibility in selecting which files to pack.

When using `--stdin`, the specified files are effectively added to the include patterns. This means that the normal include and ignore behavior still applies - files specified via stdin will still be excluded if they match ignore patterns.

> [!NOTE]
> When using `--stdin`, file paths can be relative or absolute, and Repomix will automatically handle path resolution and deduplication.

To include git logs in the output:

```bash
# Include git logs with default count (50 commits)
repomix --include-logs

# Include git logs with specific commit count
repomix --include-logs --include-logs-count 10

# Combine with diffs for comprehensive git context
repomix --include-logs --include-diffs
```

The git logs include commit dates, messages, and file paths for each commit, providing valuable context for AI analysis of code evolution and development patterns.

To compress the output:

```bash
repomix --compress

# You can also use it with remote repositories:
repomix --remote yamadashy/repomix --compress
```

To initialize a new configuration file (`repomix.config.json`):

```bash
repomix --init
```

Once you have generated the packed file, you can use it with Generative AI tools like ChatGPT, DeepSeek, Perplexity, Gemini, Gemma, Llama, Grok, and more.

### Docker Usage 🐳

You can also run Repomix using Docker.  
This is useful if you want to run Repomix in an isolated environment or prefer using containers.

Basic usage (current directory):

```bash
docker run -v .:/app -it --rm ghcr.io/yamadashy/repomix
```

To pack a specific directory:

```bash
docker run -v .:/app -it --rm ghcr.io/yamadashy/repomix path/to/directory
```

Process a remote repository and output to a `

## configuration

#### Basic Options
- `-v, --version`: Show version information and exit

#### CLI Input/Output Options

| Option | Description |
|--------|-------------|
| `--verbose` | Enable detailed debug logging (shows file processing, token counts, and configuration details) |
| `--quiet` | Suppress all console output except errors (useful for scripting) |
| `--stdout` | Write packed output directly to stdout instead of a file (suppresses all logging) |
| `--stdin` | Read file paths from stdin, one per line (specified files are processed directly) |
| `--copy` | Copy the generated output to system clipboard after processing |
| `--token-count-tree [threshold]` | Show file tree with token counts; optional threshold to show only files with ≥N tokens (e.g., `--token-count-tree 100`) |
| `--top-files-len <number>` | Number of largest files to show in summary (default: `5`) |

#### Repomix Output Options

| Option | Description |
|--------|-------------|
| `-o, --output <file>` | Output file path (default: `repomix-output.xml`, use `"-"` for stdout) |
| `--style <style>` | Output format: `xml`, `markdown`, `json`, or `plain` (default: `xml`) |
| `--output-file-path-style <style>` | How file paths are shown in output: `target-relative` or `cwd-relative` (default: `target-relative`) |
| `--parsable-style` | Escape special characters to ensure valid XML/Markdown (needed when output contains code that breaks formatting) |
| `--compress` | Extract essential code structure (classes, functions, interfaces) using Tree-sitter parsing |
| `--output-show-line-numbers` | Prefix each line with its line number in the output |
| `--no-file-summary` | Omit the file summary section from output |
| `--no-directory-structure` | Omit the directory tree visualization from output |
| `--no-files` | Generate metadata only without file contents (useful for repository analysis) |
| `--remove-comments` | Strip all code comments before packing |
| `--remove-empty-lines` | Remove blank lines from all files |
| `--truncate-base64` | Truncate long base64 data strings to reduce output size |
| `--header-text <text>` | Custom text to include at the beginning of the output |
| `--instruction-file-path <path>` | Path to file containing custom instructions to include in output |
| `--split-output <size>` | Split output into multiple numbered files (e.g., `repomix-output.1.xml`); size like `500kb`, `2mb`, or `1.5mb` |
| `--include-empty-directories` | Include folders with no files in directory structure |
| `--include-full-directory-structure` | Show complete directory tree in output, including files not matched by `--include` patterns |
| `--no-git-sort-by-changes` | Don't sort files by git change frequency (default: most changed files first) |
| `--include-diffs` | Add git diff section showing working tree and staged changes |
| `--include-logs` | Add git commit history with messages and changed files |
| `--include-logs-count <count>` | Number of recent commits to include with `--include-logs` (default: `50`) |

#### File Selection Options

| Option | Description |
|--------|-------------|
| `--include <patterns>` | Include only files matching these glob patterns (comma-separated, e.g., `"src/**/*.js,*.md"`) |
| `-i, --ignore <patterns>` | Additional patterns to exclude (comma-separated, e.g., `"*.test.js,docs/**"`) |
| `--no-gitignore` | Don't use `.gitignore` rules for filtering files |
| `--no-dot-ignore` | Don't use `.ignore` rules for filtering files |
| `--no-default-patterns` | Don't apply built-in ignore patterns (`node_modules`, `.git`, build dirs, etc.) |

#### Remote Repository Options

| Option | Description |
|--------|-------------|
| `--remote <url>` | Clone and pack a remote repository (GitHub URL or `user/repo` format) |
| `--remote-branch <name>` | Specific branch, tag, or commit to use (default: repository's default branch) |
| `--remote-trust-config` | Trust and load config files from remote repositories (disabled by default for security). On an interacti
