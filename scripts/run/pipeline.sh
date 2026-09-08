#!/usr/bin/env bash

set -euo pipefail

ROOT="$(
    cd "$(dirname "${BASH_SOURCE[0]}")/../.."
    pwd
)"

cd "$ROOT"

echo "==> Validating repository"
./scripts/run/validate.sh

echo
echo "==> Synchronizing metadata"
./scripts/run/synchronize.sh

echo
echo "==> Validating final state"
./scripts/run/validate.sh

echo
echo "Repository workflow completed successfully."
