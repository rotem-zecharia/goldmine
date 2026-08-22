# cheeriojs/cheerio

The fast, flexible, and elegant library for parsing and manipulating HTML and XML.

## installation

Install Cheerio using a package manager like npm, yarn, bun, or Deno.

```bash
npm install cheerio
# or
bun add cheerio
# or
deno install cheerio
```

## features

**&#10084; Proven syntax:** Cheerio implements a subset of core jQuery. Cheerio
removes all the DOM inconsistencies and browser cruft from the jQuery library,
revealing its truly gorgeous API.

**&#991; Blazingly fast:** Cheerio works with a very simple, consistent DOM
model. As a result parsing, manipulating, and rendering are incredibly
efficient.

**&#10049; Incredibly flexible:** Cheerio wraps around
[parse5](https://github.com/inikulin/parse5) for parsing HTML and can optionally
use the forgiving [htmlparser2](https://github.com/fb55/htmlparser2/). Cheerio
can parse nearly any HTML or XML document. Cheerio works in both browser and
server environments.

## tools

### Loading

First you need to load in the HTML. This step in jQuery is implicit, since
jQuery operates on the one, baked-in DOM. With Cheerio, we need to pass in the
HTML document.

```js
// ESM or TypeScript:
import * as cheerio from 'cheerio';

// In other environments:
const cheerio = require('cheerio');

const $ = cheerio.load('<ul id="fruits">...</ul>');

$.html();
//=> <html><head></head><body><ul id="fruits">...</ul></body></html>
```

### Selectors

Once you've loaded the HTML, you can use jQuery-style selectors to find elements
within the document.

#### \$( selector, [context], [root] )

`selector` searches within the `context` scope which searches within the `root`
scope. `selector` and `context` can be a string expression, DOM Element, array
of DOM elements, or cheerio object. `root`, if provided, is typically the HTML
document string.

This selector method is the starting point for traversing and manipulating the
document. Like in jQuery, it's the primary method for selecting elements in the
document.

```js
$('.apple', '#fruits').text();
//=> Apple

$('ul .pear').attr('class');
//=> pear

$('li[class=orange]').html();
//=> Orange
```

### Rendering

When you're ready to render the document, you can call the `html` method on the
"root" selection:

```js
$.root().html();
//=>  <html>
//      <head></head>
//      <body>
//        <ul id="fruits">
//          <li class="apple">Apple</li>
//          <li class="orange">Orange</li>
//          <li class="pear">Pear</li>
//        </ul>
//      </body>
//    </html>
```

If you want to render the
[`outerHTML`](https://developer.mozilla.org/en-US/docs/Web/API/Element/outerHTML)
of a selection, you can use the `outerHTML` prop:

```js
$('.pear').prop('outerHTML');
//=> <li class="pear">Pear</li>
```

You may also render the text content of a Cheerio object using the `text`
method:

```js
const $ = cheerio.load('This is <em>content</em>.');
$('body').text();
//=> This is content.
```

### The "DOM Node" object

Cheerio collections are made up of objects that bear some resemblance to
[browser-based DOM nodes](https://developer.mozilla.org/en-US/docs/Web/API/Node).
You can expect them to define the following properties:

- `tagName`
- `parentNode`
- `previousSibling`
- `nextSibling`
- `nodeValue`
- `firstChild`
- `childNodes`
- `lastChild`

## Screencasts

[https://vimeo.com/31950192](https://vimeo.com/31950192)

> This video tutorial is a follow-up to Nettut's "How to Scrape Web Pages with
> Node.js and jQuery", using cheerio instead of JSDOM + jQuery. This video shows
> how easy it is to use cheerio and how much faster cheerio is than JSDOM +
> jQuery.

## Cheerio in the real world

Are you using cheerio in production? Add it to the
[wiki](https://github.com/cheeriojs/cheerio/wiki/Cheerio-in-Production)!

## Sponsors

Does your company use Cheerio in production? Please consider
[sponsoring this project](https://github.com/cheeriojs/cheerio?sponsor=1)! Your
help will allow maintainers to dedicate more time and resources to its
development and support.

**Headlining Sponsors**

<!-- BEGIN SPONSORS: headliner -->

<a href="https://www.scrapingbee.com/" target="_blank" rel="noopener noreferrer">
            <img height="128px" width="128px" src="https://humble.imgix.net/https%3A%2F%2Fimages.opencollective.com%2Fscrapingbee%2F6d5dc95%2Flogo.png?ixlib=js-3.8.0&w=128&h=128&fit=fillmax&fill=solid&s=c21a60153bbb00aade922fe9254436e6" title="ScrapingBee" alt="ScrapingBee"></img>
          </a>
<a href="https://github.com/" target="_blank" rel="noopener noreferrer">
            <img height="128px" width="128px" src="https://humble.imgix.net/https%3A%2F%2Favatars.githubusercontent.com%2Fgithub?ixlib=js-3.8.0&w=128&h=128&fit=fillmax&fill=solid&s=65172918690f124c0adebece30c66471" title="Github" alt="Github"></img>
          </a>
<a href="https://www.airbnb.com/" target="_blank" rel="noopener noreferrer">
            <img height="128px" width="128px" src="https://humble.imgix.net/https%
