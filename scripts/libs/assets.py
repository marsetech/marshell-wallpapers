from pathlib import Path

from PIL import Image

SUPPORTED_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".webp",
    ".gif",
    ".apng",
}


MIME_TYPES = {
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".webp": "image/webp",
    ".gif": "image/gif",
    ".apng": "image/apng",
}


def is_supported_asset(path: Path) -> bool:
    return path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS


def get_mime_type(path: Path) -> str:
    return MIME_TYPES.get(
        path.suffix.lower(),
        "application/octet-stream",
    )


def get_image_metadata(
    path: Path,
) -> dict:
    stat = path.stat()

    with Image.open(path) as image:
        width, height = image.size

        frame_count = getattr(
            image,
            "n_frames",
            1,
        )

        animated = frame_count > 1

        image_format = (
            image.format.lower() if image.format else path.suffix.lower().lstrip(".")
        )

    if width > height:
        orientation = "landscape"
    elif height > width:
        orientation = "portrait"
    else:
        orientation = "square"

    return {
        "extension": (path.suffix.lower().lstrip(".")),
        "mime_type": get_mime_type(path),
        "format": image_format,
        "size_bytes": stat.st_size,
        "width": width,
        "height": height,
        "orientation": orientation,
        "animated": animated,
        "frame_count": frame_count,
    }
