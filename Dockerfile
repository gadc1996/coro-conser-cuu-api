# Python image to use.
FROM python:3.11-alpine

# Install system dependencies for mysqlclient
RUN apk add --no-cache mariadb-dev build-base

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN  poetry install --with deploy

# Copy the rest of the application code to the working directory
COPY . /app/

# Expose the port on which the application will run
EXPOSE 8080

# Set the working directory to /app/src
WORKDIR /app/src

# Run Daphne when the container launches
ENTRYPOINT ["poetry", "run", "daphne", "-b", "0.0.0.0", "-p", "8080", "core.asgi:application"]
