import re
import sys

from scripts.libs.assets import (
    is_supported_asset,
)
from scripts.libs.paths import (
    COLLECTIONS_ROOT,
)

ASSET_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*-\d{6}$")


def main() -> None:
    errors = []

    for category in sorted(COLLECTIONS_ROOT.iterdir()):
        if not category.is_dir():
            continue

        for collection in sorted(category.iterdir()):
            if not collection.is_dir():
                continue

            asset_directory = collection / "assets"

            if not asset_directory.exists():
                continue

            prefix = f"{collection.name}-"

            for asset in sorted(asset_directory.rglob("*")):
                if not is_supported_asset(asset):
                    continue

                if not asset.stem.startswith(prefix):
                    errors.append(f"{asset}: invalid collection prefix")

                if not ASSET_PATTERN.match(asset.stem):
                    errors.append(f"{asset}: invalid filename convention")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")

        sys.exit(1)

    print("Asset validation passed.")


if __name__ == "__main__":
    main()
