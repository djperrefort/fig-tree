"""
The ``permissions`` module defines permission objects for regulating access
to API endpoints. Permission classes can implement permissions on the level of
individual requests and/or objects (database records).
"""

from django.views import View
from rest_framework.permissions import BasePermission, SAFE_METHODS

from . import models


class IsTreeMember(BasePermission):
    """Object-level permissions for regulating access to `Tree` records

    Access permissions are determined based on the user permissions stored in
    the `TreePermission` database table.

    Read access is given to any user with `read` permissions or higher.
    Write permissions are given to users with `admin` permissions or higher.
    """

    def has_object_permission(self, request, view: View, obj: models.Tree) -> bool:
        """Return whether an incoming request has the necessary permissions

        Args:
            request: The incoming HTTP request
            view: The view used to process the request
            obj: Database model with a ``tree`` attribute

        Return:
            A boolean indicating the success/failure of the permissions check
        """

        permission_record = obj.treepermission_set.filter(user=request.user).first()
        if not permission_record:
            return False

        if request.method in SAFE_METHODS:
            return permission_record.role >= models.TreePermission.Role.READ

        return permission_record.role >= models.TreePermission.Role.ADMIN


class IsTreePermissionObjectAdmin(BasePermission):
    """Object-level permissions for regulating access to `Tree` records

    Access permissions are determined based on the user permissions stored in
    the `TreePermission` database table.

    Access is only granted to the requested object if the user has `admin`
    permissions or higher on the corresponding family tree.
    """

    def has_object_permission(self, request, view: View, obj: models.TreePermission) -> bool:
        """Return whether an incoming request has the necessary permissions

        Args:
            request: The incoming HTTP request
            view: The view used to process the request
            obj: Database model with a ``tree`` attribute

        Return:
            A boolean indicating the success/failure of the permissions check
        """

        permission_record = models.TreePermission.objects.filter(user=request.user.id, tree=obj.tree).first()
        if not permission_record:
            return False

        return permission_record.role >= models.TreePermission.Role.ADMIN


class FamilyTreeObjectPermission(BasePermission):
    """Object-level permissions for generic genealogical records

    Access permissions are determined based on the user permissions stored in
    the `TreePermission` database table.
    """

    def has_object_permission(self, request, view: View, obj: models.BaseRecordModel) -> bool:
        """Return whether a request has permissions to interact with an object

        Args:
            request: The incoming HTTP request
            view: The view used to process the request
            obj: Database model with a ``tree`` attribute

        Returns:
            Whether the request has permission to access the object
        """

        permission_record = obj.tree.treepermission_set.filter(user=request.user.id, tree=obj.tree).first()
        if not permission_record:
            return False

        # Check the user's permission level
        can_read_public = permission_record.role >= models.TreePermission.Role.READ
        can_read_private = permission_record.role >= models.TreePermission.Role.READ_PRIVATE
        can_write = permission_record.role >= models.TreePermission.Role.WRITE

        # Check permissions for read-only operations
        if request.method in SAFE_METHODS:
            return can_read_private or (can_read_public and not permission_record.private)

        # All other operations require write permissions at minimum
        return can_write
