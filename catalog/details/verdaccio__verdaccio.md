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

## Plugins

You can develop your own [plugins](https://verdaccio.org/docs/plugins) with the [verdaccio generator](https://github.com/verdaccio/generator-verdaccio-plugin). Installing [Yeoman](https://yeoman.io/) is required.

```
npm install -g yo
npm install -g generator-verdaccio-plugin
```

Learn more [here](https://verdaccio.org/docs/dev-plugins) how to develop plugins. Share your plugins with the community.

## End to End Testing

We test compatibility across different versions of npm, pnpm, and Yarn to ensure your favorite commands — from publishing packages to managing dependencies — work seamlessly with Verdaccio.

E2E CLI tests run in CI via the `verdaccio-e2e` tool on Node.js 24 against the following matrix:

| Package Manager | Versions        |
| --------------- | --------------- |
| npm             | 7, 8, 9, 10, 11 |
| yarn classic    | 1               |
| yarn modern     | 2, 3, 4         |
| pnpm            | 9, 10, 11       |

## Donations

Verdaccio is run by **volunteers**; nobody works on it full-time. If you find this project useful and would like to support its development, consider making a long-term support donation — **your logo will be featured in this section of the README.**

You can support the project via **[Donate](https://opencollective.com/verdaccio)** 💵👍🏻 — starting from _just $1/month_, or with a one-time contribution.

> **Note:** There is currently **no funding available for contributions or security research**.

## What does Verdaccio do for me?

### Use private packages

If you want to use all benefits of npm package system in your company without sending all code to the public, and use your private packages just as easy as public ones.

### Cache npmjs.org registry

If you have more than one server you want to install packages on, you might want to use this to decrease latency
(presumably "slow" npmjs.org will be connected to only once per package/version) and provide limited failover (if npmjs.org is down, we might still find something useful in the cache) or avoid issues like _[How one developer just broke Node, Babel and thousands of projects in 11 lines of JavaScript](https://www.theregister.co.uk/2016/03/23/npm_left_pad_chaos/)_, _[Many packages suddenly disappeared](https://github.com/npm/registry-issue-archive/issues/255)_ or _[Registry returns 404 for a package I have installed before](https://github.com/npm/registry-issue-archive/issues/329)_.

### Link multiple registries

If you use multiples registries in your organization and need to fetch packages from multiple sources in one single project you might take advance of the uplinks feature with Verdaccio, chaining multiple registries and fetching from one single endpoint.

### Override public packages

If you want to use a modified version of some 3rd-party package (for example, you found a bug, but maintainer didn't accept pull request yet), you can publish your version locally under the same name. See in detail [here](https://verdaccio.org/docs/best#override-public-packages).

### E2E Testing

Verdaccio has proved to be a lightweight registry that can be booted in a couple of seconds, fast enough for any CI. Many open source projects use Verdaccio for end to end testing, to mention some examples, **create-react-app**,

## features

- Installing packages (`npm install`, `npm update`, etc.) - **supported**
- Publishing packages (`npm publish`) - **supported**

### Advanced package control

- Unpublishing packages (`npm unpublish`) - **supported**
- Tagging (`npm dist-tag`) - **supported**
- Deprecation (`npm deprecate`) - **supported**

### User management

- Registering new users (`npm adduser {newuser}`) - **supported**
- Change password (`npm profile set password`) - **supported**
- Transferring ownership (`npm owner`) - **supported**
- Token (`npm token`) - **supported**

### Miscellaneous

- Searching (`npm search`) - **supported** (cli / browser)
- Ping (`npm ping`) - **supported**
- Starring (`npm star`, `npm unstar`, `npm stars`) - **supported**

### Security

- Audit (`npm/yarn audit`) - **supported**

## Report a vulnerability

If you want to report a security vulnerability, please follow the steps which we have defined for you in our [security policy](https://github.com/verdaccio/verdaccio/security/policy).

## Special Thanks

Thanks to the following companies to help us to achieve our goals providing free open source licenses. Every company provides enough resources to move this project forward.

| Company      | Logo                                                                                                                                    | License                                                                           |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| JetBrains    | [![jetbrain](https://github.com/verdaccio/verdaccio/blob/master/assets/thanks/jetbrains/logo.png?raw=true)](https://www.jetbrains.com/) | JetBrains provides licenses for products for active maintainers, renewable yearly |
| Crowdin      | [![crowdin](https://github.com/verdaccio/verdaccio/blob/master/assets/thanks/crowdin/logo.png?raw=true)](https://crowdin.com/)          | Crowdin provides platform for translations                                        |
| BrowserStack | [![browserstack](https://cdn.verdaccio.dev/readme/browserstack_logo.png)](https://www.browserstack.com/)                                | BrowserStack provides plan to run End to End testing for the UI                   |
| Algolia      | [![algolia](https://cdn.verdaccio.dev/sponsor/logo/algolia/logo.png)](https://algolia.com/)                                             | Algolia provides search services for the website                                  |
| Docker       | [![docker](https://cdn.verdaccio.dev/sponsor/logo/docker/docker.png)](https://www.docker.com/community/open-source/application)         | Docker offers unlimited pulls and unlimited egress to any and all users           |

## Maintainers

| [Juan Picado](https://github.com/juanpicado)                                   | [Ayush Sharma](https://github.com/ayusharma)                             | [Sergio Hg](https://github.com/sergiohgz)                                 |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------- |
| ![jotadeveloper](https://avatars3.githubusercontent.com/u/558752?s=120&v=4)    | ![ayusharma](https://avatars2.githubusercontent.com/u/6918450?s=120&v=4) | ![sergiohgz](https://avatars2.githubusercontent.com/u/14012309?s=120&v=4) |
|                                                                                | [@ayusharma\_](https://twitter.com/ayusharma_)                           | [@sergiohgz](https://twitter.com/sergiohgz)                               |
| [Priscila Oliveria](https://github.com/priscilawebdev)                         | [Daniel Ruf](https://github.com/DanielRuf)                               |
| ![priscilawebdev
