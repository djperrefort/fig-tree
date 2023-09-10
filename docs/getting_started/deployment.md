# Deploying Fig-Tree

The following instructions detail how to install and deploy Fig-Tree.


1. A configured instance of the Fig-Tree application
2. A dedicated application database
3. Dedicated static file hosting (optional, but recommended for deployment at scale)

Fig-Tree is designed to be deployed using the Docker suite of containerization tools.
However, developers may wish to install and run the application source code directly.
The table below summarizes the suggested deployment strategies and their typical use case.

| Deployment Method                           | Use Case                                                                                                                 |
|---------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| [Docker](#using-docker)                     | Best for first time users or for deployments with an existing backend infrastructure (e.g. an existing database server). |
| [Docker Compose](#using-docker-compose)     | An "all in one" solution suitable for medium to large scale deployments or for users looking for a long term solution.   |
| [Running from Source](#running-from-source) | Intended for use by project developers to test and evaluate source code changes in real time.                            |


### Using Docker

To deploy a new instance using docker, start by pulling the latest Fig-Tree image from the project container registry.

```bash
docker pull ghcr.io/djperrefort/fig-tree:latest
```



```bash
docker run -p 8000:80 fig-tree
```

```bash
docker run -p 8000:80 --env-file .env fig-tree
```

### Using Docker Compose



=== "Dockerfile"

    ```dockerfile
    FROM nginx:1.25
    
    RUN rm /etc/nginx/conf.d/default.conf
    COPY nginx.conf /etc/nginx/conf.d
    
    RUN mkdir -p /home/app/web/staticfiles
    WORKDIR /home/app/web
    ```

=== "nginx.conf"

    ```nginx
    upstream django_app {
        server web:8000;
    }
    
    server {
        listen 80;
        location / {
            proxy_pass http://django_app;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header Host $host;
            proxy_redirect off;
        }
    
        location /static/ {
            alias /home/app/web/staticfiles/;
        }
    }
    ```

this is a sentance

=== ".web.env"

    ```env
    SECRET_KEY=asdf
    DB_DRIVER=postgresql
    DB_USER=asdf
    DB_PASSWORD=asdf
    DB_HOST=db
    DB_PORT=5432
    ```

=== ".db.env"

    ```env
    POSTGRES_USER=asdf
    POSTGRES_PASSWORD=asdf
    POSTGRES_DB=fig_tree
    ```


```yaml
version: '3.4'

services:
  nginx:
    build: ./nginx
    volumes:
      - static_app_data:/home/app/web/staticfiles
    ports:
      - 80:80
    depends_on:
      - web

  web:
    build: fig_tree
    command: |
      sh -c '
        fig-tree-manage collectstatic --noinput
        fig-tree-manage migrate --noinput
        uvicorn fig_tree.main.asgi:application --host 0.0.0.0 --port 8000
      '
    volumes:
      - static_app_data:/app/fig_tree/static_root
    expose:
      - 8000
    env_file:
      - .web.env
    depends_on:
      - db

  db:
    image: postgres:15
    volumes:
      - postgres_data:/var/lib/postgresql/data/
    env_file:
      - .db.env

volumes:
  postgres_data:
  static_app_data:
```


### Running from Source

!!! note

    The following instructions expect the [conda](https://docs.conda.io/en/latest/) and 
    [poetry](https://python-poetry.org/) utilities are already installed in your working environment.
    Please refer to their official documentation for installation and usage instructions.

In keeping with best practices, new source installations should be run from a dedicated virtual environment:

```bash
conda create -y -n fig-tree python=3.11
conda activate fig-tree
```

Application dependencies are installed and managed using poetry.
Optional dependency groups can be installed using the --with keyword.
To install the necessary Python dependencies, select from the following commands:

=== "Core Dependencies Only"

    ```bash
    # Install only core application dependencies
    poetry install
    ```

=== "Install Everything"

    ```bash
    # Include utilitis for building docs and running tests
    poetry install --with docs tests
    ```

The Django web framework provides a `manage.py` utility for executing administrative tasks.
For your convenience, Fig-Tree exposes this utility as the `fig-tree-manage` command line utility.
If your installation was successful, running the utility will display a list of available subcommands.

```bash
fig-tree-manage
```

The remaining setup follows as standard for a Django based application:

!!! danger

    The following example enables debug mode (`DEBUG=True`).
    This setting is insecure and intended for use locally in a develpment environemnt.
    **Never** enable debug mode in a production setting.
    See [Configuration and Settings](configuration.md) for more details.

```bash
export DEBUG=True
fig-tree-manage migrate  # Migrate the applicatin database schema
fig-tree-manage runserver  # Run the application
```
