# fission/fission

Fast and Simple Serverless Functions for Kubernetes

## installation

```bash
  # Add the stock NodeJS env to your Fission deployment
  $ fission env create --name nodejs --image ghcr.io/fission/node-env

  # Create a function with a javascript one-liner that prints "hello world"
  $ fission function create --name hello --env nodejs --code https://raw.githubusercontent.com/fission/examples/master/nodejs/hello.js

  # Run the function.  This takes about 100msec the first time.
  $ fission function test --name hello
  Hello, world!
```

## Learn More

- Understand [Fission Concepts](https://fission.io/docs/concepts/).
- See the [installation guide](https://fission.io/docs/installation/) for installing and running Fission.
- You can learn more about Fission and get started from [Fission Docs](https://fission.io/docs).
- To see Fission in action, check out the [Fission Examples Repo](https://github.com/fission/examples).
- See the [troubleshooting guide](https://fission.io/docs/trouble-shooting/) for debugging your functions and Fission installation.

## Contributing

Check out the [contributing guide](CONTRIBUTING.md).

## Who is using Fission?
- [Fareye](https://www.getfareye.com)
- Apple
- [iQuanti](https://www.iquanti.com)
- A large telecom CSP
- [Gadget](https://gadget.dev)
- [CinnamonAI](https://cinnamon.is/en)
- [Armo](https://www.armosec.io/)
- [The Social Audience](https://thesocialaudience.com/)
- [KubeML](https://github.com/DiegoStock12/kubeml)
- Unilever
- [BD](https://www.bd.com/en-in)
- [Biofourmis](https://biofourmis.com/)
- [Babylon](https://www.babylonhealth.com/en-gb)

## Sponsors

The following companies, organizations, and individuals support Fission's ongoing maintenance and development. If you are using/contributing to Fission, we would be happy to list you here, please raise a Pull request.

<p>
  <a href="https://infracloud.io/"><img src="https://fission.io/sponsors/infracloud.png" alt="InfraCloud" height="70"></a>
  <a href="https://srcmesh.com/"><img src="https://fission.io/sponsors/srcmesh.png" alt="Srcmesh" height="70"></a>
  <a href="https://www.digitalocean.com/?utm_medium=opensource&utm_source=fissionio">
    <img src="https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/PoweredByDO/DO_Powered_by_Badge_blue.svg" width="201px">
  </a>
</p>

# License

Fission is licensed under the Apache License 2.0 - see the [LICENSE](./LICENSE) file for details
