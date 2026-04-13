# AI Design Blueprint — OpenAI GPT Actions Status

OpenAI-style schema integrations are intentionally deferred until matching public HTTP routes and a truthful public OpenAPI contract exist.

## Steps

1. Do not publish or rely on an OpenAPI schema yet for this project.
2. Use the public MCP endpoint for live doctrine retrieval today.
3. Use `agentic-design-blueprint.json`, `.md`, and `llms.txt` for static setup paths today.
4. Move to schema-based integrations only after stable public `/api/v1/...` routes exist and are versioned.

## What is live today

- Public read-only MCP endpoint
- Shared instruction files
- Prompt packs for local and open-weight models
- Machine-readable and markdown doctrine exports

## What is still deferred

- Public `openapi.json`
- Stable `/api/v1/...` route set for schema consumers
- One-click installer tooling
