# AI Design Blueprint — Local Models Setup

For local or open-weight runtimes, start with static prompt packs and only add HTTP MCP if your runtime supports it safely.

## Steps

1. Choose `system-prompt-deepseek.md` or `system-prompt-qwen.md` as the primary prompt pack.
2. Keep `llms.txt` as the lightweight discovery companion.
3. Use `agentic-design-blueprint.json` or `.md` as the offline export when you want broader local context.
4. Only add the public MCP endpoint if your runtime can call HTTP MCP safely and explicitly.

## Public read-only MCP tools worth using

- `list_principles(cluster?)`
- `list_clusters()`
- `get_principle(slug)`
- `get_cluster(slug)`
- `get_example(slug)`
- `search_principles(query, limit?)`
- `search_examples(query, principle_ids?, difficulty?, library?, limit?)`
- `list_agent_assets()`
