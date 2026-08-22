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
