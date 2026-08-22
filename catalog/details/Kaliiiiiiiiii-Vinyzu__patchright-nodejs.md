# Kaliiiiiiiiii-Vinyzu/patchright-nodejs

Undetected NodeJS version of the Playwright testing and automation library.

## installation

```bash

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
