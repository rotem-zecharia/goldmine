# onsi/ginkgo

A Modern Testing Framework for Go

## features

Whether writing basic unit specs, complex integration specs, or even performance specs - Ginkgo gives you an expressive Domain-Specific Language (DSL) that will be familiar to users coming from frameworks such as [Quick](https://github.com/Quick/Quick), [RSpec](https://rspec.info), [Jasmine](https://jasmine.github.io), and [Busted](https://lunarmodules.github.io/busted/).  This style of testing is sometimes referred to as "Behavior-Driven Development" (BDD) though Ginkgo's utility extends beyond acceptance-level testing.

With Ginkgo's DSL you can use nestable [`Describe`, `Context` and `When` container nodes](https://onsi.github.io/ginkgo/#organizing-specs-with-container-nodes) to help you organize your specs.  [`BeforeEach` and `AfterEach` setup nodes](https://onsi.github.io/ginkgo/#extracting-common-setup-beforeeach) for setup and cleanup.  [`It` and `Specify` subject nodes](https://onsi.github.io/ginkgo/#spec-subjects-it) that hold your assertions. [`BeforeSuite` and `AfterSuite` nodes](https://onsi.github.io/ginkgo/#suite-setup-and-cleanup-beforesuite-and-aftersuite) to prep for and cleanup after a suite... and [much more!](https://onsi.github.io/ginkgo/#writing-specs).

At runtime, Ginkgo can run your specs in reproducibly [random order](https://onsi.github.io/ginkgo/#spec-randomization) and has sophisticated support for [spec parallelization](https://onsi.github.io/ginkgo/#spec-parallelization).  In fact, running specs in parallel is as easy as

```bash
ginkgo -p
```

By following [established patterns for writing parallel specs](https://onsi.github.io/ginkgo/#patterns-for-parallel-integration-specs) you can build even large, complex integration suites that parallelize cleanly and run performantly.  And you don't have to worry about your spec suite hanging or leaving a mess behind - Ginkgo provides a per-node `context.Context` and the capability to interrupt the spec after a set period of time - and then clean up.

As your suites grow Ginkgo helps you keep your specs organized with [labels](https://onsi.github.io/ginkgo/#spec-labels) and lets you easily run [subsets of specs](https://onsi.github.io/ginkgo/#filtering-specs), either [programmatically](https://onsi.github.io/ginkgo/#focused-specs) or on the [command line](https://onsi.github.io/ginkgo/#combining-filters).  And Ginkgo's reporting infrastructure generates machine-readable output in a [variety of formats](https://onsi.github.io/ginkgo/#generating-machine-readable-reports) _and_ allows you to build your own [custom reporting infrastructure](https://onsi.github.io/ginkgo/#generating-reports-programmatically).

Ginkgo ships with `ginkgo`, a [command line tool](https://onsi.github.io/ginkgo/#ginkgo-cli-overview) with support for generating, running, filtering, and profiling Ginkgo suites.  You can even have Ginkgo automatically run your specs when it detects a change with `ginkgo watch`, enabling rapid feedback loops during test-driven development.

And that's just Ginkgo!  [Gomega](https://onsi.github.io/gomega/) brings a rich, mature, family of [assertions and matchers](https://onsi.github.io/gomega/#provided-matchers) to your suites.  With Gomega you can easily mix [synchronous and asynchronous assertions](https://onsi.github.io/ginkgo/#patterns-for-asynchronous-testing) in your specs.  You can even build your own set of expressive domain-specific matchers quickly and easily by composing Gomega's [existing building blocks](https://onsi.github.io/ginkgo/#building-custom-matchers).

Happy Testing!
