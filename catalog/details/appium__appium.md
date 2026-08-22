# appium/appium

Cross-platform automation framework for all kinds of apps, built on top of the W3C WebDriver protocol

## installation

Appium can be installed using `npm` (other package managers are not currently supported). Please
check the [installation docs](http://appium.io/docs/en/latest/quickstart/install/) for the
system requirements and further information.

If upgrading from Appium 1, make sure Appium 1 is fully uninstalled (`npm uninstall -g appium`).
Unexpected errors might appear if this has not been done.

```bash
npm i -g appium
```

Note that this will only install the core Appium server, which cannot automate anything on its own.
Please install [drivers](#drivers) for your target platforms in order to automate them.

## features

1. You usually don't have to recompile your app or modify it in any way, due to the use of standard
   automation APIs on all platforms.
2. You can write tests with your favorite dev tools using any WebDriver-compatible language such as
   Java, Python, Ruby and C#. There are also third party client implementations for other languages.
3. You can use any testing framework.
4. Some drivers like `xcuitest` and `uiautomator2` have built-in mobile web and hybrid app support.
   Within the same script, you can switch seamlessly between native app automation and webview
   automation, all using the WebDriver model that's already the standard for web automation.
5. You can run your automated tests locally and in a cloud. There are multiple cloud providers that
   support various Appium drivers (mostly targeting iOS and Android mobile automation).
6. [Appium Inspector](https://github.com/appium/appium-inspector) can be used to visually inspect
   the page source of applications across different platforms, facilitating easier test development.

Investing in the [WebDriver](https://w3c.github.io/webdriver/webdriver-spec.html) protocol means you
are betting on a single, free, and open protocol for testing that has become a web standard. Don't
lock yourself into a proprietary stack.

For example, if you use Apple's XCUITest library without Appium, you can only write tests using
Obj-C/Swift, and you can only run tests through Xcode. Similarly, with Google's UiAutomator or
Espresso, you can only write tests in Java/Kotlin. Appium opens up the possibility of true
cross-platform native app automation, for mobile and beyond!

If you are looking for a more comprehensive description of what this is all about, please read our
documentation on [How Does Appium Work?](https://appium.io/docs/en/latest/intro/appium/).
