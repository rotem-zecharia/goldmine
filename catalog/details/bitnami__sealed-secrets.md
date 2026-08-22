# bitnami/sealed-secrets

A Kubernetes controller and tool for one-way encrypted Secrets

## features

Sealed Secrets is composed of two parts:

- A cluster-side controller / operator
- A client-side utility: `kubeseal`

The `kubeseal` utility uses asymmetric crypto to encrypt secrets that only the controller can decrypt.

These encrypted secrets are encoded in a `SealedSecret` resource, which you can see as a recipe for creating
a secret. Here is how it looks:

```yaml
apiVersion: bitnami.com/v1alpha1
kind: SealedSecret
metadata:
  name: mysecret
  namespace: mynamespace
spec:
  encryptedData:
    foo: AgBy3i4OJSWK+PiTySYZZA9rO43cGDEq.....
```

Once unsealed this will produce a secret equivalent to this:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: mysecret
  namespace: mynamespace
data:
  foo: YmFy  # <- base64 encoded "bar"
```

This normal [kubernetes secret](https://kubernetes.io/docs/concepts/configuration/secret/) will appear in the cluster
after a few seconds you can use it as you would use any secret that you would have created directly (e.g. reference it from a `Pod`).

Jump to the [Installation](#installation) section to get up and running.

The [Usage](#usage) section explores in more detail how you craft `SealedSecret` resources.

### SealedSecrets as templates for secrets

The previous example only focused on the encrypted secret items themselves, but the relationship between a `SealedSecret` custom resource and the `Secret` it unseals into is similar in many ways (but not in all of them) to the familiar `Deployment` vs `Pod`.

In particular, the annotations and labels of a `SealedSecret` resource are not the same as the annotations of the `Secret` that gets generated out of it.

To capture this distinction, the `SealedSecret` object has a `template` section which encodes all the fields you want the controller to put in the unsealed `Secret`.

The [Sprig function library](https://masterminds.github.io/sprig/) is available (except for `env`, `expandenv` and `getHostByName`) in addition to the default Go Text Template functions.

The `metadata` block is copied as is (the `ownerReference` field will be updated [unless disabled](#seal-secret-which-can-skip-set-owner-references)).

Other secret fields are handled individually. The `type` and `immutable` fields are copied, and the `data` field can be used to [template complex values](docs/examples/config-template) on the `Secret`. All other fields are currently ignored.

```yaml
apiVersion: bitnami.com/v1alpha1
kind: SealedSecret
metadata:
  name: mysecret
  namespace: mynamespace
  annotations:
    "kubectl.kubernetes.io/last-applied-configuration": ....
spec:
  encryptedData:
    .dockerconfigjson: AgBy3i4OJSWK+PiTySYZZA9rO43cGDEq.....
  template:
    type: kubernetes.io/dockerconfigjson
    immutable: true
    # this is an example of labels and annotations that will be added to the output secret
    metadata:
      labels:
        "jenkins.io/credentials-type": usernamePassword
      annotations:
        "jenkins.io/credentials-description": credentials from Kubernetes
```

The controller would unseal that into something like:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: mysecret
  namespace: mynamespace
  labels:
    "jenkins.io/credentials-type": usernamePassword
  annotations:
    "jenkins.io/credentials-description": credentials from Kubernetes
  ownerReferences:
  - apiVersion: bitnami.com/v1alpha1
    controller: true
    kind: SealedSecret
    name: mysecret
    uid: 5caff6a0-c9ac-11e9-881e-42010aac003e
type: kubernetes.io/dockerconfigjson
immutable: true
data:
  .dockerconfigjson: ewogICJjcmVk...
```

As you can see, the generated `Secret` resource is a "dependent object" of the `SealedSecret` and as such
it will be updated and deleted whenever the `SealedSecret` object gets updated or deleted.

### Public key / Certificate

The key certificate (public key portion) is used for sealing secrets,
and needs to be available wherever `kubeseal` is going to be
used. The certificate is not secret information, although you need to
ensure you are us

## installation

See https://github.com/bitnami/sealed-secrets/releases for the latest release and detailed installation instructions.

Cloud platform specific notes and instructions:

- [GKE](docs/GKE.md)

### Installation in Restricted Environments (No RBAC)

In environments where you lack permissions to create cluster-wide RBAC resources (like `ClusterRoles`), you can use the **`controller-norbac.yaml`** manifest available on the Releases page.

This version is a minimal deployment that includes only the **Deployment**, **Service**, and **CustomResourceDefinition**. It intentionally omits `ServiceAccount`, `ClusterRole`, and `ClusterRoleBinding`.

**Requirements:**
1. A cluster administrator must have already installed the SealedSecret CRDs.
2. You must have an allocated Service Account to run the deployment

### Controller

Once you deploy the manifest it will create the `SealedSecret` resource
and install the controller into `kube-system` namespace, create a service
account and necessary RBAC roles.

After a few moments, the controller will start, generate a key pair,
and be ready for operation. If it does not, check the controller logs.

#### Kustomize

The official controller manifest installation mechanism is just a YAML file.

In some cases you might need to apply your own customizations, like set a custom namespace or set some env variables.

`kubectl` has native support for that, see [kustomize](https://kustomize.io/).

#### Helm Chart

The Sealed Secrets helm chart is now officially supported and hosted in this GitHub repo.

```bash
helm repo add sealed-secrets https://bitnami.github.io/sealed-secrets
```

> NOTE: The versioning scheme of the helm chart differs from the versioning scheme of the sealed secrets project itself.

Originally the helm chart was maintained by the community and the first version adopted a major version of 1 while the
sealed secrets project itself is still at major 0.
This is ok because the version of the helm chart itself is not meant to be necessarily the version of the app itself.
However this is confusing, so our current versioning rule is:

1. The `SealedSecret` controller version scheme: 0.X.Y
2. The helm chart version scheme: 1.X.Y-rZ

There can be thus multiple revisions of the helm chart, with fixes that apply only to the helm chart without
affecting the static YAML manifests or the controller image itself.

> NOTE: The helm chart by default installs the controller with the name `sealed-secrets`, while the `kubeseal` command line interface (CLI) tries to access the controller with the name `sealed-secrets-controller`. You can explicitly pass `--controller-name` to the CLI:

```bash
kubeseal --controller-name sealed-secrets <args>
```

Alternatively, you can set `fullnameOverride` when installing the chart to override the name. Note also that `kubeseal` assumes that the controller is installed within the `kube-system` namespace by default. So if you want to use the `kubeseal` CLI without having to pass the expected controller name and namespace you should install the Helm Chart like this:

```bash
helm install sealed-secrets -n kube-system --set-string fullnameOverride=sealed-secrets-controller sealed-secrets/sealed-secrets
```

##### Helm Chart on a restricted environment

In some companies you might be given access only to a single namespace, not a full cluster.

One of the most restrictive environments you can encounter is:
- A `namespace` was allocated to you with some `service account`.
- You do not have access to the rest of the cluster, not even cluster CRDs.
- You may not even be able to create further service accounts or roles in your namespace.
- You are required to include resource limits in all your deployments.

Even with these restrictions you can still install the sealed secrets Helm Chart, there is only one pre-requisite:
- *The cluster must already have the sealed secrets CRDs installed*.

Once your admins installed the CRDs, if they were not there already, you can install the chart

## tools

KUBESEAL_VERSION=$(curl -s https://api.github.com/repos/bitnami/sealed-secrets/tags | jq -r '.[0].name' | cut -c 2-)

# Check if the version was fetched successfully
if [ -z "$KUBESEAL_VERSION" ]; then
    echo "Failed to fetch the latest KUBESEAL_VERSION"
    exit 1
fi

curl -OL "https://github.com/bitnami/sealed-secrets/releases/download/v${KUBESEAL_VERSION}/kubeseal-${KUBESEAL_VERSION}-linux-amd64.tar.gz"
tar -xvzf kubeseal-${KUBESEAL_VERSION}-linux-amd64.tar.gz kubeseal
sudo install -m 755 kubeseal /usr/local/bin/kubeseal
```

where `KUBESEAL_VERSION` is the [version tag](https://github.com/bitnami/sealed-secrets/tags) of the kubeseal release you want to use. For example: `v0.18.0`.

#### Installation from source

If you just want the latest client tool, it can be installed into
`$GOPATH/bin` with:

```bash
go install github.com/bitnami/sealed-secrets/cmd/kubeseal@main
```

You can specify a release tag or a commit SHA instead of `main`.

The `go install` command will place the `kubeseal` binary at `$GOPATH/bin`:

```bash
$(go env GOPATH)/bin/kubeseal
```

## Upgrade

Don't forget to check the [release notes](RELEASE-NOTES.md) for guidance about
possible breaking changes when you upgrade the client tool
and/or the controller.

### Supported Versions
Currently, only the latest version of Sealed Secrets is supported for production environments.

### Compatibility with Kubernetes versions
The Sealed Secrets controller ensures compatibility with different versions of Kubernetes by relying on a stable Kubernetes API. Typically, Kubernetes versions above 1.16 are considered compatible. However, we officially support the [currently recommended Kubernetes versions](https://kubernetes.io/releases/). Additionally, versions above 1.24 undergo thorough verification through our CI process with every release.

## Usage

```bash
# Create a json/yaml-encoded Secret somehow:
# (note use of `--dry-run` - this is just a local file!)
echo -n bar | kubectl create secret generic mysecret --dry-run=client --from-file=foo=/dev/stdin -o json >mysecret.json

# This is the important bit:
kubeseal -f mysecret.json -w mysealedsecret.json

# At this point mysealedsecret.json is safe to upload to Github,
# post on Twitter, etc.

# Eventually:
kubectl create -f mysealedsecret.json

# Profit!
kubectl get secret mysecret
```

Note the `SealedSecret` and `Secret` must have **the same namespace and
name**. This is a feature to prevent other users on the same cluster
from re-using your sealed secrets. See the [Scopes](#scopes) section for more info.

`kubeseal` reads the namespace from the input secret, accepts an explicit `--namespace` argument, and uses
the `kubectl` default namespace (in that order). Any labels,
annotations, etc on the original `Secret` are preserved, but not
automatically reflected in the `SealedSecret`.

By design, this scheme *does not authenticate the user*. In other
words, *anyone* can create a `SealedSecret` containing any `Secret`
they like (provided the namespace/name matches). It is up to your
existing config management workflow, cluster RBAC rules, etc to ensure
that only the intended `SealedSecret` is uploaded to the cluster. The
only change from existing Kubernetes is that the *contents* of the
`Secret` are now hidden while outside the cluster.

### Managing existing secrets

If you want the Sealed Secrets controller to manage an existing `Secret`, you can annotate your `Secret` with the `sealedsecrets.bitnami.com/managed: "true"` annotation. The existing `Secret` will be overwritten when unsealing a `SealedSecret` with the same name and namespace, and the `SealedSecret` will take ownership of the `Secret` (so that when the `SealedSecret` is deleted the `Secret` will also be deleted).

### Patching existing secrets

> New in v0.23.0

There are some use cases in which you don't want to replace the whole `Secret` but just add or modify some keys from the existing `Secret`. For this, you can annotate your `Secret` with `sealedsecr

## configuration

The answer is yes, you can configure the number of retries in your controller using the flag `--max-unseal-retries`. This flag allows you to configure the number of maximum retries to unseal your Sealed Secrets.

### How to manage SealedSecrets across the cluster or specific namespaces?

By default, the controller watches for `SealedSecret` resources across **all namespaces** using the `--all-namespaces` flag (which defaults to `true`).

If you need to restrict the controller's scope, you have two options:
- **Watch a subset of namespaces:** Use the `--additional-namespaces=<ns1>,<ns2>` flag to provide a comma-separated list of namespaces for the controller to manage.
- **Watch only the local namespace:** Set `--all-namespaces=false` (or the environment variable `SEALED_SECRETS_ALL_NAMESPACES=false`). This is useful for multi-tenant clusters where you want isolated controllers with independent sealing keys in each namespace.

## Community

- [#sealed-secrets on Kubernetes Slack](https://kubernetes.slack.com/messages/sealed-secrets)

Click [here](http://slack.k8s.io) to sign up to the Kubernetes Slack org.

### Related projects

- `kseal` A Kubeseal Companion: [https://github.com/eznix86/kseal](https://github.com/eznix86/kseal)
- `kubeseal-convert`: [https://github.com/EladLeev/kubeseal-convert](https://github.com/EladLeev/kubeseal-convert)
- Visual Studio Code extension: [https://marketplace.visualstudio.com/items?itemName=codecontemplator.kubeseal](https://marketplace.visualstudio.com/items?itemName=codecontemplator.kubeseal)
- WebSeal: generates secrets in the browser: [https://socialgouv.github.io/webseal](https://socialgouv.github.io/webseal)
- HybridEncrypt TypeScript implementation: [https://github.com/SocialGouv/aes-gcm-rsa-oaep](https://github.com/SocialGouv/aes-gcm-rsa-oaep)
- [DEPRACATED] Sealed Secrets Operator: [https://github.com/disposab1e/sealed-secrets-operator-helm](https://github.com/disposab1e/sealed-secrets-operator-helm)
