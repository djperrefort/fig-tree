# Deployments with Docker
 
For instructions on deploying Fig-Tree against existing backend services (e.g., a database and static file host),
see the [Using Docker](#using-docker) section. To deploy Fig-Tree in addition to any necessary supporting
services, see the [Using Docker Compose](#using-docker-compose) section.

## Using Docker

Start by pulling the latest Fig-Tree image from the project container registry.

```bash
docker pull ghcr.io/djperrefort/fig-tree:latest
```

Next, create a `.env` file defining the desired [application settings](configuration.md).
The following example demonstrates settings for a remote postgres database.

```bash
DB_NAME=fig_tree
DB_USER=my_user
DB_PASSWORD=secure_secret
DB_HOST=my.host.com
DB_PORT=5432
```

Finally, launch the application using the standard django management command:

```bash
docker run --env-file .env djperrefort/fig-tree migrate --noinput
docker run --env-file .env -p 8000:80 djperrefort/fig-tree uvicorn fig_tree.main.asgi:application --host 0.0.0.0 --port 8000
```

## Using Docker Compose



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
