# AI Design Blueprint — Claude Code Setup

Use Claude Code with the public read-only MCP endpoint plus the Blueprint skill pack for always-on doctrine context.

## Steps

1. Download `claude-skill-pack.zip` and install it into your Claude skills directory.
2. Add the MCP server config below to the Claude MCP config file you already use.
3. Verify the connection with `list_clusters()` after initialize succeeds.
4. Keep `agent-kickoff-prompts.md` nearby for first-turn audit and retrieval prompts.

## Copy block

```json
{
  "aidesignblueprint": {
    "type": "http",
    "url": "https://aidesignblueprint.com/mcp"
  }
}
```

## Public read-only MCP tools

- `list_principles(cluster?)`
- `list_clusters()`
- `get_principle(slug)`
- `get_cluster(slug)`
- `get_example(slug)`
- `search_principles(query, limit?)`
- `search_examples(query, principle_ids?, difficulty?, library?, limit?)`
- `list_agent_assets()`

## First proof call

1. Start a session with the MCP server connected.
2. Call `list_clusters()`.
3. Then call `search_examples(query="orchestration visibility steering", limit=3)`.
4. Only use protected tools after authenticated setup exists.
