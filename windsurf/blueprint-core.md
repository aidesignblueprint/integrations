# AI Design Blueprint — Windsurf Rule

Apply this rule to AI features, agents, copilots, and workflow automations.

## Always do

- Keep agent boundaries explicit.
- Prefer prepare / propose / draft before execute.
- Use human approval for risky or irreversible actions.
- Show progress and intermediate runtime state.
- Design fallback paths for model failure.
- Preserve undo, retry, rollback, or repair when state changes happen.
- Prefer structured outputs and inspectable payloads.
- Optimize for real production usage, not just demo behavior.

## Setup

- Save this file as `.windsurf/rules/blueprint-core.md`.
- Optionally add `AGENTS.md` at repo root if you want the same doctrine readable by other tools.
- Use the public MCP endpoint only when you want live retrieval during a session.

## Public MCP tools worth using

- `list_principles(cluster?)`
- `list_clusters()`
- `get_principle(slug)`
- `get_cluster(slug)`
- `get_example(slug)`
- `search_principles(query, limit?)`
- `search_examples(query, principle_ids?, difficulty?, library?, limit?)`
- `list_agent_assets()`
