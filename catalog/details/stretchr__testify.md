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
