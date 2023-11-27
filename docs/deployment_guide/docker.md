# Deployments with Docker

For instructions on deploying Fig-Tree against existing backend services (e.g., a database and static file host)
or in debug mode see the [Using Docker](#using-docker) section. 

To deploy Fig-Tree in addition to any necessary supporting services, see the 
[Using Docker Compose](#using-docker-compose) section.

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

Finally, launch the application using the standard django management commands:

```bash
docker run --env-file .env djperrefort/fig-tree migrate --noinput
docker run --env-file .env -p 8000:80 djperrefort/fig-tree uvicorn fig_tree.main.asgi:application --host 0.0.0.0 --port 8000
```

## Using Docker Compose

The following docker compose recipe includes all services necessary to deploy a full Fig-Tree instance.

```yaml
version: '3.4'

services:
   nginx: # (1)!
      build: ./nginx
      volumes:
         - static_app_data:/home/app/web/staticfiles # (2)!
      ports:
         - "80:80"
      depends_on:
         - web

   web: # (3)!
      build: fig_tree
      command: |
         sh -c '
           fig-tree-manage collectstatic --no-input
           fig-tree-manage migrate --no-input
           uvicorn fig_tree.main.asgi:application --host 0.0.0.0 --port 8000'
      volumes:
         - static_app_data:/app/fig_tree/static_root
      expose:
         - 8000
      env_file:
         - .web.env # (4)!
      depends_on:
         - db

   db: # (5)!
      image: postgres:15
      volumes:
         - postgres_data:/var/lib/postgresql/data/
      env_file:
         - .db.env # (6)!

volumes:
   postgres_data:
   static_app_data: 
```

1. The `nginx` service uses a custom Nginx image to serve static files. 
   SSL handling is left to the user and should be handled upstream.
2. This volume is used to shared static files between the `web` and `nginx` services.
3. This service launches a Fig-Tree application instance using the Unicorn ASGI web server.
4. The `.web.env` file is used to define [application settings](configuration.md) for Fig-Tree.
5. The `db` service deploys a Postgres database.
6. The `.db.env` file is used to configure the Postgres database.
   This will include some of the same values as `.web.env` (e.g., the database name, username, and password).

For static file hosting, we use a custom image built using Nginx.
We use the `nginx.conf` file to configure traffic routing.
By default, all traffic is directed to the Fig-Tree application.
Requests submitted to `/static/` are redirected to static files stored in the `static_app_data` volume mounted at `/home/app/web/staticfiles`.

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

The following examples demonstrate environmental files used to configure the `web` and `db` services.
Database credentials (database name, username, and password) must match between the two files. 

=== ".web.env"

    ```env
    SECRET_KEY=asdf
    DB_NAME=fig_tree
    DB_USER=fig_tree_app
    DB_PASSWORD=securepassword
    DB_HOST=db  # Maches the name of the docker database service
    DB_PORT=5432
    ```

=== ".db.env"

    ```env
    POSTGRES_DB=fig_tree
    POSTGRES_USER=fig_tree_app
    POSTGRES_PASSWORD=securepassword
    ```


