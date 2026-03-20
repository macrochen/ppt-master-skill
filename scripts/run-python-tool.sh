#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="$ROOT_DIR/.venv/bin/python"
UPSTREAM_DIR="$ROOT_DIR/vendor/ppt-master"
TOOL_NAME="${1:-}"

if [[ -z "$TOOL_NAME" ]]; then
  echo "Usage: $0 <tool-file> [args...]" >&2
  exit 1
fi

if [[ ! -x "$PYTHON_BIN" ]]; then
  echo "Missing virtual environment: $PYTHON_BIN" >&2
  echo "Run $ROOT_DIR/scripts/bootstrap.sh first." >&2
  exit 1
fi

if [[ ! -d "$UPSTREAM_DIR" ]]; then
  echo "Missing upstream checkout: $UPSTREAM_DIR" >&2
  echo "Run $ROOT_DIR/scripts/bootstrap.sh first." >&2
  exit 1
fi

shift

TOOL_PATH="$UPSTREAM_DIR/tools/$TOOL_NAME"
if [[ ! -f "$TOOL_PATH" ]]; then
  echo "Tool not found: $TOOL_PATH" >&2
  exit 1
fi

exec "$PYTHON_BIN" "$TOOL_PATH" "$@"
