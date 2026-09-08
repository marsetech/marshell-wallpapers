from pathlib import Path

from PIL import Image, ImageOps

from scripts.libs.assets import (
    is_supported_asset,
)
from scripts.libs.paths import (
    COLLECTIONS_ROOT,
)

PREVIEW_SIZE = 640
PREVIEW_QUALITY = 80


def generate_preview(
    source: Path,
    destination: Path,
) -> None:
    destination.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with Image.open(source) as image:
        if (
            getattr(
                image,
                "n_frames",
                1,
            )
            > 1
        ):
            image.seek(0)

        image = ImageOps.exif_transpose(image)

        image = image.convert("RGB")

        image.thumbnail(
            (
                PREVIEW_SIZE,
                PREVIEW_SIZE,
            ),
            Image.Resampling.LANCZOS,
        )

        image.save(
            destination,
            "WEBP",
            quality=PREVIEW_QUALITY,
            method=6,
        )


def generate_collection_previews(
    collection: Path,
) -> None:
    assets_directory = collection / "assets"

    previews_directory = collection / "previews"

    if not assets_directory.is_dir():
        return

    for asset in sorted(assets_directory.iterdir()):
        if not is_supported_asset(asset):
            continue

        preview = previews_directory / f"{asset.stem}.webp"

        generate_preview(
            asset,
            preview,
        )

        print(f"Generated: {preview.relative_to(COLLECTIONS_ROOT.parent)}")


def main() -> None:
    for category in sorted(COLLECTIONS_ROOT.iterdir()):
        if not category.is_dir():
            continue

        for collection in sorted(category.iterdir()):
            if not collection.is_dir():
                continue

            generate_collection_previews(collection)


if __name__ == "__main__":
    main()
