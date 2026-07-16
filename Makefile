env_path=.env

install:
	uv sync --python 3.13
	uv pip install -e .
	test -f .env || cp .env.example .env

run:
	uv run dotenv -f "$(env_path)" run fastmcp run expl_mcp/main.py:mcp --transport http --port 8000 --reload

test:
	uv run dotenv -f "$(env_path)" run pytest

typecheck:
	uvx lefthook run pre-commit --command backend-typecheck --all-files

lint:
	uvx lefthook run pre-commit --command backend-lint --all-files

format:
	uvx lefthook run pre-commit --command backend-format --all-files

generate-openapi-json:
	uv run python scripts/generate_openapi_json.py
