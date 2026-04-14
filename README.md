# AI Design Blueprint Integrations

Official integrations and installable doctrine for AI Design Blueprint across MCP, IDE rules, prompt files, and agent runtimes.

## What is in this repo

- `shared/`: cross-tool doctrine files
- `mcp/`: public MCP configuration and usage notes
- `docs/setup/`: copy-first setup guides by tool
- `cursor/`, `windsurf/`, `github-copilot/`, `gemini/`: provider-specific instruction files
- `open-weights/`: static prompt packs for open-weight and local model workflows
- `exports/`: structured doctrine export

## Public contract

Canonical public endpoints:

- Site: `https://aidesignblueprint.com`
- MCP: `https://aidesignblueprint.com/mcp`
- Developer docs: `https://aidesignblueprint.com/en/for-agents`

## Quick start

1. Pick a setup guide in `docs/setup/`.
2. Add the relevant file or MCP config to your own repository or client.
3. If using MCP, initialize against `https://aidesignblueprint.com/mcp`.
4. Run the first proof call:
   - `list_clusters()`
5. Then run a second proof call:
   - `search_examples(query="orchestration visibility steering", limit=3)`

## Public MCP tools

### Public retrieval tools (anonymous-allowed, read-only)

- `list_principles(cluster?)`
- `list_clusters()`
- `get_principle(slug)`
- `get_cluster(slug)`
- `get_example(slug)`
- `search_principles(query, limit?)`
- `search_examples(query, principle_ids?, difficulty?, library?, limit?)`
- `list_agent_assets()`

### Public signal tools (anonymous-allowed, opt-in write)

- `report_value_event(event_type, surface_used?, brief_context?, perceived_value?, workflow_stage?, would_recommend?, team_size?)` — records a value moment; only offer after the user clearly expresses something was useful; never call automatically or silently
- `submit_feedback(task_type?, surface?, rating_clarity?, rating_usefulness?, what_helped?, what_missing?, would_use_again?, contact_email?, permission_to_follow_up?)` — explicit qualitative feedback; only call when the user explicitly asks to leave feedback

Signal tools write only the structured fields you pass. No prompts, no code, no file contents are stored. See the [privacy policy](https://aidesignblueprint.com/en/privacy) for full data-handling details.

### Protected tools (authenticated, not part of anonymous setup path)

- `get_my_learning_path()`
- `get_my_coaching_context()`
- `validate_agent_architecture(implementation_context, ..., private_session?)` — Pro/Teams; set `private_session=true` to skip all server-side logging for that call
- `summarize_team_usage(days_back?, private_session?)` — Pro/Teams; usage reflection and recommended next assets
- `add_evidence_note(course_slug, stage_id, note)`

## Feedback and value signal rules

- Only call `report_value_event` after the user has clearly expressed that something was useful. Never call automatically or silently. Offer at most once per session after a clear success signal.
- Only call `submit_feedback` when the user explicitly asks to leave feedback. Never prompt for it proactively.
- Never include proprietary code, file contents, or secrets in `brief_context`.

## What is intentionally not here yet

- no public OpenAPI schema
- no public HTTP API contract beyond MCP and static assets
- no CLI installer
- no speculative partner-specific distributions

## Source of truth

This repo is intended to mirror the canonical public contract already shipped on `aidesignblueprint.com`.

Before publishing changes here, verify:

- `/mcp`
- `/llms.txt`
- `/agent-assets/[slug]`
- `/en/for-agents`

remain consistent with the files committed in this repo.
