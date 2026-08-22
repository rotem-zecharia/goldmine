# codeceptjs/CodeceptJS

Supercharged End 2 End Testing Framework for NodeJS

## features

CodeceptJS is a successor of [Codeception](http://codeception.com), a popular full-stack testing framework for PHP.
With CodeceptJS your scenario-driven functional and acceptance tests will be as simple and clean as they can be.
You don't need to worry about asynchronous nature of NodeJS or about various APIs of Playwright, Selenium, Puppeteer, etc. as CodeceptJS unifies them and makes them work as they are synchronous.

## installation

```sh
npm i codeceptjs --save
```

Move to directory where you'd like to have your tests (and CodeceptJS config) stored, and execute:

```sh
npx codeceptjs init
```

to create and configure test environment. It is recommended to select WebDriver from the list of helpers, if you need to write Selenium WebDriver tests.

After that create your first test by executing:

```sh
npx codeceptjs generate:test
```

Now test is created and can be executed with

```sh
npx codeceptjs run
```

If you want to write your tests using TypeScript just generate standard Type Definitions by executing:

```sh
npx codeceptjs def .
```

Later you can even automagically update Type Definitions to include your own custom [helpers methods](docs/helpers.md).

Note:

- CodeceptJS requires Node.js version `12+` or later.

## tools

Learn CodeceptJS by examples. Let's assume we have CodeceptJS installed and WebDriver helper enabled.

## configuration

Add the `testomatio` plugin to your `codecept.conf.js`:

```js
plugins: {
  testomatio: {
    enabled: true,
    require: '@testomatio/reporter/codecept',
    html: true,
    reportDir: 'output/report',
  },
