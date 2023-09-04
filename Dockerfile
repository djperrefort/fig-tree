FROM python:3.11.4-slim

# Disable Python byte code caching and output buffering
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy application source code
WORKDIR /app
COPY . .

# Install the application and its dependencies
ENV PIP_ROOT_USER_ACTION=ignore
RUN pip3 install --upgrade pip \
    && pip3 install uvicorn["standard"] \
    && pip3 install -e .

EXPOSE 8000
