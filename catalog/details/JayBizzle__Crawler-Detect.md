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
