# rerun-io/rerun

Visualize, query, and stream to train on multimodal robotics data.

## installation

* [**C++**](https://www.rerun.io/docs/getting-started/data-in/cpp)
* [**Python**](https://www.rerun.io/docs/getting-started/data-in/python): `pip install rerun-sdk` or on [`conda`](https://github.com/conda-forge/rerun-sdk-feedstock)
* [**Rust**](https://www.rerun.io/docs/getting-started/data-in/rust): `cargo add rerun`

### Installing the Rerun Viewer binary
To stream log data over the network or load our `.rrd` data files you also need the `rerun` binary.
It can be installed with `pip install rerun-sdk` or with `cargo install rerun-cli --locked --features nasm` (see note below).
Note that only the Python SDK comes bundled with the Viewer whereas C++ & Rust always rely on a separate install.

**Note**: the `nasm` Cargo feature requires the [`nasm`](https://github.com/netwide-assembler/nasm) CLI to be installed and available in your path.
Alternatively, you may skip enabling this feature, but this may result in inferior video decoding performance.

You should now be able to run `rerun --help` in any terminal.


### Documentation
- 📚 [High-level docs](https://rerun.io/docs)
- ⏃ [Loggable Types](https://www.rerun.io/docs/reference/types)
- ⚙️ [Examples](https://rerun.io/examples)
- 📖 [Code snippets](./docs/snippets/INDEX.md)
- 🌊 [C++ API docs](https://ref.rerun.io/docs/cpp)
- 🐍 [Python API docs](https://ref.rerun.io/docs/python)
- 🦀 [Rust API docs](https://docs.rs/rerun/)
- ⁉️ [Troubleshooting](https://www.rerun.io/docs/overview/installing-rerun/troubleshooting)


### Agent skills
This repo ships a set of agent skills that help coding agents write Rerun code.

Install them into your agent with the `skills` CLI:

```sh
npx skills add rerun-io/rerun
```

The skills themselves live in [`skills/`](./skills) if you want to read them directly.


## Status
We are in active development.
There are many features we want to add, and the API is still evolving.
_Expect breaking changes!_

Some shortcomings:
* [The viewer slows down when there are too many entities](https://github.com/rerun-io/rerun/issues/7115)
* [Multi-million point clouds can be slow](https://github.com/rerun-io/rerun/issues/1136)


## What is Rerun for?

Rerun is built to help you understand and improve complex processes that include rich multimodal data, like 2D, 3D, text, time series, tensors, etc.
It is used in many industries, including robotics, simulation, computer vision,
or anything that involves a lot of sensors or other signals that evolve over time.

### Example use case
Say you're building a vacuum cleaning robot and it keeps running into walls. Why is it doing that? You need some tool to debug it, but a normal debugger isn't gonna be helpful. Similarly, just logging text won't be very helpful either. The robot may log "Going through doorway" but that won't explain why it thinks the wall is a door.

What you need is a visual and temporal debugger, that can log all the different representations of the world the robots holds in its little head, such as:

* RGB camera feed
* depth images
* lidar scan
* segmentation image (how the robot interprets what it sees)
* its 3D map of the apartment
* all the objects the robot has detected (or thinks it has detected), as 3D shapes in the 3D map
* its confidence in its prediction
* etc

You also want to see how all these streams of data evolve over time so you can go back and pinpoint exactly what went wrong, when and why.

Maybe it turns out that a glare from the sun hit one of the sensors in the wrong way, confusing the segmentation network leading to bad object detection. Or maybe it was a bug in the lidar scanning code. Or maybe the robot thought it was somewhere else in the apartment, because its odometry was broken. Or it could be one of a thousand other things. Rerun will help you find out!

But seeing the world from the point of the view of the robot is not just for debugging - it will also give you ideas on how to improve the algorithms, new test cases to set up, or datasets to collect. It will also let you explain 
