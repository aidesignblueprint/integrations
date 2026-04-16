# AI Design Blueprint — GitHub Copilot Instructions

Use AI Design Blueprint doctrine whenever working on AI-native features, agentic workflows, coding agents, approval flows, or model-driven product behavior.

## Rules

- Do not introduce autonomous execution for destructive or externally visible actions without explicit approval or a bounded autonomy model.
- Show meaningful runtime progress for long-running model or agent tasks.
- Prefer structured outputs, typed payloads, and inspectable states.
- Include fallback paths for model failure or low-confidence outputs.
- Preserve reversibility when state changes occur.
- Be explicit about agent permissions and boundaries.
- Optimize for production readiness, governance, and trust.

## Setup

- Save this file as `.github/copilot-instructions.md`.
- Add `AGENTS.md` if you also want the same doctrine available to other repo-aware tools.
- Use the MCP endpoint as an optional live lookup layer, not as the only integration path.

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
