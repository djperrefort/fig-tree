"""
The `gen_data` application acts as a data management utility for genealogical
data.

## Installation

Add the application to the `installed_apps` list in the package settings:

```python
INSTALLED_APPS = [
    'apps.gen_data',
]
```

Register application URLs in the package's primary URL configuration file:

```python
from django.urls import include, path

urlpatterns = [
    path('gen_data/', include('apps.gen_data.urls', namespace='gen_data')),
]
```
"""
