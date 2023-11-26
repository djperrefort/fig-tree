"""
The `urls` module maps URL endpoints to django views defined in the parent
application. For root level URL routing, see the project level `urls` module.
View objects can be found in the `views` module.

# URL Routing Configuration

| URL                   | View / View Set         | Name               |
|-----------------------|------------------------|---------------------|
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

from .views import *

app_name = 'gen_data'

router = routers.SimpleRouter()
router.register(r'address', AddressViewSet)
router.register(r'citation', CitationViewSet)
router.register(r'event', EventViewSet)
router.register(r'family', FamilyViewSet)
router.register(r'media', MediaViewSet)
router.register(r'name', NameViewSet)
router.register(r'person', PersonViewSet)
router.register(r'place', PlaceViewSet)
router.register(r'repository', RepositoryViewSet)
router.register(r'source', SourceViewSet)
router.register(r'tag', TagViewSet)
router.register(r'url', URLViewSet)
urlpatterns = router.urls
