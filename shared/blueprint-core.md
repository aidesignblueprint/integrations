---
trigger: model_decision
description: Use when designing, reviewing, or implementing agentic AI workflows, tool use, approvals, orchestration, background work, trust surfaces, or human-in-the-loop systems.
---

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
- To connect the MCP endpoint, add the snippet below to `~/.codeium/windsurf/mcp_config.json` (global) or `.windsurf/mcp.json` (project-local).

## MCP config

```json
{
  "mcpServers": {
    "aidesignblueprint": {
      "serverUrl": "https://aidesignblueprint.com/mcp"
    }
  }
}
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
