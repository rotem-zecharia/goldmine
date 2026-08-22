# allinurl/goaccess

GoAccess is a real-time web log analyzer and interactive viewer that runs in a terminal in *nix systems or through your browser.

## features

GoAccess parses the specified web log file and outputs the data to the X
terminal. Features include:

* **Completely Real Time**<br>
  All panels and metrics are timed to be updated every 200 ms on the terminal
  output and every second on the HTML output.

* **Minimal Configuration needed**<br>
  You can just run it against your access log file, pick the log format and let
  GoAccess parse the access log and show you the stats.

* **Track Application Response Time**<br>
  Track the time taken to serve the request. Extremely useful if you want to
  track pages that are slowing down your site.

* **WebSocket Authentication:**<br>
  GoAccess offers enhanced WebSocket authentication, supporting local and
  external JWT verification, with secure token refresh capabilities and seamless
  integration with external authentication systems.

* **Nearly All Web Log Formats**<br>
  GoAccess allows any custom log format string.  Predefined options include,
  Apache, Nginx, Amazon S3, Elastic Load Balancing, CloudFront, etc.

* **Incremental Log Processing**<br>
  Need data persistence? GoAccess has the ability to process logs incrementally
  through the on-disk persistence options.

* **Only one dependency**<br>
  GoAccess is written in C. To run it, you only need ncurses as a dependency.
  That's it. It even features its own Web Socket server — http://gwsocket.io/.

* **Visitors**<br>
  Determine the amount of hits, visitors, bandwidth, and metrics for slowest
  running requests by the hour, or date.

* **Metrics per Virtual Host**<br>
  Have multiple Virtual Hosts (Server Blocks)? It features a panel that
  displays which virtual host is consuming most of the web server resources.

* **ASN (Autonomous System Number mapping)**<br>
  Great for detecting malicious traffic patterns and block them accordingly.

* **Color Scheme Customizable**<br>
  Tailor GoAccess to suit your own color taste/schemes. Either through the
  terminal, or by simply applying the stylesheet on the HTML output.

* **Support for Large Datasets**<br>
  GoAccess features the ability to parse large logs due to its optimized
  in-memory hash tables. It has very good memory usage and pretty good
  performance. This storage has support for on-disk persistence as well.

* **Docker Support**<br>
  Ability to build GoAccess' Docker image from upstream. You can still fully
  configure it, by using Volume mapping and editing `goaccess.conf`.  See
  [Docker](https://github.com/allinurl/goaccess#docker) section below.
  There is also documentation how to use [docker-compose](./docker-compose/README.md).

## installation

<a href="https://repology.org/project/goaccess/versions">
    <img src="https://repology.org/badge/vertical-allrepos/goaccess.svg" alt="Packaging status" align="right">
</a>

## configuration

See [**options**](https://goaccess.io/man#options) that can be supplied to the command or
specified in the configuration file. If specified in the configuration file, long
options need to be used without prepending `--`.

## tools

**Note**: Piping data into GoAccess won't prompt a log/date/time
configuration dialog, you will need to previously define it in your
configuration file or in the command line.
