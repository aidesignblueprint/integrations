# AI Design Blueprint — Claude Code Setup

Use Claude Code with the public read-only MCP endpoint plus the Blueprint skill pack for always-on doctrine context.

## Steps

1. Download `claude-skill-pack.zip` and install it into your Claude skills directory.
2. Add the MCP server config below to the Claude MCP config file you already use.
3. Verify the connection with `clusters.list()` after initialize succeeds.
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

- `principles.list(cluster?)`
- `clusters.list()`
- `principles.get(slug)`
- `clusters.get(slug)`
- `examples.get(slug)`
- `principles.search(query, limit?)`
- `examples.search(query, principle_ids?, difficulty?, library?, limit?)`
- `assets.list()`
- `guides.list()`
- `guides.get(slug)`
- `guides.search(query, limit?)`

## First proof call

1. Start a session with the MCP server connected.
2. Call `clusters.list()`.
3. Then call `examples.search(query="orchestration visibility steering", limit=3)`.
4. Only use protected tools after authenticated setup exists.
