# Shopify/toxiproxy

:alarm_clock: :fire: A TCP proxy to simulate network and system conditions for chaos and resiliency testing

## features

The existing ones we found didn't provide the kind of dynamic API we needed for
integration and unit testing. Linux tools like `nc` and so on are not
cross-platform and require root, which makes them problematic in test,
development and CI environments.

## Clients

* [toxiproxy-ruby](https://github.com/Shopify/toxiproxy-ruby)
* [toxiproxy-go](https://github.com/Shopify/toxiproxy/tree/main/client)
* [toxiproxy-python](https://github.com/douglas/toxiproxy-python)
* [toxiproxy.net](https://github.com/mdevilliers/Toxiproxy.Net)
* [toxiproxy-php-client](https://github.com/ihsw/toxiproxy-php-client)
* [toxiproxy-node-client](https://github.com/ihsw/toxiproxy-node-client)
* [toxiproxy-java](https://github.com/trekawek/toxiproxy-java)
* [toxiproxy-haskell](https://github.com/jpittis/toxiproxy-haskell)
* [toxiproxy-rust](https://github.com/itarato/toxiproxy_rust)
* [toxiproxy-elixir](https://github.com/Jcambass/toxiproxy_ex)

## Example

Let's walk through an example with a Rails application. Note that Toxiproxy is
in no way tied to Ruby, it's just been our first use case. You can see the full example at
[sirupsen/toxiproxy-rails-example](https://github.com/sirupsen/toxiproxy-rails-example).
To get started right away, jump down to [Usage](#usage).

For our popular blog, for some reason we're storing the tags for our posts in
Redis and the posts themselves in MySQL. We might have a `Post` class that
includes some methods to manipulate tags in a [Redis set](http://redis.io/commands#set):

```ruby
class Post < ActiveRecord::Base
  # Return an Array of all the tags.
  def tags
    TagRedis.smembers(tag_key)
  end

  # Add a tag to the post.
  def add_tag(tag)
    TagRedis.sadd(tag_key, tag)
  end

  # Remove a tag from the post.
  def remove_tag(tag)
    TagRedis.srem(tag_key, tag)
  end

  # Return the key in Redis for the set of tags for the post.
  def tag_key
    "post:tags:#{self.id}"
  end
end
```

We've decided that erroring while writing to the tag data store
(adding/removing) is OK. However, if the tag data store is down, we should be
able to see the post with no tags. We could simply rescue the
`Redis::CannotConnectError` around the `SMEMBERS` Redis call in the `tags`
method. Let's use Toxiproxy to test that.

Since we've already installed Toxiproxy and it's running on our machine, we can
skip to step 2. This is where we need to make sure Toxiproxy has a mapping for
Redis tags. To `config/boot.rb` (before any connection is made) we add:

```ruby
require 'toxiproxy'

Toxiproxy.populate([
  {
    name: "toxiproxy_test_redis_tags",
    listen: "127.0.0.1:22222",
    upstream: "127.0.0.1:6379"
  }
])
```

Then in `config/environments/test.rb` we set the `TagRedis` to be a Redis client
that connects to Redis through Toxiproxy by adding this line:

```ruby
TagRedis = Redis.new(port: 22222)
```

All calls in the test environment now go through Toxiproxy. That means we can
add a unit test where we simulate a failure:

```ruby
test "should return empty array when tag redis is down when listing tags" do
  @post.add_tag "mammals"

  # Take down all Redises in Toxiproxy
  Toxiproxy[/redis/].down do
    assert_equal [], @post.tags
  end
end
```

The test fails with `Redis::CannotConnectError`. Perfect! Toxiproxy took down
the Redis successfully for the duration of the closure. Let's fix the `tags`
method to be resilient:

```ruby
def tags
  TagRedis.smembers(tag_key)
rescue Redis::CannotConnectError
  []
end
```

The tests pass! We now have a unit test that proves fetching the tags when Redis
is down returns an empty array, instead of throwing an exception. For full
coverage you should also write an integration test that wraps fetching the
entire blog post page when Redis is down.

Full example application is at
[sirupsen/toxiproxy-rails-example](https://github.com/sirupsen/toxiproxy-rails-example).

## tools

Configuring a project to use Toxiproxy consists of three steps:

1. Installing Toxiproxy
2. Populating Toxiproxy
3. Using Toxiproxy

## installation

**Linux**

See [`Releases`](https://github.com/Shopify/toxiproxy/releases) for the latest
binaries and system packages for your architecture.

**Ubuntu**

```bash
$ wget -O toxiproxy-2.1.4.deb https://github.com/Shopify/toxiproxy/releases/download/v2.1.4/toxiproxy_2.1.4_amd64.deb
$ sudo dpkg -i toxiproxy-2.1.4.deb
$ sudo service toxiproxy start
```

**OS X**

With [Homebrew](https://brew.sh/):

```bash
$ brew tap shopify/shopify
$ brew install toxiproxy
```

Or with [MacPorts](https://www.macports.org/):

```bash
$ port install toxiproxy
```

**Windows**

Toxiproxy for Windows is available for download at https://github.com/Shopify/toxiproxy/releases/download/v2.1.4/toxiproxy-server-windows-amd64.exe

**Docker**

Toxiproxy is available on [Github container registry](https://github.com/Shopify/toxiproxy/pkgs/container/toxiproxy).
Old versions `<= 2.1.4` are available on on [Docker Hub](https://hub.docker.com/r/shopify/toxiproxy/).

```bash
$ docker pull ghcr.io/shopify/toxiproxy
$ docker run --rm -it ghcr.io/shopify/toxiproxy
```

If using Toxiproxy from the host rather than other containers, enable host networking with `--net=host`.

```shell
$ docker run --rm --entrypoint="/toxiproxy-cli" -it ghcr.io/shopify/toxiproxy list
```

**Source**

If you have Go installed, you can build Toxiproxy from source using the make file:
```bash
$ make build
$ ./toxiproxy-server
```

#### Upgrading from Toxiproxy 1.x

In Toxiproxy 2.0 several changes were made to the API that make it incompatible with version 1.x.
In order to use version 2.x of the Toxiproxy server, you will need to make sure your client
library supports the same version. You can check which version of Toxiproxy you are running by
looking at the `/version` endpoint.

See the documentation for your client library for specific library changes. Detailed changes
for the Toxiproxy server can been found in [CHANGELOG.md](./CHANGELOG.md).

### 2. Populating Toxiproxy

When your application boots, it needs to make sure that Toxiproxy knows which
endpoints to proxy where. The main parameters are: name, address for Toxiproxy
to **listen** on and the address of the upstream.

Some client libraries have helpers for this task, which is essentially just
making sure each proxy in a list is created. Example from the Ruby client:

```ruby
# Make sure `shopify_test_redis_master` and `shopify_test_mysql_master` are
# present in Toxiproxy
Toxiproxy.populate([
  {
    name: "shopify_test_redis_master",
    listen: "127.0.0.1:22220",
    upstream: "127.0.0.1:6379"
  },
  {
    name: "shopify_test_mysql_master",
    listen: "127.0.0.1:24220",
    upstream: "127.0.0.1:3306"
  }
])
```

This code needs to run as early in boot as possible, before any code establishes
a connection through Toxiproxy. Please check your client library for
documentation on the population helpers.

Alternatively use the CLI to create proxies, e.g.:

```bash
toxiproxy-cli create -l localhost:26379 -u localhost:6379 shopify_test_redis_master
```

We recommend a naming such as the above: `<app>_<env>_<data store>_<shard>`.
This makes sure there are no clashes between applications using the same
Toxiproxy.

For large application we recommend storing the Toxiproxy configurations in a
separate configuration file. We use `config/toxiproxy.json`. This file can be
passed to the server using the `-config` option, or loaded by the application
to use with the `populate` function.

An example `config/toxiproxy.json`:

```json
[
  {
    "name": "web_dev_frontend_1",
    "listen": "[::]:18080",
    "upstream": "webapp.domain:8080",
    "enabled": true
  },
  {
    "name": "web_dev_mysql_1",
    "listen": "[::]:13306",
    "upstream": "database.domain:3306",
    "enabled": true
  }
]
```

Use ports outside the ephemeral port range to avoid random port conflicts.
It's `32,768` to `61,000` on Linux by default, see
`/proc/sys/net/ipv4/ip_local_port_range`.

### 3. Using Toxiproxy

To use Toxiproxy, you now need to configure your application t
