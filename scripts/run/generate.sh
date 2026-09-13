#!/usr/bin/env bash

set -euo pipefail

source "$(dirname -- "${BASH_SOURCE[0]}")/_lib.sh"


readonly GENERATION_MODULES=(
    scripts.generation.generate_categories
    scripts.generation.generate_collection_metadata
    scripts.generation.merge_metadata
    scripts.generation.generate_statistics
    scripts.generation.generate_indexes
    scripts.generation.generate_galleries
)


cd_root

run_modules "${GENERATION_MODULES[@]}"
