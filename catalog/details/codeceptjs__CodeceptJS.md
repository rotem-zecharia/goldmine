# codeceptjs/CodeceptJS

Supercharged End 2 End Testing Framework for NodeJS

## features

CodeceptJS is a successor of [Codeception](http://codeception.com), a popular full-stack testing framework for PHP.
With CodeceptJS your scenario-driven functional and acceptance tests will be as simple and clean as they can be.
You don't need to worry about asynchronous nature of NodeJS or about various APIs of Playwright, Selenium, Puppeteer, etc. as CodeceptJS unifies them and makes them work as they are synchronous.

## Features

- 🪄 **AI-powered** with GPT features to assist and heal failing tests.
- ☕ Based on [Mocha](https://mochajs.org/) testing framework.
- 💼 Designed for scenario driven acceptance testing in BDD-style.
- 💻 Uses ES6 natively without transpiler.
- Also plays nice with TypeScript.
- </> Smart locators: use names, labels, matching text, CSS or XPath to locate elements.
- 🌐 Interactive debugging shell: pause test at any point and try different commands in a browser.
- ⚡ **Parallel testing** with dynamic test pooling for optimal load balancing and performance.
- 📊 **Built-in HTML Reporter** with interactive dashboard, step-by-step execution details, and comprehensive test analytics.
- Easily create tests, pageobjects, stepobjects with CLI generators.

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

### Basics

Let's see how we can handle basic form testing:

```js
Feature('CodeceptJS Demonstration')

Scenario('test some forms', ({ I }) => {
  I.amOnPage('http://simple-form-bootstrap.plataformatec.com.br/documentation')
  I.fillField('Email', 'hello@world.com')
  I.fillField('Password', secret('123456'))
  I.checkOption('Active')
  I.checkOption('Male')
  I.click('Create User')
  I.see('User is valid')
  I.dontSeeInCurrentUrl('/documentation')
})
```

All actions are performed by `I` object; assertions functions start with `see` function.
In these examples all methods of `I` are taken from WebDriver helper, see [reference](https://github.com/codeceptjs/CodeceptJS/blob/master/docs/helpers/WebDriver.md) to learn how to use them.

Let's execute this test with `run` command. Additional option `--steps` will show us the running process. We recommend use `--steps` or `--debug` during development.

```sh
npx codeceptjs run --steps
```

This will produce an output:

```sh
CodeceptJS Demonstration --
 test some forms
 • I am on page "http://simple-form-bootstrap.plataformatec.com.br/documentation"
 • I fill field "Email", "hello@world.com"
 • I fill field "Password", "****"
 • I check option "Active"
 • I check option "Male"
 • I click "Create User"
 • I see "User is valid"
 • I dont see in current url "/documentation"
 ✓ OK in 17752ms
```

CodeceptJS has an ultimate feature to help you develop and debug your test.
You can **pause execution of test in any place and use interactive shell** to try different actions and locators.
Just add `pause()` call at any place in a test and run it.

Interactive shell can be started outside test context by running:

```sh
npx codeceptjs shell
```

### Actions

We filled form with `fillField` methods, which located form elements by their label.
The same way you can locate element by name, `CSS` or `XPath` locators in tests:

```js
// by name
I.fillField('user_basic[email]', 'hello@world.com')
// by CSS
I.fillField('#user_basic_email', 'hello@world.com')
// don't make us guess locator type, specify it
I.fillField({ css: '#user_basic_email' }, 'hello@world.com')
```

Other methods like `checkOption`, and `click` work in a similar manner. They can take labels or CSS or XPath locators to find elements to interact.

### Assertions

Assertions start with `see` or `dontSee` prefix. In our case we are asserting that string 'User is valid' is somewhere in a webpage.
However, we can narrow the search to particular element by providing a second parameter:

```js
I.see('User is valid')
// better to specify context:
I.see('User is valid', '.alert-success')
```

In this case 'User is valid' string will be searched only inside elements located by CSS `.alert-success`.

### Grabbers

In case you need to return a value from a webpage and use it directly in test, you should use methods with `grab` prefix.
They are expected to be used inside `async/await` functions, and their results will be available in test:

```js
Feature('CodeceptJS Demonstration')

Scenario('test page title', async ({ I }) => {
  I.amOnPage('http://simple-form-bootstrap.plataformatec.com.br/documentation')
  const title = await I.grabTitle()
  I.expectEqual(title, 'Example application with SimpleForm and Twitter Bootstrap') // Avaiable with Expect helper. -> https://codecept.io/helpers/Expect/
})
```

The same way you can grab text, attributes, or form values and use them in next test steps.

### Before/After

Common preparation steps like opening a web page, logging in a user, can be placed in `Before` or `Background`:

```js
const { I } = inject()

Feature('CodeceptJS Demonstration')

Before(() => {
  // or Background
  I.amOnPage('http://simple-form-bootstrap.plataformatec.com.br/documentation')
})

Scenario('test some forms', () => {
  I.click('Create User')
  I.see('User is valid')
  I.dontSeeInCurrentUrl('/documentation')
})

Scenario('

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
}
```
