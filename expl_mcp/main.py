from fastmcp import FastMCP
from fastmcp.server.auth.providers.jwt import StaticTokenVerifier

from expl_mcp.config import config


auth = StaticTokenVerifier(
    tokens={
        config.MCP_API_KEY: {
            "client_id": "expl-mcp-client",
            "scopes": [],
        },
    },
)


mcp = FastMCP(
    "EXPL",
    instructions="Provides an interface the EXPL unit's MSSQL database and AREE API.",
    auth=auth,
)


@mcp.tool
def greet(name: str) -> str:
    """Say hello."""

    return f"Hello, {name}!"


def main() -> None:
    mcp.run(transport="http", port=8000)


if __name__ == "__main__":
    main()
