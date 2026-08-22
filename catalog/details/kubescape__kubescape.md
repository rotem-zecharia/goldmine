# kubescape/kubescape

Kubescape is an open-source Kubernetes security platform for your IDE, CI/CD pipelines, and clusters. It includes risk analysis, security, compliance, and misconfiguration scanning, saving Kubernetes 

## features

| Feature | Description |
|---------|-------------|
| 🔍 **Misconfiguration Scanning** | Scan clusters, YAML files, and Helm charts against NSA-CISA, MITRE ATT&CK®, and CIS Benchmarks |
| 🐳 **Image Vulnerability Scanning** | Detect CVEs in container images using [Grype](https://github.com/anchore/grype) |
| 🩹 **Image Patching** | Automatically patch vulnerable images using [Copacetic](https://github.com/project-copacetic/copacetic) |
| 🔧 **Auto-Remediation** | Automatically fix misconfigurations in Kubernetes manifests |
| 🛡️ **Admission Control** | Enforce security policies with Validating Admission Policies (VAP) |
| 📊 **Runtime Security** | eBPF-based runtime monitoring via [Inspektor Gadget](https://github.com/inspektor-gadget) |
| 🤖 **AI Integration** | MCP server for AI assistant integration |

---

## installation

```sh
curl -s https://raw.githubusercontent.com/kubescape/kubescape/master/install.sh | /bin/bash
```

> 💡 See [Installation](#-installation) for more options (Homebrew, Krew, Windows, etc.)

## tools

Kubescape provides a comprehensive CLI with the following commands:

| Command | Description |
|---------|-------------|
| [`kubescape scan`](#scanning) | Scan cluster, files, or images for security issues |
| [`kubescape scan image`](#image-scanning) | Scan container images for vulnerabilities |
| [`kubescape fix`](#auto-fix) | Auto-fix misconfigurations in manifest files |
| [`kubescape patch`](#image-patching) | Patch container images to fix vulnerabilities |
| [`kubescape list`](#list-frameworks-and-controls) | List available frameworks and controls |
| [`kubescape download`](#offline-support) | Download artifacts for offline/air-gapped use |
| [`kubescape config`](#configuration) | Manage cached configurations |
| [`kubescape operator`](#operator-commands) | Interact with in-cluster Kubescape operator |
| [`kubescape vap`](#validating-admission-policies) | Manage Validating Admission Policies |
| [`kubescape mcpserver`](#mcp-server) | Start MCP server for AI assistant integration |
| `kubescape completion` | Generate shell completion scripts |
| `kubescape version` | Display version information |

---

## configuration

kubescape scan --kubeconfig /path/to/kubeconfig
