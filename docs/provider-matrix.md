# AI Design Blueprint — Provider Matrix

Use this matrix to pick the smallest truthful setup for each tool or runtime.

| Tool | Primary asset | Optional companion | Retrieval path | Status |
| --- | --- | --- | --- | --- |
| Claude Code | `claude-skill-pack.zip + claude-code.mcp.json` | `agent-kickoff-prompts.md` | MCP + skill + local prompt pack | Live now |
| Codex | `AGENTS.md + agentic-design-blueprint.json` | `llms.txt` | MCP optional, static exports first | Live now |
| Cursor | `agentic-design-principles.mdc` | `llms.txt` | MCP optional, .mdc first | Live now |
| Windsurf | `blueprint-core.md` | `AGENTS.md` | MCP optional, workspace rule first | Live now |
| GitHub Copilot | `copilot-instructions.md` | `AGENTS.md` | MCP optional, repo instructions first | Live now |
| Gemini CLI | `GEMINI.md` | `llms.txt` | MCP optional, project context first | Live now |
| DeepSeek | `system-prompt-deepseek.md` | `llms.txt` | Static prompt pack | Live now |
| Qwen | `system-prompt-qwen.md` | `llms.txt` | Static prompt pack | Live now |
| OpenAI / GPT actions | `setup-openai-actions.md` | `agentic-design-blueprint.json` | OpenAPI deferred until public schema routes exist | Deferred |
| Continue / Cline / RooCode / Aider | `AGENTS.md` | `llms.txt` | Shared-file path first | Next phase |

## Public read-only MCP tools

- `list_principles(cluster?)`
- `list_clusters()`
- `get_principle(slug)`
- `get_cluster(slug)`
- `get_example(slug)`
- `search_principles(query, limit?)`
- `search_examples(query, principle_ids?, difficulty?, library?, limit?)`
- `list_agent_assets()`

## Protected tools not part of the anonymous setup path

- `get_my_learning_path()`
- `get_my_coaching_context()`
- `validate_agent_architecture(implementation_context, focus_area?, task?, language?, repository?, files?, goals?, example_limit?)`
- `add_evidence_note(course_slug, stage_id, note)`
