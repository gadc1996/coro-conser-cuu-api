#!/bin/bash
# This script is used to start the application

# Apply database migrations
poetry run python manage.py migrate

# Collect static files
poetry run python manage.py collectstatic --noinput

# Start server
poetry run gunicorn --bind 0.0.0.0:8080 core.wsgi:application