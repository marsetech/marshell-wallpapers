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


def generate_collection(category: Path):

    wallpapers = {}

    # Cerca ricorsivamente tutte le immagini
    for image in sorted(category.rglob("*")):
        if not image.is_file():
            continue

        if image.suffix.lower() not in IMAGE_EXTENSIONS:
            continue

        relative_key = str(image.relative_to(category))

        wallpapers[relative_key] = get_image_metadata(image, category)

    data = {
        "category": category.name,
        "generated_at": datetime.now().isoformat(),
        "total": len(wallpapers),
        "wallpapers": wallpapers,
    }

    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)

    output = OUTPUT_ROOT / f"{category.name}.json"

    output.write_text(json.dumps(data, indent=4, ensure_ascii=False), encoding="utf-8")


def main():

    for category in WALLPAPER_ROOT.iterdir():
        if category.is_dir():
            generate_collection(category)


if __name__ == "__main__":
    main()
