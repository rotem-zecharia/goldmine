# oraios/serena

A powerful MCP toolkit for coding, providing semantic retrieval and editing capabilities - the IDE for your agent

## features

Serena provides a set of versatile code querying and editing functionalities
based on symbolic understanding of the code.
Equipped with these capabilities, your agent discovers and edits code just like a seasoned developer
making use of an IDE's capabilities would.
Serena can efficiently find the right context and do the right thing even in very large and
complex projects!

There are two alternative technologies powering these capabilities:

* **Language servers** implementing the language server protocol (LSP) — the free/open-source alternative 
  which is used by default.
* **The Serena JetBrains Plugin**, which leverages the powerful code analysis and editing
  capabilities of your JetBrains IDE (paid plugin; free trial available).

You can choose either of these backends depending on your preferences and requirements.

### Language Servers

Serena incorporates a powerful abstraction layer for the integration of language servers that implement the language server protocol (LSP). 
The underlying language servers are typically open-source projects or at least freely available for use.

When using Serena's language server backend, we provide **support for over 40 programming languages**, including
Ada / SPARK, AL, Angular, Ansible, Bash, BSL, C#, C/C++, Clojure, Crystal, CUE, Dart, Deno, Elixir, Elm, Erlang, Fortran, F#, GDScript, Gleam, GLSL, Go, Groovy, Haskell, Haxe, HLSL, HTML, Java, JavaScript, JSON, Julia, Kotlin, LaTeX, Lean 4, Lua, Luau, Markdown, MATLAB, mSL, Nextflow, Nix, OCaml, Pascal, Perl, PHP, PowerShell, Python, QML, R, Rego, Ruby, Rust, Scala, SCSS / Sass / CSS, Solidity, Svelte, Swift, SystemVerilog, Terraform, TOML, TypeScript, Vue, WGSL, Wolfram Language, YAML, and Zig.

### The Serena JetBrains Plugin

The paid Serena JetBrains Plugin (free trial available)
leverages the powerful code analysis capabilities of your JetBrains IDE.
The plugin naturally supports all programming languages and frameworks that are supported by JetBrains IDEs,
including IntelliJ IDEA, PyCharm, Android Studio, WebStorm, PhpStorm, RubyMine, GoLand, and potentially others (Rider and CLion are unsupported though).

<a href="https://plugins.jetbrains.com/plugin/28946-serena/"><img src="docs/_static/images/jetbrains-marketplace-button.png"></a>

See our [documentation page](https://oraios.github.io/serena/02-usage/025_jetbrains_plugin.html) for further details and instructions on how to apply the plugin.

## Features

Serena provides a wide range of tools for efficient code retrieval, editing and refactoring, as well as 
a memory system for long-lived agent workflows.

Given its large scope, Serena adapts to your needs by offering a multi-layered configuration system.

<details>
<summary>Details</summary>

### Retrieval

Serena's retrieval tools allow agents to explore codebases at the symbol level, understanding structure and relationships
without reading entire files.

| Capability                       | Language Servers | JetBrains Plugin |
|----------------------------------|------------------|------------------|
| find symbol                      | yes              | yes              |
| symbol overview (file outline)   | yes              | yes              |
| find referencing symbols         | yes              | yes              |
| search in project dependencies   | --               | yes              |
| type hierarchy                   | --               | yes              |
| find declaration                 | yes*             | yes              |
| find implementations             | yes**            | yes              |
| query external projects          | yes              | yes              |
| diagnostics/inspections          | yes              | yes              |

*: Will generally not work for declarations in external dependencies. <br>
**: Only available for some languages, limited by the language server functionality.

### Refactoring

Without precise refactoring tools, agents are forced to resort to unreliable and e

## configuration

Active tools, tool descriptions, prompts, language backend details and many other aspects of Serena
can be flexibly configured on a per-case basis by simply adjusting a few lines of YAML.
To achieve this, Serena offers multiple levels of (composable) configuration:

* global configuration
* MCP launch command (CLI) configuration
* per-project configuration (with local overrides)
* execution context-specific configuration (e.g. for particular clients)
* dynamically composable configuration fragments (modes)

</details>

## installation

**Prerequisites**. Serena is managed by *uv*, and [installing uv](https://docs.astral.sh/uv/getting-started/installation/) is the only required prerequisite.

> [!NOTE]
> When using the language server backend, some additional dependencies may need to be installed to support certain languages;
> see the [Language Support](https://oraios.github.io/serena/01-about/020_programming-languages.html) page for details.

**Install Serena**. Serena is installed via uv as follows:

```bash
uv tool install -p 3.13 serena-agent
```

After successful installation, the command `serena` should be available in your shell.

**Initialise Serena**. To initialise Serena and verify that your setup works correctly, simply run:

```bash
serena init
```

By default, this will set up Serena to use the language server backend. To use the JetBrains backend instead, add the parameters `-b JetBrains` 
(see the [JetBrains Plugin documentation page](https://oraios.github.io/serena/02-usage/025_jetbrains_plugin.html) for additional usage details).  
Either way, you should receive a success message indicating that Serena has been initialised successfully.

**Configuring Your Client**. To connect Serena to your preferred MCP client, you typically need to [configure a launch command in your client](https://oraios.github.io/serena/02-usage/030_clients.html).
Follow the link for specific instructions on how to set up Serena for Claude Code, Codex, Claude Desktop, MCP-enabled IDEs and other clients (such as local and web-based GUIs). 

> [!TIP]
> While getting started quickly is easy, Serena is a powerful toolkit with many configuration options.
> We highly recommend reading through the [user guide](https://oraios.github.io/serena/02-usage/000_intro.html) to get the most out of Serena.
> 
> Specifically, we recommend to read about ...
>   * [Serena's project-based workflow](https://oraios.github.io/serena/02-usage/040_workflow.html) and
>   * [configuring Serena](https://oraios.github.io/serena/02-usage/050_configuration.html).

## User Guide

Please refer to the [user guide](https://oraios.github.io/serena/02-usage/000_intro.html) for detailed instructions on how to use Serena effectively.

## Acknowledgements

A significant part of Serena, especially support for various languages, was contributed by the open source community.
We are very grateful for the many contributors who made this possible and who played an important role in making Serena
what it is today.

<!-- mcp-name: io.github.oraios/serena -->
