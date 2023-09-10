"""
The ``urls`` module maps URL endpoints to django views defined by the parent
application. For root level URL routing, see the project level ``urls`` module.
View objects can be found in the ``views`` module.

# URL Routing Configuration

| URL                   | View                   | Name                |
|-----------------------|------------------------|---------------------|
| `address`             | `AddressListView`      | `address-list`      |
| `address/<str:id>`    | `AddressDetailView`    | `address-detail`    |
| `citation`            | `CitationListView`     | `citation-list`     |
| `citation/<str:id>`   | `CitationDetailView`   | `citation-detail`   |
| `event`               | `EventListView`        | `event-list`        |
| `event/<str:id>`      | `EventDetailView`      | `event-detail`      |
| `family`              | `FamilyListView`       | `family-list`       |
| `family/<str:id>`     | `FamilyDetailView`     | `family-detail`     |
| `media`               | `MediaListView`        | `media-list`        |
| `media/<str:id>`      | `MediaDetailView`      | `media-detail`      |
| `name`                | `NameListView`         | `name-list`         |
| `name/<str:id>`       | `NameDetailView`       | `name-detail`       |
| `note`                | `NoteListView`         | `note-list`         |
| `note/<str:id>`       | `NoteDetailView`       | `note-detail`       |
| `person`              | `PersonListView`       | `person-list`       |
| `person/<str:id>`     | `PersonDetailView`     | `person-detail`     |
| `place`               | `PlaceListView`        | `place-list`        |
| `place/<str:id>`      | `PlaceDetailView`      | `place-detail`      |
| `repository`          | `RepositoryListView`   | `repository-list`   |
| `repository/<str:id>` | `RepositoryDetailView` | `repository-detail` |
| `source`              | `SourceListView`       | `source-list`       |
| `source/<str:id>`     | `SourceDetailView`     | `source-detail`     |
| `tag`                 | `TagListView`          | `tag-list`          |
| `tag/<str:id>`        | `TagDetailView`        | `tag-detail`        |
| `url`                 | `URLListView`          | `url-list`          |
| `url/<str:id>`        | `URLDetailView`        | `url-detail`        |
"""

from django.urls import path

from . import views

app_name = 'gen_rest_api'

urlpatterns = [
    path('address', views.AddressListView.as_view(), name='address-list'),
    path('address/<str:id>', views.AddressDetailView.as_view(), name='address-detail'),
    path('citation', views.CitationListView.as_view(), name='citation-list'),
    path('citation/<str:id>', views.CitationDetailView.as_view(), name='citation-detail'),
    path('event', views.EventListView.as_view(), name='event-list'),
    path('event/<str:id>', views.EventDetailView.as_view(), name='event-detail'),
    path('family', views.FamilyListView.as_view(), name='family-list'),
    path('family/<str:id>', views.FamilyDetailView.as_view(), name='family-detail'),
    path('media', views.MediaListView.as_view(), name='media-list'),
    path('media/<str:id>', views.MediaDetailView.as_view(), name='media-detail'),
    path('name', views.NameListView.as_view(), name='name-list'),
    path('name/<str:id>', views.NameDetailView.as_view(), name='name-detail'),
    path('note', views.NoteListView.as_view(), name='note-list'),
    path('note/<str:id>', views.NoteDetailView.as_view(), name='note-detail'),
    path('person', views.PersonListView.as_view(), name='person-list'),
    path('person/<str:id>', views.PersonDetailView.as_view(), name='person-detail'),
    path('place', views.PlaceListView.as_view(), name='place-list'),
    path('place/<str:id>', views.PlaceDetailView.as_view(), name='place-detail'),
    path('repository', views.RepositoryListView.as_view(), name='repository-list'),
    path('repository/<str:id>', views.RepositoryDetailView.as_view(), name='repository-detail'),
    path('source', views.SourceListView.as_view(), name='source-list'),
    path('source/<str:id>', views.SourceDetailView.as_view(), name='source-detail'),
    path('tag', views.TagListView.as_view(), name='tag-list'),
    path('tag/<str:id>', views.TagDetailView.as_view(), name='tag-detail'),
    path('url', views.URLListView.as_view(), name='url-list'),
    path('url/<str:id>', views.URLDetailView.as_view(), name='url-detail'),
]
