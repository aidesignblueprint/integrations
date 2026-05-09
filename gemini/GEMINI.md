# AI Design Blueprint — Gemini Context

Use this file as persistent project context for Gemini CLI when working on AI-native systems.

## Core behavior

- prefer delegation before autonomous execution,
- require explicit approval for risky actions,
- surface runtime state clearly,
- preserve reversibility,
- use deterministic fallback paths,
- keep execution boundaries explicit,
- prefer structured outputs and typed data,
- optimize for production readiness.

## Setup

- Keep this file at project root as `GEMINI.md`.
- Install `gemini-skill-pack.zip` for the always-on Agent Skill: unzip into project root or `~` — installs `.agents/skills/agentic-design-blueprint/SKILL.md`.
- Keep `llms.txt` nearby as the lightweight discovery companion.
- Use the MCP endpoint only when you want live doctrine retrieval.

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

## Public feedback MCP tool (opt-in, anonymous-allowed)

- `signals.feedback(task_type?, surface?, rating_clarity?, rating_usefulness?, what_helped?, what_missing?, would_use_again?, contact_email?, permission_to_follow_up?)`

Only call signal tools after explicit user confirmation. Never call silently.
