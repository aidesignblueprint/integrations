# AI Design Blueprint Integrations

Official integrations and installable doctrine for AI Design Blueprint across MCP, IDE rules, prompt files, and agent runtimes.

## What is in this repo

- `shared/`: cross-tool doctrine files
- `mcp/`: public read-only MCP configuration and usage notes
- `docs/setup/`: copy-first setup guides by tool
- `cursor/`, `windsurf/`, `github-copilot/`, `gemini/`: provider-specific instruction files
- `open-weights/`: static prompt packs for open-weight and local model workflows
- `exports/`: structured doctrine export

## Public contract

Canonical public endpoints:

- Site: `https://aidesignblueprint.com`
- MCP: `https://aidesignblueprint.com/mcp`
- Developer docs: `https://aidesignblueprint.com/en/for-agents`

The public MCP tier is:

- read-only
- safe for discovery
- intended for doctrine and example retrieval

## Quick start

1. Pick a setup guide in `docs/setup/`.
2. Add the relevant file or MCP config to your own repository or client.
3. If using MCP, initialize against `https://aidesignblueprint.com/mcp`.
4. Run the first proof call:
   - `list_clusters()`
5. Then run a second proof call:
   - `search_examples(query="orchestration visibility steering", limit=3)`

## Public read-only MCP tools

- `list_principles(cluster?)`
- `list_clusters()`
- `get_principle(slug)`
- `get_cluster(slug)`
- `get_example(slug)`
- `search_principles(query, limit?)`
- `search_examples(query, principle_ids?, difficulty?, library?, limit?)`
- `list_agent_assets()`

Protected tools exist, but they are not part of the anonymous setup path.

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
