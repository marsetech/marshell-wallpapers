import json
from pathlib import Path

WALLPAPER_ROOT = Path("collections")
COLLECTIONS_ROOT = Path("metadata/collections")

CATEGORIES_FILE = Path("metadata/categories.json")
TEMPLATE_FILE = Path("templates/README_CATEGORY_WALLPAPERS.md")

IMAGE_WIDTH = 450
IMAGE_HEIGHT = 250

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}


def load_json(path: Path):

    return json.loads(path.read_text(encoding="utf-8"))


def generate_image(path: str, filename: str):

    return (
        f"<img "
        f'src="{path}" '
        f'alt="{filename}" '
        f'width="{IMAGE_WIDTH}" '
        f'height="{IMAGE_HEIGHT}" '
        f'style="object-fit: cover;">'
    )


def generate_grid(images):

    if not images:
        return ""

    rows = []

    for i in range(0, len(images), 2):
        pair = images[i : i + 2]

        if len(pair) == 2:
            rows.append(
                "<table>\n"
                "<tr>\n"
                f"<td>{pair[0]}</td>\n"
                f"<td>{pair[1]}</td>\n"
                "</tr>\n"
                "</table>"
            )

        else:
            rows.append(
                "<table>\n"
                "<tr>\n"
                "<td></td>\n"
                f"<td>{pair[0]}</td>\n"
                "<td></td>\n"
                "</tr>\n"
                "</table>"
            )

    return "\n\n".join(rows)


def generate_section(title, images):

    if not images:
        return ""

    content = ""

    if title:
        content += f"### {title}\n\n"

    content += generate_grid(images)
    content += "\n\n"

    return content


def get_images(directory: Path):

    if not directory.is_dir():
        return []

    return [
        file
        for file in sorted(directory.iterdir())
        if file.is_file() and file.suffix.lower() in IMAGE_EXTENSIONS
    ]


def build_gallery(category):

    category_path = WALLPAPER_ROOT / category

    # Categoria anime:
    #
    # collections/anime/{collection}/assets/*
    #
    if category == "anime":
        gallery = ""

        for collection_dir in sorted(category_path.iterdir()):
            if not collection_dir.is_dir():
                continue

            assets_dir = collection_dir / "assets"

            images = [
                generate_image(
                    str(file.relative_to(category_path)),
                    file.name,
                )
                for file in get_images(assets_dir)
            ]

            gallery += generate_section(
                collection_dir.name.replace("-", " ").title(),
                images,
            )

        return gallery

    # Tutte le altre categorie:
    #
    # collections/{category}/assets/*
    #
    assets_dir = category_path / "assets"

    images = [
        generate_image(
            str(file.relative_to(category_path)),
            file.name,
        )
        for file in get_images(assets_dir)
    ]

    return generate_section("", images)


def generate_readme(category):

    categories = load_json(CATEGORIES_FILE)

    collection_info = categories.get(category, {})

    template = TEMPLATE_FILE.read_text(encoding="utf-8")

    content = template.replace(
        "{{DISPLAY_NAME}}",
        collection_info.get(
            "display_name",
            category.title(),
        ),
    )

    content = content.replace(
        "{{DESCRIPTION}}",
        collection_info.get(
            "description",
            "",
        ),
    )

    content = content.replace(
        "{{GALLERY}}",
        build_gallery(category),
    )

    output = WALLPAPER_ROOT / category / "README.md"

    # Assicura che la directory esista
    output.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    output.write_text(
        content,
        encoding="utf-8",
    )


def main():

    for collection in COLLECTIONS_ROOT.glob("*.json"):
        category = collection.stem

        generate_readme(category)


if __name__ == "__main__":
    main()
