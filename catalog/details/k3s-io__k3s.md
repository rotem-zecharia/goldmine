# k3s-io/k3s

Lightweight Kubernetes

## configuration

sudo k3s kubectl get nodes

# On a different node run the below. NODE_TOKEN comes from
# /var/lib/rancher/k3s/server/node-token on your server
sudo k3s agent --server https://myserver:6443 --token ${NODE_TOKEN}
```

Contributing
------------

Please check out our [contributing guide](CONTRIBUTING.md) if you're interested in contributing to K3s.

Security
--------

Security issues in K3s can be reported by sending an email to [security@k3s.io](mailto:security@k3s.io).
Please do not file issues about security issues.
