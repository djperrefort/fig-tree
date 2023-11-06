"""
The `urls` module maps URL endpoints to django views defined in the parent
application. For root level URL routing, see the project level `urls` module.
View objects can be found in the `views` module.

# URL Routing Configuration

| URL                   | View / View Set         | Name               |
|-----------------------|------------------------|---------------------|
| `tree/`               | `FamilyTreeViewSet`    | `tree-list`         |
| `tree/<str:pk>`       | `FamilyTreeViewSet`    | `tree-detail`       |
| `permission/`         | `PermissionViewSet`    | `permission-list`   |
| `permission/<str:pk>` | `PermissionViewSet`    | `permission-detail` |
"""

from rest_framework import routers

from .views import *

app_name = 'family_trees'

router = routers.SimpleRouter()
router.register(r'tree', FamilyTreeViewSet)
router.register(r'permission', TreePermissionViewSet)
urlpatterns = router.urls
