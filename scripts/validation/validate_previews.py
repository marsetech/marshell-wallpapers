import sys

from scripts.libs.assets import (
    is_supported_asset,
)
from scripts.libs.paths import (
    COLLECTIONS_ROOT,
)


def main() -> None:
    errors = []

    for category in sorted(
        COLLECTIONS_ROOT.iterdir()
    ):
        if not category.is_dir():
            continue

        for collection in sorted(
            category.iterdir()
        ):
            if not collection.is_dir():
                continue

            assets_dir = (
                collection / "assets"
            )

            previews_dir = (
                collection / "previews"
            )

            if not assets_dir.exists():
                continue

            asset_ids = {
                asset.stem
                for asset in assets_dir.rglob("*")
                if is_supported_asset(asset)
            }

            preview_ids = {
                preview.stem
                for preview in previews_dir.rglob(
                    "*.webp"
                )
            } if previews_dir.exists() else set()

            missing = (
                asset_ids - preview_ids
            )

            stale = (
                preview_ids - asset_ids
            )

            for asset_id in sorted(
                missing
            ):
                errors.append(
                    f"{collection}: missing "
                    f"preview for {asset_id}"
                )

            for preview_id in sorted(
                stale
            ):
                errors.append(
                    f"{collection}: stale "
                    f"preview for {preview_id}"
                )

    if errors:
        for error in errors:
            print(
                f"ERROR: {error}"
            )

        sys.exit(1)

    print(
        "Preview validation passed."
    )


if __name__ == "__main__":
    main()
