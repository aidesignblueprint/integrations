# API Contract

## Current public contract

The public integration contract is:

- MCP at `https://aidesignblueprint.com/mcp`
- static downloadable assets

## What is public today

Public read-only MCP tools:

- `list_principles`
- `list_clusters`
- `get_principle`
- `get_cluster`
- `get_example`
- `search_principles`
- `search_examples`
- `list_agent_assets`

## What is not public yet

The following are not part of the anonymous public setup path:

- authenticated member tools
- pro validation tools
- handoff tools
- a stable public REST API
- an `openapi.json` contract

## OpenAPI status

Deferred.

Do not publish an OpenAPI schema until stable public HTTP routes exist and are intentionally supported for external consumers.
