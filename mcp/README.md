# MCP Setup

Use the public read-only MCP endpoint:

```json
{
  "aidesignblueprint": {
    "type": "http",
    "url": "https://aidesignblueprint.com/mcp"
  }
}
```

## Expected initialize payload

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "initialize",
  "params": {
    "protocolVersion": "2025-03-26",
    "capabilities": {},
    "clientInfo": {
      "name": "manual-check",
      "version": "1.0.0"
    }
  }
}
```

## First proof calls

1. `list_clusters()`
2. `search_examples(query="orchestration visibility steering", limit=3)`

The public MCP tier is intended for doctrine retrieval and implementation discovery.
