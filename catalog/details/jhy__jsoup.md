# jhy/jsoup

jsoup: the Java HTML parser, built for HTML editing, cleaning, scraping, and XSS safety.

## installation

1. [**Download**](https://jsoup.org/download) the [latest](https://github.com/jhy/jsoup/releases/tag/jsoup-1.23.1) jsoup jar (or add it to your Maven/Gradle build)
2. Read the [cookbook introduction](https://jsoup.org/cookbook/introduction/parsing-a-document).
3. Enjoy!

Maven:

```xml
<dependency>
  <!-- jsoup HTML parser library @ https://jsoup.org/ -->
  <groupId>org.jsoup</groupId>
  <artifactId>jsoup</artifactId>
  <version>1.23.1</version>
</dependency>
```

Gradle:

```groovy
// jsoup HTML parser library @ https://jsoup.org/
implementation 'org.jsoup:jsoup:1.23.1'
```

### Android Support
When used in Android projects, [core library desugaring](https://developer.android.com/studio/write/java8-support#library-desugaring) with the [NIO specification](https://developer.android.com/studio/write/java11-nio-support-table) should be enabled to support Java 8+ features.

## Development and Support
If you have any questions on how to use jsoup or have ideas for future development, please get in touch via [jsoup Discussions](https://github.com/jhy/jsoup/discussions).

If you find any issues, please file a [bug](https://jsoup.org/bugs) after checking for duplicates.

The [colophon](https://jsoup.org/colophon) talks about the history of and tools used to build jsoup.

## Status
jsoup is in general, stable release.

## Author
jsoup was created and is maintained by [Jonathan Hedley](//jhedley.com), its primary author.

jsoup is an open-source project, and many contributors have helped improve it over the years. You can see their contributions and join the development on [GitHub](https://github.com/jhy/jsoup/graphs/contributors).

## Citing jsoup
If you use jsoup in research or technical documentation, you can cite it as:

> **Jonathan Hedley & jsoup contributors. jsoup: Java HTML Parser (2009–present).** Available at: https://jsoup.org

```plaintext
@misc{jsoup,
  author = {Jonathan Hedley and jsoup contributors},
  title = {jsoup: Java HTML Parser},
  year = {2026},
  url = {https://jsoup.org}
}
```
