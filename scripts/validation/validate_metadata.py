import sys

from scripts.libs.metadata import load_json
from scripts.libs.paths import (
    GENERATED_METADATA_ROOT,
    MANUAL_METADATA_ROOT,
)


def main() -> None:
    errors = []

    generated_root = GENERATED_METADATA_ROOT / "collections"

    for generated_file in generated_root.rglob("*.json"):
        generated = load_json(generated_file)

        category = generated.get("category")

        collection = generated.get("collection")

        if not category or not collection:
            errors.append(f"{generated_file}: missing category or collection")

            continue

        manual_file = (
            MANUAL_METADATA_ROOT / "collections" / category / collection / "assets.json"
        )

        manual = load_json(
            manual_file,
            {"assets": {}},
        )

        generated_assets = set(
            generated.get(
                "assets",
                {},
            )
        )

        manual_assets = set(
            manual.get(
                "assets",
                {},
            )
        )

        missing_manual = generated_assets - manual_assets

        stale_manual = manual_assets - generated_assets

        for asset_id in sorted(missing_manual):
            errors.append(f"{manual_file}: missing metadata for {asset_id}")

        for asset_id in sorted(stale_manual):
            errors.append(f"{manual_file}: stale metadata for {asset_id}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")

        sys.exit(1)

    print("Metadata consistency validation passed.")


if __name__ == "__main__":
    main()
