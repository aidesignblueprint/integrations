# AI Design Blueprint — Codex Setup

Codex should start from the public HTTP MCP server and keep the doctrine exports locally as a readable fallback when live calls are unnecessary.

## Steps

1. Run `codex mcp add aidesignblueprint --url https://aidesignblueprint.com/mcp` in the Codex CLI, or copy the TOML block below into `~/.codex/config.toml`.
2. Keep `agentic-design-blueprint.json` or `agentic-design-blueprint.md` in the repo or nearby as the offline doctrine fallback.
3. Verify the live connection with `list_clusters()` first, then move into a real doctrine lookup for the current task.
4. Add `AGENTS.md` only if you also want the same cross-tool doctrine file readable by other repo-aware clients.

## Copy block

```toml
[mcp_servers.aidesignblueprint]
url = "https://aidesignblueprint.com/mcp"
```

## Kickoff prompt

Configure the blueprint as an HTTP MCP server and keep the local JSON as fallback. Start with `list_principles()`, then search examples for visibility, orchestration, or steering based on the task.

## Public read-only MCP tools worth using

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
