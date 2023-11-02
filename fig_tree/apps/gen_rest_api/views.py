"""
The `views` module defines classes for rendering templates based on incoming
HTTP requests. View classes are responsible for processing form/request data,
interacting with database models/serializers, managing application business
logic, and returning rendered HTTP responses.

Whenever possible, generic base classes are used to implement common behavior
for HTTP request handling.
"""

from django.db.models import Subquery, Manager, Q
from rest_framework import mixins, viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import *
from .permissions import *
from .serializers import *

__all__ = [
    'TreeViewSet',
    'TreePermissionViewSet',
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


# -----------------------------------------------------------------------------
# ViewSets for family trees and their associated user permissions
# -----------------------------------------------------------------------------

class TreeViewSet(BaseViewSet):
    """ViewSet for CRUD operations on `Tree` records"""

    serializer_class = TreeSerializer
    queryset = Tree.objects
    permission_classes = (IsAuthenticated, IsTreeMember)

    def get_queryset(self) -> Manager:
        """Return the filtered queryset used by the API endpoint to execute DB queries

        Records are only returned where the requesting user has `read` permissions or higher.
        """

        return self.queryset.filter(
            treepermission__user=self.request.user.pk,
            treepermission__role__gte=TreePermission.Role.READ)

    def create(self, request, *args, **kwargs):
        """Create a new Family Tree

        The user crating the tree is automatically granted admin 
        """

        serializer = TreeSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Create a new tree object and give the submitting user admin tree permissions
        tree_obj = serializer.create(serializer.validated_data)
        treepermission_obj = TreePermission(user=request.user, tree=tree_obj, role=TreePermission.Role.ADMIN)
        treepermission_obj.save()

        # Return the same response data/header as the parent class `create` method
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class TreePermissionViewSet(BaseViewSet):
    """ViewSet for CRUD operations on `TreePermission` records"""

    serializer_class = TreePermissionSerializer
    queryset = TreePermission.objects
    permission_classes = (IsAuthenticated, IsTreePermissionObjectAdmin)

    def get_queryset(self) -> Manager:
        """Return the filtered queryset used by the API endpoint to execute DB queries

        Records are only returned where the requesting user has `admin` permissions or higher.
        """

        # Return all permission objects related to family trees where the user is an admin
        tree_ids = TreePermission.objects.filter(
            user=self.request.user.pk,
            role__gte=TreePermission.Role.ADMIN
        ).values('tree_id')

        return self.queryset.filter(tree_id__in=Subquery(tree_ids))


# -----------------------------------------------------------------------------
# ViewSets for individual genealogical record types
# -----------------------------------------------------------------------------


class BaseRecordViewSet(BaseViewSet):
    """Base ViewSet used to build REST endpoints for genealogical record types

    This class modifies the class level queryset by limiting the records
    returned during list operations. Records are only returned where the user
    has appropriate permissions on the parent family tree.
    """

    def get_queryset(self) -> Manager:
        """Filter the class level `queryset` attribute based on user tree permissions"""

        user = self.request.user  # Assume the request is made from an authenticated session
        return self.queryset.filter(
            Q(
                tree__treepermission__user=user,
                tree__treepermission__role__gte=TreePermission.Role.READ_PRIVATE,
            ) | Q(
                tree__treepermission__user=user,
                tree__treepermission__role__gte=TreePermission.Role.READ,
                private=False
            )
        )


class AddressViewSet(BaseRecordViewSet):
    """ViewSet for CRUD operations on `Address` records"""

    serializer_class = AddressSerializer
    queryset = Address.objects
    permission_classes = (IsAuthenticated, FamilyTreeObjectPermission,)


class CitationViewSet(BaseRecordViewSet):
    """ViewSet for CRUD operations on `Citation` records"""

    serializer_class = CitationSerializer
    queryset = Citation.objects
    permission_classes = (IsAuthenticated, FamilyTreeObjectPermission)


class EventViewSet(BaseRecordViewSet):
    """ViewSet for CRUD operations on `Event` records"""

    serializer_class = EventSerializer
    queryset = Event.objects
    permission_classes = (IsAuthenticated, FamilyTreeObjectPermission)


class FamilyViewSet(BaseRecordViewSet):
    """ViewSet for CRUD operations on `Family` records"""

    serializer_class = FamilySerializer
    queryset = Family.objects
    permission_classes = (IsAuthenticated, FamilyTreeObjectPermission)


class MediaViewSet(BaseRecordViewSet):
    """ViewSet for CRUD operations on `Media` records"""

    serializer_class = MediaSerializer
    queryset = Media.objects
    permission_classes = (IsAuthenticated, FamilyTreeObjectPermission)


class NameViewSet(BaseRecordViewSet):
    """ViewSet for CRUD operations on `Name` records"""

    serializer_class = NameSerializer
    queryset = Name.objects
    permission_classes = (IsAuthenticated, FamilyTreeObjectPermission)


class NoteViewSet(BaseRecordViewSet):
    """ViewSet for CRUD operations on `Note` records"""

    serializer_class = NoteSerializer
    queryset = Note.objects
    permission_classes = (IsAuthenticated, FamilyTreeObjectPermission)


class PersonViewSet(BaseRecordViewSet):
    """ViewSet for CRUD operations on `Person` records"""

    serializer_class = PersonSerializer
    queryset = Person.objects
    permission_classes = (IsAuthenticated, FamilyTreeObjectPermission)


class PlaceViewSet(BaseRecordViewSet):
    """ViewSet for CRUD operations on `Place` records"""

    serializer_class = PlaceSerializer
    queryset = Place.objects
    permission_classes = (IsAuthenticated, FamilyTreeObjectPermission)


class RepositoryViewSet(BaseRecordViewSet):
    """ViewSet for CRUD operations on `Repository` records"""

    serializer_class = RepositorySerializer
    queryset = Repository.objects
    permission_classes = (IsAuthenticated, FamilyTreeObjectPermission)


class SourceViewSet(BaseRecordViewSet):
    """ViewSet for CRUD operations on `Source` records"""

    serializer_class = SourceSerializer
    queryset = Source.objects
    permission_classes = (IsAuthenticated, FamilyTreeObjectPermission)


class TagViewSet(BaseRecordViewSet):
    """ViewSet for CRUD operations on `Tag` records"""

    serializer_class = TagSerializer
    queryset = Tag.objects
    permission_classes = (IsAuthenticated, FamilyTreeObjectPermission)


class URLViewSet(BaseRecordViewSet):
    """ViewSet for CRUD operations on `URL` records"""

    serializer_class = URLSerializer
    queryset = URL.objects
    permission_classes = (IsAuthenticated, FamilyTreeObjectPermission)