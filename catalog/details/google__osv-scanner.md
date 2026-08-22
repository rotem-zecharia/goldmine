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
