# RipMeApp/ripme

Downloads albums from the web in bulk for archive purposes

## requirements

Requires Java 21 or later to run. RipMe has been tested on and is confirmed working on Windows, Linux, and Mac.

Java 21 is the most modern possible Java version that allows us to support the most platforms; it's the default JDK on current Debian stable. See [thread](https://github.com/RipMeApp/ripme/pull/2057#issuecomment-2571472016) and [issue #2055](https://github.com/RipMeApp/ripme/issues/2055).

## installation

On macOS, there is a [cask](https://github.com/Homebrew/homebrew-cask/blob/main/Casks/r/ripme.rb).

```
brew install --cask ripme && xattr -d com.apple.quarantine /Applications/ripme.jar
```

## features

- Quickly downloads all images in an online album. [See supported sites](https://github.com/ripmeapp/ripme/wiki/Supported-Sites)
- Easily re-rip albums to fetch new content
- Built in updater
- Skips already downloaded images by default
- Can auto skip e-hentai and nhentai albums containing certain tags. [See here for how to enable](https://github.com/RipMeApp/ripme/wiki/Config-options#nhentaiblacklisttags)
- Download a range of urls. [See here for how](https://github.com/RipMeApp/ripme/wiki/How-To-Run-RipMe#downloading-a-url-range)

## limitations

Request support for more sites by adding a comment to [this Github issue](https://github.com/RipMeApp/ripme/issues/2068).

If you're a developer, you can add your own Ripper by following the wiki guide:
[How To Create A Ripper for HTML Websites](https://github.com/ripmeapp/ripme/wiki/How-To-Create-A-Ripper-for-HTML-websites).
