# halfrost/Halfrost-Field

✍🏻 Source Code Deep Dives, System Design & Engineering Blogs / Halfrost-Field 冰霜之地：源码解析、系统设计与工程实践笔记

## features

People often say that reading the source code of open-source frameworks can significantly improve one’s skills, so I have also tried reading open-source framework source code and analyzing and understanding it in detail. Here I record my thoughts and insights from reading open-source framework source code, hoping they will be helpful to other developers. I will keep updating the articles in this repository; if you’d like to follow along, please give it a `star`.



## 📖 Table of Contents


# 🔥 LLM


| Project | Version | Article |
|:-------:|:-------:|:------|
|vLLM|v1 @ 6cf7b26bd|[vLLM Source Walkthrough: From `generate()` to the First Token](https://github.com/halfrost/Halfrost-Field/blob/master/contents-en/LLM/vllm/01-from-generate-to-first-token.md)<br>[Entrypoints: `LLM`, CLI, and the OpenAI-Compatible Server](https://github.com/halfrost/Halfrost-Field/blob/master/contents-en/LLM/vllm/02-entrypoints-llm-cli-openai-server.md)<br>[V1 Process Architecture: API Server, EngineCore, and GPU Workers](https://github.com/halfrost/Halfrost-Field/blob/master/contents-en/LLM/vllm/03-v1-process-architecture.md)<br>[EngineCore Loop: Request Lifecycle, Step, and Output Processing](https://github.com/halfrost/Halfrost-Field/blob/master/contents-en/LLM/vllm/04-enginecore-loop-request-lifecycle.md)|


---------------------------

# 🐳 Go

| Project | Version | Article |
|:-------:|:-------:|:------|
|Go|1.16 darwin/amd64| [A Go Beginner's Journey](https://github.com/halfrost/Halfrost-Field/blob/master/contents-en/Go/new_gopher_tips.md)<br>[A First Look at How Go Compile Commands Execute](https://github.com/halfrost/Halfrost-Field/blob/master/contents-en/Go/go_command.md)<br>[In-Depth Analysis of Go Slice Internals](https://github.com/halfrost/Halfrost-Field/blob/master/contents-en/Go/go_slice.md)<br>[How to Design and Implement a Thread-Safe Map? (Part 1)](https://github.com/halfrost/Halfrost-Field/blob/master/contents-en/Go/go_map_chapter_one.md)<br>[How to Design and Implement a Thread-Safe Map? (Part 2)](https://github.com/halfrost/Halfrost-Field/blob/master/contents-en/Go/go_map_chapter_two.md)<br>[LRU / LFU in Interviews: Bronze vs. King](https://github.com/halfrost/Halfrost-Field/blob/master/contents-en/Go/LRU_LFU_interview.md)<br>[In-Depth Study of Go interface Internals](https://github.com/halfrost/Halfrost-Field/blob/master/contents-en/Go/go_interface.md)<br>[The Three Laws of Go reflection and Best Practices](https://github.com/halfrost/Halfrost-Field/blob/master/contents-en/Go/go_reflection.md)<br>[Inside Go Concurrency Primitives — Channel Internals](https://github.com/halfrost/Halfrost-Field/blob/master/contents-en/Go/go_channel.md)<br>|
|Spatial Search|golang/geo|[Understanding n-Dimensional Space and n-Dimensional Spacetime](https://github.com/halfrost/Halfrost-Field/blob/master/contents-en/Go/n-dimensional_space_and_n-dimensional_space-time.md)<br>[Efficient Multidimensional Point Indexing Algorithms — Geohash and Google S2](https://github.com/halfrost/Halfrost-Field/blob/master/contents-en/Go/go_spatial_search.md)<br>[How Is CellID Generated in Google S2?](https://github.com/halfrost/Halfrost-Field/blob/master/contents-en/Go/go_s2_CellID.md)<br>[Finding the LCA in a Quadtree in Google S2](https://github.com/halfrost/Halfrost-Field/blob/master/contents-en/Go/go_s2_lowest_common_ancestor.md)<br>[The Magical De Bruijn Sequence](https://github.com/halfrost/Halfrost-Field/blob/master/contents-en/Go/go_s2_De_Bruijn.md)<br>[How to Find Hilbert Curve Neighbors in a Quadtree?](https://github.com/halfrost/Halfrost-Field/blob/master/contents-en/Go/go_s2_Hilbert_neighbor.md)<br>[How Does Google S2 Solve the Optimal Spatial Covering Problem?](https://github.com/halfrost/Halfrost-Field/blob/master/contents-en/Go/go_s2_regionCoverer.md)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbs
