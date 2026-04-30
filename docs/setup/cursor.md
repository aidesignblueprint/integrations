# AI Design Blueprint — Cursor Setup

Cursor works best with the Cursor Rule Pack: a ready-to-unzip bundle of the doctrine .mdc file and MCP config. One command installs both.

## Steps

1. Install the Cursor Rule Pack: `curl -L -o /tmp/cursor-rule-pack.zip https://aidesignblueprint.com/agent-assets/cursor-rule-pack.zip && unzip -o /tmp/cursor-rule-pack.zip -d .` — installs `.cursor/rules/blueprint-doctrine.mdc` and `.cursor/mcp.json` at project root.
2. Restart Cursor or reload the project window — Cursor picks up new rules automatically.
3. Check **Settings → MCP** to confirm the `aidesignblueprint` server is listed and connected.
4. Or install the `.mdc` file only: download `agentic-design-principles.mdc` and place it at `.cursor/rules/blueprint-doctrine.mdc` manually.
5. Keep `llms.txt` or `agentic-design-blueprint.md` as the lightweight local doctrine fallback.

## Public read-only MCP tools worth using

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
