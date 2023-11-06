"""
The `views` module defines classes for rendering templates based on incoming
HTTP requests. View classes are responsible for processing form/request data,
interacting with database models/serializers, managing application business
logic, and returning rendered HTTP responses.

Whenever possible, generic base classes are used to implement common behavior
for HTTP request handling.
"""

from django.db.models import Manager, Q
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

import apps.family_trees.permissions as tree_permissions
from .models import *
from .serializers import *

__all__ = [
    'AddressViewSet',
    'CitationViewSet',
    'EventViewSet',
    'FamilyViewSet',
    'MediaViewSet',
    'NameViewSet',
    'NoteViewSet',
    'PersonViewSet',
    'PlaceViewSet',
    'RepositoryViewSet',
    'SourceViewSet',
    'TagViewSet',
    'URLViewSet',
]


class BaseViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    """
    Base ViewSet providing `list`, `create`, `retrieve`, `update`, and `delete` actions.

    To use this class, inherit it and set the `queryset` and `serializer_class` attributes.
    """


class BaseRecordViewSet(BaseViewSet):
    """Base ViewSet used to build REST endpoints for genealogical record types

    This class modifies the class level queryset by limiting the records
    returned during list operations. Records are only returned where the user
    has appropriate permissions on the parent family tree.
    """

    permission_classes = (IsAuthenticated, tree_permissions.FamilyTreeObjectPermission,)

    def get_queryset(self) -> Manager:
        """Filter the class level `queryset` attribute based on user tree permissions"""

        user = self.request.user  # Assume the request is made from an authenticated session
        return self.queryset.filter(
            Q(
                tree__treepermission__user=user,
                tree__treepermission__role__gte=tree_permissions.TreePermission.Role.READ_PRIVATE,
            ) | Q(
                tree__treepermission__user=user,
                tree__treepermission__role__gte=tree_permissions.TreePermission.Role.READ,
                private=False
            )
        )


class AddressViewSet(BaseRecordViewSet):
    """ViewSet for CRUD operations on `Address` records"""

    serializer_class = AddressSerializer
    queryset = Address.objects


class CitationViewSet(BaseRecordViewSet):
    """ViewSet for CRUD operations on `Citation` records"""

    serializer_class = CitationSerializer
    queryset = Citation.objects


class EventViewSet(BaseRecordViewSet):
    """ViewSet for CRUD operations on `Event` records"""

    serializer_class = EventSerializer
    queryset = Event.objects


class FamilyViewSet(BaseRecordViewSet):
    """ViewSet for CRUD operations on `Family` records"""

    serializer_class = FamilySerializer
    queryset = Family.objects


class MediaViewSet(BaseRecordViewSet):
    """ViewSet for CRUD operations on `Media` records"""

    serializer_class = MediaSerializer
    queryset = Media.objects


class NameViewSet(BaseRecordViewSet):
    """ViewSet for CRUD operations on `Name` records"""

    serializer_class = NameSerializer
    queryset = Name.objects


class NoteViewSet(BaseRecordViewSet):
    """ViewSet for CRUD operations on `Note` records"""

    serializer_class = NoteSerializer
    queryset = Note.objects


class PersonViewSet(BaseRecordViewSet):
    """ViewSet for CRUD operations on `Person` records"""

    serializer_class = PersonSerializer
    queryset = Person.objects


class PlaceViewSet(BaseRecordViewSet):
    """ViewSet for CRUD operations on `Place` records"""

    serializer_class = PlaceSerializer
    queryset = Place.objects


class RepositoryViewSet(BaseRecordViewSet):
    """ViewSet for CRUD operations on `Repository` records"""

    serializer_class = RepositorySerializer
    queryset = Repository.objects


class SourceViewSet(BaseRecordViewSet):
    """ViewSet for CRUD operations on `Source` records"""

    serializer_class = SourceSerializer
    queryset = Source.objects


class TagViewSet(BaseRecordViewSet):
    """ViewSet for CRUD operations on `Tag` records"""

    serializer_class = TagSerializer
    queryset = Tag.objects


class URLViewSet(BaseRecordViewSet):
    """ViewSet for CRUD operations on `URL` records"""

    serializer_class = URLSerializer
    queryset = URL.objects
