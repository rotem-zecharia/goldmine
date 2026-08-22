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

npm install -g repomix

## tools

If you're using Python, you might want to check out `Gitingest`, which is better suited for Python ecosystem and data
science workflows:
https://github.com/cyclotruc/gitingest

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
