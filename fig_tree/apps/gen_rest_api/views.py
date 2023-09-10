"""
The ``views`` module defines classes for handling incoming HTTP requests.
Each view class is responsible for processing of form/request data, interacting
with database models/serializers, managing application business logic, and
returning rendered HTTP responses.

Whenever possible, generic base classes are used to implement common behavior
for HTTP request handling.
"""

from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from . import models
from . import serializers


class AddressListView(ListAPIView):
    """Read-only view for fetching multiple ``Address`` records"""

    serializer_class = serializers.AddressSerializer
    queryset = models.Address.objects.all()


class AddressDetailView(RetrieveUpdateDestroyAPIView):
    """Read/write view for CRUD operations on a single ``Address`` record"""

    serializer_class = serializers.AddressSerializer
    queryset = models.Address.objects.all()


class CitationListView(ListAPIView):
    """Read-only view for fetching multiple ``Citation`` records"""

    serializer_class = serializers.CitationSerializer
    queryset = models.Citation.objects.all()


class CitationDetailView(RetrieveUpdateDestroyAPIView):
    """Read/write view for CRUD operations on a single ``Citation`` record"""

    serializer_class = serializers.CitationSerializer
    queryset = models.Citation.objects.all()


class EventListView(ListAPIView):
    """Read-only view for fetching multiple ``Event`` records"""

    serializer_class = serializers.EventSerializer
    queryset = models.Event.objects.all()


class EventDetailView(RetrieveUpdateDestroyAPIView):
    """Read/write view for CRUD operations on a single ``Event`` record"""

    serializer_class = serializers.EventSerializer
    queryset = models.Event.objects.all()


class FamilyListView(ListAPIView):
    """Read-only view for fetching multiple ``Family`` records"""

    serializer_class = serializers.FamilySerializer
    queryset = models.Family.objects.all()


class FamilyDetailView(RetrieveUpdateDestroyAPIView):
    """Read/write view for CRUD operations on a single ``Family`` record"""

    serializer_class = serializers.FamilySerializer
    queryset = models.Family.objects.all()


class MediaListView(ListAPIView):
    """Read-only view for fetching multiple ``Media`` records"""

    serializer_class = serializers.MediaSerializer
    queryset = models.Media.objects.all()


class MediaDetailView(RetrieveUpdateDestroyAPIView):
    """Read/write view for CRUD operations on a single ``Media`` record"""

    serializer_class = serializers.MediaSerializer
    queryset = models.Media.objects.all()


class NameListView(ListAPIView):
    """Read-only view for fetching multiple ``Name`` records"""

    serializer_class = serializers.NameSerializer
    queryset = models.Name.objects.all()


class NameDetailView(RetrieveUpdateDestroyAPIView):
    """Read/write view for CRUD operations on a single ``Name`` record"""

    serializer_class = serializers.NameSerializer
    queryset = models.Name.objects.all()


class NoteListView(ListAPIView):
    """Read-only view for fetching multiple ``Note`` records"""

    serializer_class = serializers.NoteSerializer
    queryset = models.Note.objects.all()


class NoteDetailView(RetrieveUpdateDestroyAPIView):
    """Read/write view for CRUD operations on a single ``Note`` record"""

    serializer_class = serializers.NoteSerializer
    queryset = models.Note.objects.all()


class PersonListView(ListAPIView):
    """Read-only view for fetching multiple ``Person`` records"""

    serializer_class = serializers.PersonSerializer
    queryset = models.Person.objects.all()


class PersonDetailView(RetrieveUpdateDestroyAPIView):
    """Read/write view for CRUD operations on a single ``Person`` record"""

    serializer_class = serializers.PersonSerializer
    queryset = models.Person.objects.all()


class PlaceListView(ListAPIView):
    """Read-only view for fetching multiple ``Place`` records"""

    serializer_class = serializers.PlaceSerializer
    queryset = models.Place.objects.all()


class PlaceDetailView(RetrieveUpdateDestroyAPIView):
    """Read/write view for CRUD operations on a single ``Place`` record"""

    serializer_class = serializers.PlaceSerializer
    queryset = models.Place.objects.all()


class RepositoryListView(ListAPIView):
    """Read-only view for fetching multiple ``Repository`` records"""

    serializer_class = serializers.RepositorySerializer
    queryset = models.Repository.objects.all()


class RepositoryDetailView(RetrieveUpdateDestroyAPIView):
    """Read/write view for CRUD operations on a single ``Repository`` record"""

    serializer_class = serializers.RepositorySerializer
    queryset = models.Repository.objects.all()


class SourceListView(ListAPIView):
    """Read-only view for fetching multiple ``Source`` records"""

    serializer_class = serializers.SourceSerializer
    queryset = models.Source.objects.all()


class SourceDetailView(RetrieveUpdateDestroyAPIView):
    """Read/write view for CRUD operations on a single ``Source`` record"""

    serializer_class = serializers.SourceSerializer
    queryset = models.Source.objects.all()


class TagListView(ListAPIView):
    """Read-only view for fetching multiple ``Tag`` records"""

    serializer_class = serializers.TagSerializer
    queryset = models.Tag.objects.all()


class TagDetailView(RetrieveUpdateDestroyAPIView):
    """Read/write view for CRUD operations on a single ``Tag`` record"""

    serializer_class = serializers.TagSerializer
    queryset = models.Tag.objects.all()


class URLListView(ListAPIView):
    """Read-only view for fetching multiple ``URL`` records"""

    serializer_class = serializers.URLSerializer
    queryset = models.URL.objects.all()


class URLDetailView(RetrieveUpdateDestroyAPIView):
    """Read/write view for CRUD operations on a single ``URL`` record"""

    serializer_class = serializers.URLSerializer
    queryset = models.URL.objects.all()
