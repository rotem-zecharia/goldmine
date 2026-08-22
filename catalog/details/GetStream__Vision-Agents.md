# GetStream/Vision-Agents

Open Vision Agents by Stream. Build voice and vision agents quickly with any model or video provider. Uses Stream's edge network for ultra-low latency.

## installation

**Step 1: Install via uv**

`uv add vision-agents`

**Step 2: (Optional) Install with extra integrations**

`uv add "vision-agents[getstream, openai, elevenlabs, deepgram]"`

**Step 3: Obtain your Stream API credentials**

Get a free API key from [Stream](https://getstream.io/try-for-free/?utm_source=github.com&utm_medium=referral&utm_campaign=vision_agents). Developers receive **333,000 participant minutes** per month,
plus extra credits via the Maker Program.

Follow the [quickstart guide](https://visionagents.ai/introduction/quickstart) to build your first agent.

## tools

agent = Agent(
    edge=getstream.Edge(),
    agent_user=agent_user,
    instructions="Read @golf_coach.md",
    llm=gemini.Realtime(fps=10),
    processors=[ultralytics.YOLOPoseProcessor(model_path="yolo11n-pose.pt", device="cuda")],

## features

| **Feature**              | **Description**                                                                                         |
|--------------------------|---------------------------------------------------------------------------------------------------------|
| **Real-time WebRTC**     | Stream video directly to model providers for instant visual understanding.                              |
| **Video Processing**     | Pluggable processor pipeline for YOLO, Roboflow, or custom PyTorch/ONNX models before/after LLM calls. |
| **Turn Detection**       | Natural conversation flow with VAD, diarization, and smart turn-taking.                                 |
| **Tool Calling & MCP**   | Execute code and APIs mid-conversation — Linear issues, weather, telephony, or any MCP server.          |
| **Phone Integration**    | Inbound and outbound voice calls via Twilio or Telnyx with bidirectional audio streaming.               |
| **RAG**                  | Retrieval-augmented generation with TurboPuffer/Qdrant vector search or Gemini FileSearch.                     |
| **Memory**               | Agents recall context across turns and sessions via Stream Chat.                                        |
| **Text Back-channel**    | Message the agent silently during a call — coaching overlays, silent instructions, etc.                 |
| **Production Ready**     | Built-in HTTP server, Prometheus metrics, horizontal scaling, and Kubernetes deployment.                |

## limitations

- Video AI struggles with small text — models may hallucinate scores, signs, etc.
- Context degrades on longer sessions (~30s+) for continuous video understanding
- Most use cases need a mix of specialized models (YOLO, Roboflow) with larger LLMs
- Real-time models require audio/text to trigger responses — video alone won't prompt output
