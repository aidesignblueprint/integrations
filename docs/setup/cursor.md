# AI Design Blueprint — Cursor Setup

Cursor works best with the `.mdc` doctrine file first, then the public MCP endpoint as an optional live retrieval layer.

## Steps

1. Download `agentic-design-principles.mdc`.
2. Place it at `.cursor/rules/blueprint-doctrine.mdc`.
3. Optionally connect the public MCP endpoint if you want live lookup for principles and examples.
4. Keep `llms.txt` or `agentic-design-blueprint.md` as the lightweight local fallback.

## Public read-only MCP tools worth using

- `list_principles(cluster?)`
- `list_clusters()`
- `get_principle(slug)`
- `get_cluster(slug)`
- `get_example(slug)`
- `search_principles(query, limit?)`
- `search_examples(query, principle_ids?, difficulty?, library?, limit?)`
- `list_agent_assets()`
