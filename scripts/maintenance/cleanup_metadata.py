from scripts.libs.assets import (
    is_supported_asset,
)
from scripts.libs.metadata import (
    load_json,
    write_json,
)
from scripts.libs.paths import (
    COLLECTIONS_ROOT,
    MANUAL_METADATA_ROOT,
)


def main() -> None:
    root = MANUAL_METADATA_ROOT / "collections"

    for file in root.rglob("assets.json"):
        relative = file.relative_to(root)

        if len(relative.parts) < 2:
            continue

        category = relative.parts[0]
        collection = relative.parts[1]

        asset_directory = COLLECTIONS_ROOT / category / collection / "assets"

        if not asset_directory.exists():
            continue

        data = load_json(file)

        assets = data.get(
            "assets",
            {},
        )

        existing_ids = {
            asset.stem
            for asset in asset_directory.rglob("*")
            if is_supported_asset(asset)
        }

        stale_ids = set(assets) - existing_ids

        for asset_id in sorted(stale_ids):
            print(f"Removing stale metadata: {asset_id}")

            del assets[asset_id]

        write_json(
            file,
            data,
        )


if __name__ == "__main__":
    main()
