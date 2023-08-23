"""The ``authentication`` app is responsible for authenticating users with
existing accounts. It handles user logins/logouts and password reset requests.
It is **not** responsible for creating new user accounts.

Features:
  - Extend built-in authentication functionality with useful features like "remember me" session cookies.
  - Provide a secure, token-based mechanism for users to reset forgotten or outdated passwords.

Installation
------------

Add the application to the ``installed_apps`` list in the package settings:

.. doctest:: python

   >>> INSTALLED_APPS = [
   ...    'apps.authentication',
   ... ]

Next, register the application URLs in the package's primary URL configuration file:

.. doctest:: python

   >>> from django.urls import include, path
   >>>
   >>> urlpatterns = [
   ...     path('auth/', include('apps.authentication.urls', namespace='auth')),
   ... ]

Finally, configure the pakage settings for the login URL using the same namespace value:

.. doctest:: python

   >>> LOGIN_URL = 'auth:login'

Configuring Application Settings
--------------------------------

The ``authentication`` app supports a *remember me* option that will keep
users logged in for a given duration. The length of this duration is configurable:

.. doctest:: python

   >>> from datetime import timedelta
   >>>
   >>> REMEMBER_ME_DURATION = timedelta(weeks=4).total_seconds()
"""
