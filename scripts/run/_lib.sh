#!/usr/bin/env bash

set -euo pipefail


ROOT="$(
    cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../.." &&
    pwd
)"

PYTHON_BIN="${PYTHON_BIN:-python}"


cd_root() {
    cd -- "$ROOT"
}


run_module() {
    "$PYTHON_BIN" -m "$1"
}


run_modules() {
    local module

    for module in "$@"; do
        run_module "$module"
    done
}
