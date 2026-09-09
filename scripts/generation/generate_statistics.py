from scripts.libs.assets import (
    get_image_metadata,
    is_supported_asset,
)
from scripts.libs.metadata import write_json
from scripts.libs.paths import (
    COLLECTIONS_ROOT,
    GENERATED_METADATA_ROOT,
)


def main() -> None:
    categories = 0
    collections = 0
    assets = 0
    animated = 0
    total_size = 0

    formats = {}
    orientations = {}

    for category in sorted(COLLECTIONS_ROOT.iterdir()):
        if not category.is_dir():
            continue

        categories += 1

        for collection in sorted(category.iterdir()):
            if not collection.is_dir():
                continue

            collections += 1

            asset_directory = collection / "assets"

            if not asset_directory.exists():
                continue

            for asset in sorted(asset_directory.rglob("*")):
                if not is_supported_asset(asset):
                    continue

                metadata = get_image_metadata(asset)

                assets += 1
                total_size += metadata["size_bytes"]

                if metadata["animated"]:
                    animated += 1

                image_format = metadata["format"]

                formats[image_format] = (
                    formats.get(
                        image_format,
                        0,
                    )
                    + 1
                )

                orientation = metadata["orientation"]

                orientations[orientation] = (
                    orientations.get(
                        orientation,
                        0,
                    )
                    + 1
                )

    statistics = {
        "schema_version": 1,
        "categories": categories,
        "collections": collections,
        "assets": {
            "total": assets,
            "static": assets - animated,
            "animated": animated,
        },
        "storage": {
            "total_bytes": total_size,
        },
        "formats": dict(sorted(formats.items())),
        "orientations": dict(sorted(orientations.items())),
    }

    output = GENERATED_METADATA_ROOT / "statistics.json"

    write_json(
        output,
        statistics,
    )

    print(f"Generated: {output}")


if __name__ == "__main__":
    main()
