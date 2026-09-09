import re

from scripts.libs.assets import (
    is_supported_asset,
)
from scripts.libs.paths import (
    COLLECTIONS_ROOT,
)

ID_PATTERN = re.compile(r"^(?P<prefix>.+)-(?P<number>\d{6})$")


def get_used_ids(
    asset_directory,
    prefix,
):
    used = set()

    for asset in asset_directory.iterdir():
        if not is_supported_asset(asset):
            continue

        match = ID_PATTERN.match(asset.stem)

        if not match:
            continue

        if match.group("prefix") != prefix:
            continue

        used.add(int(match.group("number")))

    return used


def get_next_id(used):
    candidate = 1

    while candidate in used:
        candidate += 1

    return candidate


def normalize_collection(
    collection,
):
    asset_directory = collection / "assets"

    if not asset_directory.exists():
        return

    prefix = collection.name

    used_ids = get_used_ids(
        asset_directory,
        prefix,
    )

    invalid_assets = []

    for asset in sorted(asset_directory.iterdir()):
        if not is_supported_asset(asset):
            continue

        match = ID_PATTERN.match(asset.stem)

        if match and match.group("prefix") == prefix:
            continue

        invalid_assets.append(asset)

    for asset in invalid_assets:
        next_id = get_next_id(used_ids)

        new_name = f"{prefix}-{next_id:06d}{asset.suffix.lower()}"

        destination = asset_directory / new_name

        asset.rename(destination)

        used_ids.add(next_id)

        print(f"Renamed: {asset.name} -> {new_name}")


def main() -> None:
    for category in sorted(COLLECTIONS_ROOT.iterdir()):
        if not category.is_dir():
            continue

        for collection in sorted(category.iterdir()):
            if collection.is_dir():
                normalize_collection(collection)

    print("Filename normalization complete.")


if __name__ == "__main__":
    main()
