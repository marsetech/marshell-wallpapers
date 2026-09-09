from scripts.libs.metadata import (
    load_json,
    write_json,
)
from scripts.libs.paths import (
    GENERATED_METADATA_ROOT,
    MANUAL_METADATA_ROOT,
)

OPTIONAL_FIELDS = (
    "characters",
    "scenes",
    "environments",
)


def merge_asset(
    generated: dict,
    manual: dict,
) -> dict:
    result = dict(generated)

    result["title"] = manual["title"]
    result["description"] = manual["description"]

    for field in OPTIONAL_FIELDS:
        result[field] = manual.get(
            field,
            [],
        )

    return result


def main() -> None:
    generated_root = GENERATED_METADATA_ROOT / "collections"

    for generated_file in generated_root.rglob("*.json"):
        generated = load_json(generated_file)

        category = generated["category"]
        collection = generated["collection"]

        manual_file = (
            MANUAL_METADATA_ROOT / "collections" / category / collection / "assets.json"
        )

        manual = load_json(
            manual_file,
            {"assets": {}},
        )

        merged_assets = {}

        for asset_id, generated_asset in generated.get(
            "assets",
            {},
        ).items():
            manual_asset = manual.get(
                "assets",
                {},
            ).get(asset_id)

            if manual_asset is None:
                continue

            merged_assets[asset_id] = merge_asset(
                generated_asset,
                manual_asset,
            )

        output = GENERATED_METADATA_ROOT / "merged" / category / f"{collection}.json"

        write_json(
            output,
            {
                "schema_version": 1,
                "category": category,
                "collection": collection,
                "generated_at": generated.get("generated_at"),
                "total": len(merged_assets),
                "assets": merged_assets,
            },
        )

        print(f"Merged: {output}")


if __name__ == "__main__":
    main()
