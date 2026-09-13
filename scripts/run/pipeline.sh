#!/usr/bin/env bash

set -euo pipefail

source "$(dirname -- "${BASH_SOURCE[0]}")/_lib.sh"


cd_root

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
