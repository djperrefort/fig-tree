"""
The ``authentication`` app is responsible for authenticating users with
existing accounts. It handles user logins/logouts and password reset requests.
It is **not** responsible for creating new user accounts.

Application features include:

- Extended authentication functionality with useful features like "remember me" session cookies.
- A secure, token-based mechanism for users to reset forgotten or outdated passwords.

# Installation

Start by adding the application to the ``installed_apps`` list in the package settings:

```python
INSTALLED_APPS = [
   'apps.authentication',
]
```

Next, register the application URLs in the package's primary URL configuration file:

```python
from django.urls import include, path

urlpatterns = [
    path('auth/', include('apps.authentication.urls', namespace='auth')),
]
```

Finally, configure the pakage settings for the login URL using the same namespace value:

```python
LOGIN_URL = 'auth:login'
```

# Application Settings

The `authentication` app supports a *remember me* option that will keep
users logged in for a given duration. Users are remembered for seven days by
default, but the length of this duration is configurable in the ``setings.py``
file:

```python
from datetime import timedelta

REMEMBER_ME_DURATION = timedelta(days=4)
```
"""
