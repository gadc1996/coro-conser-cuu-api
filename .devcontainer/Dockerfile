FROM python:3.11-bullseye

RUN useradd -m devcontainer

RUN chsh -s /bin/bash devcontainer

WORKDIR /home/devcontainer

RUN apt-get update && \
    apt-get install -y git

RUN pip install poetry

USER devcontainer