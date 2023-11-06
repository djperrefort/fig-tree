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

from .models import *
from .permissions import *
from .serializers import *

__all__ = [
    'FamilyTreeViewSet',
    'TreePermissionViewSet',
]


class FamilyTreeViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    """ViewSet for CRUD operations on `FamilyTree` records"""

    serializer_class = FamilyTreeSerializer
    queryset = FamilyTree.objects
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

        serializer = FamilyTreeSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Create a new tree object and give the submitting user admin tree permissions
        tree_obj = serializer.create(serializer.validated_data)
        treepermission_obj = TreePermission(user=request.user, tree=tree_obj, role=TreePermission.Role.ADMIN)
        treepermission_obj.save()

        # Return the same response data/header as the parent class `create` method
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class TreePermissionViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
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
