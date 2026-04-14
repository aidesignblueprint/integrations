# AI Design Blueprint — Agent Instructions

Use this doctrine when building or reviewing AI-native features, coding agents, approval flows, or agentic workflows.

## Rules

1. Do not over-automate risky actions.
2. Show meaningful runtime state.
3. Preserve reversibility.
4. Use deterministic fallback paths.
5. Keep outputs structured and inspectable.
6. Separate proposing from executing for high-impact work.
7. Keep boundaries explicit.
8. Optimize for production readiness, not demo theatrics.

## Working method

- Start by naming the principle or cluster most relevant to the task.
- Prefer prepare, propose, or draft before execute when the action is risky or externally visible.
- Keep intermediate agent state visible during long-running work.
- Use deterministic fallback paths when the model is uncertain or a tool fails.
- Keep payloads structured, typed, and inspectable where possible.

## Public retrieval surface

- MCP endpoint: `https://aidesignblueprint.com/mcp`
- Principles: `https://aidesignblueprint.com/principles`
- Examples: `https://aidesignblueprint.com/examples`
- Download hub: `https://aidesignblueprint.com/en/for-agents`

Public retrieval MCP tools:

- `list_principles(cluster?)`
- `list_clusters()`
- `get_principle(slug)`
- `get_cluster(slug)`
- `get_example(slug)`
- `search_principles(query, limit?)`
- `search_examples(query, principle_ids?, difficulty?, library?, limit?)`
- `list_agent_assets()`

Public signal MCP tools (write, opt-in — anonymous-allowed):

- `report_value_event(event_type, surface_used?, brief_context?, perceived_value?, workflow_stage?, would_recommend?, team_size?)` — records a value moment; only offer after clear user satisfaction; never call automatically or silently
- `submit_feedback(task_type?, surface?, rating_clarity?, rating_usefulness?, what_helped?, what_missing?, would_use_again?, contact_email?, permission_to_follow_up?)` — explicit qualitative feedback; only call on explicit user request

Protected tools exist, but they are not part of the public anonymous setup path:

- `get_my_learning_path()`
- `get_my_coaching_context()`
- `validate_agent_architecture(implementation_context, focus_area?, task?, language?, repository?, files?, goals?, example_limit?, private_session?)` — Pro/Teams only; set private_session=true to skip all server-side logging for that call
- `add_evidence_note(course_slug, stage_id, note)`

## Feedback and value signal rules

- Only call `report_value_event` after the user has clearly expressed that something was useful.
  Never call it automatically, never call it silently.
  Offer at most once per session after a clear success signal. Do not offer again unless the user asks.
- Only call `submit_feedback` when the user explicitly asks to leave feedback.
  Never prompt for it without a clear signal from the user.
- Never include proprietary code, file contents, or secrets in `brief_context`.
- These tools only send the structured fields you pass. Static files send nothing.

## First prompt

Use the Blueprint as a doctrine layer for this task.

1. Name the most relevant doctrine cluster first.
2. Call `list_clusters()` or `search_principles(...)` only if you need retrieval.
3. State the execution boundary, approval boundary, and fallback path before implementation.
4. Return the next concrete step, not only analysis.
