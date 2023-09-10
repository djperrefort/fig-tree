"""The `signup` application is responsible for the creation and verification
of new user accounts.

- Allows users to create new accounts using a unique username, email address, and password.
- Extends the default user database model with additional fields and functionality
- Manages user account information via customized administrative interfaces in the website admin portal.
- Verifys user contact information by sending confirmation requests to user email addresss.

## Installation

Add the application and it's required dependencies to the ``installed_apps``
list in the package settings:

```python
INSTALLED_APPS = [
    'django.contrib.sites',
    'apps.signup',
]
```

Register application URLs in the package's primary URL configuration file:

```python
from django.urls import include, path

urlpatterns = [
    path('signup/', include('apps.signup.urls', namespace='signup')),
]
```

Using the same namespace value as chosen in the previous step, override the
default user model by adding the following definition to the package settings file:

```python
AUTH_USER_MODEL = 'signup.AuthUser'
```

To make sure everything is integrated correctly, run the application test suite:

```bash
fig-tree-manage test apps.signup
```
"""
