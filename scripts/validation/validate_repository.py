import sys

from scripts.libs.paths import (
    COLLECTIONS_ROOT,
    METADATA_ROOT,
    SCRIPTS_ROOT,
    TEMPLATES_ROOT,
)

REQUIRED_DIRECTORIES = (
    COLLECTIONS_ROOT,
    METADATA_ROOT,
    SCRIPTS_ROOT,
    TEMPLATES_ROOT,
)


def main() -> None:
    errors = []

    for directory in REQUIRED_DIRECTORIES:
        if not directory.is_dir():
            errors.append(f"Missing directory: {directory}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")

        sys.exit(1)

    print("Repository structure validation passed.")


if __name__ == "__main__":
    main()
