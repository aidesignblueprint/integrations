# Publishing Rules

## Canonical URL rule

Public files in this repo must point only to:

- `https://aidesignblueprint.com`
- `https://aidesignblueprint.com/mcp`

Do not publish files here that point to:

- `localhost`
- `127.0.0.1`
- `0.0.0.0`
- `*.run.app`
- raw backend service URLs

## Contract rule

This repo mirrors the live public contract. Do not publish:

- non-existent routes
- future/private tools as if they are public
- setup paths that differ from the site

## Scope rule

This repo is for:

- public read-only MCP setup
- shared doctrine files
- provider setup docs
- static prompt packs
- structured public exports

This repo is not for:

- admin tools
- private overlays
- sandbox-only URLs
- internal deployment topology

## Release rule

Before publishing:

1. verify the live public endpoint descriptor at `/mcp`
2. verify the setup files still point to the canonical public URLs
3. verify the first proof calls still work:
   - `list_clusters()`
   - `search_examples(query="orchestration visibility steering", limit=3)`
