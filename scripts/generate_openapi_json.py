"""Fetch AREE's Swagger 2.0 spec and convert it to OpenAPI 3.x via converter.swagger.io."""

import json
import urllib.request

SWAGGER_URL = "http://aree.epfl.ch/AREEService/doc/swagger.json"
CONVERTER_URL = "https://converter.swagger.io/api/convert"
OUTPUT_PATH = "expl_mcp/openapi.json"


def main() -> None:
    print(f"Fetching {SWAGGER_URL} ...")
    with urllib.request.urlopen(SWAGGER_URL) as resp:
        swagger_data = resp.read()

    print(f"Posting to {CONVERTER_URL} ...")
    req = urllib.request.Request(
        CONVERTER_URL,
        data=swagger_data,
        headers={
            "accept": "application/json",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req) as resp:
        openapi_data = resp.read()

    parsed = json.loads(openapi_data)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(parsed, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Wrote OpenAPI spec to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
