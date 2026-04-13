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
- Keep `llms.txt` nearby as the lightweight discovery companion.
- Use the MCP endpoint only when you want live doctrine retrieval.

## Public MCP tools worth using

- `list_principles(cluster?)`
- `list_clusters()`
- `get_principle(slug)`
- `get_cluster(slug)`
- `get_example(slug)`
- `search_principles(query, limit?)`
- `search_examples(query, principle_ids?, difficulty?, library?, limit?)`
- `list_agent_assets()`
