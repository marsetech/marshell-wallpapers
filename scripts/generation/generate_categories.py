from scripts.libs.metadata import write_json
from scripts.libs.paths import (
    COLLECTIONS_ROOT,
    GENERATED_METADATA_ROOT,
)


def main() -> None:
    categories = {}

    for category in sorted(COLLECTIONS_ROOT.iterdir()):
        if not category.is_dir():
            continue

        categories[category.name] = {
            "display_name": (category.name.replace("-", " ").title()),
        }

    output = GENERATED_METADATA_ROOT / "categories.json"

    write_json(
        output,
        {
            "schema_version": 1,
            "categories": categories,
        },
    )

    print(f"Generated: {output}")


if __name__ == "__main__":
    main()
