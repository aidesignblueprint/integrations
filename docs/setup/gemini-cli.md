# AI Design Blueprint — Gemini CLI Setup

Gemini CLI should start with `GEMINI.md` at project root and use `llms.txt` as the lightweight discovery companion.

## Steps

1. Download `GEMINI.md`.
2. Place it at project root as `GEMINI.md`.
3. Keep `llms.txt` nearby for discovery and doctrine recall.
4. Use the MCP endpoint only when you want live retrieval during the session.

## Public read-only MCP tools worth using

- `list_principles(cluster?)`
- `list_clusters()`
- `get_principle(slug)`
- `get_cluster(slug)`
- `get_example(slug)`
- `search_principles(query, limit?)`
- `search_examples(query, principle_ids?, difficulty?, library?, limit?)`
- `list_agent_assets()`
