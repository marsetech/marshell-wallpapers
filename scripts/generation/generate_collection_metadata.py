from datetime import datetime, timezone

from scripts.libs.assets import (
    get_image_metadata,
    is_supported_asset,
)
from scripts.libs.metadata import write_json
from scripts.libs.paths import (
    COLLECTIONS_ROOT,
    GENERATED_METADATA_ROOT,
)


def generate_asset_metadata(
    image,
) -> dict:
    metadata = get_image_metadata(image)

    return {
        "id": image.stem,
        "filename": image.name,
        "path": str(image.relative_to(COLLECTIONS_ROOT)),
        **metadata,
        "modified_at": datetime.fromtimestamp(
            image.stat().st_mtime,
            tz=timezone.utc,
        ).isoformat(),
    }


def generate_collection(
    category,
    collection,
) -> dict:
    assets = {}

    asset_directory = collection / "assets"

    if asset_directory.exists():
        for image in sorted(asset_directory.rglob("*")):
            if not is_supported_asset(image):
                continue

            assets[image.stem] = generate_asset_metadata(image)

    return {
        "schema_version": 1,
        "category": category.name,
        "collection": collection.name,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total": len(assets),
        "assets": assets,
    }


def main() -> None:
    for category in sorted(COLLECTIONS_ROOT.iterdir()):
        if not category.is_dir():
            continue

        for collection in sorted(category.iterdir()):
            if not collection.is_dir():
                continue

            data = generate_collection(
                category,
                collection,
            )

            output = (
                GENERATED_METADATA_ROOT
                / "collections"
                / category.name
                / f"{collection.name}.json"
            )

            write_json(
                output,
                data,
            )

            print(f"Generated: {output}")


if __name__ == "__main__":
    main()
