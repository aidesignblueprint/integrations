# AI Design Blueprint — Provider Matrix

Use this matrix to pick the smallest truthful setup for each tool or runtime.

| Tool | Primary asset | Optional companion | Retrieval path | Status |
| --- | --- | --- | --- | --- |
| Claude Code | `claude-skill-pack.zip + claude-code.mcp.json` | `agent-kickoff-prompts.md` | MCP + skill + local prompt pack | Live now |
| Codex | `codex.config.toml + agentic-design-blueprint.json` | `agentic-design-blueprint.md` | Codex CLI or config.toml + local exports | Live now |
| Cursor | `agentic-design-principles.mdc` | `llms.txt` | MCP optional, .mdc first | Live now |
| Windsurf | `blueprint-core.md` | `AGENTS.md` | MCP optional, workspace rule first | Live now |
| GitHub Copilot | `copilot-instructions.md` | `AGENTS.md` | MCP optional, repo instructions first | Live now |
| Gemini CLI | `GEMINI.md` | `llms.txt` | MCP optional, project context first | Live now |
| DeepSeek | `system-prompt-deepseek.md` | `llms.txt` | Static prompt pack | Live now |
| Qwen | `system-prompt-qwen.md` | `llms.txt` | Static prompt pack | Live now |
| OpenAI / GPT actions | `setup-openai-actions.md` | `agentic-design-blueprint.json` | OpenAPI deferred until public schema routes exist | Deferred |
| Continue / Cline / RooCode / Aider | `AGENTS.md` | `llms.txt` | Shared-file path first | Next phase |

## Public retrieval MCP tools

- `list_principles(cluster?)`
- `list_clusters()`
- `get_principle(slug)`
- `get_cluster(slug)`
- `get_example(slug)`
- `search_principles(query, limit?)`
- `search_examples(query, principle_ids?, difficulty?, library?, limit?)`
- `list_agent_assets()`
- `list_application_guides()`
- `get_application_guide(slug)`
- `search_application_guides(query, limit?)`

## Public signal MCP tools (write, opt-in)

- `report_value_event(event_type, surface_used?, brief_context?, perceived_value?, workflow_stage?, would_recommend?, team_size?)`
- `submit_feedback(task_type?, surface?, rating_clarity?, rating_usefulness?, what_helped?, what_missing?, would_use_again?, contact_email?, permission_to_follow_up?)`

## Protected tools not part of the anonymous setup path

- `get_my_learning_path()`
- `get_my_coaching_context()`
- `validate_agent_architecture(implementation_context, focus_area?, task?, language?, repository?, files?, goals?, example_limit?)`
- `add_evidence_note(course_slug, stage_id, note)`
