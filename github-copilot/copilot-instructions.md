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

## MCP support notes

Copilot coding agent supports MCP **tools** only — resources and prompts are not supported.
Remote MCP servers require OAuth authentication; the Blueprint public endpoint is anonymous read-only and does not require OAuth.
Add the Blueprint server under `.github/copilot/mcp.json` (repo-level) or user settings → MCP (personal). Example:

```json
{"mcpServers": {"aidesignblueprint": {"type": "http", "url": "https://aidesignblueprint.com/mcp"}}}
```

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
