# AI Design Blueprint — Provider Matrix

Use this matrix to pick the smallest truthful setup for each tool or runtime.

| Tool | Primary asset | Optional companion | Retrieval path | Status |
| --- | --- | --- | --- | --- |
| Claude Code | `claude-skill-pack.zip + claude-code.mcp.json` | `agent-kickoff-prompts.md` | MCP + skill + local prompt pack | Live now |
| Codex | `codex-skill-pack.zip + codex.config.toml` | `agentic-design-blueprint.json` | MCP + skill (.agents/skills/) + local exports | Live now |
| Cursor | `cursor-rule-pack.zip` | `agentic-design-principles.mdc` | Rule pack (rules + MCP config), MCP optional | Live now |
| Windsurf | `blueprint-core.md` | `AGENTS.md` | MCP optional, workspace rule first | Live now |
| GitHub Copilot | `copilot-instructions.md` | `AGENTS.md` | MCP optional, repo instructions first | Live now |
| Gemini CLI | `gemini-skill-pack.zip + GEMINI.md` | `llms.txt` | Skill (.agents/skills/) + GEMINI.md + MCP optional | Live now |
| DeepSeek | `system-prompt-deepseek.md` | `llms.txt` | Static prompt pack | Live now |
| Qwen Code | `qwen-skill-pack.zip + system-prompt-qwen.md` | `agentic-design-blueprint.json` | Skill (.qwen/skills/) + MCP optional | Live now |
| OpenAI / GPT actions | `setup-openai-actions.md` | `agentic-design-blueprint.json` | OpenAPI deferred until public schema routes exist | Deferred |
| Continue / Cline / RooCode / Aider | `AGENTS.md` | `llms.txt` | Shared-file path first | Next phase |

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

## Public signal MCP tools (write, opt-in)

- `signals.report(event_type, surface_used?, brief_context?, perceived_value?, workflow_stage?, would_recommend?, team_size?)`
- `signals.feedback(task_type?, surface?, rating_clarity?, rating_usefulness?, what_helped?, what_missing?, would_use_again?, contact_email?, permission_to_follow_up?)`

## Protected tools not part of the anonymous setup path

- `me.learning_path()`
- `me.coaching_context()`
- `me.add_evidence(course_slug, stage_id, note)`
- `me.validation_history(repository?, run_id?, limit?)`
- `architect.validate(implementation_context, focus_area?, task?, language?, repository?, files?, goals?, example_limit?)`
- `team.summarize(days_back?)`
- `handoffs.operator(...)`
- `handoffs.partnership(...)`
- `handoffs.agency(...)`
