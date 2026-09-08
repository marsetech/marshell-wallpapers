import json
from pathlib import Path

WALLPAPER_ROOT = Path("collections")

OUTPUT = Path("metadata/categories.json")


def load_existing():

    if not OUTPUT.exists():
        return {}

    return json.loads(OUTPUT.read_text(encoding="utf-8"))


def main():

    categories = load_existing()

    for folder in WALLPAPER_ROOT.iterdir():
        if not folder.is_dir():
            continue

        name = folder.name

        if name not in categories:
            categories[name] = {
                "display_name": name.replace("-", " ").title(),
                "description": "",
            }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    OUTPUT.write_text(
        json.dumps(dict(sorted(categories.items())), indent=4, ensure_ascii=False),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
