# bridgecrewio/checkov

Prevent cloud misconfigurations and find vulnerabilities during build-time in infrastructure as code, container images and open source packages with Checkov by Bridgecrew.

## requirements

* Python >= 3.9, <=3.12
 * Terraform >= 0.12

## installation

To install pip follow the official [docs](https://pip.pypa.io/en/stable/cli/pip_install/)

```sh
pip3 install checkov
```

Certain environments (e.g., Debian 12) may require you to install Checkov in a virtual environment

```sh

## configuration

python3 -m venv /path/to/venv/checkov
cd /path/to/venv/checkov
source ./bin/activate

## tools

Allow only the two specified checks to run:
```sh
checkov --directory . --check CKV_AWS_20,CKV_AWS_57
```

Run all checks except the one specified:
```sh
checkov -d . --skip-check CKV_AWS_20
```

Run all checks except checks with specified patterns:
```sh
checkov -d . --skip-check CKV_AWS*
```

Run all checks that are MEDIUM severity or higher (requires API key):
```sh
checkov -d . --check MEDIUM --bc-api-key ...
```

Run all checks that are MEDIUM severity or higher, as well as check CKV_123 (assume this is a LOW severity check):
```sh
checkov -d . --check MEDIUM,CKV_123 --bc-api-key ...
```

Skip all checks that are MEDIUM severity or lower:
```sh
checkov -d . --skip-check MEDIUM --bc-api-key ...
```

Skip all checks that are MEDIUM severity or lower, as well as check CKV_789 (assume this is a high severity check):
```sh
checkov -d . --skip-check MEDIUM,CKV_789 --bc-api-key ...
```

Run all checks that are MEDIUM severity or higher, but skip check CKV_123 (assume this is a medium or higher severity check):
```sh
checkov -d . --check MEDIUM --skip-check CKV_123 --bc-api-key ...
```

Run check CKV_789, but skip it if it is a medium severity (the --check logic is always applied before --skip-check)
```sh
checkov -d . --skip-check MEDIUM --check CKV_789 --bc-api-key ...
```

For Kubernetes workloads, you can also use allow/deny namespaces.  For example, do not report any results for the
kube-system namespace:
```sh
checkov -d . --skip-check kube-system
```

Run a scan of a container image. First pull or build the image then refer to it by the hash, ID, or name:tag:
```sh
checkov --framework sca_image --docker-image sha256:1234example --dockerfile-path /Users/path/to/Dockerfile --repo-id ... --bc-api-key ...

checkov --docker-image <image-name>:tag --dockerfile-path /User/path/to/Dockerfile --repo-id ... --bc-api-key ...
```

You can use --image flag also to scan container image instead of --docker-image for shortener:
```sh
checkov --image <image-name>:tag --dockerfile-path /User/path/to/Dockerfile --repo-id ... --bc-api-key ...
```

Run an SCA scan of packages in a repo:
```sh
checkov -d . --framework sca_package --bc-api-key ... --repo-id <repo_id(arbitrary)>
```

Run a scan of a directory with environment variables removing buffering, adding debug level logs:
```sh
PYTHONUNBUFFERED=1 LOG_LEVEL=DEBUG checkov -d .
```
OR enable the environment variables for multiple runs
```sh
export PYTHONUNBUFFERED=1 LOG_LEVEL=DEBUG
checkov -d .
```

Run secrets scanning on all files in MyDirectory. Skip CKV_SECRET_6 check on json files that their suffix is DontScan
```sh
checkov -d /MyDirectory --framework secrets --repo-id ... --bc-api-key ... --skip-check CKV_SECRET_6:.*DontScan.json$
```

Run secrets scanning on all files in MyDirectory. Skip CKV_SECRET_6 check on json files that contains "skip_test" in path
```sh
checkov -d /MyDirectory --framework secrets --repo-id ... --bc-api-key ... --skip-check CKV_SECRET_6:.*skip_test.*json$
```

One can mask values from scanning results by supplying a configuration file (using --config-file flag) with mask entry.
The masking can apply on resource & value (or multiple values, separated with a comma).
Examples:
```sh
mask:
- aws_instance:user_data
- azurerm_key_vault_secret:admin_password,user_passwords
```
In the example above, the following values will be masked:
- user_data for aws_instance resource
- both admin_password &user_passwords for azurerm_key_vault_secret


### Suppressing/Ignoring a check

Like any static-analysis tool it is limited by its analysis scope.
For example, if a resource is managed manually, or using subsequent configuration management tooling,
suppression can be inserted as a simple code annotation.

#### Suppression comment format

To skip a check on a given Terraform definition block or CloudFormation resource, apply the following comment pattern inside it's scope:

`checkov:skip=<check_id>:<suppression_comment>`

* `<check_id>` is one of the [available check scanners](do
