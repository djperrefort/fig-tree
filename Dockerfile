FROM python:3.11.4-slim-buster

# Disable Python byte code caching and output buffering
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy application source code
WORKDIR /usr/src/app
COPY . .

# Install the application and its dependencies
RUN pip install --upgrade pip \
    && pip install uvicorn["standard"] \
    && pip install -e .

EXPOSE 8000
