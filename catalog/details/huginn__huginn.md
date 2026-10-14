# huginn/huginn

Create agents that monitor and act on your behalf. Your agents are standing by!

## tools

Here are some example screenshots.  Below them are instructions to get you started.

![Example list of agents](https://raw.githubusercontent.com/huginn/huginn/master/doc/imgs/your-agents.png)

![Event flow diagram](https://raw.githubusercontent.com/huginn/huginn/master/doc/imgs/diagram.png)

![Detecting peaks in a stream of events](https://raw.githubusercontent.com/huginn/huginn/master/doc/imgs/peaks.png)

![Browsing the Events your Agents created](https://raw.githubusercontent.com/huginn/huginn/master/doc/imgs/events.png)

![Logging your location over time](https://raw.githubusercontent.com/huginn/huginn/master/doc/imgs/my-locations.png)

![Making a new agent](https://raw.githubusercontent.com/huginn/huginn/master/doc/imgs/new-agent.png)

## installation

### Try it with Docker

The quickest way to check out Huginn is the official Docker image, which runs everything in one container:

```bash
docker run -it -p 3000:3000 ghcr.io/huginn/huginn
```

Open [http://localhost:3000/](http://localhost:3000/) and log in as `admin` with the password printed once in the container log.  See the [Docker documentation](doc/docker/install.md) for persistent storage, an external database, and the multi-container image.

### Local development

If you want to hack on Huginn, fork this repository and then:

* Run `git remote add upstream https://github.com/huginn/huginn.git` to add the main repository as a remote for your fork.
* Copy `.env.example` to `.env` (`cp .env.example .env`) and edit `.env`, at least updating the `APP_SECRET_TOKEN` variable.
* Make sure that you have MySQL or PostgreSQL installed.  (On a Mac, the easiest way is with [Homebrew](http://brew.sh/).  If you're going to use PostgreSQL, you'll need to prepend all commands below with `DATABASE_ADAPTER=postgresql`.)
* Run `bundle` and `npm install` to install dependencies.  Node.js is needed for frontend libraries such as Font Awesome.
* Run `bundle exec rake db:create`, `bundle exec rake db:migrate`, and then `bundle exec rake db:seed` to create a development database with some example Agents.
* Run `bundle exec foreman start`, visit [http://localhost:3000/](http://localhost:3000/), and log in with the username `admin` and the password printed by `rake db:seed` (or set `SEED_PASSWORD` to choose one).
* Set up some Agents!
* Read the [wiki](https://github.com/huginn/huginn/wiki) for usage examples and to get started making new Agents.
* Periodically run `git fetch upstream` and then `git checkout master && git merge upstream/master` to merge in the newest version of Huginn.

By default, email messages are intercepted in the `development` Rails environment and shown at [http://localhost:3000/letter_opener](http://localhost:3000/letter_opener).  To send real email via SMTP while developing, set `SEND_EMAIL_IN_DEVELOPMENT` to `true` in your `.env` file.

If you need more detailed instructions, see the [Novice setup guide](https://github.com/huginn/huginn/wiki/Novice-setup-guide).

### Running the specs

All Agents have specs, and there are acceptance tests that run Huginn in a headless browser.

* Install Google Chrome and ChromeDriver for local feature specs, or use the Docker-based test environment in [`docker/test/README.md`](docker/test/README.md).
* Run all specs with `bundle exec rspec`, or a single file with `bundle exec rspec path/to/specific/test_spec.rb`.
* Regenerate the screenshots above with `bin/screenshots` after UI changes.

## Deployment

Huginn runs as a web process plus a background worker, backed by MySQL or PostgreSQL.  Pick whichever of the following fits how you run things.

### Docker Compose on your own server

This is the recommended way to run Huginn in production.  The official images are published to `ghcr.io/huginn/huginn` (all processes in one container) and `ghcr.io/huginn/huginn-single-process` (one process per container).  Example Compose files for MySQL and PostgreSQL are in [`docker/single-process/`](docker/single-process/); the [Docker documentation](doc/docker/install.md) explains configuration through environment variables.

The same Compose files work on self-hosted platforms that deploy from Compose, such as [Coolify](https://coolify.io/) and [Dokploy](https://dokploy.com/).

### Managed platforms

Any platform that runs a public Docker image with an always-on worker and a managed database can host Huginn.  Create a web service and a worker service from the single-process image (the worker runs `/scripts/init bin/threaded.rb`), attach a PostgreSQL or MySQL database, and set the environment variables described in the [Docker documentation](doc/docker/install.md).  Platforms known to fit this shape include [Render](https://render.com/docs/deploying-an-image), [Fly.io](https://docs.fly.io/launch/

## configuration

See [doc/manual/configuration.md](doc/manual/configuration.md) for outbound request restrictions on shared instances, the WeatherAgent API key, running without SSL, and private development setups.

## Using Huginn Agent gems

Huginn Agents can be written as external gems and added to your Huginn installation with the `ADDITIONAL_GEMS` environment variable.  See the `Additional Agent gems` section of `.env.example` for more information.

If you'd like to write your own Huginn Agent gem, please see [huginn_agent](https://github.com/huginn/huginn_agent).

Our general intention is to encourage complex and specific Agents to be written as gems, while continuing to add new general-purpose Agents to the core Huginn repository.

## Sponsors

Huginn is maintained by [Akinori Musha (@knu)](https://github.com/knu) in spare time.  You can support its development by [sponsoring the maintainer](https://github.com/sponsors/knu).  Company sponsors and sponsored hosting providers are listed in [doc/sponsors.md](doc/sponsors.md), along with the listing policy.

## License

Huginn is provided under the MIT License.

Huginn was originally created by [@cantino](https://github.com/cantino) in 2013.  Since then, many people's dedicated contributions have made it what it is today.
