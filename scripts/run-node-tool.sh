#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
UPSTREAM_DIR="$ROOT_DIR/vendor/ppt-master"
SCRIPT_NAME="${1:-}"

if [[ -z "$SCRIPT_NAME" ]]; then
  echo "Usage: $0 <node-script> [args...]" >&2
  exit 1
fi

if ! command -v node >/dev/null 2>&1; then
  echo "node is required but was not found." >&2
  exit 1
fi

if [[ ! -d "$UPSTREAM_DIR" ]]; then
  echo "Missing upstream checkout: $UPSTREAM_DIR" >&2
  echo "Run $ROOT_DIR/scripts/bootstrap.sh first." >&2
  exit 1
fi

shift

SCRIPT_PATH="$UPSTREAM_DIR/tools/$SCRIPT_NAME"
if [[ ! -f "$SCRIPT_PATH" ]]; then
  echo "Node tool not found: $SCRIPT_PATH" >&2
  exit 1
fi

exec node "$SCRIPT_PATH" "$@"
