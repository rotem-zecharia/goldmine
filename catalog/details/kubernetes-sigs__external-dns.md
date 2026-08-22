# kubernetes-sigs/external-dns

Configure external DNS servers dynamically from Kubernetes resources

## features

Inspired by [Kubernetes DNS](https://github.com/kubernetes/dns), Kubernetes' cluster-internal DNS server, ExternalDNS makes Kubernetes resources discoverable via public DNS servers.
Like KubeDNS, it retrieves a list of resources (Services, Ingresses, etc.) from the [Kubernetes API](https://kubernetes.io/docs/api/) to determine a desired list of DNS records.
_Unlike_ KubeDNS, however, it's not a DNS server itself, but merely configures other DNS providers accordingly—e.g. [AWS Route 53](https://aws.amazon.com/route53/) or [Google Cloud DNS](https://cloud.google.com/dns/docs/).

In a broader sense, ExternalDNS allows you to control DNS records dynamically via Kubernetes resources in a DNS provider-agnostic way.

The [FAQ](docs/faq.md) contains additional information and addresses several questions about key concepts of ExternalDNS.

To see ExternalDNS in action, have a look at this [video](https://www.youtube.com/watch?v=9HQ2XgL9YVI) or read this [blogpost](https://codemine.be/posts/20190125-devops-eks-externaldns/).

## Running ExternalDNS

ExternalDNS allows you to keep selected zones (via `--domain-filter`) synchronized with Ingresses and Services of `type=LoadBalancer` and nodes in many DNS providers. See [In-tree providers](#in-tree-providers) for the built-in list, and [New providers](#new-providers) for webhook-based ones.

ExternalDNS is, by default, aware of the records it is managing, therefore it can safely manage non-empty hosted zones.
We strongly encourage you to set `--txt-owner-id` to a unique value that doesn't change for the lifetime of your cluster.
You might also want to run ExternalDNS in a dry run mode (`--dry-run` flag) to see the changes to be submitted to your DNS Provider API.

Note that all flags can be replaced with environment variables; for instance,
`--dry-run` could be replaced with `EXTERNAL_DNS_DRY_RUN=1`.

ExternalDNS runs as a controller in your cluster, and can also be run locally to test a configuration. For provider-specific setup, see the [In-tree providers](#in-tree-providers) table (each row links its tutorial) or the [webhook providers](#new-providers).
More tutorials — ingress controllers, sources, and provider extras — are in the [full documentation](https://kubernetes-sigs.github.io/external-dns/).

<details>
<summary><b>Running Locally</b></summary>

See the [contributor guide](docs/contributing/dev-guide.md) for details on compiling
from source.

## installation

Next, run an application and expose it via a Kubernetes Service:

```console
kubectl run nginx --image=nginx --port=80
kubectl expose pod nginx --port=80 --target-port=80 --type=LoadBalancer
```

Annotate the Service with your desired external DNS name. Make sure to change `example.org` to your domain.

```console
kubectl annotate service nginx "external-dns.kubernetes.io/hostname=nginx.example.org."
```

Optionally, you can customize the TTL value of the resulting DNS record by using the `external-dns.kubernetes.io/ttl` annotation:

```console
kubectl annotate service nginx "external-dns.kubernetes.io/ttl=10"
```

For more details on configuring TTL, see [advanced ttl](docs/advanced/ttl.md).

Use the internal-hostname annotation to create DNS records with ClusterIP as the target.

```console
kubectl annotate service nginx "external-dns.kubernetes.io/internal-hostname=nginx.internal.example.org."
```

If the service is not of type Loadbalancer you need the --publish-internal-services flag.

Locally run a single sync loop of ExternalDNS.

```console
external-dns --txt-owner-id my-cluster-id --provider google --google-project example-project --source service --once --dry-run
```

This should output the DNS records it will modify to match the managed zone with the DNS records you desire.
It also assumes you are running in the `default` namespace. See the [FAQ](docs/faq.md) for more information regarding namespaces.

Note: TXT records will have the `my-cluster-id` value embedded. Those are used to ensure that ExternalDNS is aware of the records it manages.

Once you're satisfied with the result, you can run ExternalDNS like you would run it in your cluster: as a control loop, and **not in dry-run** mode:

```console
external-dns --txt-owner-id my-cluster-id --provider google --google-project example-project --source service
```

Check that ExternalDNS has created the desired DNS record for your Service and that it points to its load balancer's IP. Then try to resolve it:

```console
dig +short nginx.example.org.
104.155.60.49
```

Now you can experiment and watch how ExternalDNS makes sure that your DNS records are configured as desired. Here are a couple of things you can try out:

- Change the desired hostname by modifying the Service's annotation.
- Recreate the Service and see that the DNS record will be updated to point to the new load balancer IP.
- Add another Service to create more DNS records.
- Remove Services to clean up your managed zone (record deletion requires `--policy=sync`; with `--policy=upsert-only` records are never deleted).

</details>

## Note

If using a txt registry and attempting to use a CNAME the `--txt-prefix` must be set to avoid conflicts. Changing `--txt-prefix` will result in lost ownership over previously created records.

If `externalIPs` list is defined for a `LoadBalancer` service, this list will be used instead of an assigned load balancer IP to create a DNS record.
It's useful when you run bare metal Kubernetes clusters behind NAT or in a similar setup, where a load balancer IP differs from a public IP (e.g. with [MetalLB](https://metallb.universe.tf)).

## New providers

No new provider will be added to ExternalDNS _in-tree_.

ExternalDNS has introduced a webhook system, which can be used to add a new provider.
See PR #3063 for all the discussions about it.

Some known providers using webhooks are the ones in the table below.

**NOTE**: The maintainers of ExternalDNS have not reviewed those providers, use them at your own risk and following the license
and usage recommendations provided by the respective projects. The maintainers of ExternalDNS take no responsibility for any issue or damage
from the usage of any externally developed webhook.

| Provider              | Repo                                                                 |
| --------------------- | -------------------------------------------------------------------- |
| Abion                 | https://github.com/abiondevelopm

## tools

- A full demo on GKE Kubernetes. See [How-to Kubernetes with DNS management (ssl-manager pre-req)](https://medium.com/@jpantjsoha/how-to-kubernetes-with-dns-management-for-gitops-31239ea75d8d)
- Run external-dns on GKE with workload identity. See [Kubernetes, ingress-nginx, cert-manager & external-dns](https://blog.atomist.com/kubernetes-ingress-nginx-cert-manager-external-dns/)
- [ExternalDNS integration with Azure DNS using workload identity](https://cloudchronicles.blog/blog/ExternalDNS-integration-with-Azure-DNS-using-workload-identity/)
