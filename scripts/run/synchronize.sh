#!/usr/bin/env bash

set -euo pipefail

source "$(dirname -- "${BASH_SOURCE[0]}")/_lib.sh"


readonly SYNCHRONIZATION_MODULES=(
    scripts.maintenance.convert_images
    scripts.maintenance.normalize_filenames
    scripts.generation.generate_categories
    scripts.generation.generate_collection_metadata
    scripts.maintenance.cleanup_metadata
    scripts.validation.validate_manual_metadata
    scripts.validation.validate_metadata
    scripts.generation.merge_metadata
    scripts.generation.generate_statistics
    scripts.generation.generate_indexes
    scripts.generation.generate_galleries
)


cd_root

run_modules "${SYNCHRONIZATION_MODULES[@]}"
