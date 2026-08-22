# guanguans/music-dl

Music Searcher and Downloader. - 音乐搜索下载器。

## requirements

* PHP >= 8.5

## installation

```shell
composer global require guanguans/music-dl:dev-master --dev -v --ignore-platform-req=ext-pcntl # global
composer require guanguans/music-dl:dev-master --dev -v --ignore-platform-req=ext-pcntl # local
```

## tools

```shell
╰─ ./music-dl list                                                                                                        ─╯

  Music DL  refs/tags/6.2.5

  USAGE:  <command> [options] [arguments]

  completion  Dump the shell completion script
  inspire     Display an inspiring quote
  music       Search and download music
  self-update Self-update the installed application
  thanks      Thanks for using this tool.
```

```shell
╰─ ./music-dl music --help                                                                                                                                                   ─╯
Description:
  Search and download music

Usage:
  music [options] [--] [<keyword>]

Arguments:
  keyword                              Search keyword for music

Options:
  -b, --break                          Specify whether to break after download
  -d, --directory[=DIRECTORY]          Specify the download directory
  -D, --driver[=DRIVER]                Specify the search driver(sync、fork、process)
  -l, --locale[=LOCALE]                Specify the locale language [default: "zh_CN"]
  -N, --no-notify                      Specify whether to disable desktop notification
  -p, --page[=PAGE]                    Specify the page number [default: "1"]
  -P, --per-page[=PER-PAGE]            Specify the per page number [default: "30"]
  -s, --sources[=SOURCES]              Specify the music sources(tencent、netease、kugou) (multiple values allowed)
      --isolated[=ISOLATED]            Do not run the command if another instance of the command is already running [default: false]
      --xdebug                         Display xdebug output
      --configuration[=CONFIGURATION]  Used to dynamically pass one or more configuration key-value pairs(e.g. `--configuration=app.name=guanguans`). (multiple values allowed)
  -h, --help                           Display help for the given command. When no command is given display help for the music command
      --silent                         Do not output any message
  -q, --quiet                          Only errors are displayed. All other output is suppressed
  -V, --version                        Display this application version
      --ansi|--no-ansi                 Force (or disable --no-ansi) ANSI output
  -n, --no-interaction                 Do not ask any interactive question
      --env[=ENV]                      The environment the command should run under
  -v|vv|vvv, --verbose                 Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug
```

![usage](resources/images/music-dl.gif)
