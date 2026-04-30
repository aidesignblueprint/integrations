# AI Design Blueprint — Local Models Setup

For local or open-weight runtimes, start with static prompt packs and only add HTTP MCP if your runtime supports it safely.

## Steps

1. Choose `system-prompt-deepseek.md` or `system-prompt-qwen.md` as the primary prompt pack.
2. Keep `llms.txt` as the lightweight discovery companion.
3. Use `agentic-design-blueprint.json` or `.md` as the offline export when you want broader local context.
4. Only add the public MCP endpoint if your runtime can call HTTP MCP safely and explicitly.

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
