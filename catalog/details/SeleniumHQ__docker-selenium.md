# SeleniumHQ/docker-selenium

Provides a simple way to run Selenium Grid with Chrome, Firefox, and Edge using Container Platform, making it easier to perform browser automation at scale

## installation

1. Start a Docker container with Firefox

```bash
docker run -d -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-firefox:4.47.0-20260808
```

2. Point your WebDriver tests to http://localhost:4444

3. That's it! 

4. (Optional) To see what is happening inside the container, head to <http://localhost:7900/?autoconnect=1&resize=scale&password=secret>.

For more details about visualising the container activity, check the [Debugging](#debugging) section.

:point_up: When executing `docker run` for an image that contains a browser please use 
the flag `--shm-size=2g` to use the host's shared memory.
  
:point_up: Always use a Docker image with a full tag to pin a specific browser and Grid version.
See [Tagging Conventions](https://github.com/SeleniumHQ/docker-selenium/wiki/Tagging-Convention) for details.

## configuration

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/SeleniumHQ/docker-selenium)

___

## Experimental Multi-Arch amd64/aarch64/armhf Images

From image tag based `4.21.0` onwards, the architectures supported by this project are as below:

|       Architecture        | Available |
|:-------------------------:|:---------:|
|    x86_64 (aka amd64)     |     ✅     |
| aarch64 (aka arm64/armv8) |     ✅     |
| armhf (aka arm32/armv7l)  |     ❌     |

### Browser images in multi-arch

The following browsers are available in multi-arch images:

|       Architecture        | Chrome | Chromium | Firefox | Edge | CfT |
|:-------------------------:|:------:|:--------:|:-------:|:----:|-----|
|    x86_64 (aka amd64)     |   ✅    |    ✅     |    ✅    |  ✅   | ✅   |
| aarch64 (aka arm64/armv8) |   ✅    |    ✅     |    ✅    |  ❌   | ❌   |
| armhf (aka arm32/armv7l)  |   ❌    |    ❌     |    ❌    |  ❌   | ❌   |

Note:

- **Running an AMD64 image under emulation on an ARM64 platform is not recommended due to performance and [stability issues](https://github.com/SeleniumHQ/docker-selenium/issues/2298), or browsers could not launch.**

- Google Chrome (`google-chrome`) now is available for Linux/ARM64 via APT stable channel from v150+. The Chrome (node and standalone) images are available in multi-arch. Older Chrome versions remain AMD64 only; the supported platforms per version are tracked in the [browser matrix](tests/build-backward-compatible/browser-matrix.yml) via the `CHROME_PLATFORMS` key.
Microsoft does not build Edge (`microsoft-edge`) for Linux/ARM platforms, hence the Edge (node and standalone) images are only available for AMD64.

- Google does not publish a ChromeDriver build for Linux/ARM64 (Chrome for Testing only ships `linux64`). On ARM64 the Chrome images use the Chromium driver of the same major version instead, taken from the Debian `chromium-driver` package archived at [NDViet/chromium-stable](https://github.com/NDViet/chromium-stable). Those packages follow the stable channel, hence the Chrome `dev` and `beta` images are only available for AMD64.

- We also supply Chrome for Testing (CfT), but it is only available for Linux/AMD64.

- For older Linux/ARM setups you can also use the open source Chromium browser. The Chromium (node and standalone) images are available in multi-arch.

```bash
$ docker run --rm -it -p 4444:4444 -p 5900:5900 -p 7900:7900 --shm-size 2g selenium/standalone-chromium:latest
```

- Mozilla Firefox now is available for Linux/ARM64 via APT stable channel from v136+. The Firefox (node and standalone) images are available in multi-arch.

~~Multi-arch images are tested on CircleCI with resource class Linux/ARM64. See the status below.~~ (Moved to GitHub Actions)

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/SeleniumHQ/docker-selenium/tree/trunk.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/SeleniumHQ/docker-selenium/tree/trunk)

### History of the multi-arch images

For experimental docker container images, which run on platforms such as the Apple M-series or Raspberry Pi,
the repository at
[seleniumhq-community/docker-seleniarm](https://github.com/seleniumhq-community/docker-seleniarm) provided images which
are published on the [Seleniarm Docker Hub](https://hub.docker.com/u/seleniarm) registry.

See issue [#1076](https://github.com/SeleniumHQ/docker-selenium/issues/1076) for more information on these images.

Now, the fork [seleniumhq-community/docker-seleniarm](https://github.com/seleniumhq-community/docker-seleniarm) was merged.

### Build the multi-arch images locally

We recommend to enable the experimental feature [containerd image store](https://docs.docker.com/storage/containerd/) in Docker Engine.
`containerd` understands multiplatform images, where a single image tag can refer to different variants covering a range of OS and hardware architectures.
It simplifies the process of building, storing, and distributing im

## features

| Environment variable          | Default value                                | Description                                                                               |
|-------------------------------|----------------------------------------------|-------------------------------------------------------------------------------------------|
| `SE_UPLOAD_RETAIN_LOCAL_FILE` | `false`                                      | Keep local file after uploading successfully                                              |
| `SE_UPLOAD_COMMAND`           | `copy`                                       | RCLONE command is used to transfer file. Enforce `move` when retain local file is `false` |
| `SE_UPLOAD_OPTS`              | `-P --cutoff-mode SOFT --metadata --inplace` | Other options belong to RCLONE command can be set.                                        |
| `SE_UPLOAD_CONFIG_FILE_NAME`  | `upload.conf`                                | Config file for remote host instead of set via env variable prefix SE_RCLONE_*            |
| `SE_UPLOAD_CONFIG_DIRECTORY`  | `/opt/bin`                                   | Directory of config file (change it when conf file in another directory is mounted)       |

## Retain recordings for failed sessions only

In event-driven mode (`SE_VIDEO_EVENT_DRIVEN=true`, the default), the video service subscribes to the Grid's ZeroMQ event bus and reacts to session lifecycle events in real time. This enables a **retain-on-failure** strategy: record every session, but automatically discard the video when the session passes and only keep (and upload) recordings from sessions that fail.

Enable it globally with the environment variable:

```yaml
SE_RETAIN_ON_FAILURE=true
```

A session is treated as **failed** when either of the following is true:

1. The test code fires a session event whose `eventType` contains a substring from `SE_FAILURE_SESSION_EVENTS` (default: `:failed,:failure,:error,:aborted`).
2. The session closes with an abnormal reason — `TIMEOUT`, `NODE_REMOVED`, or `NODE_RESTARTED` — instead of the normal `QUIT_COMMAND`.

| Environment variable      | Default                          | Description                                                                                                                         |
|---------------------------|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| `SE_RETAIN_ON_FAILURE`    | `false`                          | Discard recordings of sessions that pass. Only recordings from failed sessions are retained on disk and queued for upload.          |
| `SE_FAILURE_SESSION_EVENTS` | `:failed,:failure,:error,:aborted` | Comma-separated substrings. Any session event whose `eventType` contains one of these (case-insensitive) marks the session as failed. |

The `se:retainOnFailure` session **capability** overrides the global container env var for a specific session. For example, to retain the recording of a single session regardless of the global setting:

```python
options.set_capability('se:retainOnFailure', True)
```

| `se:retainOnFailure` cap | `SE_RETAIN_ON_FAILURE` env | Effective behaviour              |
|--------------------------|----------------------------|----------------------------------|
| `true`                   | `false` (default)          | Retain on failure for this session |
| `false`                  | `true`                     | Always retain for this session   |
| absent                   | `true`                     | Retain on failure (global default) |
| absent                   | `false` (default)          | Always retain (global default)   |

#### Firing session events from test code

The [Session Event API](https://www.selenium.dev/blog/2026/selenium-grid-4-41-deep-dive/) lets test code push named events directly to the Grid. The video service listens for these events on the ZeroMQ bus and uses them to determine 

## tools

Relaying commands to a service endpoint that supports WebDriver.
It is useful to connect an external service that supports WebDriver to Selenium Grid. An example of such service could be a cloud provider or an Appium server. 
In this way, Grid can enable more coverage to platforms and versions not present locally.

The following is an en example of configuration relay commands.

[docker-compose-v3-test-node-relay.yml](tests/docker-compose-v3-test-node-relay.yml)

If you want to relay commands only, `selenium/node-base` is suitable and lightweight for this purpose.
In case you want to configure node with both browsers and relay commands, respective node images can be used.

To use environment variables for generate relay configs, set `SE_NODE_RELAY_URL` and other variables as below. Those will be used to generate the default relay config in TOML format looks like below.

```toml
[relay]
url = "${SE_NODE_RELAY_URL}"
status-endpoint = "${SE_NODE_RELAY_STATUS_ENDPOINT}"
protocol-version = "${SE_NODE_RELAY_PROTOCOL_VERSION}"
configs = [ '${SE_NODE_RELAY_MAX_SESSIONS}', '{"browserName": "${SE_NODE_RELAY_BROWSER_NAME}", "platformName": "${SE_NODE_RELAY_PLATFORM_NAME}", "appium:platformVersion": "${SE_NODE_RELAY_PLATFORM_VERSION}"}' ]
```

Instead of input value for each environment variable to construct the default relay stereotype, you can use the `SE_NODE_RELAY_STEREOTYPE` environment variable to overwrite the default relay stereotype with your custom stereotype.

In another case, if you want to retain the default relay stereotype and append additional capabilities, you can use the `SE_NODE_RELAY_STEREOTYPE_EXTRA` environment variable to set your capabilities. Those will be merged to the default relay stereotype.

To run a sample test with the relayed node, you can clone the project and try below command:

```bash
make test_node_relay
```

### Setting Sub Path

By default, Selenium is reachable at `http://127.0.0.1:4444/`. Selenium can be configured to use a custom subpath by specifying the `SE_SUB_PATH`
environmental variable. In the example below Selenium is reachable at `http://127.0.0.1:4444/selenium-grid/`

```bash
$ docker run -d -p 4444:4444 -e SE_SUB_PATH=/selenium-grid/ --name selenium-hub selenium/hub:4.47.0-20260808
```

### Setting Screen Resolution

By default, nodes start with a screen resolution of 1920 x 1080 with a color depth of 24 bits and a dpi of 96. 
These settings can be adjusted by specifying `SE_SCREEN_WIDTH`, `SE_SCREEN_HEIGHT`, `SE_SCREEN_DEPTH`, and/or `SE_SCREEN_DPI` 
environmental variables when starting the container.

``` bash
docker run -d -e SE_SCREEN_WIDTH=1366 -e SE_SCREEN_HEIGHT=768 -e SE_SCREEN_DEPTH=24 -e SE_SCREEN_DPI=74 selenium/standalone-firefox:4.47.0-20260808
```

### Grid Url and Session Timeout

In some use cases, you might need to set the Grid URL to the Node, for example, if you'd like to access the BiDi/CDP endpoint. 
This is also needed when you want to use the new `RemoteWebDriver.builder()` or `Augmenter()` present in Selenium 4 
(since they setup the BiDi/CDP connection implicitly). You can do that through the `SE_NODE_GRID_URL` environment 
variable, eg `-e SE_NODE_GRID_URL=http://<hostMachine>:4444`. Setting this env var is needed if you want to see the live view while sessions are executing.

Grid has a default session timeout of 300 seconds, where the session can be in a stale state until it is killed. You can use
`SE_NODE_SESSION_TIMEOUT` to overwrite that value in seconds.


### Session request timeout

A new session request is placed in the Session Queue before it is processed, and the request sits in the queue until a matching
slot is found across the registered Nodes. However, the new session request might timeout if no slot was found. By default, a 
request will stay in the queue for up to 300 seconds before it a timeout is reached. In addition, an attempt to process the request
is done every 5 seconds (by default).

It is possible to override those values through envi
