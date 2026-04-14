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

## Public MCP retrieval tools

- `list_principles(cluster?)`
- `list_clusters()`
- `get_principle(slug)`
- `get_cluster(slug)`
- `get_example(slug)`
- `search_principles(query, limit?)`
- `search_examples(query, principle_ids?, difficulty?, library?, limit?)`
- `list_agent_assets()`

## Public MCP signal tools (write, opt-in)

- `report_value_event(event_type, surface_used?, brief_context?, perceived_value?, workflow_stage?, would_recommend?, team_size?)` — only offer after clear user satisfaction; never call automatically
- `submit_feedback(task_type?, surface?, rating_clarity?, rating_usefulness?, what_helped?, what_missing?, would_use_again?, contact_email?, permission_to_follow_up?)` — only call on explicit user request

## Feedback and value signal rules

- Only call `report_value_event` after the user has clearly expressed that something was useful. Never call it automatically or silently. Offer at most once per session.
- Only call `submit_feedback` when the user explicitly asks to leave feedback.
- Never include proprietary code, file contents, or secrets in `brief_context`.
- Static files send nothing. These tools only send the structured fields you pass.
