# rendro/vintageJS

Add a retro/vintage effect to images using the HTML5 canvas element

## installation

```
$ npm install vintagejs
```

## How to use

`vintagejs` is a function that takes a source (URL, ImageElement or CanvasElement) and an effect (object with all the options) and returns a Promise that resolves to a result object.

```javascript
vintagejs('./path/to/picture.jpg', { brightness: 0.2 })
  .then(res => res.genImage())
  .then(img => document.body.appendChild(img));
```

The result object provides the following methods to access the modified image data:

```javascript
// returns the data url of the updated image. Use it to update the source of an existing image
getDataURL(mimeType?: string, quality?: number): string;
// returns the canvas with the updated image. Use it to draw your changes onto another canvas
getCanvas(): HTMLCanvasElement;
// returns a promise that resolves to an HTMLImageElement of the updated image
genImage(mimeType?: string, quality?: number): Promise<HTMLImageElement>;
```

If not provided, mimeType defaults to `image/jpeg` and quality defaults to `1`.

## tools

```javascript
// use an image as source and update image with data url
const srcEl = document.querySelector('img.myImage');
vintagejs(srcEl, { brightness: 0.2 })
  .then(res => {
    srcEl.src = res.getDataURL();
  });

// use a canvas as source and draw result to canvas
const srcEl = document.querySelector('canvas.myCanvas');
const ctx = srcEl.getContext('2d');
vintagejs(srcEl, { brightness: 0.2 })
  .then(res => {
    ctx.drawImage(res.getCanvas(), 0, 0, srcEl.width, srcEl.height);
  });
```

## configuration

```javascript
type TEffect = {
  curves: false | TCurve,     // default: false
  screen: false | TRGBAColor, // default: false
  saturation: number,         // float between 0 and 1, default: 1
  vignette: number,           // float between 0 and 1, default: 0
  lighten: number,            // float between 0 and 1, default: 0
  viewfinder: false | string, // string must be URL, default: false
  sepia: boolean,             // default: false
  gray: boolean,              // default: false
  brightness: number,         // float between -1 and 1, default: 0
  contrast: number,           // float between -1 and 1, default: 0
};

// every channel, r=red, g=green, b=blue serves as a look up table for color mappings
type TCurve = {
  r: Array<Uint8> | Uint8ClampedArray, // array of int between 0 and 255, length of array === 256
  g: Array<Uint8> | Uint8ClampedArray, // array of int between 0 and 255, length of array === 256
  b: Array<Uint8> | Uint8ClampedArray, // array of int between 0 and 255, length of array === 256
};

type TRGBAColor = {
  r: Uint8,  // int between 0 and 255
  g: Uint8,  // int between 0 and 255
  b: Uint8,  // int between 0 and 255
  a: number, // float between 0 and 1
};
```
