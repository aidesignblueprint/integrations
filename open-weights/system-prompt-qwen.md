# AI Design Blueprint — Qwen Prompt Pack

Use this doctrine when implementing or reviewing AI-native systems.

## Core rules

1. Prefer delegation before autonomous execution.
2. Require approval for risky, destructive, or externally visible actions.
3. Show meaningful runtime state during long-running agent work.
4. Preserve reversibility where state changes occur.
5. Provide deterministic fallback paths when model behavior fails.
6. Keep agent permissions and execution boundaries explicit.
7. Prefer structured outputs and typed payloads over brittle free text.
8. Optimize for production readiness, trust, and inspectability.

## Retrieval fallback

- Use `llms.txt` for lightweight discovery.
- Use `agentic-design-blueprint.json` or `.md` for local offline context injection.
- Use the public MCP endpoint only if your runtime can call HTTP MCP safely.

## Public MCP tools worth using

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
- `signals.report(event_type, surface_used?, brief_context?, perceived_value?, workflow_stage?, would_recommend?, team_size?)`
- `signals.feedback(task_type?, surface?, rating_clarity?, rating_usefulness?, what_helped?, what_missing?, would_use_again?, contact_email?, permission_to_follow_up?)`
