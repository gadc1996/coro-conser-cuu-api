# Python image to use.
FROM python:3.11-slim-bullseye

# Set the working directory to /app
WORKDIR /app

# Install apt-get packages
RUN apt-get update && \
    apt-get install -y \
    pkg-config \
    default-libmysqlclient-dev \
    gcc

# Install poetry
RUN pip install poetry

# Copy poetry files
COPY pyproject.toml poetry.lock ./

# Install poetry dependencies
RUN poetry install --with deploy --no-root

# Copy the rest of the working directory contents into the container at /app
COPY src/. .

# Expose port 8080
EXPOSE 8080

# Run migrations and start server
ENTRYPOINT poetry run python manage.py migrate && poetry run python manage.py collectstatic --no-input && poetry run python manage.py runserver
