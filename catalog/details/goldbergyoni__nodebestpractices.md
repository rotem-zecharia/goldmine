# goldbergyoni/nodebestpractices

✅ The Node.js best practices list (July 2026)

## configuration

### `📝 #updated`

**TL;DR:** A flawless configuration setup should ensure (a) keys can be read from file AND from environment variable (b) secrets are kept outside committed code (c) config is hierarchical for easier findability (d) typing support (e) validation for failing fast (f) Specify default for each key. There are a few packages that can help tick most of those boxes like [convict](https://www.npmjs.com/package/convict), [env-var](https://github.com/evanshortiss/env-var), [zod](https://github.com/colinhacks/zod), and others

**Otherwise:** Consider a mandatory environment variable that wasn't provided. The app starts successfully and serve requests, some information is already persisted to DB. Then, it's realized that without this mandatory key the request can't complete, leaving the app in a dirty state

🔗 [**Read More: configuration best practices**](./sections/projectstructre/configguide.md)

<br/><br/>

## ![✔] 1.5 Consider all the consequences when choosing the main framework

### `🌟 #new`

**TL;DR:** When building apps and APIs, using a framework is mandatory. It's easy to overlook alternative frameworks or important considerations and then finally land on a sub optimal option. As of 2023/2024, we believe that these four frameworks are worth considering: [Nest.js](https://nestjs.com/), [Fastify](https://www.fastify.io/), [express](https://expressjs.com/), and [Koa](https://koajs.com/). Click read more below for a detailed pros/cons of each framework. Simplistically, we believe that Nest.js is the best match for teams who wish to go OOP and/or build large-scale apps that can't get partitioned into smaller _autonomous_ components. Fastify is our recommendation for apps with reasonably-sized components (e.g., Microservices) that are built around simple Node.js mechanics. Read our [full considerations guide here](./sections/projectstructre/choose-framework.md)

**Otherwise:** Due to the overwhelming amount of considerations, it's easy to make decisions based on partial information and compare apples with oranges. For example, it's believed that Fastify is a minimal web-server that should get compared with express only. In reality, it's a rich framework with many official plugins that cover many concerns

🔗 [**Read More: Choosing the right framework**](./sections/projectstructre/choose-framework.md)

## ![✔] 1.6 Use TypeScript sparingly and thoughtfully

### `🌟 #new`

**TL;DR:** Coding without type safety is no longer an option, TypeScript is the most popular option for this mission. Use it to define variables and functions return types. With that, it is also a double edge sword that can greatly _encourage_ complexity with its additional ~ 50 keywords and sophisticated features. Consider using it sparingly, mostly with simple types, and utilize advanced features only when a real need arises

**Otherwise:** [Researches](https://earlbarr.com/publications/typestudy.pdf) show that using TypeScript can help in detecting ~20% bugs earlier. Without it, also the developer experience in the IDE is intolerable. On the flip side, 80% of other bugs were not discovered using types. Consequently, typed syntax is valuable but limited. Only efficient tests can discover the whole spectrum of bugs, including type-related bugs. It might also defeat its purpose: sophisticated code features are likely to increase the code complexity, which by itself increases both the amount of bugs and the average bug fix time

🔗 [**Read More: TypeScript considerations**](./sections/projectstructre/typescript-considerations.md)

<br/><br/><br/>

<p align="right"><a href="#table-of-contents">⬆ Return to top</a></p>

# `2. Error Handling Practices`

## ![✔] 2.1 Use Async-Await or promises for async error handling

**TL;DR:** Handling async errors in callback style is probably the fastest way to hell (a.k.a the pyramid of doom). The best gift you can give to your code is using Promises with async-await which enables a much more compact and familiar code syn

## tools

**TL;DR:** Let your API callers know which errors might come in return so they can handle these thoughtfully without crashing. For RESTful APIs, this is usually done with documentation frameworks like OpenAPI. If you're using GraphQL, you can utilize your schema and comments as well

**Otherwise:** An API client might decide to crash and restart only because it received back an error it couldn’t understand. Note: the caller of your API might be you (very typical in a microservice environment)

🔗 [**Read More: documenting API errors in Swagger or GraphQL**](./sections/errorhandling/documentingusingswagger.md)

<br/><br/>

## ![✔] 2.6 Exit the process gracefully when a stranger comes to town

**TL;DR:** When an unknown error occurs (catastrophic error, see best practice 2.3) - there is uncertainty about the application healthiness. In this case, there is no escape from making the error observable, shutting off connections and exiting the process. Any reputable runtime framework like Dockerized services or cloud serverless solutions will take care to restart

**Otherwise:** When an unfamiliar exception occurs, some object might be in a faulty state (e.g. an event emitter which is used globally and not firing events anymore due to some internal failure) and all future requests might fail or behave crazily

🔗 [**Read More: shutting the process**](./sections/errorhandling/shuttingtheprocess.md)

<br/><br/>

## ![✔] 2.7 Use a mature logger to increase errors visibility

### `📝 #updated`

**TL;DR:** A robust logging tools like [Pino](https://github.com/pinojs/pino) or [Winston](https://github.com/winstonjs/winston) increases the errors visibility using features like log-levels, pretty print coloring and more. Console.log lacks these imperative features and should be avoided. The best in class logger allows attaching custom useful properties to log entries with minimized serialization performance penalty. Developers should write logs to `stdout` and let the infrastructure pipe the stream to the appropriate log aggregator

**Otherwise:** Skimming through console.logs or manually through messy text file without querying tools or a decent log viewer might keep you busy at work until late

🔗 [**Read More: using a mature logger**](./sections/errorhandling/usematurelogger.md)

<br/><br/>

## ![✔] 2.8 Test error flows using your favorite test framework

### `📝 #updated`

**TL;DR:** Whether professional automated QA or plain manual developer testing – Ensure that your code not only satisfies positive scenarios but also handles and returns the right errors. On top of this, simulate deeper error flows like uncaught exceptions and ensure that the error handler treat these properly (see code examples within the "read more" section)

**Otherwise:** Without testing, whether automatically or manually, you can’t rely on your code to return the right errors. Without meaningful errors – there’s no error handling

🔗 [**Read More: testing error flows**](./sections/errorhandling/testingerrorflows.md)

<br/><br/>

## ![✔] 2.9 Discover errors and downtime using APM products

**TL;DR:** Monitoring and performance products (a.k.a APM) proactively gauge your codebase or API so they can automagically highlight errors, crashes, and slow parts that you were missing

**Otherwise:** You might spend great effort on measuring API performance and downtimes, probably you’ll never be aware which are your slowest code parts under real-world scenario and how these affect the UX

🔗 [**Read More: using APM products**](./sections/errorhandling/apmproducts.md)

<br/><br/>

## ![✔] 2.10 Catch unhandled promise rejections

### `📝 #updated`

**TL;DR:** Any exception thrown within a promise will get swallowed and discarded unless a developer didn’t forget to explicitly handle it. Even if your code is subscribed to `process.uncaughtException`! Overcome this by registering to the event `process.unhandledRejection`

**Otherwise:** Your errors will get swallowed and leave no trace. No

## requirements

**TL;DR:** Your code must be identical across all environments, but without a special lockfile npm lets dependencies drift across environments. Ensure to commit your package-lock.json so all the environments will be identical

**Otherwise:** QA will thoroughly test the code and approve a version that will behave differently in production. Even worse, different servers in the same production cluster might run different code

🔗 [**Read More: Lock dependencies**](./sections/production/lockdependencies.md)

<br/><br/>

## ![✔] 5.5. Guard process uptime using the right tool

**TL;DR:** The process must go on and get restarted upon failures. Modern runtime platforms like Docker-ized platforms (e.g. Kubernetes), and Serverless take care for this automatically. When the app is hosted on a bare metal server, one must take care for a process management tools like [systemd](https://systemd.io/). Avoid including a custom process management tool in a modern platform that monitors an app instance (e.g., Kubernetes) - doing so will hide failures from the infrastructure. When the underlying infrastructure is not aware of errors, it can't perform useful mitigation steps like re-placing the instance in a different location

**Otherwise:** Running dozens of instances without a clear strategy and too many tools together (cluster management, docker, PM2) might lead to DevOps chaos

🔗 [**Read More: Guard process uptime using the right tool**](./sections/production/guardprocess.md)

<br/><br/>

## ![✔] 5.6. Utilize all CPU cores

**TL;DR:** At its basic form, a Node app runs on a single CPU core while all others are left idling. It’s your duty to replicate the Node process and utilize all CPUs. Most of the modern run-times platform (e.g., Kubernetes) allow replicating instances of the app but they won't verify that all cores are utilized - this is your duty. If the app is hosted on a bare server, it's also your duty to use some process replication solution (e.g. systemd)

**Otherwise:** Your app will likely utilize only 25% of its available resources(!) or even less. Note that a typical server has 4 CPU cores or more, naive deployment of Node.js utilizes only 1 (even using PaaS services like AWS beanstalk!)

🔗 [**Read More: Utilize all CPU cores**](./sections/production/utilizecpu.md)

<br/><br/>

## ![✔] 5.7. Create a ‘maintenance endpoint’

**TL;DR:** Expose a set of system-related information, like memory usage and REPL, etc in a secured API. Although it’s highly recommended to rely on standard and battle-tested tools, some valuable information and operations are easier done using code

**Otherwise:** You’ll find that you’re performing many “diagnostic deploys” – shipping code to production only to extract some information for diagnostic purposes

🔗 [**Read More: Create a ‘maintenance endpoint’**](./sections/production/createmaintenanceendpoint.md)

<br/><br/>

## ![✔] 5.8. Discover the unknowns using APM products

### `📝 #updated`

**TL;DR:** Consider adding another safety layer to the production stack - APM. While the majority of symptoms and causes can be detected using traditional monitoring techniques, in a distributed system there is more than meets the eye. Application monitoring and performance products (a.k.a. APM) can auto-magically go beyond traditional monitoring and provide additional layer of discovery and developer-experience. For example, some APM products can highlight a transaction that loads too slow on the **end-user's side** while suggesting the root cause. APMs also provide more context for developers who try to troubleshoot a log error by showing what was the server busy with when the error occurred. To name a few example

**Otherwise:** You might spend great effort on measuring API performance and downtimes, probably you’ll never be aware which is your slowest code parts under real-world scenario and how these affect the UX

🔗 [**Read More: Discover errors and downtime using APM products**](./sections/production/apmproduct

## installation

**TL;DR:** Run `npm ci` to strictly do a clean install of your dependencies matching package.json and package-lock.json. Obviously production code must use the exact version of the packages that were used for testing. While package-lock.json file sets strict version for dependencies, in case of mismatch with the file package.json, the command 'npm install' will treat package.json as the source of truth. On the other hand, the command 'npm ci' will exit with error in case of mismatch between these files

**Otherwise:** QA will thoroughly test the code and approve a version that will behave differently in production. Even worse, different servers in the same production cluster might run different code.

🔗 [**Read More: Use npm ci**](./sections/production/installpackageswithnpmci.md)

<br/><br/><br/>

<p align="right"><a href="#table-of-contents">⬆ Return to top</a></p>

# `6. Security Best Practices`

<div align="center">
<img src="https://img.shields.io/badge/OWASP%20Threats-Top%2010-green.svg" alt="54 items"/>
</div>

## ![✔] 6.1. Embrace linter security rules

<a href="https://www.owasp.org/index.php/Top_10-2017_A1-Injection" target="_blank"><img src="https://img.shields.io/badge/%E2%9C%94%20OWASP%20Threats%20-%20A1:Injection%20-green.svg" alt=""/></a> <a href="https://www.owasp.org/index.php/Top_10-2017_A7-Cross-Site_Scripting_(XSS)" target="_blank"><img src="https://img.shields.io/badge/%E2%9C%94%20OWASP%20Threats%20-%20XSS%20-green.svg" alt=""/></a>

**TL;DR:** Make use of security-related linter plugins such as [eslint-plugin-security](https://github.com/nodesecurity/eslint-plugin-security) to catch security vulnerabilities and issues as early as possible, preferably while they're being coded. This can help catching security weaknesses like using eval, invoking a child process or importing a module with a string literal (e.g. user input). Click 'Read more' below to see code examples that will get caught by a security linter

**Otherwise:** What could have been a straightforward security weakness during development becomes a major issue in production. Also, the project may not follow consistent code security practices, leading to vulnerabilities being introduced, or sensitive secrets committed into remote repositories

🔗 [**Read More: Lint rules**](./sections/security/lintrules.md)

<br/><br/>

## ![✔] 6.2. Limit concurrent requests using a middleware

<a href="https://www.owasp.org/index.php/Denial_of_Service" target="_blank"><img src="https://img.shields.io/badge/%E2%9C%94%20OWASP%20Threats%20-%20DDOS%20-green.svg" alt=""/></a>

**TL;DR:** DOS attacks are very popular and relatively easy to conduct. Implement rate limiting using an external service such as cloud load balancers, cloud firewalls, nginx, [rate-limiter-flexible](https://www.npmjs.com/package/rate-limiter-flexible) package, or (for smaller and less critical apps) a rate-limiting middleware (e.g. [express-rate-limit](https://www.npmjs.com/package/express-rate-limit))

**Otherwise:** An application could be subject to an attack resulting in a denial of service where real users receive a degraded or unavailable service.

🔗 [**Read More: Implement rate limiting**](./sections/security/limitrequests.md)

<br/><br/>
