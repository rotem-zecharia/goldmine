# getgauge/taiko

A node.js library for testing modern web applications

## features

Taiko is built ground up to test modern web applications. Here’s a list of a few unique features that sets it apart from other browser automation tools.

* Easy Installation
* Interactive Recorder
* Smart Selectors
* Handle XHR and dynamic content
* Request/Response stubbing and mocking

## installation

## Easy Installation

Taiko works on Windows, MacOS and Linux. You only need [Node.js](https://nodejs.org/en/) installed in your system to start writing Taiko scripts in JavaScript. After you’ve installed Node.js open a terminal application (or powershell in the case of Windows) and install Taiko using [npm](https://www.npmjs.com/) with the command

    $ npm install -g taiko

This installs Taiko and the latest version of Chromium browser. We are all set to do some testing!

## Interactive Recorder

Taiko comes with a Recorder that’s a REPL for writing test scripts. You can use Taiko’s JavaScript API to control the browser from the REPL. To launch the REPL type taiko in your favorite terminal application

    $ taiko
    Version: 1.4.0 (Chromium: 126.0.6468.0)
    Type .api for help and .exit to quit
    >

This launches the Taiko prompt. You can now use Taiko’s API as commands in this prompt. For example, launch a Chromium browser instance using

    > openBrowser()

You can now automate this Chromium browser instance with commands, for example, make the browser search google for something.

    > goto("google.com/?hl=en")
    > write("taiko test automation")
    > click("Google Search")

These commands make the browser go to google’s home page, type the text "taiko test automation" and click on the "Google Search" button. You can see the browser performing these actions as you type and press enter for each command.

Taiko’s REPL keeps a history of all successful commands. Once you finish a flow of execution, you can generate a test script using the special command .code

    > .code
    const { openBrowser, goto, write, click, closeBrowser } = require('taiko');

    (async () => {
        try {
            await openBrowser();
            await goto("google.com");
            await write("taiko test automation");
            await click("Google Search");
        } catch (error) {
                console.error(error);
        } finally {
                closeBrowser();
        }
    })();

Taiko generates readable and maintainable JavaScript code. Copy and modify this code or
save it directly to a file using

    > .code googlesearch.js

You can choose to continue automating or finish the recording using

    > .exit

To run a Taiko script pass the file as an argument to taiko

    $ taiko googlesearch.js
    ✔ Browser opened
    ✔ Navigated to url "http://google.com"
    ✔ Wrote taiko test automation into the focused element.
    ✔ Clicked element containing text "Google Search"
    ✔ Browser closed

By default Taiko runs the script in headless mode, that means it does not launch a browser window. This makes it easy to run Taiko in containers (ex. Docker). To view the browser when the script executes use

    $ taiko googlesearch.js --observe

Taiko’s REPL also documents all the API’s. To view all available API’s use the special command `.api`

    $ taiko
    Version: 1.4.0 (Chromium: 126.0.6468.0)
    Type .api for help and .exit to quit
    > .api
    Browser actions
        openBrowser, closeBrowser, client, switchTo, setViewPort, openTab, closeTab
    ...

To see more details of an API along with examples use

    >.api openBrowser

    Launches a browser with a tab. The browser will be closed when the parent node.js process is closed.

    Example:
        openBrowser()
        openBrowser({ headless: false })
        openBrowser({args:['--window-size=1440,900']})


## Smart Selectors

Taiko’s API treats the browser as a black box. With Taiko we can write scripts by looking at a web page and without inspecting it’s source code For example on `google.com` the command

    > click("Google Search")

clicks on any element with the text `Google Search` (a button on the page at https://google.com). Taiko’s API mimics user interactions with the browser. For example if you want to write into an element that’s currently in focus use

    > write("something")

Or if you want to write into a specific text field

    > write("some
