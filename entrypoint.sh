#!/bin/bash
# This script is executed when container starts.

# Start Server
poetry run gunicorn --bind 0.0.0.0:8080 core.wsgi:application