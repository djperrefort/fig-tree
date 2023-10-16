"""
The `views` module defines classes for rendering templates based on incoming
HTTP requests. View classes are responsible for processing form/request data,
interacting with database models/serializers, managing application business
logic, and returning rendered HTTP responses.

Whenever possible, generic base classes are used to implement common behavior
for HTTP request handling.
"""

from django.db.models import Subquery, Manager
from rest_framework import mixins, viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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


# -----------------------------------------------------------------------------
# ViewSets for family trees and their associated user permissions
# -----------------------------------------------------------------------------

class TreeViewSet(BaseViewSet):
    """ViewSet for CRUD operations on `Tree` records"""

    serializer_class = serializers.TreeSerializer
    queryset = models.Tree.objects
    permission_classes = (IsAuthenticated, permissions.IsTreeMember)

    def get_queryset(self) -> Manager:
        """Return the filtered queryset used by the API endpoint to execute DB queries

        Records are only returned where the requesting user has `read` permissions or higher.
        """

        return self.queryset.filter(treepermission__user=self.request.user.pk, treepermission__read=True)

    def create(self, request, *args, **kwargs):
        """Create a new Family Tree

        The user crating the tree is automatically granted admin permissions.
        """

        serializer = serializers.TreeSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Create a new tree object and give the submitting user admin tree permissions
        tree_obj = serializer.create(serializer.validated_data)
        treepermission_obj = models.TreePermission(user=request.user, tree=tree_obj, admin=True)
        treepermission_obj.save()

        # Return the same response data/header as the parent class `create` method
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class TreePermissionViewSet(BaseViewSet):
    """ViewSet for CRUD operations on `TreePermission` records"""

    serializer_class = serializers.TreePermissionSerializer
    queryset = models.TreePermission.objects
    permission_classes = (IsAuthenticated, permissions.IsTreePermissionObjectAdmin)

    def get_queryset(self) -> Manager:
        """Return the filtered queryset used by the API endpoint to execute DB queries

        Records are only returned where the requesting user has `admin` permissions or higher.
        """

        # Return all permission objects related to family trees where the user is an admin
        tree_ids = models.TreePermission.objects.filter(user=self.request.user.pk, admin=True).values('tree_id')
        return self.queryset.filter(tree_id__in=Subquery(tree_ids))


# -----------------------------------------------------------------------------
# Viewsets for individual genealogical record types
# -----------------------------------------------------------------------------


class AddressViewSet(BaseViewSet):
    """ViewSet for CRUD operations on `Address` records"""

    serializer_class = serializers.AddressSerializer
    queryset = models.Address.objects
    permission_classes = (permissions.FamilyTreeObjectPermission,)


class CitationViewSet(BaseViewSet):
    """ViewSet for CRUD operations on `Citation` records"""

    serializer_class = serializers.CitationSerializer
    queryset = models.Citation.objects
    permission_classes = (IsAuthenticated, permissions.FamilyTreeObjectPermission)


class EventViewSet(BaseViewSet):
    """ViewSet for CRUD operations on `Event` records"""

    serializer_class = serializers.EventSerializer
    queryset = models.Event.objects
    permission_classes = (IsAuthenticated, permissions.FamilyTreeObjectPermission)


class FamilyViewSet(BaseViewSet):
    """ViewSet for CRUD operations on `Family` records"""

    serializer_class = serializers.FamilySerializer
    queryset = models.Family.objects
    permission_classes = (IsAuthenticated, permissions.FamilyTreeObjectPermission)


class MediaViewSet(BaseViewSet):
    """ViewSet for CRUD operations on `Media` records"""

    serializer_class = serializers.MediaSerializer
    queryset = models.Media.objects
    permission_classes = (IsAuthenticated, permissions.FamilyTreeObjectPermission)


class NameViewSet(BaseViewSet):
    """ViewSet for CRUD operations on `Name` records"""

    serializer_class = serializers.NameSerializer
    queryset = models.Name.objects
    permission_classes = (IsAuthenticated, permissions.FamilyTreeObjectPermission)


class NoteViewSet(BaseViewSet):
    """ViewSet for CRUD operations on `Note` records"""

    serializer_class = serializers.NoteSerializer
    queryset = models.Note.objects
    permission_classes = (IsAuthenticated, permissions.FamilyTreeObjectPermission)


class PersonViewSet(BaseViewSet):
    """ViewSet for CRUD operations on `Person` records"""

    serializer_class = serializers.PersonSerializer
    queryset = models.Person.objects
    permission_classes = (IsAuthenticated, permissions.FamilyTreeObjectPermission)


class PlaceViewSet(BaseViewSet):
    """ViewSet for CRUD operations on `Place` records"""

    serializer_class = serializers.PlaceSerializer
    queryset = models.Place.objects
    permission_classes = (IsAuthenticated, permissions.FamilyTreeObjectPermission)


class RepositoryViewSet(BaseViewSet):
    """ViewSet for CRUD operations on `Repository` records"""

    serializer_class = serializers.RepositorySerializer
    queryset = models.Repository.objects
    permission_classes = (IsAuthenticated, permissions.FamilyTreeObjectPermission)


class SourceViewSet(BaseViewSet):
    """ViewSet for CRUD operations on `Source` records"""

    serializer_class = serializers.SourceSerializer
    queryset = models.Source.objects
    permission_classes = (IsAuthenticated, permissions.FamilyTreeObjectPermission)


class TagViewSet(BaseViewSet):
    """ViewSet for CRUD operations on `Tag` records"""

    serializer_class = serializers.TagSerializer
    queryset = models.Tag.objects
    permission_classes = (IsAuthenticated, permissions.FamilyTreeObjectPermission)


class URLViewSet(BaseViewSet):
    """ViewSet for CRUD operations on `URL` records"""

    serializer_class = serializers.URLSerializer
    queryset = models.URL.objects
    permission_classes = (IsAuthenticated, permissions.FamilyTreeObjectPermission)
