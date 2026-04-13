# AI Design Blueprint — Windsurf Setup

Windsurf should start from the workspace rule file, with `AGENTS.md` as the cross-tool companion if you want repo-level consistency.

## Steps

1. Download `blueprint-core.md`.
2. Save it as `.windsurf/rules/blueprint-core.md`.
3. Optionally add `AGENTS.md` at repo root for shared doctrine across tools.
4. Use the MCP endpoint only when you want live retrieval during a session.

## Public read-only MCP tools worth using

- `list_principles(cluster?)`
- `list_clusters()`
- `get_principle(slug)`
- `get_cluster(slug)`
- `get_example(slug)`
- `search_principles(query, limit?)`
- `search_examples(query, principle_ids?, difficulty?, library?, limit?)`
- `list_agent_assets()`
