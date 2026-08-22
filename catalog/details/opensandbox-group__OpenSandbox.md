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

## Official Container Images

OpenSandbox release images are published under the same component name in
three official registries:

- Docker Hub: `docker.io/opensandbox/<component>`
- GitHub Container Registry: `ghcr.io/opensandbox-group/opensandbox/<component>`
- Alibaba Cloud Container Registry: `sandbox-registry.cn-zhangjiakou.cr.aliyuncs.com/opensandbox/<component>`

Tagged release images are signed keylessly with Cosign and include provenance
attestations. Pin production images by digest and follow the
[release verification guide](docs/community/release-verification.md) to verify
the image against the OpenSandbox GitHub Actions identity before deployment.

## SDKs

Python:

```bash
pip install opensandbox
```

Java/Kotlin (Gradle Kotlin DSL):

```kotlin
dependencies {
    implementation("com.alibaba.opensandbox:sandbox:{latest_version}")
}
```

Java/Kotlin (Maven):

```xml
<dependency>
    <groupId>com.alibaba.opensandbox</groupId>
    <artifactId>sandbox</artifactId>
    <version>{latest_version}</version>
</dependency>
```

JavaScript/TypeScript:

```bash
npm install @alibaba-group/opensandbox
```

C#/.NET:

```bash
dotnet add package Alibaba.OpenSandbox
```

Go:

```bash
go get github.com/alibaba/OpenSandbox/sdks/sandbox/go
```

## CLI

OpenSandbox also provides `osb`, a terminal CLI for the common sandbox workflow: create sandboxes, run commands, move files, inspect diagnostics, and manage runtime egress policy.

Install:

```bash
pip install opensandbox-cli
# or
uv tool install opensandbox-cli
```

Quick start:

```bash
osb config init
osb config set connection.domain localhost:8080
osb config set connection.protocol http
osb config set connection.api_key <your-api-key>
osb sandbox create --image python:3.12 --timeout 30m -o json
osb command run <sandbox-id> -o raw -- python -c "print(1 + 1)"
```

See the [CLI README](cli/README.md) for the full command reference.

## MCP

The OpenSandbox MCP server exposes sandbox creation, command execution, and text file operations to MCP-capable clients such as Claude Code and Cursor.

Install and run:

```bash
pip install opensandbox-mcp
opensandbox-mcp --domain localhost:8080 --protocol http
```

Minimal stdio config:

```json
{
  "mcpServers": {
    "opensandbox": {
      "command": "opensandbox-mcp",
      "args": ["--domain", "localhost:8080", "--protocol", "http"]
    }
  }
}
```

See the [MCP README](sdks/mcp/sandbox/python/README.md) for client-specific setup.

## installation

Requirements:

- Docker (required for local execution)
- Python 3.10+ (required for examples and local runtime)

### Install and Configure the Sandbox Server

```bash
uvx opensandbox-server init-config ~/.sandbox.toml --example docker

uvx opensandbox-server

# Show help
# uvx opensandbox-server -h
```

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

### More Examples

OpenSandbox provides examples covering SDK usage, agent integrations, browser automation, and training workloads. All example code is located in the `examples/` directory.

#### 🎯 Basic Examples

- **[code-interpreter](docs/examples/code-interpreter.md)** - End-to-end Code Interpreter SDK workflow in a sandbox.
- **[aio-sandbox](docs/examples/aio-sandbox.md)** - All-in-One sandbox setup using the OpenSandbox SDK.
- **[agent-sandbox](docs/examples/agent-sandbox.md)** - Example integration for running OpenSandbox workloads on Kubernetes with [kubernetes-sigs/agent-sandbox](https://github.com/kubernetes-sigs/agent-sandbox).
- **Volumes** — [Docker PVC / named volumes](docs/examples/docker-pvc-volume-mount.md), [Docker OSSFS](docs/examples/docker-ossfs-volume-mount.md), [Kubernetes PVC](docs/examples/kubernetes-pvc-volume-mount.md): persistent and shared storage patterns.

#### 🤖 Coding Agent Integrations

- **Coding CLIs** — [Claude Code](docs/examples/claude-code.md), [Gemini CLI](docs/examples/gemini-cli.md), [OpenAI Codex CLI](docs/examples/codex-cli.md), [OpenCode](docs/examples/opencode.md), [Qwen Code](docs/examples/qwen-code.md), [Kimi CLI](docs/examples/kimi-cli.md): run each CLI inside OpenSandbox.
- **[langgraph](docs/examples/langgraph.md)** - LangGraph state-machine workflow that creates/runs a sandbox job with fallback retry.
- **[google-adk](docs/examples/google-adk.md)** - Google ADK agent using OpenSandbox tools to write/read files and run commands.
- **[openclaw](docs/examples/openclaw.md)** - Launch an OpenClaw Gateway inside a sandbox.

#### 🌐 Browser and Desktop Environments

- **[chrome](docs/examples/chrome.md)** - Chromium sandbox with VNC and DevTools access for automation and debugging.
- **[playwright](docs/examples/playwright.md)** - Playwright + Chromium headless scraping and testing example.
- **[desktop](docs/examples/desktop.md)** - Full desktop environment in a sandbox with VNC access.
- **[vscode](docs/examples/vscode.md)** - code-server (VS Code Web) running inside a sandbox for remote dev.

#### 🧠 Training and Evaluation

- **[harbor-evaluation](docs/examples/harbor-evaluation.md)** - Run a [Harbor](https://github.com/harbor-framework/harbor) ag

## limitations

See [ROADMAP.md](ROADMAP.md) for the current project roadmap, planning scope,
and how roadmap items are managed.

## Contact and Discussion

- Issues: Submit bugs, feature requests, or design discussions through GitHub Issues
- Discord: Join the [OpenSandbox Discord community](https://discord.gg/g7FuPs8YeD)
- DingTalk: Join the [OpenSandbox technical discussion group](https://qr.dingtalk.com/action/joingroup?code=v1,k1,A4Bgl5q1I1eNU/r33D18YFNrMY108aFF38V+r19RJOM=&_dt_no_comment=1&origin=11)

## Star History

[![Star History Chart](https://star-history.dera.page/svg?repos=opensandbox-group/OpenSandbox&type=date&legend=top-left)](https://star-history.dera.page/#opensandbox-group/OpenSandbox&type=date&legend=top-left)
