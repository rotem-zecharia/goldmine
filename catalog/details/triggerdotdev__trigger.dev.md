# triggerdotdev/trigger.dev

Trigger.dev – build and deploy fully‑managed AI agents and workflows

## features

- **[JavaScript and TypeScript SDK](https://trigger.dev/docs/tasks/overview)** - Build background tasks using familiar programming models
- **[Long-running tasks](https://trigger.dev/docs/runs/max-duration)** - Handle resource-heavy tasks without timeouts
- **[Durable cron schedules](https://trigger.dev/docs/tasks/scheduled#scheduled-tasks-cron)** - Create and attach recurring schedules of up to a year
- **[Trigger.dev Realtime](https://trigger.dev/docs/realtime/overview)** - Trigger, subscribe to, and get real-time updates for runs, with LLM streaming support
- **[Build extensions](https://trigger.dev/docs/config/extensions/overview#build-extensions)** - Hook directly into the build system and customize the build process. Run Python scripts, FFmpeg, browsers, and more.
- **[React hooks](https://trigger.dev/docs/frontend/react-hooks#react-hooks)** - Interact with the Trigger.dev API on your frontend using our React hooks package
- **[Batch triggering](https://trigger.dev/docs/triggering#tasks-batchtrigger)** - Use batchTrigger() to initiate multiple runs of a task with custom payloads and options
- **[Structured inputs / outputs](https://trigger.dev/docs/tasks/schemaTask#schematask)** - Define precise data schemas for your tasks with runtime payload validation
- **[Waits](https://trigger.dev/docs/wait)** - Add waits to your tasks to pause execution for a specified duration
- **[Preview branches](https://trigger.dev/docs/deployment/preview-branches)** - Create isolated environments for testing and development. Integrates with Vercel and git workflows
- **[Waitpoints](https://trigger.dev/docs/wait-for-token#wait-for-token)** - Add human-in-the-loop judgment at critical decision points without disrupting workflow
- **[Concurrency & queues](https://trigger.dev/docs/queue-concurrency#concurrency-and-queues)** - Set concurrency rules to manage how multiple tasks execute
- **[Multiple environments](https://trigger.dev/docs/how-it-works#dev-mode)** - Support for DEV, PREVIEW, STAGING, and PROD environments
- **[No infrastructure to manage](https://trigger.dev/docs/how-it-works#trigger-dev-architecture)** - Auto-scaling infrastructure that eliminates timeouts and server management
- **[Automatic retries](https://trigger.dev/docs/errors-retrying)** - If your task encounters an uncaught error, we automatically attempt to run it again
- **[Checkpointing](https://trigger.dev/docs/how-it-works#the-checkpoint-resume-system)** - Tasks are inherently durable, thanks to our checkpointing feature
- **[Versioning](https://trigger.dev/docs/versioning)** - Atomic versioning allows you to deploy new versions without affecting running tasks
- **[Machines](https://trigger.dev/docs/machines)** - Configure the number of vCPUs and GBs of RAM you want the task to use
- **[Observability & monitoring](https://trigger.dev/product/observability-and-monitoring)** - Monitor every aspect of your tasks' performance with comprehensive logging and visualization tools
- **[Logging & tracing](https://trigger.dev/docs/logging)** - Comprehensive logging and tracing for all your tasks
- **[Tags](https://trigger.dev/docs/tags#tags)** - Attach up to ten tags to each run, allowing you to filter via the dashboard, realtime, and the SDK
- **[Run metadata](https://trigger.dev/docs/runs/metadata#run-metadata)** - Attach metadata to runs which updates as the run progresses and is available to use in your frontend for live updates
- **[Bulk actions](https://trigger.dev/docs/bulk-actions)** - Perform actions on multiple runs simultaneously, including replaying and cancelling
- **[Real-time alerts](https://trigger.dev/docs/troubleshooting-alerts#alerts)** - Choose your preferred notification method for run failures and deployments

## configuration

We support `Development`, `Staging`, `Preview`, and `Production` environments, allowing you to test your tasks before deploying them to production.

## installation

The quickest way to get started is to create an account and project in our [web app](https://cloud.trigger.dev), and follow the instructions in the onboarding. Build and deploy your first task in minutes.
