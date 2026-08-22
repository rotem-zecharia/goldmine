# MemoriLabs/Memori

Memori is agent-native memory infrastructure. A LLM-agnostic layer that turns agent execution and conversation into structured, persistent state for production systems. Built for enterprise, Memori wo

## installation

<details>
<summary><b>TypeScript SDK</b></summary>

```bash
npm install @memorilabs/memori
```
</details>

<details>
<summary><b>Python SDK</b></summary>

```bash
pip install memori
```
</details>

## tools

client = OpenAI()
mem = Memori().llm.register(client)

mem.attribution(entity_id="user_123", process_id="support_agent")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "My favorite color is blue."}]
)
