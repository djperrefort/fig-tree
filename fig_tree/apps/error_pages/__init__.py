"""
The `error_pages` application extends the error handling functionality built
into django. It provides automatic request routing to customizable error pages
for 400, 403, 404, and 500 errors (the same as those supported by Django).

# Installation

Add the application to the `installed_apps` list in the package settings:

```python
INSTALLED_APPS = [
   'apps.error_pages',
]
```

Next, add the handler objects to the root URL configuration file:

```python
from apps.error_pages import handlers

# Add handlers for different error codes as desired
handler400 = handlers.handler400
handler403 = handlers.handler403
handler404 = handlers.handler404
handler500 = handlers.handler500
```

# Configuring Application Templates

By default, all HTTP errors are redirected to the HTML template `error_pages/default.html`.
Template files can also be specified for individual HTTP error codes using the
naming scheme `error_pages/http_[ERROR CODE].html`. For example, a 404 error
will render the template located at `error_pages/http_404.html`.

Rendered templates are automatically provided with context values for describing
the corresponding error code. A summary of these values is provided below.

## Context Values for 400 Errors

| Template Variable Name | Value                                                       |
|------------------------|-------------------------------------------------------------|
| `error_code`           | 400                                                         |
| `description`          | Bad Request                                                 |
| `description_long`     | The server could not process your request.                  |

## Context Values for 403 Errors

| Template Variable Name | Value                                                       |
|------------------------|-------------------------------------------------------------|
| `error_code`           | 403                                                         |
| `description`          | Forbidden                                                   |
| `description_long`     | You are not authorized for access to the requested content. |

## Context Values for 404 Errors

| Template Variable Name | Value                                                       |
|------------------------|-------------------------------------------------------------|
| `error_code`           | 404                                                         |
| `description`          | Page Not Found                                              |
| `description_long`     | The server could not find the resource you requested.       |

## Context Values for 500 Errors

| Template Variable Name | Value                                                       |
|------------------------|-------------------------------------------------------------|
| `error_code`           | 500                                                         |
| `description`          | Internal Server Error                                       |
| `description_long`     | The server has encountered an internal error.               |
"""

from django.conf import settings

# Allow reloading of the module without Django raising an error
# This is useful for running tests without a running django server
try:
    settings.configure()

except RuntimeError:
    pass

# Set default setting values
try:
    getattr(settings, 'ERROR_CODE_DESCRIPTIONS')

except AttributeError:
    setattr(settings, 'ERROR_CODE_DESCRIPTIONS', {
        400: 'Bad Request',
        403: 'Forbidden',
        404: 'Page Not Found',
        500: 'Internal Server Error'
    })

try:
    getattr(settings, 'ERROR_CODE_DESCRIPTIONS_LONG')

except AttributeError:
    setattr(settings, 'ERROR_CODE_DESCRIPTIONS_LONG', {
        400: 'The server could not process your request.',
        403: 'You are not authorized for access to the requested content.',
        404: 'The server could not find the resource you requested.',
        500: 'The server has encountered an internal error.',
    })
