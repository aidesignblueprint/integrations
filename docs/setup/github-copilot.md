# AI Design Blueprint — GitHub Copilot Setup

GitHub Copilot should start with persistent repo instructions. `AGENTS.md` is the companion layer when you want the same doctrine shared with other repo-aware tools.

## Steps

1. Download `copilot-instructions.md`.
2. Save it as `.github/copilot-instructions.md`.
3. Optionally add `AGENTS.md` at repo root for cross-tool consistency.
4. Use the public MCP endpoint only as an optional retrieval extension.

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
- `signals.report(event_type, surface_used?, brief_context?, perceived_value?, workflow_stage?, would_recommend?, team_size?)`
- `signals.feedback(task_type?, surface?, rating_clarity?, rating_usefulness?, what_helped?, what_missing?, would_use_again?, contact_email?, permission_to_follow_up?)`
