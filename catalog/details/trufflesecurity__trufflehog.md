# trufflesecurity/trufflehog

Find, verify, and analyze leaked credentials

## installation

Several options are available for you:

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
