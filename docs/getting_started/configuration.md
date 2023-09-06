# Application Settings

Fig-Tree is designed to run securely by default.
However, most deployments at customizing the application settings is still required 

## Security Settings

| Variable        | Default                  | Description                                       |
|-----------------|--------------------------|---------------------------------------------------|
| `DEBUG`         | `0`                      | Used to enable (`1`) or disable (`0`) debug mode. |
| `SECRET_KEY`    | Random                   |                                                   |
| `ALLOWED_HOSTS` | `*`                      |                                                   |

## Database Settings

| Variable        | Default                  | Description                                       |
|-----------------|--------------------------|---------------------------------------------------|
| `DB_DRIVER`     | `sqite3` or `postgresql` |                                                   |
| `DB_NAME`       | `fig_tree`               |                                                   |
| `DB_USER`       | `fig_tree`               |                                                   |
| `DB_PASSWORD`   | `fig_tree`               |                                                   |
| `DB_HOST`       | `fig_tree`               |                                                   |
| `DB_PORT`       | `fig_tree`               |                                                   |

## Custom File Hosting

| Variable      | Default                  | Description                                       |
|---------------|--------------------------|---------------------------------------------------|
| `STATIC_URL`  | `static/`                |                                                   |
| `STATIC_ROOT` | `static/`                |                                                   |
