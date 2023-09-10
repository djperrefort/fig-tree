# Deployments with Docker

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
