"""Application level URL routing.

The ``urls`` module maps URL endpoints to django views defined by the parent
application. For root level URL routing, see the project level ``urls`` module.
View objects can be found in the ``views`` module.

URL Routing Configuration
-------------------------

+-------------------------+--------------------------+------------------------+
| URL                     | View                     | Name                   |
+=========================+==========================+========================+
| ``address``             | ``AddressListView``      | ``address_list``       |
+-------------------------+--------------------------+------------------------+
| ``address/<str:id>``    | ``AddressDetailView``    | ``address_detail``     |
+-------------------------+--------------------------+------------------------+
| ``citation``            | ``CitationListView``     | ``citation_list``      |
+-------------------------+--------------------------+------------------------+
| ``citation/<str:id>``   | ``CitationDetailView``   | ``citation_detail``    |
+-------------------------+--------------------------+------------------------+
| ``event``               | ``EventListView``        | ``event_list``         |
+-------------------------+--------------------------+------------------------+
| ``event/<str:id>``      | ``EventDetailView``      | ``event_detail``       |
+-------------------------+--------------------------+------------------------+
| ``family``              | ``FamilyListView``       | ``family_list``        |
+-------------------------+--------------------------+------------------------+
| ``family/<str:id>``     | ``FamilyDetailView``     | ``family_detail``      |
+-------------------------+--------------------------+------------------------+
| ``media``               | ``MediaListView``        | ``media_list``         |
+-------------------------+--------------------------+------------------------+
| ``media/<str:id>``      | ``MediaDetailView``      | ``media_detail``       |
+-------------------------+--------------------------+------------------------+
| ``name``                | ``NameListView``         | ``name_list``          |
+-------------------------+--------------------------+------------------------+
| ``name/<str:id>``       | ``NameDetailView``       | ``name_detail``        |
+-------------------------+--------------------------+------------------------+
| ``note``                | ``NoteListView``         | ``note_list``          |
+-------------------------+--------------------------+------------------------+
| ``note/<str:id>``       | ``NoteDetailView``       | ``note_detail``        |
+-------------------------+--------------------------+------------------------+
| ``person``              | ``PersonListView``       | ``person_list``        |
+-------------------------+--------------------------+------------------------+
| ``person/<str:id>``     | ``PersonDetailView``     | ``person_detail``      |
+-------------------------+--------------------------+------------------------+
| ``place``               | ``PlaceListView``        | ``place_list``         |
+-------------------------+--------------------------+------------------------+
| ``place/<str:id>``      | ``PlaceDetailView``      | ``place_detail``       |
+-------------------------+--------------------------+------------------------+
| ``repository``          | ``RepositoryListView``   | ``repository_list``    |
+-------------------------+--------------------------+------------------------+
| ``repository/<str:id>`` | ``RepositoryDetailView`` | ``repository_detail``  |
+-------------------------+--------------------------+------------------------+
| ``source``              | ``SourceListView``       | ``source_list``        |
+-------------------------+--------------------------+------------------------+
| ``source/<str:id>``     | ``SourceDetailView``     | ``source_detail``      |
+-------------------------+--------------------------+------------------------+
| ``tag``                 | ``TagListView``          | ``tag_list``           |
+-------------------------+--------------------------+------------------------+
| ``tag/<str:id>``        | ``TagDetailView``        | ``tag_detail``         |
+-------------------------+--------------------------+------------------------+
| ``url``                 | ``URLListView``          | ``url_list``           |
+-------------------------+--------------------------+------------------------+
| ``url/<str:id>``        | ``URLDetailView``        | ``url_detail``         |
+-------------------------+--------------------------+------------------------+
"""

from django.urls import path

from . import views

app_name = 'data_api'

urlpatterns = [
    path('address', views.AddressListView.as_view(), name='address_list'),
    path('address/<str:id>', views.AddressDetailView.as_view(), name='address_detail'),
    path('citation', views.CitationListView.as_view(), name='citation_list'),
    path('citation/<str:id>', views.CitationDetailView.as_view(), name='citation_detail'),
    path('event', views.EventListView.as_view(), name='event_list'),
    path('event/<str:id>', views.EventDetailView.as_view(), name='event_detail'),
    path('family', views.FamilyListView.as_view(), name='family_list'),
    path('family/<str:id>', views.FamilyDetailView.as_view(), name='family_detail'),
    path('media', views.MediaListView.as_view(), name='media_list'),
    path('media/<str:id>', views.MediaDetailView.as_view(), name='media_detail'),
    path('name', views.NameListView.as_view(), name='name_list'),
    path('name/<str:id>', views.NameDetailView.as_view(), name='name_detail'),
    path('note', views.NoteListView.as_view(), name='note_list'),
    path('note/<str:id>', views.NoteDetailView.as_view(), name='note_detail'),
    path('person', views.PersonListView.as_view(), name='person_list'),
    path('person/<str:id>', views.PersonDetailView.as_view(), name='person_detail'),
    path('place', views.PlaceListView.as_view(), name='place_list'),
    path('place/<str:id>', views.PlaceDetailView.as_view(), name='place_detail'),
    path('repository', views.RepositoryListView.as_view(), name='repository_list'),
    path('repository/<str:id>', views.RepositoryDetailView.as_view(), name='repository_detail'),
    path('source', views.SourceListView.as_view(), name='source_list'),
    path('source/<str:id>', views.SourceDetailView.as_view(), name='source_detail'),
    path('tag', views.TagListView.as_view(), name='tag_list'),
    path('tag/<str:id>', views.TagDetailView.as_view(), name='tag_detail'),
    path('url', views.URLListView.as_view(), name='url_list'),
    path('url/<str:id>', views.URLDetailView.as_view(), name='url_detail'),
]
