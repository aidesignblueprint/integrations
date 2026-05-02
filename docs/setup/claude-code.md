# AI Design Blueprint — Claude Code Setup

Use Claude Code with the public read-only MCP endpoint plus the Blueprint skill pack for always-on doctrine context.

## Steps

1. Download `claude-skill-pack.zip` and install it into your Claude skills directory.
2. Add the MCP server config below to the Claude MCP config file you already use.
3. Verify the connection with `clusters.list()` after initialize succeeds.
4. Keep `agent-kickoff-prompts.md` nearby for first-turn audit and retrieval prompts.

## Copy block

```json
{
  "aidesignblueprint": {
    "type": "http",
    "url": "https://aidesignblueprint.com/mcp"
  }
}
```

## Public read-only MCP tools

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

## First proof call

1. Start a session with the MCP server connected.
2. Call `clusters.list()`.
3. Then call `examples.search(query="orchestration visibility steering", limit=3)`.
4. Only use protected tools after authenticated setup exists.

## Governance badges

Show that your agent or repo follows the Blueprint doctrine.

**Free badge** — paste into your `README.md` (no account required):

```markdown
[![AI Design Blueprint](https://aidesignblueprint.com/api/badge/free.svg)](https://aidesignblueprint.com)
```

**Pro badge** — run `architect.validate()` with your architecture description.
The response includes `run_id`, `badge_url`, and `review_url`. Two embeddable variants are available — replace `<run_id>` with the value returned:

Small flat badge:

```markdown
[![Blueprint Readiness Score](https://aidesignblueprint.com/api/badge/run/<run_id>.svg)](https://aidesignblueprint.com/en/readiness-review/<run_id>)
```

Score card (Glama-style panel — score, grade, tier, repository):

```markdown
[![Blueprint Readiness Score card](https://aidesignblueprint.com/api/badge/run/<run_id>/card.svg)](https://aidesignblueprint.com/en/readiness-review/<run_id>)
```

The flat badge shows the Blueprint Readiness Score on one line; the score card is a richer panel with the 0–100 score, A–F grade, tier (Production-ready / Emerging / Draft), and the repository scored. Both link to a public readiness review page anyone can inspect. Requires a Pro or Beta account.
