# AI Design Blueprint — GitHub Copilot Setup

GitHub Copilot should start with persistent repo instructions. `AGENTS.md` is the companion layer when you want the same doctrine shared with other repo-aware tools.

## Steps

1. Download `copilot-instructions.md`.
2. Save it as `.github/copilot-instructions.md`.
3. Optionally add `AGENTS.md` at repo root for cross-tool consistency.
4. Use the public MCP endpoint only as an optional retrieval extension.

## Public read-only MCP tools worth using

- `list_principles(cluster?)`
- `list_clusters()`
- `get_principle(slug)`
- `get_cluster(slug)`
- `get_example(slug)`
- `search_principles(query, limit?)`
- `search_examples(query, principle_ids?, difficulty?, library?, limit?)`
- `list_agent_assets()`
