from scripts.libs.metadata import (
    load_json,
    write_json,
)
from scripts.libs.paths import (
    GENERATED_METADATA_ROOT,
    MANUAL_METADATA_ROOT,
)


def create_asset_template() -> dict:
    return {
        "description": "",
        "characters": [],
        "scenes": [],
        "environments": [],
    }


def synchronize_collection(
    generated_file,
) -> None:
    generated = load_json(generated_file)

    category = generated["category"]
    collection = generated["collection"]

    manual_file = (
        MANUAL_METADATA_ROOT / "collections" / category / collection / "assets.json"
    )

    manual = load_json(
        manual_file,
        {
            "assets": {},
        },
    )

    assets = manual.setdefault(
        "assets",
        {},
    )

    changed = False

    for asset_id in generated.get(
        "assets",
        {},
    ):
        if asset_id in assets:
            continue

        assets[asset_id] = create_asset_template()

        changed = True

        print(f"Created manual metadata entry: {category}/{collection}/{asset_id}")

    if changed or not manual_file.exists():
        write_json(
            manual_file,
            manual,
        )


def main() -> None:
    generated_root = GENERATED_METADATA_ROOT / "collections"

    for generated_file in sorted(generated_root.rglob("*.json")):
        synchronize_collection(generated_file)

    print("Manual metadata synchronized.")


if __name__ == "__main__":
    main()
