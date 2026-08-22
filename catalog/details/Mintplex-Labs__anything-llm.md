# Mintplex-Labs/anything-llm

Stop renting your intelligence. Own it with AnythingLLM. Everything you need for a powerful local-first agent experience

## features

AnythingLLM is the all-in-one AI application that lets you build a private, fully-featured ChatGPT—without compromises. Connect your favorite local or cloud LLM, ingest your documents, and start chatting in minutes. Out of the box you get built-in agents, multi-user support, vector databases, and document pipelines — no extra configuration required.

AnythingLLM supports multiple users as well where you can control the access and experience per user without compromising the security or privacy of the instance or your intellectual property.

## installation

- `yarn setup` To fill in the required `.env` files you'll need in each of the application sections (from root of repo).
  - Go fill those out before proceeding. Ensure `server/.env.development` is filled or else things won't work right.
- `yarn dev:server` To boot the server locally (from root of repo).
- `yarn dev:frontend` To boot the frontend locally (from root of repo).
- `yarn dev:collector` To then run the document collector (from root of repo).

[Learn about documents](./server/storage/documents/DOCUMENTS.md)
