#!/usr/bin/env bash
set -o errexit
pip install -r requirements.txt
if command -v npm >/dev/null 2>&1; then
  npm ci
  npm run build:css
else
  echo "WARNING: npm not found; using pre-built site.css if present."
fi
python manage.py collectstatic --no-input
if [ -n "${DATABASE_URL:-}" ]; then
  if ! python manage.py migrate --no-input; then
    echo "WARNING: migrate failed (database suspended or unreachable). Continuing build."
  fi
else
  echo "DATABASE_URL not set; skipping migrate."
fi
