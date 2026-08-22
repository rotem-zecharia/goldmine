# Kaliiiiiiiiii-Vinyzu/patchright-nodejs

Undetected NodeJS version of the Playwright testing and automation library.

## installation

```bash
# Install Patchright from NPM
npm i patchright
```

```bash
# Install Chromium-Driver for Patchright
npx patchright install chromium
```

---

## tools

#### Just change the import and use it like playwright. Patchright is a drop-in-replacement for Playwright!

> [!IMPORTANT]  
> Patchright only patches CHROMIUM based browsers. Firefox and Webkit are not supported.

```js
// patchright here!
const { chromium } = require('patchright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('http://example.com');
  // other actions...
  await browser.close();
})();
```

### Best Practice  - use Chrome without Fingerprint Injection

To be completely undetected, use the following configuration:
```js
chromium.launchPersistentContext("...", {
    channel: "chrome",
    headless: false,
    viewport: null,
    // do NOT add custom browser headers or userAgent
});
```

> [!NOTE]
> We recommend using Google Chrome instead of Chromium.
> You can install it via `npx patchright install chrome` (or via any other installation method) and use it with `channel: "chrome"`.


---

## Patches

### [Runtime.enable](https://vanilla.aslushnikov.com/?Runtime.enable) Leak
This is the biggest Patch Patchright uses. To avoid detection by this leak, patchright avoids using [Runtime.enable](https://vanilla.aslushnikov.com/?Runtime.enable) by executing Javascript in (isolated) ExecutionContexts.

### [Console.enable](https://vanilla.aslushnikov.com/?Console.enable) Leak
Patchright patches this leak by disabling the Console API all together. This means, console functionality will not work in Patchright. If you really need the console, you might be better off using Javascript loggers, although they also can be easily detected.

### Command Flags Leaks
Patchright tweaks the Playwright Default Args to avoid detection by Command Flag Leaks. This (most importantly) affects:
- `--disable-blink-features=AutomationControlled` (added) to avoid navigator.webdriver detection.
- `--enable-automation` (removed) to avoid navigator.webdriver detection.
- `--disable-popup-blocking` (removed) to avoid popup crashing.
- `--disable-component-update` (removed) to avoid detection as a Stealth Driver.
- `--disable-default-apps` (removed) to enable default apps.
- `--disable-extensions` (removed) to enable extensions

### General Leaks
Patchright patches some general leaks in the Playwright codebase. This mainly includes poor setups and obvious detection points.

### Closed Shadow Roots
Patchright is able to interact with elements in Closed Shadow Roots. Just use normal locators and Patchright will do the rest.
<br/>
Patchright is now also able to use XPaths in Closed Shadow Roots.

---

## Stealth

With the right setup, Patchright currently is considered undetectable.
Patchright passes:
- [Brotector](https://kaliiiiiiiiii.github.io/brotector/) ✅ (with [CDP-Patches](https://github.com/Kaliiiiiiiiii-Vinyzu/CDP-Patches/))
- [Cloudflare](https://cloudflare.com/) ✅
- [Kasada](https://www.kasada.io/) ✅
- [Akamai](https://www.akamai.com/products/bot-manager/) ✅
- [Shape/F5](https://www.f5.com/) ✅
- [Bet365](https://bet365.com/) ✅
- [Datadome](https://datadome.co/products/bot-protection/) ✅
- [Fingerprint.com](https://fingerprint.com/products/bot-detection/) ✅
- [CreepJS](https://abrahamjuliot.github.io/creepjs/) ✅
- [Sannysoft](https://bot.sannysoft.com/) ✅
- [Incolumitas](https://bot.incolumitas.com/) ✅
- [IPHey](https://iphey.com/) ✅
- [Browserscan](https://browserscan.net/) ✅
- [Pixelscan](https://pixelscan.net/) ✅

---

## Documentation and API Reference
See the original [Playwright Documentation](https://playwright.dev/docs/intro) and [API Reference](https://playwright.dev/docs/api/class-playwright)

## Extended Patchright API
#### **`evaluate`** Method <sub>([`Frame.evaluate`](https://playwright.dev/docs/api/class-frame#frame-evaluate), [`Page.evaluate`](https://playwright.dev/docs/api/class-page#page-evaluate),  [`Locator.evaluate`](https://playwright.dev/docs/api/class-locator#locator-evaluate),  [`Worker.evaluate`](https://playwright.dev/docs/api/class-worker#work
