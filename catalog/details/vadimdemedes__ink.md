# vadimdemedes/ink

🌈 React for interactive command-line apps

## installation

```sh
npm install ink react
```

> [!NOTE]
> This readme documents the upcoming version of Ink. For the latest stable release, see [Ink on npm](https://www.npmjs.com/package/ink).

## tools

```jsx
import React, {useState, useEffect} from 'react';
import {render, Text} from 'ink';

const Counter = () => {
	const [counter, setCounter] = useState(0);

	useEffect(() => {
		const timer = setInterval(() => {
			setCounter(previousCounter => previousCounter + 1);
		}, 100);

		return () => {
			clearInterval(timer);
		};
	}, []);

	return <Text color="green">{counter} tests passed</Text>;
};

render(<Counter />);
```

<img src="media/demo.svg" width="600">

## Who's Using Ink?

- [Claude Code](https://github.com/anthropics/claude-code) - An agentic coding tool made by Anthropic.
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) - An agentic coding tool made by Google.
- [GitHub Copilot CLI](https://github.com/features/copilot/cli) - Just say what you want the shell to do.
- [Canva CLI](https://www.canva.dev/docs/apps/canva-cli/) - CLI for creating and managing Canva Apps.
- [Cloudflare's Wrangler](https://github.com/cloudflare/wrangler2) - The CLI for Cloudflare Workers.
- [Linear](https://linear.app) - Linear built an internal CLI for managing deployments, configs, and other housekeeping tasks.
- [Gatsby](https://www.gatsbyjs.org) - Gatsby is a modern web framework for blazing-fast websites.
- [tap](https://node-tap.org) - A Test-Anything-Protocol library for JavaScript.
- [Terraform CDK](https://github.com/hashicorp/terraform-cdk) - Cloud Development Kit (CDK) for HashiCorp Terraform.
- [Specify CLI](https://specifyapp.com) - Automate the distribution of your design tokens.
- [Twilio's SIGNAL](https://github.com/twilio-labs/plugin-signal2020) - CLI for Twilio's SIGNAL conference. [Blog post](https://www.twilio.com/blog/building-conference-cli-in-react).
- [Typewriter](https://github.com/segmentio/typewriter) - Generates strongly-typed [Segment](https://segment.com) analytics clients from arbitrary JSON Schema.
- [Prisma](https://www.prisma.io) - The unified data layer for modern applications.
- [Blitz](https://blitzjs.com) - The Fullstack React Framework.
- [New York Times](https://github.com/nytimes/kyt) - NYT uses Ink's `kyt` - a toolkit that encapsulates and manages the configuration for web apps.
- [tink](https://github.com/npm/tink) - A next-generation runtime and package manager.
- [Inkle](https://github.com/jrr/inkle) - A Wordle game.
- [loki](https://github.com/oblador/loki) - Visual regression testing tool for Storybook.
- [Bit](https://github.com/teambit/bit) - Build, distribute, and collaborate on components.
- [Remirror](https://github.com/remirror/remirror) - Your friendly, world-class editor toolkit.
- [Prime](https://github.com/birkir/prime) - Open-source GraphQL CMS.
- [emoj](https://github.com/sindresorhus/emoj) - Find relevant emojis.
- [emma](https://github.com/maticzav/emma-cli) - Find and install npm packages easily.
- [npm-check-extras](https://github.com/akgondber/npm-check-extras) - Check for outdated and unused dependencies, and run update/delete actions on selected ones.
- [swiff](https://github.com/simple-integrated-marketing/swiff) - Multi-environment command-line tools for time-saving web developers.
- [share](https://github.com/marionebl/share-cli) - Share files quickly.
- [Kubelive](https://github.com/ameerthehacker/kubelive) - A CLI for Kubernetes that provides live data about the cluster and its resources.
- [changelog-view](https://github.com/jdeniau/changelog-view) - View changelogs.
- [cfpush](https://github.com/mamachanko/cfpush) - Interactive Cloud Foundry tutorial.
- [startd](https://github.com/mgrip/startd) - Turn your React component into a web app.
- [wiki-cli](https://github.com/hexrcs/wiki-cli) - Search Wikipedia and read article summaries.
- [garson](https://github.com/goliney/garson) - Build interactive, config-based command-line interfaces.
- [git-contrib-calendar](https://github.com/giannisp/git-contrib-calendar) - Display a contributions calendar for any Git repository.
- [gitgud](https://github.com/GitGud-org/GitGud) - Interactive command-line GUI for Git.
- 

## configuration

A React hook that returns `void` and handles user input.
It's a more convenient alternative to using `useStdin` and listening for `data` events.
The callback you pass to `useInput` is called for each character when the user enters any input.
However, if the user pastes text and it's more than one character, the callback will be called only once, and the whole string will be passed as `input`.
You can find a full example of using `useInput` at [examples/use-input](examples/use-input/use-input.tsx).

```jsx
import {useInput} from 'ink';

const UserInput = () => {
	useInput((input, key) => {
		if (input === 'q') {
			// Exit program
		}

		if (key.leftArrow) {
			// Left arrow key pressed
		}
	});

	return …
};
```

#### inputHandler(input, key)

Type: `Function`

The handler function that you pass to `useInput` receives two arguments:

##### input

Type: `string`

The input that the program received.

##### key

Type: `object`

Handy information about a key that was pressed.

###### key.leftArrow

###### key.rightArrow

###### key.upArrow

###### key.downArrow

Type: `boolean`\
Default: `false`

If an arrow key was pressed, the corresponding property will be `true`.
For example, if the user presses the left arrow key, `key.leftArrow` equals `true`.

###### key.return

Type: `boolean`\
Default: `false`

Return (Enter) key was pressed.

###### key.escape

Type: `boolean`\
Default: `false`

Escape key was pressed.

###### key.ctrl

Type: `boolean`\
Default: `false`

Ctrl key was pressed.

###### key.shift

Type: `boolean`\
Default: `false`

Shift key was pressed.

###### key.tab

Type: `boolean`\
Default: `false`

Tab key was pressed.

###### key.backspace

Type: `boolean`\
Default: `false`

Backspace key was pressed.

###### key.delete

Type: `boolean`\
Default: `false`

Delete key was pressed.

###### key.pageDown

###### key.pageUp

Type: `boolean`\
Default: `false`

If the Page Up or Page Down key was pressed, the corresponding property will be `true`.
For example, if the user presses Page Down, `key.pageDown` equals `true`.

###### key.home

###### key.end

Type: `boolean`\
Default: `false`

If the Home or End key was pressed, the corresponding property will be `true`.
For example, if the user presses End, `key.end` equals `true`.

###### key.meta

Type: `boolean`\
Default: `false`

[Meta key](https://en.wikipedia.org/wiki/Meta_key) was pressed.

###### key.super

Type: `boolean`\
Default: `false`

Super key (Cmd on macOS, Win on Windows) was pressed. Requires [kitty keyboard protocol](#kittykeyboard).

###### key.hyper

Type: `boolean`\
Default: `false`

Hyper key was pressed. Requires [kitty keyboard protocol](#kittykeyboard).

###### key.capsLock

Type: `boolean`\
Default: `false`

Caps Lock was active. Requires [kitty keyboard protocol](#kittykeyboard).

###### key.numLock

Type: `boolean`\
Default: `false`

Num Lock was active. Requires [kitty keyboard protocol](#kittykeyboard).

###### key.eventType

Type: `'press' | 'repeat' | 'release'`\
Default: `undefined`

The type of key event. Only available with [kitty keyboard protocol](#kittykeyboard). Without the protocol, this property is `undefined`.

#### options

Type: `object`

##### isActive

Type: `boolean`\
Default: `true`

Enable or disable capturing of user input.
Useful when there are multiple `useInput` hooks used at once to avoid handling the same input several times.

### usePaste(handler, options?)

A React hook that calls `handler` whenever the user pastes text. Bracketed paste mode (`\x1b[?2004h`) is automatically enabled while the hook is active, so pasted text arrives as a single string rather than being misinterpreted as individual key presses.

`usePaste` and `useInput` can be used together in the same component. They operate on separate event channels, so paste content is never forwarded to `useInput` handlers when `usePaste` is active.

```jsx
import {useInput, usePaste} from 'ink';

const MyInput = () => {
	useInput((input, key) => {
		// Only receives 
