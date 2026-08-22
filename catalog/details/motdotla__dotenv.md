# motdotla/dotenv

Loads environment variables from .env for nodejs projects.

## tools

Install it.

```sh
npm install dotenv --save
```

Create a `.env` file in the root of your project:

```ini

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
