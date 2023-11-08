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

The `FamilyTreeModelMixin` class defines the fields and methods
necessary to support family tree based permissions using the model
backend. Add the mixin to your database models as follows:

```python
from apps.family_trees import FamilyTreeModelMixin


class ExampleModel(FamilyTreeModelMixin, models.Model):
    # Define the rest of your model class as normal
    ...
```

User permissions can then be assigned to corresponding views (or view set)
using the `IsTreeMember` permission object:

```python
class ExampleViewSet(viewsets.GenericViewSet):
    # Define the view set permissions
    permission_classes = (IsAuthenticated, FamilyTreeObjectPermission)

    # Define the rest of the view set as normal
    serializer_class = ExampleSerializer
    queryset = ExampleModel.objects
```
"""
