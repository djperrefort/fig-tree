"""
The `data_api` application provides a comprehensive REST API for managing
genealogical data. The API is designed to facilitate the creation, retrieval,
updating, and deletion of genealogical data in a flexible manner.

Application features include:

  - REST endpoints for CRUD operations on genealogical records including persons, families, events, locations, and more.
  - Support for query parameters and filters to search and retrieve specific genealogical records.
  - Robust data validation when creating/updating records to ensure data integrity.

Installation
------------

Add the application to the ``installed_apps`` list in the package settings:

```python
INSTALLED_APPS = [
    'apps.gen_rest_api',
]
```

Register application URLs in the package's primary URL configuration file:

```python
from django.urls import include, path

urlpatterns = [
    path('api/', include('apps.gen_rest_api.urls', namespace='gen_rest_api')),
]
```
"""
