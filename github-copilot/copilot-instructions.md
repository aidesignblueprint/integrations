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
