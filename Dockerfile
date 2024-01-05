# Python image to use.
FROM python:3.12-slim-bullseye

# Set the working directory to /app
WORKDIR /app

# copy the requirements file used for dependencies
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN pip install gunicorn

# Copy the rest of the working directory contents into the container at /app
COPY src/. .
EXPOSE 8080
# Run app.py when the container launches
# ENTRYPOINT ["python", "manage.py", "runserver", "--noreload"]
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8080", "core.wsgi:application"]
