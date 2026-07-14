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

## Public feedback MCP tool (write, opt-in)

- `signals.feedback(task_type?, surface?, rating_clarity?, rating_usefulness?, what_helped?, what_missing?, would_use_again?, contact_email?, permission_to_follow_up?)`

## Protected tools not part of the anonymous setup path

- `me.learning_path()`
- `me.coaching_context()`
- `me.add_evidence(course_slug, stage_id, note)`
- `me.validation_history(repository?, run_id?, limit?)`
- `me.sessions(session_id?)`
- `me.session_event(session_id, event_type, actor, summary). GEP-M6 team mode: append a typed team event (handoff | pushback | plan_preview | gate | ack; actor pm | engineer | designer | system) to a Governed Session's timeline. ack = the IDE agent confirms it started working on a steer (post FIRST, then execute, then handoff). Steers and actor 'human' are cockpit-only (posted from the Studio session surface; agents receive steers via me.await_steer) — refused on this channel so timeline provenance stays trustworthy. Requires team_agents enabled on the session; refused on standalone sessions.`
- `me.await_steer(session_id, after_event_id?, timeout_s?). Long-poll for the next cockpit steer on a team-mode Governed Session: blocks server-side and returns the steer the moment the owner posts it, or timed_out with your cursor. Cursor-based at-least-once delivery (pass the highest event id you have seen; a lost response is safely re-issuable). timeout_s clamps to 5-240, default 45; waits above 45s require the per-server timeout raised in the MCP client config (see the pack SETTINGS).`
- `signals.report(event_type, surface_used?, brief_context?, perceived_value?, workflow_stage?, would_recommend?, team_size?)`
- `architect.validate(implementation_context, focus_area?, task?, language?, repository?, files?, goals?, example_limit?, private_session?, session_id?) — Tasks-augmented invocation supported (MCP 2025-11-25, SEP-1686): clients that advertise the `tasks` capability can include `task: {ttl: <ms>}` in request params to receive a CreateTaskResult immediately and poll via tasks/get + tasks/result; sync clients work unchanged. Scope note: only architect.validate task-augments in this release; architect.validate_consensus and architect.certify are sync-only today and extend to task augmentation in the next release. Use me.validation_history(run_id=...) recovery for the sync tools.`
- `architect.validate_consensus(implementation_context, n?, focus_area?, task?, language?, repository?, files?, goals?, example_limit?)`
- `design.validate(implementation_context, task?, goals?, files?, repository?, private_session?, session_id?). Surface-craft mirror of architect.validate: grades a frontend artefact against the 8 experience-design laws, own weekly quota bucket, sync-only (recover timeouts via me.validation_history(run_id=...)). Sends the artefact to OpenAI for processing (no-training; retained under OpenAI's API data-retention terms), same egress path as architect.validate.`
- `spec.validate(implementation_context, task?, goals?, files?, repository?, private_session?, session_id?). The what-to-build lens: grades a WRITTEN SPEC (proposal, design doc, tasks, or an OpenSpec-style change) against the 8 spec-quality laws BEFORE code exists, own weekly quota bucket, sync-only (recover timeouts via me.validation_history(run_id=...)). Sends the spec to OpenAI for processing (no-training; retained under OpenAI's API data-retention terms), same egress path as the sibling validators.`
- `architect.certify(run_id, code)`
- `team.summarize(days_back?)`
- `handoffs.operator(...)`
- `handoffs.partnership(...)`
- `handoffs.agency(...)`
