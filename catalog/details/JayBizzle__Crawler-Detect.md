# JayBizzle/Crawler-Detect

🕷 CrawlerDetect is a PHP class for detecting bots/crawlers/spiders via the user agent

## installation

```bash
composer require jaybizzle/crawler-detect
```

## tools

```php
use Jaybizzle\CrawlerDetect\CrawlerDetect;

$CrawlerDetect = new CrawlerDetect;

// Check the user agent of the current visitor
if ($CrawlerDetect->isCrawler()) {
    // true if a crawler user agent was detected
}

// Pass a user agent as a string
if ($CrawlerDetect->isCrawler('Mozilla/5.0 (compatible; Sosospider/2.0; +http://help.soso.com/webspider.htm)')) {
    // true if a crawler user agent was detected
}

// Output the name of the bot that matched (if any)
echo $CrawlerDetect->getMatches();
```

### Passing headers from a request object

With no arguments, CrawlerDetect reads `$_SERVER`. If your headers come from somewhere else — a PSR-7 request, Symfony's `HeaderBag`, Swoole, or a Lambda event — pass them in directly. Both real header names (`User-Agent`) and PHP's SAPI names (`HTTP_USER_AGENT`) are understood, and values may be strings or arrays of strings.

```php
// PSR-7 (Slim, Mezzio, Laminas, League)
$CrawlerDetect = new CrawlerDetect($request->getHeaders());

// Symfony HttpFoundation
$CrawlerDetect = new CrawlerDetect($request->headers->all());

// Swoole
$CrawlerDetect = new CrawlerDetect($request->header);

if ($CrawlerDetect->isCrawler()) {
    // ...
}
```

Prefer this over `isCrawler($request->getHeaderLine('User-Agent'))`. Some crawlers — Googlebot in particular — send a genuine browser `User-Agent` and identify themselves in another header such as `From` or `Sec-CH-UA`. Passing the full set lets CrawlerDetect check all of them; passing a single string can only ever check one.

## Contributing

If you find a bot, spider or crawler that CrawlerDetect fails to detect, please open a pull request that:

- adds the regex pattern to the `$data` array in `src/Fixtures/Crawlers.php`
- adds the failing user agent string to `tests/data/user_agent/crawlers.txt`

The `raw/Crawlers.json` and `raw/Crawlers.txt` files are regenerated automatically by `export.php` after merge — no need to touch them.

If you're not able to submit a PR, open an issue with the user agent string and we'll take it from there.

## Ports & Integrations

CrawlerDetect has been ported to a number of other languages and frameworks. If you maintain a port not listed here, please open a PR.

| Platform | Project |
| --- | --- |
| Laravel | [Laravel-Crawler-Detect](https://github.com/JayBizzle/Laravel-Crawler-Detect) |
| Symfony 2 / 3 / 4 | [CrawlerDetectBundle](https://github.com/nicolasmure/CrawlerDetectBundle) |
| Yii2 | [yii2-crawler-detect](https://github.com/AlikDex/yii2-crawler-detect) |
| Node.js / ES6 | [es6-crawler-detect](https://github.com/JefferyHus/es6-crawler-detect) |
| Python | [crawlerdetect](https://github.com/moskrc/CrawlerDetect) |
| JVM (Java, Scala, Kotlin) | [CrawlerDetect](https://github.com/nekosoftllc/crawler-detect) |
| .NET / .NET Core | [NetCrawlerDetect](https://github.com/gplumb/NetCrawlerDetect) |
| Ruby | [crawler_detect](https://github.com/loadkpi/crawler_detect) |
| Go | [crawlerdetect](https://github.com/x-way/crawlerdetect) |

## Credits

Parts of this library are based on the excellent [MobileDetect](https://github.com/serbanghita/Mobile-Detect).

## License

Released under the [MIT License](LICENSE).
