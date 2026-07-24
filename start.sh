#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"
mkdir -p data

HOST="${HOST:-0.0.0.0}"
PORT="${PORT:-8080}"
PYTHON="${PYTHON:-python3}"

exec "$PYTHON" -m uvicorn backend.main:app --host "$HOST" --port "$PORT"
