# motdotla/dotenv

Loads environment variables from .env for nodejs projects.

## tools

Install it.

```sh
npm install dotenv --save
```

Create a `.env` file in the root of your project:

```ini
# .env
HELLO="Dotenv"
OPENAI_API_KEY="your-api-key-goes-here"
```

As early as possible in your application, import and configure dotenv:

```javascript
// index.js
require('dotenv').config()
// or import 'dotenv/config' // for esm

console.log(`Hello ${process.env.HELLO}`)
```
```sh
$ node index.js
◇ injected env (2) from .env
Hello Dotenv
```

That's it. `process.env` now has the keys and values you defined in your `.env` file.

&nbsp;

## Advanced

<details><summary>ES6</summary><br>

Import with [ES6](#how-do-i-use-dotenv-with-import):

```javascript
import 'dotenv/config'
```

`DOTENV_CONFIG_ENCODING`, `DOTENV_CONFIG_PATH`, `DOTENV_CONFIG_QUIET`, `DOTENV_CONFIG_DEBUG`, `DOTENV_CONFIG_OVERRIDE`, `DOTENV_CONFIG_SECURE`, and `DOTENV_CONFIG_FAST` provide defaults for `config()` and `dotenv run`. Options/flags passed directly take precedence.

</details>
<details><summary>bun</summary><br>

```sh
bun add dotenv
```

</details>
<details><summary>yarn</summary><br>

```sh
yarn add dotenv
```

</details>
<details><summary>pnpm</summary><br>

```sh
pnpm add dotenv
```

</details>
<details><summary>deno</summary><br>

```sh
deno add dotenv
```

</details>
<details><summary>Monorepos</summary><br>

For monorepos with a structure like `apps/backend/app.js`, put it the `.env` file in the root of the folder where your `app.js` process runs.

```ini
# app/backend/.env
S3_BUCKET="YOURS3BUCKET"
SECRET_KEY="YOURSECRETKEYGOESHERE"
```

</details>
<details><summary>Multiline Values</summary><br>

If you need multiline variables, for example private keys, those are now supported (`>= v15.0.0`) with line breaks:

```ini
PRIVATE_KEY="-----BEGIN RSA PRIVATE KEY-----
...
Kh9NV...
...
-----END RSA PRIVATE KEY-----"
```

Alternatively, you can double quote strings and use the `\n` character:

```ini
PRIVATE_KEY="-----BEGIN RSA PRIVATE KEY-----\nKh9NV...\n-----END RSA PRIVATE KEY-----\n"
```

</details>
<details><summary>Comments</summary><br>

Comments may be added to your file on their own line or inline:

```ini
# This is a comment
SECRET_KEY=YOURSECRETKEYGOESHERE # comment
SECRET_HASH="something-with-a-#-hash"
```

Comments begin where a `#` exists, so if your value contains a `#` please wrap it in quotes. This is a breaking change from `>= v15.0.0` and on.

</details>
<details><summary>Parsing</summary><br>

The engine which parses the contents of your file containing environment variables is available to use. It accepts a String or Buffer and will return an Object with the parsed keys and values.

```javascript
const dotenv = require('dotenv')
const buf = Buffer.from('BASIC=basic')
const config = dotenv.parse(buf) // will return an object
console.log(typeof config, config) // object { BASIC : 'basic' }
```

</details>
<details><summary>Run</summary><br>

Use `dotenv run --` to run a command with environment variables from your `.env` file.

```bash
$ dotenv run -- node index.js
◇ injected env (2) from .env
```

Use `-f` to select one or more `.env` files.

```bash
$ dotenv run -f .env.local -f .env -- node index.js
◇ injected env (2) from .env.local, .env
```

Use `--quiet` to suppress the injected env message.

```bash
$ dotenv run --quiet -- node index.js
```

Use `--override` to overwrite existing environment variables, and `--debug` for debug logging.

```bash
$ dotenv run --override --debug -- node index.js
```

Use `--secure` or `config({ secure: true })` to decrypt via [dotenvx](https://dotenvx.com).

```bash
$ npm i @dotenvx/dotenvx
$ dotenv run --secure -- node index.js
```

```js
require('dotenv').config({ secure: true })
```

Or with an environment variable:

```bash
$ DOTENV_CONFIG_SECURE=true dotenv run -- node index.js
$ DOTENV_CONFIG_SECURE=true node -e "require('dotenv').config()"
```

`dotenv run --secure` resolves local `@dotenvx/dotenvx` then `dotenvx` on your `PATH`. `config({ secure: true })` requires a local `@doten

## configuration

`config` will read your `.env` file, parse the contents, assign it to
[`process.env`](https://nodejs.org/docs/latest/api/process.html#process_process_env),
and return an Object with a `parsed` key containing the loaded content or an `error` key if it failed.

```js
const result = dotenv.config()

if (result.error) {
  throw result.error
}

console.log(result.parsed)
```

You can additionally, pass options to `config`.

#### Options

##### path

Default: `path.resolve(process.cwd(), '.env')`

Specify a custom path if your file containing environment variables is located elsewhere.

```js
require('dotenv').config({ path: '/custom/path/to/.env' })
```
You can also pass a `URL` object:

```js
const fileUrl = new URL('file:///custom/path/to/.env')

require('dotenv').config({ path: fileUrl })
```

By default, `config` will look for a file called .env in the current working directory.

Pass in multiple files as an array, and they will be parsed in order and combined with `process.env` (or `option.processEnv`, if set). The first value set for a variable will win, unless the `options.override` flag is set, in which case the last value set will win.  If a value already exists in `process.env` and the `options.override` flag is NOT set, no changes will be made to that value. 

```js  
require('dotenv').config({ path: ['.env.local', '.env'] })
```

##### quiet

Default: `false`

Suppress runtime logging message.

```js
// index.js
require('dotenv').config({ quiet: false }) // change to true to suppress
console.log(`Hello ${process.env.HELLO}`)
```

```ini
# .env
HELLO=World
```

```sh
$ node index.js
Hello World
```

##### encoding

Default: `utf8`

Specify the encoding of your file containing environment variables.

```js
require('dotenv').config({ encoding: 'latin1' })
```

##### debug

Default: `false`

Turn on logging to help debug why certain keys or values are not being set as you expect.

```js
require('dotenv').config({ debug: process.env.DEBUG })
```

##### override

Default: `false`

Override any environment variables that have already been set on your machine with values from your .env file(s). If multiple files have been provided in `option.path` the override will also be used as each file is combined with the next. Without `override` being set, the first value wins. With `override` set the last value wins. 

```js
require('dotenv').config({ override: true })
```

##### secure

Default: `false`

Decrypt via [dotenvx](https://dotenvx.com). Requires a local `@dotenvx/dotenvx` install.

```js
require('dotenv').config({ secure: true })
```

##### fast

Default: `false`

Use the faster character-scanner parser (~2x). Default remains the classic regex parser.

```js
require('dotenv').config({ fast: true })
```

##### processEnv

Default: `process.env`

Specify an object to write your environment variables to. Defaults to `process.env` environment variables.

```js
const myObject = {}
require('dotenv').config({ processEnv: myObject })

console.log(myObject) // values from .env
console.log(process.env) // this was not changed or written to
```

### Parse

The engine which parses the contents of your file containing environment
variables is available to use. It accepts a String or Buffer and will return
an Object with the parsed keys and values.

```js
const dotenv = require('dotenv')
const buf = Buffer.from('BASIC=basic')
const config = dotenv.parse(buf) // will return an object
console.log(typeof config, config) // object { BASIC : 'basic' }
```

#### Options

##### debug

Default: `false`

Turn on logging to help debug why certain keys or values are not being set as you expect.

```js
const dotenv = require('dotenv')
const buf = Buffer.from('hello world')
const opt = { debug: true }
const config = dotenv.parse(buf, opt)
// expect a debug message because the buffer is not in KEY=VAL form
```

### Populate

The engine which populates the contents of your .env file to `process.env` is available for use. It accepts a target, a source, a
