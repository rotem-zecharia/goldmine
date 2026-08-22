# verdaccio/verdaccio

A lightweight Node.js private proxy registry

## installation

> Node.js v24 as minimum version required

Install with npm:

```bash
npm install -g verdaccio@next-9
```

With `yarn`

```bash
yarn global add verdaccio@next-9
```

With `pnpm`

```bash
pnpm i -g verdaccio@next-9
```

or

```bash
docker pull verdaccio/verdaccio:nightly-master
```

or with _helm_ [official chart](https://github.com/verdaccio/charts).

```bash
helm repo add verdaccio https://charts.verdaccio.org
helm repo update
helm install verdaccio/verdaccio
```

Furthermore, you can read the [**Debugging Guidelines**](https://github.com/verdaccio/verdaccio/wiki/Debugging-Verdaccio) and the [**Docker Examples**](https://github.com/verdaccio/verdaccio/tree/master/docker-examples) for more advanced development.

## features

- Installing packages (`npm install`, `npm update`, etc.) - **supported**
- Publishing packages (`npm publish`) - **supported**
