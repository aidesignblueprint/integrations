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

## Public retrieval MCP tools

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

## Public signal MCP tools (opt-in, anonymous-allowed)

- `signals.report(event_type, surface_used?, brief_context?, perceived_value?, workflow_stage?, would_recommend?, team_size?)`
- `signals.feedback(task_type?, surface?, rating_clarity?, rating_usefulness?, what_helped?, what_missing?, would_use_again?, contact_email?, permission_to_follow_up?)`

Only call signal tools after explicit user confirmation. Never call silently.
