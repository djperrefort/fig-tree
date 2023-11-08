"""
The `models` module uses data classes to define and interact with the
application database schema. Each model class reflects the schema for a
distinct database table and provides a high-level API to query and interact
with table data.
"""

from __future__ import annotations

from django.contrib import auth
from django.db import models
from django.utils.translation import gettext_lazy as _

__all__ = [
    'FamilyTree',
    'TreePermission',
    'FamilyTreeModelMixin',
]


class FamilyTree(models.Model):
    """Database model used to group records together into family trees"""

    tree_name = models.CharField('Name', max_length=50)
    last_modified = models.DateTimeField(auto_now=True)
    private = models.BooleanField(default=True)

    def __str__(self) -> str:
        """Return the name of the family tree"""

        return self.tree_name


class TreePermission(models.Model):
    """User permissions for family trees"""

    class Meta:
        unique_together = (('tree', 'user',),)

    class Role(models.IntegerChoices):
        """User roles for facilitating RBAC"""

        READ = 10, _('read')
        READ_PRIVATE = 20, _('private')
        WRITE = 30, _('write')
        ADMIN = 40, _('admin')

    tree = models.ForeignKey(FamilyTree, db_index=True, on_delete=models.CASCADE)
    user = models.ForeignKey(auth.get_user_model(), db_index=True, on_delete=models.CASCADE)
    role = models.IntegerField(choices=Role.choices, default='read')
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """Return the permission level, username, and username and permission """

        return f'{self.role} permissions for {self.user} on {self.tree}'


class FamilyTreeModelMixin:
    """Model mixin class that adds the columns necessary to support family tree permissions"""

    private = models.BooleanField(default=True)
    last_modified = models.DateTimeField(auto_now=True)
    tree = models.ForeignKey(FamilyTree, db_index=True, on_delete=models.CASCADE)
