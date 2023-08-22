"""Database models for constructing and executing database queries.

The ``models`` module uses data classes to define and interact with the
application database schema. Each model class reflects the schema for a
distinct database table and provides a high-level API to query and interact
with table data.
"""

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import AuthUserManager


class AuthUser(AbstractBaseUser, PermissionsMixin):
    """Custom model for user account data"""

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    username = models.CharField(max_length=50, unique=True, null=False)
    email = models.EmailField(_('email address'), unique=True, null=False)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=100, null=False)
    date_joined = models.DateTimeField(default=timezone.now, null=False)
    is_active = models.BooleanField(default=True, null=False)
    is_staff = models.BooleanField(default=False, null=False)
    is_super_user = models.BooleanField(default=False, null=False)

    objects = AuthUserManager()
