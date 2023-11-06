"""
The `family_trees` application defines a base set of models, permissions, and
serializers for grouping database records into family trees.

## Installation

Add the application to the `installed_apps` list in the package settings:

```python
INSTALLED_APPS = [
    'apps.family_trees',
]
```

Register application URLs in the package's primary URL configuration file:

```python
from django.urls import include, path

urlpatterns = [
    path('trees/', include('apps.family_trees.urls', namespace='family_trees')),
]
```

## Usage

To group application data by family tree, add a `tree` attribute to the
appropriate database model with a relationship to the `FamilyTree` class:

```python
import apps.family_trees.models as tree_models


class ExampleModel(models.Model):
    tree = models.ForeignKey(tree_models.FamilyTree, db_index=True, on_delete=models.CASCADE)
```

User permissions can then be assigned to any corresponding views using the
`IsTreeMember` permission object. This will require the user to have
"""
