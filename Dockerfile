# Dockerfile for spaCy application
FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN chmod +x /app/entrypoint.sh


CMD ["/app/entrypoint.sh"]
