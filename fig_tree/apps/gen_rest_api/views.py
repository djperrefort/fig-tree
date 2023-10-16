"""
The `views` module defines classes for rendering templates based on incoming
HTTP requests. View classes are responsible for processing form/request data,
interacting with database models/serializers, managing application business
logic, and returning rendered HTTP responses.

Whenever possible, generic base classes are used to implement common behavior
for HTTP request handling.
"""

from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from . import models, serializers, permissions


class BaseViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    """
    Base viewset providing `list`, `create`, `retrieve`, `update`, and `delete` actions.

    To use this class, inherit it and set the `queryset` and `serializer_class` attributes.
    """


class AddressViewSet(BaseViewSet):
    """View set for CRUD operations on `Address` records"""

    serializer_class = serializers.AddressSerializer
    queryset = models.Address.objects
    permission_classes = (permissions.FamilyTreeObjectPermission,)


class CitationViewSet(BaseViewSet):
    """View set for CRUD operations on `Citation` records"""

    serializer_class = serializers.CitationSerializer
    queryset = models.Citation.objects
    permission_classes = (IsAuthenticated, permissions.FamilyTreeObjectPermission)


class EventViewSet(BaseViewSet):
    """View set for CRUD operations on `Event` records"""

    serializer_class = serializers.EventSerializer
    queryset = models.Event.objects
    permission_classes = (IsAuthenticated, permissions.FamilyTreeObjectPermission)


class FamilyViewSet(BaseViewSet):
    """View set for CRUD operations on `Family` records"""

    serializer_class = serializers.FamilySerializer
    queryset = models.Family.objects
    permission_classes = (IsAuthenticated, permissions.FamilyTreeObjectPermission)


class MediaViewSet(BaseViewSet):
    """View set for CRUD operations on `Media` records"""

    serializer_class = serializers.MediaSerializer
    queryset = models.Media.objects
    permission_classes = (IsAuthenticated, permissions.FamilyTreeObjectPermission)


class NameViewSet(BaseViewSet):
    """View set for CRUD operations on `Name` records"""

    serializer_class = serializers.NameSerializer
    queryset = models.Name.objects
    permission_classes = (IsAuthenticated, permissions.FamilyTreeObjectPermission)


class NoteViewSet(BaseViewSet):
    """View set for CRUD operations on `Note` records"""

    serializer_class = serializers.NoteSerializer
    queryset = models.Note.objects
    permission_classes = (IsAuthenticated, permissions.FamilyTreeObjectPermission)


class PersonViewSet(BaseViewSet):
    """View set for CRUD operations on `Person` records"""

    serializer_class = serializers.PersonSerializer
    queryset = models.Person.objects
    permission_classes = (IsAuthenticated, permissions.FamilyTreeObjectPermission)


class PlaceViewSet(BaseViewSet):
    """View set for CRUD operations on `Place` records"""

    serializer_class = serializers.PlaceSerializer
    queryset = models.Place.objects
    permission_classes = (IsAuthenticated, permissions.FamilyTreeObjectPermission)


class RepositoryViewSet(BaseViewSet):
    """View set for CRUD operations on `Repository` records"""

    serializer_class = serializers.RepositorySerializer
    queryset = models.Repository.objects
    permission_classes = (IsAuthenticated, permissions.FamilyTreeObjectPermission)


class SourceViewSet(BaseViewSet):
    """View set for CRUD operations on `Source` records"""

    serializer_class = serializers.SourceSerializer
    queryset = models.Source.objects
    permission_classes = (IsAuthenticated, permissions.FamilyTreeObjectPermission)


class TagViewSet(BaseViewSet):
    """View set for CRUD operations on `Tag` records"""

    serializer_class = serializers.TagSerializer
    queryset = models.Tag.objects
    permission_classes = (IsAuthenticated, permissions.FamilyTreeObjectPermission)


class URLViewSet(BaseViewSet):
    """View set for CRUD operations on `URL` records"""

    serializer_class = serializers.URLSerializer
    queryset = models.URL.objects
    permission_classes = (IsAuthenticated, permissions.FamilyTreeObjectPermission)
