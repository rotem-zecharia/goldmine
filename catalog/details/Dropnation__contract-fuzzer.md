# Dropnation/contract-fuzzer

Ethereum smart contract fuzzer

## installation

Requirements:
- Python 3.9+
- pip 26+
- Windows/macOS/Linux

Install in editable mode:

```bash
pip install -e .
```

Print diagnostics (attach to bug reports):

```bash
solfuzz doctor
```

Fuzz example contract:

```bash
solfuzz run --config configs/example.yaml
```

Replay a failure (best-effort):

```bash
solfuzz replay artifacts/run-*/failure.json
```

## configuration

See `configs/example.yaml` for a reference. Key options:
- `solidity.sources`: file(s) or directories with `.sol` files
- `solidity.optimize`, `solidity.runs`, `solidity.evm_version`
- `fuzz.max_steps`, `fuzz.stop_on_fail`, `fuzz.seed`, `fuzz.gas_limit`
- `report.dir`: artifacts directory

## limitations

- Input shrinking/minimization is basic and will be improved.
- Coverage-guided scheduling and parallel workers are on the roadmap.
