# AFLplusplus/AFLplusplus

The fuzzer afl++ is afl with community patches, qemu 5.1 upgrade, collision-free coverage, enhanced laf-intel & redqueen, AFLfast++ power schedules, MOpt mutators, unicorn_mode, and a lot more!

## installation

Here is some information to get you started:

* For an overview of the AFL++ documentation and a very helpful graphical guide,
  please visit [docs/README.md](docs/README.md).
* To get you started with tutorials, go to
  [docs/tutorials.md](docs/tutorials.md).
* For releases, see the
  [Releases tab](https://github.com/AFLplusplus/AFLplusplus/releases) and
  [branches](#branches). The best branches to use are, however, `stable` or
  `dev` - depending on your risk appetite. Also take a look at the list of
  [important changes in AFL++](docs/important_changes.md) and the list of
  [features](docs/features.md).
* If you want to use AFL++ for your academic work, check the
  [papers page](https://aflplus.plus/papers/) on the website.
* To cite our work, look at the [Cite](#cite) section.
* For comparisons, use the fuzzbench `aflplusplus` setup, or use
  `afl-clang-fast` with `AFL_LLVM_CMPLOG=1`. You can find the `aflplusplus`
  default configuration on Google's
  [fuzzbench](https://github.com/google/fuzzbench/tree/master/fuzzers/aflplusplus).

## Building and installing AFL++

To have AFL++ easily available with everything compiled, pull the image directly
from the Docker Hub (available for both x86_64 and arm64):

```shell
docker pull aflplusplus/aflplusplus
docker run -ti -v /location/of/your/target:/src aflplusplus/aflplusplus
```

This image is automatically published when a push to the stable branch happens
(see [branches](#branches)). If you use the command above, you will find your
target source code in `/src` in the container.

Note: you can also pull `aflplusplus/aflplusplus:dev` which is the most current
development state of AFL++.

To build AFL++ yourself - *which we recommend* - continue at
[docs/INSTALL.md](docs/INSTALL.md).

## Quick start: Fuzzing with AFL++

*NOTE: Before you start, please read about the
[common sense risks of fuzzing](docs/fuzzing_in_depth.md#0-common-sense-risks).*

This is a quick start for fuzzing targets with the source code available. To
read about the process in detail, see
[docs/fuzzing_in_depth.md](docs/fuzzing_in_depth.md).

To learn about fuzzing other targets, see:
* Binary-only targets:
  [docs/fuzzing_binary-only_targets.md](docs/fuzzing_binary-only_targets.md)
* Network services:
  [docs/best_practices.md#fuzzing-a-network-service](docs/best_practices.md#fuzzing-a-network-service)
* GUI programs:
  [docs/best_practices.md#fuzzing-a-gui-program](docs/best_practices.md#fuzzing-a-gui-program)

Step-by-step quick start:

1. Compile the program or library to be fuzzed using `afl-cc`. A common way to
   do this would be:

   ```
   CC=/path/to/afl-cc CXX=/path/to/afl-c++ ./configure --disable-shared
   make clean all
   ```

2. Get a small but valid input file that makes sense to the program. When
   fuzzing verbose syntax (SQL, HTTP, etc.), create a dictionary as described in
   [dictionaries/README.md](dictionaries/README.md), too.

3. If the program reads from stdin, run `afl-fuzz` like so:

   ```
   ./afl-fuzz -i seeds_dir -o output_dir -- \
   /path/to/tested/program [...program's cmdline...]
   ```

   To add a dictionary, add `-x /path/to/dictionary.txt` to afl-fuzz.

   If the program takes input from a file, you can put `@@` in the program's
   command line; AFL++ will put an auto-generated file name in there for you.

4. Investigate anything shown in red in the fuzzer UI by promptly consulting
   [docs/afl-fuzz_approach.md#understanding-the-status-screen](docs/afl-fuzz_approach.md#understanding-the-status-screen).

5. You will find found crashes and hangs in the subdirectories `crashes/` and
   `hangs/` in the `-o output_dir` directory. You can replay the crashes by
   feeding them to the target, e.g. if your target is using stdin:

   ```
   cat output_dir/crashes/id:000000,* | /path/to/tested/program [...program's cmdline...]
   ```

   You can generate cores or use gdb directly to follow up the crashes.

6. For coverage analysis of your fuzzing we recommend our partner tools

