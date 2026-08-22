# google/osv-scanner

Vulnerability scanner written in Go which uses the data provided by https://osv.dev

## installation

To install OSV-Scanner, please refer to the [installation section](https://google.github.io/osv-scanner/installation) of our documentation. OSV-Scanner releases can be found on the [releases page](https://github.com/google/osv-scanner/releases) of the GitHub repository. The recommended method is to download a prebuilt binary for your platform. Alternatively, you can use
`go install github.com/google/osv-scanner/v2/cmd/osv-scanner@latest` to build it from source.

## features

For more information, please read our [detailed documentation](https://google.github.io/osv-scanner) to learn how to use OSV-Scanner. For detailed information about each feature, click their titles in this README.

Please note: These are the instructions for the latest OSV-Scanner V2 beta. If you are using V1, checkout the V1 [README](https://github.com/google/osv-scanner-v1) and [documentation](https://google.github.io/osv-scanner-v1/) instead.

## tools

```bash
$ osv-scanner scan source -r /path/to/your/dir
```

This command will recursively scan the specified directory for any supported package files, such as `package.json`, `go.mod`, `pom.xml`, etc. and output any discovered vulnerabilities.

OSV-Scanner has the option of using call analysis to determine if a vulnerable function is actually being used in the project, resulting in fewer false positives, and actionable alerts.

OSV-Scanner can also detect vendored C/C++ code for vulnerability scanning. See [here](https://google.github.io/osv-scanner/usage/#cc-scanning) for details.

#### Supported Lockfiles

OSV-Scanner supports 11+ language ecosystems and 19+ lockfile types. To check if your ecosystem is covered, please check out our [detailed documentation](https://google.github.io/osv-scanner/supported-languages-and-lockfiles/#supported-lockfiles).

### [Container Scanning](https://google.github.io/osv-scanner/usage/scan-image)

OSV-Scanner also supports comprehensive, layer-aware scanning for container images to detect vulnerabilities in the following operating system packages and language-specific dependencies.

| Distro Support | Language Artifacts Support |
| -------------- | -------------------------- |
| Alpine OS      | Go                         |
| Debian         | Java                       |
| Ubuntu         | Node                       |
|                | Python                     |

See the [full documentation](https://google.github.io/osv-scanner/supported-languages-and-lockfiles/#supported-artifacts) for details on support.

**Usage**:

```bash
$ osv-scanner scan image my-image-name:tag
```

![screencast of html output of container scanning](https://github.com/user-attachments/assets/8bb95366-27ec-45d1-86ed-e42890f2fb46)

### [License Scanning](https://google.github.io/osv-scanner/usage/license-scanning/)

Check your dependencies' licenses using deps.dev data. For a summary:

```bash
osv-scanner --licenses path/to/repository
```

To check against an allowed license list (SPDX format):

```bash
osv-scanner --licenses="MIT,Apache-2.0" path/to/directory
```

### [Offline Scanning](https://google.github.io/osv-scanner/usage/offline-mode/)

Scan your project against a local OSV database. No network connection is required after the initial database download. The database can also be manually downloaded.

```bash
osv-scanner --offline --download-offline-databases ./path/to/your/dir
```

### [Guided Remediation](https://google.github.io/osv-scanner/experimental/guided-remediation/) (Experimental)

> [!WARNING]
> Guided remediation (the `fix` command) can be risky when run on untrusted projects. It may trigger the package manager to execute scripts or follow external registries specified in the project. Please ensure you trust the source code and artifacts before proceeding.

OSV-Scanner provides guided remediation, a feature that suggests package version upgrades based on criteria such as dependency depth, minimum severity, fix strategy, and return on investment.
We currently support remediating vulnerabilities in the following files:

| Ecosystem | File Format (Type)             | Supported Remediation Strategies                                                                                       |
| :-------- | :----------------------------- | :--------------------------------------------------------------------------------------------------------------------- |
| npm       | `package-lock.json` (lockfile) | [`in-place`](https://google.github.io/osv-scanner/experimental/guided-remediation/#in-place-lockfile-changes)          |
| npm       | `package.json` (manifest)      | [`relock`](https://google.github.io/osv-scanner/experimental/guided-remediation/#relock-and-relax-direct-dependencies) |
| Maven     | `pom.xml` (manifest)           | [`override`](https://google.github.io/osv-scanner/experimental/guided-remediation/#override-dependency-versions)       |

This is available as a headless CLI command, as well a
