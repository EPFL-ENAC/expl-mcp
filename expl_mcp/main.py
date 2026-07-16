import json
from pathlib import Path

import httpx
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


aree_api_client = httpx.AsyncClient(
    base_url=config.AREE_API_URL,
    auth=(config.AREE_API_USERNAME, config.AREE_API_PASSWORD),
)

spec_path = Path(__file__).with_name("openapi.json")
spec = json.loads(spec_path.read_text())

mcp = FastMCP.from_openapi(
    openapi_spec=spec,
    client=aree_api_client,
    name="EXPL",
    # instructions="Provides an interface the EXPL unit's MSSQL database and AREE API.",
    instructions="Provides an interface the EXPL unit's AREE API.",
    auth=auth,
)

if __name__ == "__main__":
    mcp.run()


def main() -> None:
    mcp.run(transport="http", port=8000)
