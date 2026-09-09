from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

COLLECTIONS_ROOT = ROOT / "collections"

METADATA_ROOT = ROOT / "metadata"

MANUAL_METADATA_ROOT = METADATA_ROOT / "manual"

GENERATED_METADATA_ROOT = METADATA_ROOT / "generated"

INDEXES_ROOT = METADATA_ROOT / "indexes"

TAXONOMY_ROOT = METADATA_ROOT / "taxonomy"

SCRIPTS_ROOT = ROOT / "scripts"

TEMPLATES_ROOT = ROOT / "templates"

METADATA_TEMPLATES_ROOT = TEMPLATES_ROOT / "metadata"

GALLERY_TEMPLATES_ROOT = TEMPLATES_ROOT / "galleries"
