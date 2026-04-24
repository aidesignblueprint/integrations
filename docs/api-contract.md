# API Contract

## Current public contract

The public integration contract is:

- MCP at `https://aidesignblueprint.com/mcp`
- static downloadable assets

## What is public today

Public retrieval MCP tools:

- `principles.list`
- `clusters.list`
- `principles.get`
- `clusters.get`
- `examples.get`
- `principles.search`
- `examples.search`
- `assets.list`
- `guides.list`
- `guides.get`
- `guides.search`

Public signal MCP tools:

- `signals.report`
- `signals.feedback`

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
