from scripts.libs.metadata import (
    load_json,
)
from scripts.libs.paths import (
    COLLECTIONS_ROOT,
    GALLERY_TEMPLATES_ROOT,
    GENERATED_METADATA_ROOT,
)

START_MARKER = "<!-- GENERATED:GALLERY:START -->"

END_MARKER = "<!-- GENERATED:GALLERY:END -->"


def build_gallery(
    metadata: dict,
) -> str:
    lines = []

    assets = metadata.get(
        "assets",
        {},
    )

    for asset in assets.values():
        lines.append(
            f"<img "
            f'src="./assets/{asset["filename"]}" '
            f'alt="{asset.get("title", "")}" '
            f'width="49%">'
        )

    return "\n".join(lines)


def replace_generated_section(
    content: str,
    gallery: str,
) -> str:
    generated = f"{START_MARKER}\n{gallery}\n{END_MARKER}"

    start = content.find(START_MARKER)

    end = content.find(END_MARKER)

    if start == -1 or end == -1:
        return content.rstrip() + "\n\n" + generated + "\n"

    end += len(END_MARKER)

    return content[:start] + generated + content[end:]


def main() -> None:
    template_file = GALLERY_TEMPLATES_ROOT / "collection.md"

    template = template_file.read_text(encoding="utf-8")

    merged_root = GENERATED_METADATA_ROOT / "merged"

    for metadata_file in merged_root.rglob("*.json"):
        metadata = load_json(metadata_file)

        category = metadata["category"]
        collection = metadata["collection"]

        collection_dir = COLLECTIONS_ROOT / category / collection

        readme = collection_dir / "README.md"

        if readme.exists():
            content = readme.read_text(encoding="utf-8")
        else:
            content = template.replace(
                "<Collection Name>",
                collection.replace(
                    "-",
                    " ",
                ).title(),
            )

        gallery = build_gallery(metadata)

        content = replace_generated_section(
            content,
            gallery,
        )

        readme.write_text(
            content,
            encoding="utf-8",
        )

        print(f"Generated: {readme}")


if __name__ == "__main__":
    main()
