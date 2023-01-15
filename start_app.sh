#!/bin/bash

python migrate_db.py
gunicorn -w 1 -b 0.0.0.0:8080 --timeout 0 app:app

exec "$@"
