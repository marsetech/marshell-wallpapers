import json
from datetime import datetime
from pathlib import Path

WALLPAPER_ROOT = Path("collections")
OUTPUT_ROOT = Path("metadata/collections")

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}


def get_image_metadata(image: Path, category: Path):

    stat = image.stat()
    relative_path = image.relative_to(category)

    return {
        "filename": image.name,
        "title": image.stem.replace("-", " ").title(),
        "path": str(Path("wallpapers") / category.name / relative_path),
        "extension": image.suffix.replace(".", ""),
        "size_bytes": stat.st_size,
        "modified_at": datetime.fromtimestamp(stat.st_mtime).isoformat(),
    }


def get_image_files(category: Path):

    if category.name == "anime":
        # collections/anime/{collection}/assets/*
        assets_dirs = [
            folder / "assets"
            for folder in category.iterdir()
            if folder.is_dir() and (folder / "assets").is_dir()
        ]
    else:
        # collections/{category}/assets/*
        assets_dir = category / "assets"

        if not assets_dir.is_dir():
            return []

        assets_dirs = [assets_dir]

    images = []

    for assets_dir in assets_dirs:
        for image in sorted(assets_dir.iterdir()):
            if not image.is_file():
                continue

            if image.suffix.lower() not in IMAGE_EXTENSIONS:
                continue

            images.append(image)

    return images


def generate_collection(category: Path):

    wallpapers = {}

    for image in get_image_files(category):
        relative_key = str(image.relative_to(category))

        wallpapers[relative_key] = get_image_metadata(
            image,
            category,
        )

    data = {
        "category": category.name,
        "generated_at": datetime.now().isoformat(),
        "total": len(wallpapers),
        "wallpapers": wallpapers,
    }

    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)

    output = OUTPUT_ROOT / f"{category.name}.json"

    output.write_text(
        json.dumps(data, indent=4, ensure_ascii=False),
        encoding="utf-8",
    )


def main():

    for category in WALLPAPER_ROOT.iterdir():
        if category.is_dir():
            generate_collection(category)


if __name__ == "__main__":
    main()
