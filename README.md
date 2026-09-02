# EXPL MCP server

_MCP (Model Context Protocol) server for EXPL's AREE API._


## Requirements

- [uv](https://docs.astral.sh/uv/getting-started/installation/) Python package and project manager
- Make


## Update

Tools definition rely on http://aree.epfl.ch/AREEService/doc/swagger.json. This MCP server needs an OpenAPI specification. To update/regenerate it, run:

```bash
make generate-openapi-json
```

which will write to `expl_mcp/openapi.json` based on the upstream `swagger.json`.

Adding a Git tag or pushing to the `dev` branch will update the deployments at https://expl-mcp.epfl.ch/ and https://expl-mcp-dev.epfl.ch/, respectively.


## Deploying locally

Setup your environment by running:

```bash
make install
```

Edit the values in the `.env` file to configure the MCP API key and the connection to the AREE API.


### Server

Run:

```bash
make run
```

The MCP server will run at [http://localhost:8000/mcp](http://localhost:8000/mcp).
