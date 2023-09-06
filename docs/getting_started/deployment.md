# Deploying Fig-Tree

Fig-Tree provides multiple deployment options, each designed to fit a distinct set of needs.
In general, deploying with Docker provides the simplest solution with minimal setup and configuration.
However, alternative methods are provided for application developers or for users looking to experiment with customized instances.

The table below summarizes the suggested deployment strategies and their typical use case.

| Deployment Method   | Use Case                                                                                                                 |
|---------------------|--------------------------------------------------------------------------------------------------------------------------|
| Docker              | Best for first time users or for deployments with an existing backend infrastructure (e.g. an existing database server). |
| Docker Compose      | An "all in one" solution suitable for medium to large scale deployments or for users looking for a long term solution.   |
| Running from Source | Intended for use by project developers to test and evaluate source code changes in real time.                            |


### Using Docker

To deploy a new instance using docker, start by pulling the latest Fig-Tree image from the project container registry.

```bash
docker pull ghcr.io/djperrefort/fig-tree:latest
```

First time user's looking to test-drive the application

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

```
conda create -y -n fig-tree python=3.11
conda activate fig-tree
```

```bash
poetry install --with docs --with tests
```

```bash
python fig_tree/manage.py migrate
python fig_tree/manage.py runserver
```
