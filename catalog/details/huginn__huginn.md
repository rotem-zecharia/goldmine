# huginn/huginn

Create agents that monitor and act on your behalf. Your agents are standing by!

## tools

Please checkout the [Huginn Introductory Screencast](http://vimeo.com/61976251)!

And now, some example screenshots.  Below them are instructions to get you started.

![Example list of agents](https://raw.githubusercontent.com/huginn/huginn/master/doc/imgs/your-agents.png)

![Event flow diagram](https://raw.githubusercontent.com/huginn/huginn/master/doc/imgs/diagram.png)

![Detecting peaks in Twitter](https://raw.githubusercontent.com/huginn/huginn/master/doc/imgs/peaks.png)

![Logging your location over time](https://raw.githubusercontent.com/huginn/huginn/master/doc/imgs/my-locations.png)

![Making a new agent](https://raw.githubusercontent.com/huginn/huginn/master/doc/imgs/new-agent.png)

## installation

### Docker

The quickest and easiest way to check out Huginn is to use the official Docker image. Have a look at the [documentation](https://github.com/huginn/huginn/blob/master/doc/docker/install.md).

### Local Installation

If you just want to play around, you can simply fork this repository, then perform the following steps:

* Run `git remote add upstream https://github.com/huginn/huginn.git` to add the main repository as a remote for your fork.
* Copy `.env.example` to `.env` (`cp .env.example .env`) and edit `.env`, at least updating the `APP_SECRET_TOKEN` variable.
* Make sure that you have MySQL or PostgreSQL installed. (On a Mac, the easiest way is with [Homebrew](http://brew.sh/). If you're going to use PostgreSQL, you'll need to prepend all commands below with `DATABASE_ADAPTER=postgresql`.)
* Run `bundle` to install dependencies
* Run `bundle exec rake db:create`, `bundle exec rake db:migrate`, and then `bundle exec rake db:seed` to create a development database with some example Agents.
* Run `bundle exec foreman start`, visit [http://localhost:3000/][localhost], and login with the username of `admin` and the password of `password`.
* Setup some Agents!
* Read the [wiki][wiki] for usage examples and to get started making new Agents.
* Periodically run `git fetch upstream` and then `git checkout master && git merge upstream/master` to merge in the newest version of Huginn.

Note: By default, email messages are intercepted in the `development` Rails environment, which is what you just setup.  You can view
them at [http://localhost:3000/letter_opener](http://localhost:3000/letter_opener). If you'd like to send real email via SMTP when playing
with Huginn locally, set `SEND_EMAIL_IN_DEVELOPMENT` to `true` in your `.env` file.

If you need more detailed instructions, see the [Novice setup guide][novice-setup-guide].

[localhost]: http://localhost:3000/
[wiki]: https://github.com/huginn/huginn/wiki
[novice-setup-guide]: https://github.com/huginn/huginn/wiki/Novice-setup-guide

### Develop

All agents have specs! And there's also acceptance tests that simulate running Huginn in a headless browser.

* Install Google Chrome and ChromeDriver for local feature specs
* Or use the Docker-based test environment in [`docker/test/README.md`](docker/test/README.md)
* Run all specs with `bundle exec rspec`
* Run a specific spec with `bundle exec rspec path/to/specific/test_spec.rb`.
* Read more about rspec for rails [here](https://github.com/rspec/rspec-rails).

## Using Huginn Agent gems

Huginn Agents can now be written as external gems and be added to your Huginn installation with the `ADDITIONAL_GEMS` environment variable. See the `Additional Agent gems` section of `.env.example` for more information.

If you'd like to write your own Huginn Agent Gem, please see [huginn_agent](https://github.com/huginn/huginn_agent).

Our general intention is to encourage complex and specific Agents to be written as Gems, while continuing to add new general-purpose Agents to the core Huginn repository.

## Deployment

Please see [the Huginn Wiki](https://github.com/huginn/huginn/wiki#deploying-huginn) for detailed deployment strategies for different providers.

### Heroku

Try Huginn on Heroku: [![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy) (Takes a few minutes to setup. Read the [documentation](https://github.com/huginn/huginn/blob/master/doc/heroku/install.md) while you are waiting and be sure to click 'View it' after launch!) Huginn launches only on a paid subscription plan for Heroku. For non-experimental use, we strongly recommend Heroku's 1GB paid plan or our Docker container.

### OpenShift

#### OpenShift Online

Try Huginn on OpenShift Online

Create a new app with either `mysql` or `postgres`:
```bash
oc new-app -f https://raw.githubusercontent.com/huginn/huginn/master/openshift/templates/huginn-mysql.json
```
or
```bash
oc new-app -f https://raw.githubusercontent.com/huginn/huginn/master/openshif
