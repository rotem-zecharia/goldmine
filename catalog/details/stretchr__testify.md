# stretchr/testify

A toolkit with common assertions and mocks that plays nicely with the standard library

## installation

To install Testify, use `go get`:

    go get github.com/stretchr/testify

This will then make the following packages available to you:

    github.com/stretchr/testify/assert
    github.com/stretchr/testify/require
    github.com/stretchr/testify/mock
    github.com/stretchr/testify/suite
    github.com/stretchr/testify/http (deprecated)

Import the `testify/assert` package into your code using this template:

```go
package yours

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestSomething(t *testing.T) {
	assert.True(t, true, "True is true!")
}
```

------

Staying up to date
==================

To update Testify to the latest version, use `go get -u github.com/stretchr/testify`.

------

Supported go versions
==================

We currently support the most recent major Go versions from 1.19 onward.

------

Contributing
============

Please feel free to submit issues, fork the repository and send pull requests!

When submitting an issue, we ask that you please include a complete test function that demonstrates the issue. Extra credit for those using Testify to write the test code that demonstrates it.

Code generation is used. [Look for `Code generated with`](https://github.com/search?q=repo%3Astretchr%2Ftestify%20%22Code%20generated%20with%22&type=code) at the top of some files. Run `go generate ./...` to update generated files.

We also chat on the [Gophers Slack](https://gophers.slack.com) group in the `#testify` and `#testify-dev` channels.

------

License
=======

This project is licensed under the terms of the MIT license.
