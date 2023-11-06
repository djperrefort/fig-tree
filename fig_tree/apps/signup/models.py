"""
The `models` module uses data classes to define and interact with the
application database schema. Each model class reflects the schema for a
distinct database table and provides a high-level API to query and interact
with table data.
"""

import django.contrib.auth.models
from django.contrib import auth
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import *

__all__ = ['AuthUser']


class AuthUser(auth.models.AbstractBaseUser, auth.models.PermissionsMixin):
    """Custom model for user account data"""

    class Meta:
        verbose_name = 'User'

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email', ]

    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_super_user = models.BooleanField(default=False)

    objects = AuthUserManager()
