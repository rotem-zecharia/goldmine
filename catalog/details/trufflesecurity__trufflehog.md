# trufflesecurity/trufflehog

Find, verify, and analyze leaked credentials

## installation

Several options are available for you:

### MacOS users

```bash
brew install trufflehog
```

### Docker:

<sub><i>_Ensure Docker engine is running before executing the following commands:_</i></sub>

#### &nbsp;&nbsp;&nbsp;&nbsp;Unix

```bash
docker run --rm -it -v "$PWD:/pwd" trufflesecurity/trufflehog:latest github --repo https://github.com/trufflesecurity/test_keys
```

#### &nbsp;&nbsp;&nbsp;&nbsp;Windows Command Prompt

```bash
docker run --rm -it -v "%cd:/=\%:/pwd" trufflesecurity/trufflehog:latest github --repo https://github.com/trufflesecurity/test_keys
```

#### &nbsp;&nbsp;&nbsp;&nbsp;Windows PowerShell

```bash
docker run --rm -it -v "${PWD}:/pwd" trufflesecurity/trufflehog github --repo https://github.com/trufflesecurity/test_keys
```

#### &nbsp;&nbsp;&nbsp;&nbsp;M1 and M2 Mac

```bash
docker run --platform linux/arm64 --rm -it -v "$PWD:/pwd" trufflesecurity/trufflehog:latest github --repo https://github.com/trufflesecurity/test_keys
```

### Binary releases

```bash
Download and unpack from https://github.com/trufflesecurity/trufflehog/releases
```

### Compile from source

```bash
git clone https://github.com/trufflesecurity/trufflehog.git
cd trufflehog; go install
```

### Using installation script

```bash
curl -sSfL https://raw.githubusercontent.com/trufflesecurity/trufflehog/main/scripts/install.sh | sh -s -- -b /usr/local/bin
```

### Using installation script, verify checksum signature (requires cosign to be installed)

```bash
curl -sSfL https://raw.githubusercontent.com/trufflesecurity/trufflehog/main/scripts/install.sh | sh -s -- -v -b /usr/local/bin
```

### Using installation script to install a specific version

```bash
curl -sSfL https://raw.githubusercontent.com/trufflesecurity/trufflehog/main/scripts/install.sh | sh -s -- -b /usr/local/bin <ReleaseTag like v3.56.0>
```

# :closed_lock_with_key: Verifying the artifacts

Checksums are applied to all artifacts, and the resulting checksum file is signed using cosign.

You need the following tool to verify signature:

- [Cosign](https://docs.sigstore.dev/cosign/system_config/installation/)

Verification steps are as follows:

1. Download the artifact files you want, and the following files from the [releases](https://github.com/trufflesecurity/trufflehog/releases) page.

   - trufflehog\_{version}\_checksums.txt
   - trufflehog\_{version}\_checksums.txt.pem
   - trufflehog\_{version}\_checksums.txt.sig

2. Verify the signature:

   ```shell
   cosign verify-blob <path to trufflehog_{version}_checksums.txt> \
   --certificate <path to trufflehog_{version}_checksums.txt.pem> \
   --signature <path to trufflehog_{version}_checksums.txt.sig> \
   --certificate-identity-regexp 'https://github\.com/trufflesecurity/trufflehog/\.github/workflows/.+' \
   --certificate-oidc-issuer "https://token.actions.githubusercontent.com"
   ```

3. Once the signature is confirmed as valid, you can proceed to validate that the SHA256 sums align with the downloaded artifact:

   ```shell
   sha256sum --ignore-missing -c trufflehog_{version}_checksums.txt
   ```

Replace `{version}` with the downloaded files version

Alternatively, if you are using the installation script, pass `-v` option to perform signature verification.
This requires Cosign binary to be installed prior to running the installation script.

# :rocket: Quick Start

## 1: Scan a repo for only verified secrets

Command:

```bash
trufflehog git https://github.com/trufflesecurity/test_keys --results=verified
```

Expected output:

```
🐷🔑🐷  TruffleHog. Unearth your secrets. 🐷🔑🐷

Found verified result 🐷🔑
Detector Type: AWS
Decoder Type: PLAIN
Raw result: AKIAYVP4CIPPERUVIFXG
Line: 4
Commit: fbc14303ffbf8fb1c2c1914e8dda7d0121633aca
File: keys
Email: counter <counter@counters-MacBook-Air.local>
Repository: https://github.com/trufflesecurity/test_keys
Timestamp: 2022-06-16 10:17:40 -0700 PDT
...
```

## 2: Scan a GitHub Org for only verified secrets

```bash
trufflehog github --org=trufflesecurity --results=verifie

## tools

TruffleHog has a sub-command for each source of data that you may want to scan:

- git
- github
- gitlab
- huggingface
- docker
- s3
- filesystem (files and directories)
- syslog
- circleci
- travisci
- gcs (Google Cloud Storage)
- postman
- jenkins
- elasticsearch
- stdin
- multi-scan

Each subcommand can have options that you can see with the `--help` flag provided to the sub command:

```
$ trufflehog git --help
usage: TruffleHog [<flags>] <command> [<args> ...]

TruffleHog is a tool for finding credentials.


Flags:
  -h, --[no-]help                Show context-sensitive help (also try --help-long and --help-man).
      --log-level=0              Logging verbosity on a scale of 0 (info) to 5 (trace). Can be
                                 disabled with "-1".
      --[no-]profile             Enables profiling and sets a pprof and fgprof server on :18066.
  -j, --[no-]json                Output in JSON format.
      --[no-]json-legacy         Use the pre-v3.0 JSON format. Only works with git, gitlab,
                                 and github sources.
      --[no-]github-actions      Output in GitHub Actions format.
      --[no-]sarif               Output in SARIF format for upload to GitHub code scanning (e.g.
                                 via github/codeql-action/upload-sarif).
      --concurrency=12           Number of concurrent workers.
      --[no-]no-verification     Don't verify the results.
      --results=RESULTS          Specifies which type(s) of results to output: verified (confirmed
                                 valid by API), unknown (verification failed due to error),
                                 unverified (detected but not verified), filtered_unverified
                                 (unverified but would have been filtered out). Defaults to
                                 verified,unverified,unknown.
      --[no-]no-color            Disable colorized output
      --[no-]allow-verification-overlap
                                 Allow verification of similar credentials across detectors
      --[no-]filter-unverified   Only output first unverified result per chunk per detector if there
                                 are more than one results.
      --filter-entropy=FILTER-ENTROPY
                                 Filter unverified results with Shannon entropy. Start with 3.0.
      --config=CONFIG            Path to configuration file.
      --[no-]print-avg-detector-time
                                 Print the average time spent on each detector.
      --[no-]no-update           Don't check for updates.
      --[no-]fail                Exit with code 183 if results are found.
      --[no-]fail-on-scan-errors
                                 Exit with non-zero error code if an error occurs during the scan.
      --verifier=VERIFIER ...    Set custom verification endpoints.
      --[no-]custom-verifiers-only
                                 Only use custom verification endpoints.
      --detector-timeout=DETECTOR-TIMEOUT
                                 Maximum time to spend scanning chunks per detector (e.g., 30s).
      --archive-max-size=ARCHIVE-MAX-SIZE
                                 Maximum size of archive to scan. (Byte units eg. 512B, 2KB, 4MB)
      --archive-max-depth=ARCHIVE-MAX-DEPTH
                                 Maximum depth of archive to scan.
      --archive-timeout=ARCHIVE-TIMEOUT
                                 Maximum time to spend extracting an archive.
      --include-detectors="all"  Comma separated list of detector types to include. Protobuf name or
                                 IDs may be used, as well as ranges.
      --exclude-detectors=EXCLUDE-DETECTORS
                                 Comma separated list of detector types to exclude. Protobuf name
                                 or IDs may be used, as well as ranges. IDs defined here take
                                 precedence over the include list.
      --[no-]no-verification-cache
            

## configuration

TruffleHog supports defining [custom regex detectors](#custom-regex-detector-alpha)
and multiple sources in a configuration file provided via the `--config` flag.
The regex detectors can be used with any subcommand, while the sources defined
in configuration are only for the `multi-scan` subcommand.

The configuration format for sources can be found on Truffle Security's
[source configuration documentation page](https://docs.trufflesecurity.com/scan-data-for-secrets).

Example GitHub source configuration and [options reference](https://docs.trufflesecurity.com/github#Fvm1I):

```yaml
sources:
- connection:
    '@type': type.googleapis.com/sources.GitHub
    repositories:
    - https://github.com/trufflesecurity/test_keys.git
    unauthenticated: {}
  name: example config scan
  type: SOURCE_TYPE_GITHUB
  verify: true
```

You may define multiple connections under the `sources` key (see above), and
TruffleHog will scan all of the sources concurrently.

## S3

The S3 source supports assuming IAM roles for scanning in addition to IAM users. This makes it easier for users to scan multiple AWS accounts without needing to rely on hardcoded credentials for each account.

The IAM identity that TruffleHog uses initially will need to have `AssumeRole` privileges as a principal in the [trust policy](https://aws.amazon.com/blogs/security/how-to-use-trust-policies-with-iam-roles/) of each IAM role to assume.

To scan a specific bucket using locally set credentials or instance metadata if on an EC2 instance:

```bash
trufflehog s3 --bucket=<bucket-name>
```

To scan a specific bucket using an assumed role:

```bash
trufflehog s3 --bucket=<bucket-name> --role-arn=<iam-role-arn>
```

Multiple roles can be passed as separate arguments. The following command will attempt to scan every bucket each role has permissions to list in the S3 API:

```bash
trufflehog s3 --role-arn=<iam-role-arn-1> --role-arn=<iam-role-arn-2>
```

Exit Codes:

- 0: No errors and no results were found.
- 1: An error was encountered. Sources may not have completed scans.
- 183: No errors were encountered, but results were found. Will only be returned if `--fail` flag is used.

## :octocat: TruffleHog Github Action
