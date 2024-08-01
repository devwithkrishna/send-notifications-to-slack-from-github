# Using python 3.11 as bas image
FROM python:3.11-slim-bookworm
# Label
LABEL authors="githubofkrishnadhas"
# Workdir
WORKDIR /app
# Copy files from current directory to wordir
COPY pyproject.toml send_slack_alert.py /app/
# Install poetry
RUN chmod +x entrypoint.sh &&  apt-get update -y && pip install poetry
# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/app/entrypoint.sh"]

