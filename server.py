"""Stdio proxy to the AI Design Blueprint remote MCP server.

Preserves structured tool results end-to-end:
- `outputSchema` is forwarded from the remote tool descriptors so MCP clients
  see the same contract the upstream server advertises.
- Structured tool results (`structuredContent`) are propagated alongside text
  content, so downstream agents can rely on typed fields instead of re-parsing
  a JSON-string payload.

Rationale: this proxy used to strip both. That downgrade made the proxied tool
surface look text-only to MCP Inspector and to agents that consume
`structuredContent`, even though the upstream server advertises rich schemas
on every tool. Preserving the structure restores the inspection affordance
the upstream surface already supports.
"""
import asyncio

import mcp.types as types
from mcp.client.session import ClientSession
from mcp.client.streamable_http import streamablehttp_client
from mcp.server import Server
from mcp.server.stdio import stdio_server

REMOTE_URL = "https://aidesignblueprint.com/mcp"


async def run() -> None:
    app = Server("ai-design-blueprint")

    async with streamablehttp_client(REMOTE_URL) as (r, w, _):
        async with ClientSession(r, w) as client:
            await client.initialize()
            remote_tools = (await client.list_tools()).tools

            @app.list_tools()
            async def _list_tools() -> list[types.Tool]:
                # Forward the upstream descriptor verbatim — including
                # outputSchema — so clients see the same contract the
                # remote server advertises.
                return [
                    types.Tool(
                        name=t.name,
                        description=t.description,
                        inputSchema=t.inputSchema,
                        outputSchema=getattr(t, "outputSchema", None),
                        annotations=getattr(t, "annotations", None),
                    )
                    for t in remote_tools
                ]

            @app.call_tool()
            async def _call_tool(
                name: str, arguments: dict
            ) -> (
                tuple[
                    list[
                        types.TextContent
                        | types.ImageContent
                        | types.EmbeddedResource
                    ],
                    dict,
                ]
                | list[
                    types.TextContent
                    | types.ImageContent
                    | types.EmbeddedResource
                ]
            ):
                result = await client.call_tool(name, arguments or {})
                structured = getattr(result, "structuredContent", None)
                # Return the tuple form when the upstream produced a
                # structured payload, so the MCP server emits both
                # `content` (for humans) and `structuredContent` (for
                # agents and Inspector validation against outputSchema).
                if structured is not None:
                    return result.content, structured
                return result.content

            async with stdio_server() as (stdin, stdout):
                await app.run(stdin, stdout, app.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(run())
