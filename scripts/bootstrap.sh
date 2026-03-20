#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="$ROOT_DIR/.venv"
VENDOR_DIR="$ROOT_DIR/vendor"
UPSTREAM_DIR="$VENDOR_DIR/ppt-master"
UPSTREAM_REPO="${PPT_MASTER_REPO:-https://github.com/macrochen/ppt-master.git}"
UPDATE_MODE="${1:-}"

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 is required but was not found." >&2
  exit 1
fi

if ! command -v git >/dev/null 2>&1; then
  echo "git is required but was not found." >&2
  exit 1
fi

mkdir -p "$VENDOR_DIR"

if [[ ! -d "$UPSTREAM_DIR/.git" ]]; then
  echo "Cloning ppt-master into $UPSTREAM_DIR"
  git clone "$UPSTREAM_REPO" "$UPSTREAM_DIR"
elif [[ "$UPDATE_MODE" == "--update" ]]; then
  echo "Updating existing checkout in $UPSTREAM_DIR"
  git -C "$UPSTREAM_DIR" pull --ff-only
else
  echo "Using existing checkout in $UPSTREAM_DIR"
fi

if [[ ! -d "$VENV_DIR" ]]; then
  echo "Creating virtual environment in $VENV_DIR"
  python3 -m venv "$VENV_DIR"
fi

echo "Installing Python dependencies into $VENV_DIR"
"$VENV_DIR/bin/python" -m pip install --upgrade pip
"$VENV_DIR/bin/pip" install -r "$UPSTREAM_DIR/requirements.txt"

if command -v node >/dev/null 2>&1; then
  echo "Node.js detected: optional web_to_md.cjs support is available."
else
  echo "Node.js not found: Python tools are ready, but web_to_md.cjs will be unavailable."
fi

echo
echo "ppt-master is ready."
echo "Example:"
echo "  $ROOT_DIR/scripts/run-python-tool.sh project_manager.py init demo --format ppt169"
