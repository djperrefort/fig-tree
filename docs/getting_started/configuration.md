# Configuration and Settings

Fig-Tree uses environmental variables to configure application settings.
All settings are loaded dynamically at runtime, and persist for the lifetime of the running application.
This means an application restart is required for new settings to take effect.

Setting values should be selected carefully when deploying to a production environment.
Improper configuration can lead to unexpected behavior and insecure deployments.

## General Settings

The values listed below directly affect application security and should be chosen with care.
It is important to note the following security recommendations:

- Debug mode should **never** be enabled in a production environment.
- The `SECRET_KEY` value should be a random, cryptographically secure value.
- The list of `ALLOWED_HOSTS` should be as restrictive as possible.

| Variable        | Default     | Description                                                                 |
|-----------------|-------------|-----------------------------------------------------------------------------|
| `DEBUG`         | `0`         | Used to enable (`1`) or disable (`0`) debug mode.                           |
| `SECRET_KEY`    | `<random>`  | Secret value used for security-related tasks.                               |
| `ALLOWED_HOSTS` | `localhost` | Space-delimited list of hostnames allowed to serve the running application. |

## Database Settings

Fig-Tree supports multiple database backends, including Sqlite and Postgres.
In general, Sqlite is only recommended for use in development settings or for small deployments.
Postgres is the suggested database for use in production settings.
Database connection settings are configured using the variables listed below.

| Variable      | Default                   | Description                                                |
|---------------|---------------------------|------------------------------------------------------------|
| `DB_DRIVER`   | `sqlite3` or `postgresql` | The database engine to be used.                            |
| `DB_NAME`     | `fig_tree`                | Name of the application database to use.                   |
| `DB_USER`     |                           | Username to use when authenticating against the database.  |
| `DB_PASSWORD` |                           | Password to use when authenticating against the database.  | 
| `DB_HOST`     | `localhost`               | Host address of the database server.                       |
| `DB_PORT`     | `5432`                    | Port number to use when connecting to the database server. |

## File Hosting

Like all web-based applications, Fig-Tree relies on static files to generate and style web content.
When hosting static files from the same server as the deployed application, `STATIC_URL` is typically set to `static/`.
When hosting static files from a separate location, `STATIC_URL` should be set to the URL of the static file server.

| Variable      | Default              | Description                                                                        |
|---------------|----------------------|------------------------------------------------------------------------------------|
| `STATIC_URL`  | `static/`            | Base URL (including http protocol) of the static content server.                   |
| `STATIC_ROOT` | `$(pwd)/static_root` | Local directory where static files are collected when running management commands. |
