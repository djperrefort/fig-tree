"""
The ``urls`` module maps URL endpoints to django views defined in the parent
application. For root level URL routing, see the project level ``urls`` module.
View objects can be found in the ``views`` module.

# URL Routing Configuration

| URL                   | View / View Set         | Name               |
|-----------------------|------------------------|---------------------|
| `tree/`               | `TreeViewSet`          | `tree-list`         |
| `tree/<str:pk>`       | `TreeViewSet`          | `tree-detail`       |
| `permission/`         | `PermissionViewSet`    | `permission-list`   |
| `permission/<str:pk>` | `PermissionViewSet`    | `permission-detail` |
| `address/`            | `AddressViewSet`       | `address-list`      |
| `address/<str:pk>`    | `AddressViewSet`       | `address-detail`    |
| `citation/`           | `CitationViewSet`      | `citation-list`     |
| `citation/<str:pk>`   | `CitationViewSet`      | `citation-detail`   |
| `event/`              | `EventViewSet`         | `event-list`        |
| `event/<str:pk>`      | `EventViewSet`         | `event-detail`      |
| `family/`             | `FamilyViewSet`        | `family-list`       |
| `family/<str:pk>`     | `FamilyViewSet`        | `family-detail`     |
| `media/`              | `MediaViewSet`         | `media-list`        |
| `media/<str:pk>`      | `MediaViewSet`         | `media-detail`      |
| `name/`               | `NameViewSet`          | `name-list`         |
| `name/<str:pk>`       | `NameViewSet`          | `name-detail`       |
| `note/`               | `NoteViewSet`          | `note-list`         |
| `note/<str:pk>`       | `NoteViewSet`          | `note-detail`       |
| `person/`             | `PersonViewSet`        | `person-list`       |
| `person/<str:pk>`     | `PersonViewSet`        | `person-detail`     |
| `place/`              | `PlaceViewSet`         | `place-list`        |
| `place/<str:pk>`      | `PlaceViewSet`         | `place-detail`      |
| `repository/`         | `RepositoryViewSet`    | `repository-list`   |
| `repository/<str:pk>` | `RepositoryViewSet`    | `repository-detail` |
| `source/`             | `SourceViewSet`        | `source-list`       |
| `source/<str:pk>`     | `SourceViewSet`        | `source-detail`     |
| `tag/`                | `TagViewSet`           | `tag-list`          |
| `tag/<str:pk>`        | `TagViewSet`           | `tag-detail`        |
| `url/`                | `URLViewSet`           | `url-list`          |
| `url/<str:pk>`        | `URLViewSet`           | `url-detail`        |
"""

from rest_framework import routers

from . import views

app_name = 'gen_rest_api'

# Automatically generate URL definitions using a REST API router
# See module docstring for the resulting definitions
router = routers.SimpleRouter()
router.register(r'tree', views.TreeViewSet),
router.register(r'permission', views.TreePermissionViewSet),
router.register(r'address', views.AddressViewSet),
router.register(r'citation', views.CitationViewSet),
router.register(r'event', views.EventViewSet),
router.register(r'family', views.FamilyViewSet),
router.register(r'media', views.MediaViewSet),
router.register(r'name', views.NameViewSet),
router.register(r'note', views.NoteViewSet),
router.register(r'person', views.PersonViewSet),
router.register(r'place', views.PlaceViewSet),
router.register(r'repository', views.RepositoryViewSet),
router.register(r'source', views.SourceViewSet),
router.register(r'tag', views.TagViewSet),
router.register(r'url', views.URLViewSet),
urlpatterns = router.urls
