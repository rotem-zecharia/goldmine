# D4Vinci/Scrapling

🕷️ An adaptive Web Scraping framework that handles everything from a single request to a full-scale crawl!

## tools

- 🔄 **Smart Element Tracking**: Relocate elements after website changes using intelligent similarity algorithms.
- 🎯 **Smart Flexible Selection**: CSS selectors, XPath selectors, filter-based search, text search, regex search, and more.
- 🔍 **Find Similar Elements**: Automatically locate elements similar to found elements.
- 🤖 **MCP Server to be used with AI**: Built-in MCP server for AI-assisted Web Scraping and data extraction. The MCP server features powerful, custom capabilities that leverage Scrapling to extract targeted content before passing it to the AI (Claude/Cursor/etc), thereby speeding up operations and reducing costs by minimizing token usage. ([demo video](https://www.youtube.com/watch?v=qyFk3ZNwOxE)) It can also keep browser sessions open across calls, take page screenshots, and drive remote browsers over CDP.
- 🧠 **Agent Skill**: A ready-to-install [Agent Skill](https://github.com/D4Vinci/Scrapling/tree/main/agent-skill) that teaches coding agents the whole library, so the code they write with Scrapling matches the current API instead of guessing.

## installation

Let's give you a quick glimpse of what Scrapling can do without deep diving.

## requirements

1. If you are going to use any of the extra features below, the fetchers, or their classes, you will need to install fetchers' dependencies and their browser dependencies as follows:
    ```bash
    pip install "scrapling[fetchers]"
    
    scrapling install           # normal install
    scrapling install  --force  # force reinstall
    ```

    This downloads all browsers, along with their system dependencies and fingerprint manipulation dependencies.

    Or you can install them from the code instead of running a command like this:
    ```python
    from scrapling.cli import install
    
    install([], standalone_mode=False)          # normal install
    install(["--force"], standalone_mode=False) # force reinstall
    ```

2. Extra features:
   - Install the MCP server feature:
       ```bash
       pip install "scrapling[ai]"
       ```
   - Install shell features (Web Scraping shell and the `extract` command): 
       ```bash
       pip install "scrapling[shell]"
       ```
   - Install everything: 
       ```bash
       pip install "scrapling[all]"
       ```
   Remember that you need to install the browser dependencies with `scrapling install` after any of these extras (if you didn't already)
