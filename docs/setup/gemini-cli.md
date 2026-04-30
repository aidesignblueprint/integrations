# AI Design Blueprint — Gemini CLI Setup

Gemini CLI supports Agent Skills — install the Gemini Skill Pack for always-on local doctrine context, then keep GEMINI.md as the persistent project companion.

## Steps

1. Install the Gemini Skill Pack (project-local): `curl -L -o /tmp/gemini-skill-pack.zip https://aidesignblueprint.com/agent-assets/gemini-skill-pack.zip && unzip -o /tmp/gemini-skill-pack.zip -d .` — installs `.agents/skills/agentic-design-blueprint/SKILL.md`.
2. Or install personally (home directory): `curl -L -o /tmp/gemini-skill-pack.zip https://aidesignblueprint.com/agent-assets/gemini-skill-pack.zip && unzip -o /tmp/gemini-skill-pack.zip -d ~`.
3. Download `GEMINI.md` and place it at project root as `GEMINI.md`.
4. Keep `llms.txt` nearby for discovery and doctrine recall.
5. Use the MCP endpoint only when you want live retrieval during the session.

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
