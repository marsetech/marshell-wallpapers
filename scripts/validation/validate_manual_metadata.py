import sys

from scripts.libs.metadata import load_json
from scripts.libs.paths import (
    MANUAL_METADATA_ROOT,
)

REQUIRED_FIELDS = ("description",)

OPTIONAL_FIELDS = (
    "characters",
    "scenes",
    "environments",
)


def main() -> None:
    errors = []

    root = MANUAL_METADATA_ROOT / "collections"

    for file in root.rglob("assets.json"):
        data = load_json(file)

        for asset_id, asset in data.get(
            "assets",
            {},
        ).items():
            for field in REQUIRED_FIELDS:
                value = asset.get(field)

                if not isinstance(
                    value,
                    str,
                ):
                    errors.append(f"{file}: {asset_id}: '{field}' is required")

                elif not value.strip():
                    errors.append(f"{file}: {asset_id}: '{field}' cannot be empty")

            for field in OPTIONAL_FIELDS:
                if field not in asset:
                    continue

                if not isinstance(
                    asset[field],
                    list,
                ):
                    errors.append(f"{file}: {asset_id}: '{field}' must be an array")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")

        sys.exit(1)

    print("Manual metadata validation passed.")


if __name__ == "__main__":
    main()
