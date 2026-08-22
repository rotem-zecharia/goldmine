# charmbracelet/lipgloss

Style definitions for nice terminal layouts 👄

## installation

```bash
go get charm.land/lipgloss/v2
```

> [!TIP]
>
> Upgrading from v1? Check out the [upgrade guide](./UPGRADE_GUIDE_V2.md), or
> point your LLM at it and let it go to town.

## Colors

Lip Gloss supports the following color profiles:

### ANSI 16 colors (4-bit)

```go
lipgloss.Color("5")  // magenta
lipgloss.Color("9")  // red
lipgloss.Color("12") // light blue
```

### ANSI 256 Colors (8-bit)

```go
lipgloss.Color("86")  // aqua
lipgloss.Color("201") // hot pink
lipgloss.Color("202") // orange
```

### True Color (16,777,216 colors; 24-bit)

```go
lipgloss.Color("#0000FF") // good ol' 100% blue
lipgloss.Color("#04B575") // a green
lipgloss.Color("#3C3C3C") // a dark gray
```

...as well as a 1-bit ASCII profile, which is black and white only.

There are also named constants for the 16 standard ANSI colors:

```go
lipgloss.Black
lipgloss.Red
lipgloss.Green
lipgloss.Yellow
lipgloss.Blue
lipgloss.Magenta
lipgloss.Cyan
lipgloss.White
lipgloss.BrightBlack
lipgloss.BrightRed
lipgloss.BrightGreen
lipgloss.BrightYellow
lipgloss.BrightBlue
lipgloss.BrightMagenta
lipgloss.BrightCyan
lipgloss.BrightWhite
```

### Automatically Downsampling Colors

Some users don't have Truecolor terminals. Other times, output might not
support color at all (for example, in logs). Lip Gloss was designed to handle
this gracefully by automatically downsampling colors to the best available
profile.

If you're using Lip Gloss with Bubble Tea, there’s nothing to do. If you're
using Lip Gloss standalone, just use `lipgloss.Println` or `lipgloss.Sprint`
(and their variants).

For more, see [advanced color usage](#advanced-color-usage).

### Color Utilities

Lip Gloss ships with a handful of handy tools for working with colors:

```go
c := lipgloss.Color("#EB4268")      // Sriracha sauce color
dark := lipgloss.Darken(c, 0.5)     // dark Sriracha sauce
light := lipgloss.Lighten(c, 0.35)  // light Sriracha sauce
green := lipgloss.Complementary(c)  // greenish Sriracha sauce
withAlpha := lipgloss.Alpha(c, 0.2) // watered down Sriracha sauce
```

### Advanced Color Tooling

Lip Gloss also supports color blending, automatically choosing light or dark
variants of colors at runtime, and a lot more. For details, see [Advanced Color
Usage](#advanced-color-usage) and [the docs][docs].

## Inline Formatting

Lip Gloss supports the usual ANSI text formatting options:

```go
var style = lipgloss.NewStyle().
    Bold(true).
    Italic(true).
    Faint(true).
    Blink(true).
    Strikethrough(true).
    Underline(true).
    Reverse(true)
```

### Underline Styles

Beyond simple on/off, underlines support multiple styles and custom colors:

```go
s := lipgloss.NewStyle().
    UnderlineStyle(lipgloss.UnderlineCurly).
    UnderlineColor(lipgloss.Color("#FF0000"))
```

Available styles: `UnderlineNone`, `UnderlineSingle`, `UnderlineDouble`,
`UnderlineCurly`, `UnderlineDotted`, `UnderlineDashed`.

### Hyperlinks

Styles can render clickable hyperlinks in supporting terminals:

```go
s := lipgloss.NewStyle().
    Foreground(lipgloss.Color("#7B2FBE")).
    Hyperlink("https://charm.land")

lipgloss.Println(s.Render("Visit Charm"))
```

In unsupported terminals this will degrade gracefully and hyperlinks will
simply not render.

## Block-Level Formatting

Lip Gloss also supports rules for block-level formatting:

```go
// Padding
var style = lipgloss.NewStyle().
    PaddingTop(2).
    PaddingRight(4).
    PaddingBottom(2).
    PaddingLeft(4)

// Margins
var style = lipgloss.NewStyle().
    MarginTop(2).
    MarginRight(4).
    MarginBottom(2).
    MarginLeft(4)
```

There is also shorthand syntax for margins and padding, which follows the same
format as CSS:

```go
// 2 cells on all sides
lipgloss.NewStyle().Padding(2)

// 2 cells on the top and bottom, 4 cells on the left and right
lipgloss.NewStyle().Margin(2, 4)

// 1 cell on the top, 4 cells on the sides, 2 cells on the bottom
lipgloss.NewStyle().Padding(1, 4, 2)

// Clockwise, starting from the top: 2 cells on the top, 4 on 

## tools

One of the most powerful features of Lip Gloss is the ability to render
different colors at runtime depending on the user's terminal and environment,
allowing you to present the best possible user experience.

This section shows you how to do exactly that.

<details>
<summary>Migrating from v1?</summary>

The `compat` package provides `AdaptiveColor`, `CompleteColor`, and
`CompleteAdaptiveColor` for a quicker migration from v1. These work by
looking at `stdin` and `stdout` on a global basis:

```go
import "charm.land/lipgloss/v2/compat"

color := compat.AdaptiveColor{
    Light: lipgloss.Color("#f1f1f1"),
    Dark:  lipgloss.Color("#cccccc"),
}
```

Note that we don't recommend this for new code as it removes the purity from
Lip Gloss, computationally speaking, as it removes transparency around when
I/O happens, which could cause Lip Gloss to compete for resources (like stdin)
with other tools.

</details>

### Adaptive Colors

You can render different colors at runtime depending on whether the terminal
has a light or dark background:

```go
hasDarkBG := lipgloss.HasDarkBackground(os.Stdin, os.Stdout)
lightDark := lipgloss.LightDark(hasDarkBG)

myColor := lightDark(lipgloss.Color("#D7FFAE"), lipgloss.Color("#D75FEE"))
```

#### With Bubble Tea

In Bubble Tea, request the background color, listen for a
`BackgroundColorMsg`, and respond accordingly:

```go
func (m model) Init() tea.Cmd {
    // First, send a Cmd to request the terminal background color.
    return tea.RequestBackgroundColor
}

func (m model) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
    switch msg := msg.(type) {
    case tea.BackgroundColorMsg:
        // Great, we have the background color. Now we can set up our styles
        // against the color.
        m.styles = newStyles(msg.IsDark())
        return m, nil
    }
}

func newStyles(bgIsDark bool) styles {
    // A little ternary function that will return the appropriate color
    // based on the background color.
    lightDark := lipgloss.LightDark(bgIsDark)

    return styles{
        myHotStyle: lipgloss.NewStyle().Foreground(lightDark(
            lipgloss.Color("#f1f1f1"),
            lipgloss.Color("#333333"),
        )),
    }
}
```

#### Standalone

If you’re not using Bubble Tea you can perform the query manually:

```go
// What's the background color?
hasDarkBG := lipgloss.HasDarkBackground(os.Stdin, os.Stderr)

// A helper function that will return the appropriate color based on the
// background.
lightDark := lipgloss.LightDark(hasDarkBG)

// A couple colors with light and dark variants.
thisColor := lightDark(lipgloss.Color("#C5ADF9"), lipgloss.Color("#864EFF"))
thatColor := lightDark(lipgloss.Color("#37CD96"), lipgloss.Color("#22C78A"))

a := lipgloss.NewStyle().Foreground(thisColor).Render("this")
b := lipgloss.NewStyle().Foreground(thatColor).Render("that")

// Render the appropriate colors at runtime:
lipgloss.Fprintf(os.Stderr, "my fave colors are %s and %s", a, b)
```

### Complete Colors

In some cases where you may want to specify exact values for each color profile
(ANSI 16, ANSI 156, and TrueColor). For these cases, use the `Complete` helper:

```go
// You'll need the colorprofile package.
import "github.com/charmbracelet/colorprofile"

// Get the color profile.
profile := colorprofile.Detect(os.Stdout, os.Environ())

// Create a function for rendering the appropriate color based on the profile.
var completeColor := lipgloss.Complete(profile)

// Now we'll choose the appropriate color at runtime.
myColor := completeColor(ansiColor, ansi256Color, trueColor)
```

### Color Downsampling

One of the best things about Lip Gloss is that it can automatically downsample
colors to the best available profile, stripping colors (and ANSI) entirely when
output is not a TTY.

If you’re using Lip Gloss with Bubble Tea there’s nothing to do here:
downsampling is built into Bubble Tea v2. If you’re not using Bubble Tea, use
the Lip Gloss writer functions, which are a drop-in replacement for the `fmt`
