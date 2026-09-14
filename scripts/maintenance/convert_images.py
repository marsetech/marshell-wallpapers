from pathlib import Path
from shutil import copy2
from subprocess import run
from tempfile import TemporaryDirectory

from scripts.libs.assets import (
    get_webp_path,
    is_convertible_asset,
)
from scripts.libs.paths import COLLECTIONS_ROOT

WEBP_QUALITY = "90"


def find_convertible_assets() -> list[Path]:
    return sorted(
        path for path in COLLECTIONS_ROOT.rglob("*") if is_convertible_asset(path)
    )


def convert_asset(
    source: Path,
    destination: Path,
) -> None:
    destination.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    run(
        [
            "magick",
            str(source),
            "-quality",
            WEBP_QUALITY,
            str(destination),
        ],
        check=True,
    )


def convert_assets(
    assets: list[Path],
    temporary_root: Path,
) -> None:
    for source in assets:
        relative_path = source.relative_to(
            COLLECTIONS_ROOT,
        )

        destination = temporary_root / get_webp_path(
            relative_path,
        )

        print(f"    {relative_path} → {destination.relative_to(temporary_root)}")

        convert_asset(
            source,
            destination,
        )


def replace_originals(
    assets: list[Path],
    temporary_root: Path,
) -> None:
    for source in assets:
        source.unlink()

    for converted in temporary_root.rglob("*.webp"):
        relative_path = converted.relative_to(
            temporary_root,
        )

        destination = COLLECTIONS_ROOT / relative_path

        destination.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        copy2(
            converted,
            destination,
        )


def main() -> None:
    assets = find_convertible_assets()

    print("==> Image conversion")
    print(f"    Found {len(assets)} convertible assets.")

    if not assets:
        print("    Nothing to convert.")
        return

    with TemporaryDirectory(
        prefix=".image-conversion-",
    ) as temporary_directory:
        temporary_root = Path(temporary_directory)

        convert_assets(
            assets,
            temporary_root,
        )

        replace_originals(
            assets,
            temporary_root,
        )

    print("    Image conversion completed successfully.")


if __name__ == "__main__":
    main()
