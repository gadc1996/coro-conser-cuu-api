FROM python:3.11-slim-bullseye

# Set the working directory to /app
WORKDIR /app

# Install apt-get workspace packages
RUN apt-get update && \
    apt-get install -y \
    git \
    sudo \
    wget \
    curl \
    unzip \
    groff \
    zsh

# Install mysql required packages
RUN apt-get install -y \
    default-libmysqlclient-dev \
    pkg-config \
    gcc

# Install poetry
RUN pip install poetry

# Download and install AWS CLI
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    sudo ./aws/install --bin-dir /usr/local/bin --install-dir /usr/local/aws-cli --update && \
    rm awscliv2.zip && rm -rf aws

# Create user with permissions in folder /app
ARG USERNAME=devcontainer
RUN useradd -ms /bin/bash $USERNAME && \
    chown -R $USERNAME:$USERNAME /app

# add user to sudoers
RUN echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Give full permissions to /usr/local to devcontainer user
RUN chown -R $USERNAME:$USERNAME /usr/local

# Set zsh as default shell for user
RUN chsh -s $(which zsh) $USERNAME
    
# Copy files
COPY . .

# Non root user configuration
USER $USERNAME

# Configure poetry to install packages globally
RUN poetry config virtualenvs.create false

# Install poetry dependencies
RUN poetry install --with dev --no-root
