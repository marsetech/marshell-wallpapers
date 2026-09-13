#!/usr/bin/env bash

set -euo pipefail

source "$(dirname -- "${BASH_SOURCE[0]}")/_lib.sh"


readonly VALIDATION_MODULES=(
    scripts.validation.validate_repository
    scripts.validation.validate_assets
    scripts.validation.validate_manual_metadata
    scripts.validation.validate_metadata
)


cd_root

run_modules "${VALIDATION_MODULES[@]}"
