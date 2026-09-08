#!/usr/bin/env bash

set -euo pipefail

ROOT="$(
    cd "$(dirname "${BASH_SOURCE[0]}")/../.."
    pwd
)"

cd "$ROOT"

python -m scripts.validation.validate_repository
python -m scripts.validation.validate_assets
python -m scripts.validation.validate_manual_metadata
python -m scripts.validation.validate_metadata
