"""The ``signup`` application is responsible for the creation and verification
of new user accounts.

Features:
  - Allw users to create new accounts by providing a unique username, email address, and password.
  - Manage user account information view customized administrative interfaces in the website admin portal.
  - Verify user contact information by sending confirmation requests to user email addresss.
  - Provide a secure, token-based mechanism for users to reset forgotten or outdated passwords.

Installation
------------

Add the application and it's required dependencies to the ``installed_apps``
list in the package settings:

.. doctest:: python

   >>> INSTALLED_APPS = [
   ...     'django.contrib.sites',
   ...     'apps.signup',
   ... ]


Register application URLs in the package's primary URL configuration file:

.. doctest:: python

   >>> from django.urls import include, path
   >>>
   >>> urlpatterns = [
   ...     path('signup/', include('apps.signup.urls', namespace='signup')),
   ... ]

Using the same namespace value as chosen in the previous step, overide the
default user model by adding the following to the package settings file:

.. doctest:: python

   >>> AUTH_USER_MODEL = 'signup.AuthUser'

To make sure everything is integrated correctly, run the application test suite:

.. code-block:: bash

   $ python pkg/source/manage.py test apps.signup
"""
