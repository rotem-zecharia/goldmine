# svg/svgo

SVG Optimizer for Node.js and CLI. ⚙️

## installation

You can install SVGO globally through npm, yarn, or pnpm. Alternatively, drop the global flag (`global`/`-g`) to use it in your Node.js project.

```sh
# npm
npm install -g svgo

# yarn
yarn global add svgo

# pnpm
pnpm add -g svgo
```

## tools

Process single files:

```sh
svgo one.svg two.svg -o one.min.svg two.min.svg
```

Process a directory of files recursively with `-r`/`--recursive` and `-f`/`--folder`:

```sh
svgo -rf path/to/directory_with_svgs -o path/to/output_directory
```

Help for advanced usage:

```sh
svgo --help
```

## configuration

SVGO has a plugin architecture. You can read more about all plugins in [Plugins | SVGO Documentation](https://svgo.dev/docs/plugins/), and the default plugins in [Preset Default | SVGO Documentation](https://svgo.dev/docs/preset-default/).

SVGO reads the configuration from `svgo.config.mjs` or the `--config path/to/config.mjs` command-line option. Some other parameters can be configured though command-line options too.

**`svgo.config.mjs`**

```js
export default {
  multipass: false, // boolean
  datauri: 'base64', // 'base64'|'enc'|'unenc'
  js2svg: {
    indent: 4, // number
    pretty: false, // boolean
  },
  plugins: [
    'preset-default', // built-in plugins enabled by default
    'prefixIds', // enable built-in plugins by name

    // enable built-in plugins with an object to configure plugins
    {
      name: 'prefixIds',
      params: {
        prefix: 'uwu',
      },
    },
  ],
};
```

### Default preset

Instead of configuring SVGO from scratch, you can tweak the default preset to suit your needs by configuring or disabling the respective plugin.

**`svgo.config.mjs`**

```js
export default {
  plugins: [
    {
      name: 'preset-default',
      params: {
        overrides: {
          // disable a default plugin
          cleanupIds: false,

          // customize the params of a default plugin
          inlineStyles: {
            onlyMatchedOnce: false,
          },
        },
      },
    },
  ],
};
```

You can find a list of the default plugins in the order they run in [Preset Default | SVGO Documentation](https://svgo.dev/docs/preset-default/#plugins-list).

### Custom plugins

You can also specify custom plugins:

**`svgo.config.mjs`**

```js
import importedPlugin from './imported-plugin';

export default {
  plugins: [
    // plugin imported from another JavaScript file
    importedPlugin,

    // plugin defined inline
    {
      name: 'customPlugin',
      params: {
        paramName: 'paramValue',
      },
      fn: (ast, params, info) => {},
    },
  ],
};
```
