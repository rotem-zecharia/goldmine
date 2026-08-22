# RyanCodrai/turbovec

A vector index built on TurboQuant, written in Rust with Python bindings

## tools

![x86 Speed — Single-threaded](https://raw.githubusercontent.com/RyanCodrai/turbovec/main/docs/x86_speed_st.svg)

![x86 Speed — Multi-threaded](https://raw.githubusercontent.com/RyanCodrai/turbovec/main/docs/x86_speed_mt.svg)

On x86, TurboQuant wins every config, averaging 3.4× at 4-bit (3.2–3.5× across cells — the AVX-512 VNNI dot-product kernel on the vector-major layout) and 20% at 2-bit (5–32%), where the `vpermb` LUT scan carries the short 2-bit accumulate loop.
