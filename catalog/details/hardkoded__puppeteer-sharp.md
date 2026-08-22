# hardkoded/puppeteer-sharp

Headless Chrome .NET API

## requirements

* Puppeteer-Sharp comes in two flavors: a NetStandard 2.0 library for .NET Framework 4.6.1 and .NET Core 2.0 or greater and a .NET 8 version.
* If you have issues running Chrome on Linux, the Puppeteer repo has a [great troubleshooting guide](https://github.com/puppeteer/puppeteer/blob/master/docs/troubleshooting.md).
* X-server is required on Linux.

## How to Contribute and Provide Feedback

Some of the best ways to contribute are to try things out file bugs and fix issues.

If you have an issue or a question:

* Ask a question on [Stack Overflow](https://stackoverflow.com/search?q=puppeteer-sharp).
* File a [new issue](https://github.com/hardkoded/puppeteer-sharp/issues/new).

## Contributing Guide

See [this document](https://github.com/hardkoded/puppeteer-sharp/blob/master/CONTRIBUTING.md) for information on how to contribute.

## tools

## Take screenshots

<!-- snippet: screenshotasync_example -->
<a id='snippet-screenshotasync_example'></a>
```cs
var browserFetcher = new BrowserFetcher();
await browserFetcher.DownloadAsync();
await using var browser = await Puppeteer.LaunchAsync(
    new LaunchOptions { Headless = true });
await using var page = await browser.NewPageAsync();
await page.GoToAsync("http://www.google.com");
await page.ScreenshotAsync(outputFile);
```
<sup><a href='https://github.com/hardkoded/puppeteer-sharp/blob/master/lib/PuppeteerSharp.Tests/ScreenshotTests/PageScreenshotTests.cs#L54-L62' title='Snippet source file'>snippet source</a> | <a href='#snippet-screenshotasync_example' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

You can also change the view port before generating the screenshot

<!-- snippet: setviewportasync_example -->
<a id='snippet-setviewportasync_example'></a>
```cs
await Page.SetViewportAsync(new ViewPortOptions
{
    Width = 500,
    Height = 500
});
```
<sup><a href='https://github.com/hardkoded/puppeteer-sharp/blob/master/lib/PuppeteerSharp.Tests/ScreenshotTests/ElementHandleScreenshotTests.cs#L12-L18' title='Snippet source file'>snippet source</a> | <a href='#snippet-setviewportasync_example' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

### Generate PDF files

<!-- snippet: pdfasync_example -->
<a id='snippet-pdfasync_example'></a>
```cs
var browserFetcher = new BrowserFetcher();
await browserFetcher.DownloadAsync();
await using var browser = await Puppeteer.LaunchAsync(new LaunchOptions { Headless = true });
await using var page = await browser.NewPageAsync();
await page.GoToAsync("http://www.google.com"); // In case of fonts being loaded from a CDN, use WaitUntilNavigation.Networkidle0 as a second param.
await page.EvaluateExpressionHandleAsync("document.fonts.ready"); // Wait for fonts to be loaded. Omitting this might result in no text rendered in pdf.
await page.PdfAsync(outputFile);
```
<sup><a href='https://github.com/hardkoded/puppeteer-sharp/blob/master/lib/PuppeteerSharp.Tests/PageTests/PdfTests.cs#L24-L34' title='Snippet source file'>snippet source</a> | <a href='#snippet-pdfasync_example' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

### Inject HTML

<!-- snippet: setcontentasync_example -->
<a id='snippet-setcontentasync_example'></a>
```cs
await using var page = await browser.NewPageAsync();
await page.SetContentAsync("<div>My Receipt</div>");
var result = await page.GetContentAsync();
```
<sup><a href='https://github.com/hardkoded/puppeteer-sharp/blob/master/lib/PuppeteerSharp.Tests/PageTests/SetContentTests.cs#L14-L20' title='Snippet source file'>snippet source</a> | <a href='#snippet-setcontentasync_example' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

### Evaluate Javascript

<!-- snippet: evaluate_example -->
<a id='snippet-evaluate_example'></a>
```cs
await using var page = await browser.NewPageAsync();
var seven = await page.EvaluateExpressionAsync<int>("4 + 3");
var someObject = await page.EvaluateFunctionAsync<JsonElement>("(value) => ({a: value})", 5);
Console.WriteLine(someObject.GetProperty("a").GetString());
```
<sup><a href='https://github.com/hardkoded/puppeteer-sharp/blob/master/lib/PuppeteerSharp.Tests/QuerySelectorTests/ElementHandleQuerySelectorEvalTests.cs#L17-L22' title='Snippet source file'>snippet source</a> | <a href='#snippet-evaluate_example' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

### Wait For Selector

```cs
using (var page = await browser.NewPageAsync())
{
    await page.GoToAsync("http://www.spapage.com");
    await page.WaitForSelectorAsync("div.main-content")
    await page.PdfAsync(outputFile));
}
```

### Wait For Function

```cs
using (var page = await browser.NewPageAsync())
{
    await page.GoToAsync("http://www.spapage.com");
    var watchDog = page.WaitForFunctionAsync("()=> window.innerWidth < 100");
    await page.SetViewportAsync(new ViewPortOptions { Width = 50, Height =
