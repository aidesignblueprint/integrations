# AI Design Blueprint — Qwen Code Setup

Qwen Code supports Agent Skills and MCP — install the Qwen Skill Pack for always-on local doctrine context, then register the MCP server for live retrieval.

## Steps

1. Install the Qwen Skill Pack (project-local): `curl -L -o /tmp/qwen-skill-pack.zip https://aidesignblueprint.com/agent-assets/qwen-skill-pack.zip && unzip -o /tmp/qwen-skill-pack.zip -d .` — installs `.qwen/skills/agentic-design-blueprint/SKILL.md`.
2. Or install personally (home directory): `curl -L -o /tmp/qwen-skill-pack.zip https://aidesignblueprint.com/agent-assets/qwen-skill-pack.zip && unzip -o /tmp/qwen-skill-pack.zip -d ~`.
3. Register the MCP server in Qwen Code settings. Add `https://aidesignblueprint.com/mcp` as an HTTP MCP server named `aidesignblueprint`. No API key required for public read-only tools.
4. Keep `agentic-design-blueprint.json` or `system-prompt-qwen.md` as a local offline fallback.
5. Verify the connection with `clusters.list()` first, then use `principles.search()` or `examples.search()` for doctrine lookups.

## Public read-only MCP tools worth using

- `principles.list(cluster?)`
- `clusters.list()`
- `principles.get(slug)`
- `clusters.get(slug)`
- `examples.get(slug)`
- `principles.search(query, limit?)`
- `examples.search(query, principle_ids?, difficulty?, library?, pattern_family?, limit?)`
- `assets.list()`
- `guides.list()`
- `guides.get(slug)`
- `guides.search(query, limit?)`
- `signals.feedback(task_type?, surface?, rating_clarity?, rating_usefulness?, what_helped?, what_missing?, would_use_again?, contact_email?, permission_to_follow_up?)`
