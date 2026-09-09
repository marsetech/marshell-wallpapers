#!/usr/bin/env bash

set -euo pipefail

ROOT="$(
    cd "$(dirname "${BASH_SOURCE[0]}")/../.."
    pwd
)"

cd "$ROOT"

python -m scripts.generation.generate_categories
python -m scripts.generation.generate_collection_metadata
python -m scripts.generation.merge_metadata
python -m scripts.generation.generate_statistics
python -m scripts.generation.generate_indexes
python -m scripts.generation.generate_galleries
