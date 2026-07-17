# AI Design Blueprint Integrations

[![smithery badge](https://smithery.ai/badge/zampognamichelangelo/aidesignblueprint)](https://smithery.ai/servers/zampognamichelangelo/aidesignblueprint)
[![integrations MCP server](https://glama.ai/mcp/servers/aidesignblueprint/integrations/badges/score.svg)](https://glama.ai/mcp/servers/aidesignblueprint/integrations)

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
   - `clusters.list()`
5. Then run a second proof call:
   - `examples.search(query="orchestration visibility steering", limit=3)`

## Public MCP tools

### Public retrieval tools (anonymous-allowed, read-only)

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

### Public signal tools (anonymous-allowed, opt-in write)

- `signals.report(event_type, surface_used?, brief_context?, perceived_value?, workflow_stage?, would_recommend?, team_size?)` — records a value moment; only offer after the user clearly expresses something was useful; never call automatically or silently
- `signals.feedback(task_type?, surface?, rating_clarity?, rating_usefulness?, what_helped?, what_missing?, would_use_again?, contact_email?, permission_to_follow_up?)` — explicit qualitative feedback; only call when the user explicitly asks to leave feedback

Signal tools write only the structured fields you pass. No prompts, no code, no file contents are stored. See the [privacy policy](https://aidesignblueprint.com/en/privacy) for full data-handling details.

### Protected tools (authenticated, not part of anonymous setup path)

- `me.learning_path()`
- `me.coaching_context()`
- `architect.validate(implementation_context, ..., private_session?)` — Pro/Teams; scores agentic code against the 10 principles; set `private_session=true` to skip the stored run for that call
- `design.validate(implementation_context, ..., private_session?)` — Pro/Teams; the surface mirror: scores a rendered frontend artefact against the 8 experience-design laws (own weekly bucket)
- `spec.validate(implementation_context, ..., private_session?)` — Pro/Teams; the what-to-build lens: scores a written specification against the 8 spec-quality laws (own weekly bucket)
- `team.summarize(days_back?, private_session?)` — Pro/Teams; usage reflection and recommended next assets across all three validator lenses
- `me.add_evidence(course_slug, stage_id, note)`

## Feedback and value signal rules

- Only call `signals.report` after the user has clearly expressed that something was useful. Never call automatically or silently. Offer at most once per session after a clear success signal.
- Only call `signals.feedback` when the user explicitly asks to leave feedback. Never prompt for it proactively.
- Never include proprietary code, file contents, or secrets in `brief_context`.

## Governance badges

Show that your agent or repo follows the Blueprint doctrine.

**Free badge** — paste into your `README.md` (no account required):

```markdown
[![AI Design Blueprint](https://aidesignblueprint.com/api/badge/free.svg)](https://aidesignblueprint.com)
```

**Pro badge** — run `architect.validate()` via the MCP. The response includes `run_id`, `badge_url`, and `review_url`:

```markdown
[![AI Design Blueprint](https://aidesignblueprint.com/api/badge/run/<run_id>.svg)](https://aidesignblueprint.com/en/readiness-review/<run_id>)
```

The Pro badge displays your tier (`Governed · X/Y` or `Reviewed · X/Y`) and links to a public readiness review page. Requires a Pro or Beta account.

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
