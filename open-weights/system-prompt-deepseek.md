# AI Design Blueprint — DeepSeek Prompt Pack

Use this doctrine when implementing or reviewing AI-native systems.

## Core rules

1. Prefer delegation before autonomous execution.
2. Require approval for risky, destructive, or externally visible actions.
3. Show meaningful runtime state during long-running agent work.
4. Preserve reversibility where state changes occur.
5. Provide deterministic fallback paths when model behavior fails.
6. Keep agent permissions and execution boundaries explicit.
7. Prefer structured outputs and typed payloads over brittle free text.
8. Optimize for production readiness, trust, and inspectability.

## Retrieval fallback

- Use `llms.txt` for lightweight discovery.
- Use `agentic-design-blueprint.json` or `.md` for local offline context injection.
- Use the public MCP endpoint only if your runtime can call HTTP MCP safely.

## Public MCP tools worth using

- `list_principles(cluster?)`
- `list_clusters()`
- `get_principle(slug)`
- `get_cluster(slug)`
- `get_example(slug)`
- `search_principles(query, limit?)`
- `search_examples(query, principle_ids?, difficulty?, library?, limit?)`
- `list_agent_assets()`
- `list_application_guides()`
- `get_application_guide(slug)`
- `search_application_guides(query, limit?)`
