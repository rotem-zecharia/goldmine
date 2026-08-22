# opensandbox-group/OpenSandbox

Secure, Fast, and Extensible Sandbox runtime for AI agents.

## features

- 🧩 **SDKs, CLI, and MCP**: Provides multi-language SDKs, the osb CLI, and MCP server integration for sandbox creation, command execution, and file operations. See [SDKs](#sdks), [CLI](#cli), and [MCP](#mcp).
- 📜 **Sandbox Protocol**: Defines sandbox lifecycle management APIs and sandbox execution APIs so you can extend custom sandbox runtimes. See [API specs](specs/README.md).
- 🚀 **Sandbox Runtime**: Built-in lifecycle management supporting Docker and high-performance Kubernetes runtime, enabling both local runs and large-scale distributed scheduling. See [Kubernetes runtime](./kubernetes).
- 🖥️ **Sandbox Environments**: Built-in Command, Filesystem, and Code Interpreter implementations. Examples cover Coding Agents (e.g., Claude Code), browser automation (Chrome, Playwright), and desktop environments (VNC, VS Code).
- 🚦 **Network Policy**: Unified ingress gateway with multiple routing strategies plus per-sandbox egress controls. See [Ingress Gateway](components/ingress) and [egress controls](components/egress).
- 🔑 **Credential Vault**: Secure credential injection for sandbox outbound requests without exposing real secrets to workloads. See [Credential Vault](docs/guides/credential-vault.md).
- 🏰 **Strong Isolation**: Supports secure container runtimes like gVisor, Kata Containers, and Firecracker microVM for enhanced isolation between sandbox workloads and the host. See [Secure Container Runtime Guide](docs/guides/secure-container.md) for details.

## installation

Requirements:

- Docker (required for local execution)
- Python 3.10+ (required for examples and local runtime)

## tools

Install the Code Interpreter SDK

```bash
uv pip install opensandbox-code-interpreter
```

Create a sandbox and execute commands and codes.

```python
import asyncio
from datetime import timedelta

from code_interpreter import CodeInterpreter, SupportedLanguage
from opensandbox import Sandbox
from opensandbox.models import WriteEntry

async def main() -> None:
    # 1. Create a sandbox
    sandbox = await Sandbox.create(
        "opensandbox/code-interpreter:v1.1.0",
        entrypoint=["/opt/code-interpreter/code-interpreter.sh"],
        env={"PYTHON_VERSION": "3.11"},
        timeout=timedelta(minutes=10),
    )

    async with sandbox:

        # 2. Execute a shell command
        execution = await sandbox.commands.run("echo 'Hello OpenSandbox!'")
        print(execution.logs.stdout[0].text)

        # 3. Write a file
        await sandbox.files.write_files([
            WriteEntry(path="/tmp/hello.txt", data="Hello World", mode=644)
        ])

        # 4. Read a file
        content = await sandbox.files.read_file("/tmp/hello.txt")
        print(f"Content: {content}") # Content: Hello World

        # 5. Create a code interpreter
        interpreter = await CodeInterpreter.create(sandbox)

        # 6. Execute Python code (single-run, pass language directly)
        result = await interpreter.codes.run(
              """
                  import sys
                  print(sys.version)
                  result = 2 + 2
                  result
              """,
              language=SupportedLanguage.PYTHON,
        )

        print(result.result[0].text) # 4
        print(result.logs.stdout[0].text) # 3.11.14

        # 7. Cleanup the sandbox
        await sandbox.kill()

if __name__ == "__main__":
    asyncio.run(main())
```

## limitations

See [ROADMAP.md](ROADMAP.md) for the current project roadmap, planning scope,
and how roadmap items are managed.
