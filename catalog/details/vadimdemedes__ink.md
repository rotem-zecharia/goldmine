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
