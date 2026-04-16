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

## Public signal MCP tools (opt-in, anonymous-allowed)

- `report_value_event(event_type, surface_used?, brief_context?, perceived_value?, workflow_stage?, would_recommend?, team_size?)`
- `submit_feedback(task_type?, surface?, rating_clarity?, rating_usefulness?, what_helped?, what_missing?, would_use_again?, contact_email?, permission_to_follow_up?)`

Only call signal tools after explicit user confirmation. Never call silently.
