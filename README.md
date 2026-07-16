# EXPL MCP server

_MCP (Model Context Protocol) server for EXPL MSSQL database and AREE API._


## Requirements

- [uv](https://docs.astral.sh/uv/getting-started/installation/) Python package and project manager
- Make


## Deploying locally

Setup your environment by running:

```bash
make install
```


### Server

Run:

```bash
make run
```

The MCP server will run at [http://localhost:8000/mcp](http://localhost:8000/mcp).

Tools definition rely on http://aree.epfl.ch/AREEService/doc/swagger.json. The servers needs an OpenAPI specifiction. To regenerate it, run:

```bash
make generate-openapi-json
```

which will write to `expl_mcp/openapi.json`.
