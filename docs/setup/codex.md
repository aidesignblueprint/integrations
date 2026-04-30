# AI Design Blueprint — Codex Setup

Codex uses MCP for live doctrine retrieval plus an installable skill pack for always-on local context. Install both for the full experience.

## Steps

1. Install the Codex skill pack (personal): `curl -L -o /tmp/codex-skill-pack.zip https://aidesignblueprint.com/agent-assets/codex-skill-pack.zip && unzip -o /tmp/codex-skill-pack.zip -d ~` — installs into `~/.agents/skills/agentic-design-blueprint/SKILL.md`.
2. Or install project-local: `curl -L -o /tmp/codex-skill-pack.zip https://aidesignblueprint.com/agent-assets/codex-skill-pack.zip && unzip -o /tmp/codex-skill-pack.zip -d .` — installs into `.agents/skills/agentic-design-blueprint/SKILL.md`.
3. Run `codex mcp add aidesignblueprint --url https://aidesignblueprint.com/mcp` in the Codex CLI, or copy the TOML block below into `~/.codex/config.toml`.
4. Keep `agentic-design-blueprint.json` or `agentic-design-blueprint.md` in the repo as the offline doctrine fallback when MCP is unavailable.
5. Verify the live connection with `clusters.list()` first, then move into a real doctrine lookup for the current task.
6. Add `AGENTS.md` only if you also want the same cross-tool doctrine file readable by other repo-aware clients.

## Copy block

```toml
[mcp_servers.aidesignblueprint]
url = "https://aidesignblueprint.com/mcp"
```

## Kickoff prompt

Configure the blueprint as an HTTP MCP server and keep the local JSON as fallback. Start with `principles.list()`, then search examples for visibility, orchestration, or steering based on the task.

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
