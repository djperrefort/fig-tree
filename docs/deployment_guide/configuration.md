# Configuration and Settings

Fig-Tree uses environmental variables to configure application settings.
At a minimum, setting the `DEBUG=1` option is sufficient to launch a development instance.
However, deployments in a formal production setting will require additional configuration.

All settings are loaded dynamically at runtime and persist for the lifetime of the application.
This means an application restart is required for new settings to take effect.

!!! danger

    Settings should be selected carefully when deploying to a production environment.
    Improper configuration can lead to unexpected behavior and insecure deployments.
    **Never** enable the `DEBUG` option in production.

## Security Settings

The values listed below directly affect application security and should be chosen with care.
It is important to note the following security recommendations:

- The `SECRET_KEY` value should be a random, cryptographically secure value.
- The list of `ALLOWED_HOSTS` should be as restrictive as possible.

| Variable        | Default               | Description                                                                 |
|-----------------|-----------------------|-----------------------------------------------------------------------------|
| `SECRET_KEY`    | `<random>`            | Secret value used for security-related tasks.                               |
| `ALLOWED_HOSTS` | `localhost 127.0.0.1` | Space-delimited list of hostnames allowed to serve the running application. |

!!! note

    Fig-Tree will automatically generate a secret key if one is not provided.
    This key will not persist between sessions, and any previously generated tokens will be invalidated.
    For this reason, setting an explicit secret key value is strongly recommended.

## Database Settings

Fig-Tree supports multiple database backends, including SQLite and Postgres.
In general, SQLite is only recommended for use in development settings or for small deployments.
Postgres is the suggested database for use in production.
Database connection settings are configured using the variables listed below.

| Variable      | Default     | Description                                                   |
|---------------|-------------|---------------------------------------------------------------|
| `DB_DRIVER`   | `sqlite3`   | Whether to use the `sqlite3` or `postgresql` database engine. |
| `DB_NAME`     | `fig_tree`  | Name of the application database to use.                      |
| `DB_USER`     |             | Username to use when authenticating against the database.     |
| `DB_PASSWORD` |             | Password to use when authenticating against the database.     | 
| `DB_HOST`     | `localhost` | Host address of the database server.                          |
| `DB_PORT`     | `5432`      | Port number to use when connecting to the database server.    |

## File Hosting

Like all web-based applications, Fig-Tree relies on static files to generate and style web content.
When hosting static files from the same server as the deployed application, `STATIC_URL` is typically set to `static/`.
When hosting static files from a separate location, `STATIC_URL` should be set to the URL of the static file server.

| Variable      | Default              | Description                                                                        |
|---------------|----------------------|------------------------------------------------------------------------------------|
| `STATIC_URL`  | `static/`            | Base URL (including http protocol) of the static content server.                   |
| `STATIC_ROOT` | `$(pwd)/static_root` | Local directory where static files are collected when running management commands. |

## Development Settings

The following settings are provided to assist in the development process and are only supported when `DEBUG` mode is
enabled.

| Variable          | Default                | Description                                                                                        |
|-------------------|------------------------|----------------------------------------------------------------------------------------------------|
| `DEBUG`           | `0`                    | Used to enable (`1`) or disable (`0`) debug mode.                                                  |
| `EMAIL_FILE_PATH` | `<project root>/email` | Emails issued by the application are stored as files in the given directory instead of being sent. |
