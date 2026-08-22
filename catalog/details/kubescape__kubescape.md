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

## 🎬 Demo

<img src="docs/img/demo-v3.gif" alt="Kubescape CLI demo">

---

## installation

### 1. Install Kubescape

```sh
curl -s https://raw.githubusercontent.com/kubescape/kubescape/master/install.sh | /bin/bash
```

> 💡 See [Installation](#-installation) for more options (Homebrew, Krew, Windows, etc.)

### 2. Run Your First Scan

```sh
# Scan your current cluster
kubescape scan

# Scan a specific YAML file or directory
kubescape scan /path/to/manifests/

# Scan a container image for vulnerabilities
kubescape scan image nginx:latest
```

### 3. Explore the Results

Kubescape provides a detailed security posture overview including:
- Control plane security status
- Access control risks
- Workload misconfigurations
- Network policy gaps
- Compliance scores (MITRE, NSA)

---

## 📦 Installation

### One-Line Install (Linux/macOS)

```bash
curl -s https://raw.githubusercontent.com/kubescape/kubescape/master/install.sh | /bin/bash
```

### Package Managers

| Platform | Command |
|----------|---------|
| **Homebrew** | `brew install kubescape` |
| **Krew** | `kubectl krew install kubescape` |
| **Arch Linux** | `yay -S kubescape` |
| **Ubuntu** | `sudo add-apt-repository ppa:kubescape/kubescape && sudo apt install kubescape` |
| **NixOS** | `nix-shell -p kubescape` |
| **Chocolatey** | `choco install kubescape` |
| **Scoop** | `scoop install kubescape` |

### Windows (PowerShell)

```powershell
iwr -useb https://raw.githubusercontent.com/kubescape/kubescape/master/install.ps1 | iex
```

📖 **[Full Installation Guide →](docs/installation.md)**

---

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

## 📖 Usage Examples

### Scanning

#### Scan a Running Cluster

```bash
# Default scan (all frameworks)
kubescape scan

# Scan with a specific framework
kubescape scan framework nsa
kubescape scan framework mitre
kubescape scan framework cis-v1.23-t1.0.1

# Scan a specific control
kubescape scan control C-0005 -v
```

#### Scan Files and Repositories

```bash
# Scan local YAML files
kubescape scan /path/to/manifests/

# Scan a Helm chart
kubescape scan /path/to/helm/chart/

# Scan a Git repository
kubescape scan https://github.com/kubescape/kubescape

# Scan with Kustomize
kubescape scan /path/to/kustomize/directory/
```

#### Scan Options

```bash
# Include/exclude namespaces
kubescape scan --include-namespaces production,staging
kubescape scan --exclude-namespaces kube-system,kube-public

## configuration

kubescape scan --kubeconfig /path/to/kubeconfig

# Set compliance threshold (exit code 1 if below threshold).
