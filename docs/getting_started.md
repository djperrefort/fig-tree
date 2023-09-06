# Getting Started

There are several options for running a Fig-Tree instance, each wih its own benefits and drawbacks.
It is important to carefully review each option and it's tradeoffs before selecting a method for your use case.

## Deploying Fig-Tree

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

### Using Docker

```bash
docker pull
```

```bash
docker run -p 8000:80
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


## Configuring Your Environment

Fig-Tree is configured

| Variable        | Default                  | Description                                       |
|-----------------|--------------------------|---------------------------------------------------|
| `DEBUG`         | `0`                      | Used to enable (`1`) or disable (`0`) debug mode. |
| `SECRET_KEY`    | Random                   |                                                   |
| `ALLOWED_HOSTS` | `*`                      |                                                   |
| `DB_DRIVER`     | `sqite3` or `postgresql` |                                                   |
| `DB_NAME`       | `fig_tree`               |                                                   |
| `DB_USER`       | `fig_tree`               |                                                   |
| `DB_PASSWORD`   | `fig_tree`               |                                                   |
| `DB_HOST`       | `fig_tree`               |                                                   |
| `DB_PORT`       | `fig_tree`               |                                                   |
| `STATIC_URL`    | `static/`                |                                                   |
