#!/usr/bin/env bash
set -euo pipefail

PROJECT_NAME=$1

sphinx-quickstart \
    --sep \
    -p "${PROJECT_NAME}" \
    -a nikkie \
    -l ja \
    -r '' \
    --ext-githubpages \
    --no-batchfile
