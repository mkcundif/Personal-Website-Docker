#!/usr/bin/env bash
set -e

# Ensure data directory exists
mkdir -p /data

# If DB path not provided, default to /data/projects.db
: "${PROJECTS_DB_PATH:=/data/projects.db}"
export PROJECTS_DB_PATH

# Initialize DB if missing
python - <<PY
from DAL import init_db
import os
init_db(os.environ.get('PROJECTS_DB_PATH', 'projects.db'))
print('Database initialized at', os.environ.get('PROJECTS_DB_PATH'))
PY

# Execute the CMD
exec "$@"
