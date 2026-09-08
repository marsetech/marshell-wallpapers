import json
from datetime import datetime
from pathlib import Path

COLLECTIONS_ROOT = Path("metadata/collections")

OUTPUT = Path("metadata/statistics.json")


def main():

    statistics = {
        "generated_at": datetime.now().isoformat(),
        "categories": 0,
        "wallpapers": 0,
        "total_size_bytes": 0,
        "collections": {},
    }

    for file in sorted(COLLECTIONS_ROOT.glob("*.json")):
        print(f"Loading {file}")

        data = json.loads(file.read_text(encoding="utf-8"))

        if "total" not in data:
            continue

        category = data["category"]

        total = data["total"]

        size = sum(wallpaper["size_bytes"] for wallpaper in data["wallpapers"].values())

        statistics["categories"] += 1

        statistics["wallpapers"] += total

        statistics["total_size_bytes"] += size

        statistics["collections"][category] = total

    OUTPUT.write_text(
        json.dumps(statistics, indent=4, ensure_ascii=False), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
