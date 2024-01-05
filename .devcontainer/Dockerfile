FROM python:3.11-slim-bullseye

WORKDIR /app

# Create user with permissions in folder /app
ARG USERNAME=devcontainer
RUN useradd -ms /bin/bash $USERNAME && \
    chown -R $USERNAME:$USERNAME /app

# Update pip and install requirements
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Install apt-get packages
RUN apt-get update && \
    apt-get install -y \
    git \
    sudo

# add user to sudoers
RUN echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Add pip to path
ENV PATH="/home/$USERNAME/.local/bin:${PATH}"

# Copy rest of files
COPY . .

USER $USERNAME