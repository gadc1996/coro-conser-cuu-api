# Python image to use.
FROM python:3.11-alpine

# Set the working directory to /app
WORKDIR /app

# copy the requirements file used for dependencies
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN pip install daphne

# Copy the rest of the working directory contents into the container at /app
COPY . .


EXPOSE 8080
WORKDIR /app/src
# Run app.py when the container launches
ENTRYPOINT ["daphne","-b", "0.0.0.0", "-p", "8080", "core.asgi:application"]
