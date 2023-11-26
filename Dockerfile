FROM python:3.11.4-slim

EXPOSE 8000

# Disable Python byte code caching and output buffering
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy only the files needed to build the application
WORKDIR /app
COPY fig_tree fig_tree
COPY pyproject.toml pyproject.toml

# Install the application and its dependencies
ENV PIP_ROOT_USER_ACTION=ignore
RUN pip3 install -e .

ENTRYPOINT ["fig-tree-manage"]
