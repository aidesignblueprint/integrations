"""Stdio proxy to the AI Design Blueprint remote MCP server."""
import asyncio

from mcp.client.session import ClientSession
from mcp.client.streamable_http import streamablehttp_client
from mcp.server import Server
from mcp.server.stdio import stdio_server
import mcp.types as types

REMOTE_URL = "https://aidesignblueprint.com/mcp"


async def run() -> None:
    app = Server("ai-design-blueprint")

    async with streamablehttp_client(REMOTE_URL) as (r, w, _):
        async with ClientSession(r, w) as client:
            await client.initialize()
            remote_tools = (await client.list_tools()).tools

            @app.list_tools()
            async def _list_tools() -> list[types.Tool]:
                # Strip outputSchema: this proxy returns text content only.
                # Advertising outputSchema without returning structuredContent
                # causes MCP Inspector validation errors.
                return [
                    types.Tool(
                        name=t.name,
                        description=t.description,
                        inputSchema=t.inputSchema,
                        annotations=getattr(t, "annotations", None),
                    )
                    for t in remote_tools
                ]

            @app.call_tool()
            async def _call_tool(
                name: str, arguments: dict
            ) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
                result = await client.call_tool(name, arguments or {})
                return result.content

            async with stdio_server() as (stdin, stdout):
                await app.run(stdin, stdout, app.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(run())
