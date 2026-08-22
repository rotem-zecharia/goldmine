# RyanCodrai/turbovec

A vector index built on TurboQuant, written in Rust with Python bindings

## tools

![x86 Speed — Single-threaded](https://raw.githubusercontent.com/RyanCodrai/turbovec/main/docs/x86_speed_st.svg)

![x86 Speed — Multi-threaded](https://raw.githubusercontent.com/RyanCodrai/turbovec/main/docs/x86_speed_mt.svg)

On x86, TurboQuant wins every config, averaging 3.4× at 4-bit (3.2–3.5× across cells — the AVX-512 VNNI dot-product kernel on the vector-major layout) and 20% at 2-bit (5–32%), where the `vpermb` LUT scan carries the short 2-bit accumulate loop.

## Insertion & Removal Latency

Same corpus as the search cells: 100K OpenAI vectors, median of 5 runs, timed loops including the Python-call overhead a caller actually pays per op. Insertion measures per-vector `add()` latency on a warm, populated index (built untimed) at n=1 — a single-vector `add()` — and n=100 — a 100-vector batch, showing how far batching amortizes the per-call overhead — against `add()` into the trained, populated FAISS `IndexPQFastScan` (training untimed). A single `add()` lands in 6.3–19.7 µs depending on the cell (7.6–13.9× faster than a FAISS single add), and a 100-vector batch amortizes TurboQuant to 4.6–16.3 µs/vector (4.6–15.1× faster than the same batch into FAISS). Removal measures per-op remove-by-id latency at n=1 (the steady per-op rate over 1000 removes) and n=100 (the first 100 removes on a fresh index): `IdMapIndex.remove(id)` — O(1) swap-and-pop plus the id-map bookkeeping — lands at 0.44–1.22 µs and 0.59–1.37 µs per op across the cells. The FAISS column is the same user-visible operation, `remove_ids` on an `IndexIDMap` over `IndexPQFastScan`, which repacks the stored codes on every call: 0.19–1.02 s per single remove at 100K, with cost doubling alongside code size — which is why the removal charts use a log-scale axis. Charts show the single-threaded cells (`RAYON_NUM_THREADS=1`); the `_mt` cells are measured too and match at n=1, since a single add is serial. Scripts: [`benchmarks/suite/`](https://github.com/RyanCodrai/turbovec/tree/main/benchmarks/suite/).

### ARM (GCP c4a-standard-8, Google Axion, 8 vCPUs)

![ARM Online Insert Latency — Single-threaded](https://raw.githubusercontent.com/RyanCodrai/turbovec/main/docs/arm_insert_online_st.svg)

![ARM Online Remove Latency — Single-threaded](https://raw.githubusercontent.com/RyanCodrai/turbovec/main/docs/arm_remove_online_st.svg)

Full results: [d=1536 2-bit insert](https://github.com/RyanCodrai/turbovec/blob/main/benchmarks/results/speed_insert_d1536_2bit_arm_st.json), [d=1536 4-bit insert](https://github.com/RyanCodrai/turbovec/blob/main/benchmarks/results/speed_insert_d1536_4bit_arm_st.json), [d=3072 2-bit insert](https://github.com/RyanCodrai/turbovec/blob/main/benchmarks/results/speed_insert_d3072_2bit_arm_st.json), [d=3072 4-bit insert](https://github.com/RyanCodrai/turbovec/blob/main/benchmarks/results/speed_insert_d3072_4bit_arm_st.json), and the matching [`speed_remove_*`](https://github.com/RyanCodrai/turbovec/tree/main/benchmarks/results/) and `_mt` files.

### x86 (Intel Xeon Platinum 8481C / Sapphire Rapids, 8 vCPUs)

![x86 Online Insert Latency — Single-threaded](https://raw.githubusercontent.com/RyanCodrai/turbovec/main/docs/x86_insert_online_st.svg)

![x86 Online Remove Latency — Single-threaded](https://raw.githubusercontent.com/RyanCodrai/turbovec/main/docs/x86_remove_online_st.svg)

Full results: [d=1536 2-bit insert](https://github.com/RyanCodrai/turbovec/blob/main/benchmarks/results/speed_insert_d1536_2bit_x86_st.json), [d=1536 4-bit insert](https://github.com/RyanCodrai/turbovec/blob/main/benchmarks/results/speed_insert_d1536_4bit_x86_st.json), [d=3072 2-bit insert](https://github.com/RyanCodrai/turbovec/blob/main/benchmarks/results/speed_insert_d3072_2bit_x86_st.json), [d=3072 4-bit insert](https://github.com/RyanCodrai/turbovec/blob/main/benchmarks/results/speed_insert_d3072_4bit_x86_st.json), and the matching [`speed_remove_*`](https://github.com/RyanCodrai/turbovec/tree/main/benchmarks/results/) and `_mt` files.

## Save & Load

Same corpus as t
