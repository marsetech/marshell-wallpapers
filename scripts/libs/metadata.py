import json
from pathlib import Path
from typing import Any


def load_json(
    path: Path,
    default: Any = None,
) -> Any:
    if not path.exists():
        if default is not None:
            return default

        return {}

    return json.loads(path.read_text(encoding="utf-8"))


def write_json(
    path: Path,
    data: Any,
) -> None:
    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    path.write_text(
        json.dumps(
            data,
            indent=4,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )
