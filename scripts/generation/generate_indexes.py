from scripts.libs.metadata import (
    load_json,
    write_json,
)
from scripts.libs.paths import (
    GENERATED_METADATA_ROOT,
    INDEXES_ROOT,
)


def main() -> None:
    assets_index = {}
    collections_index = {}
    categories_index = {}

    merged_root = GENERATED_METADATA_ROOT / "merged"

    for file in sorted(merged_root.rglob("*.json")):
        data = load_json(file)

        category = data["category"]
        collection = data["collection"]

        category_entry = categories_index.setdefault(
            category,
            {
                "category": category,
                "collections": [],
            },
        )

        if collection not in category_entry["collections"]:
            category_entry["collections"].append(collection)

        collection_key = f"{category}/{collection}"

        collections_index[collection_key] = {
            "category": category,
            "collection": collection,
            "total": data.get(
                "total",
                0,
            ),
        }

        for asset_id, asset in data.get(
            "assets",
            {},
        ).items():
            assets_index[asset_id] = {
                "category": category,
                "collection": collection,
                "path": asset["path"],
            }

    write_json(
        INDEXES_ROOT / "assets.json",
        {
            "schema_version": 1,
            "assets": assets_index,
        },
    )

    write_json(
        INDEXES_ROOT / "collections.json",
        {
            "schema_version": 1,
            "collections": collections_index,
        },
    )

    write_json(
        INDEXES_ROOT / "categories.json",
        {
            "schema_version": 1,
            "categories": categories_index,
        },
    )

    print("Generated metadata indexes.")


if __name__ == "__main__":
    main()
