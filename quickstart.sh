#!/usr/bin/env bash
set -euo pipefail

PROJECT_NAME=$1

sphinx-quickstart \
    -q \
    -p "${PROJECT_NAME}" \
    -a nikkie \
    -v '' \
    -l ja \
    --sep \
    --ext-githubpages \
    --no-batchfile
