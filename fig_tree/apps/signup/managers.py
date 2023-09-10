"""
The ``managers`` module defines custom model managers for encapsulating common
query logic. Managers can be attached to database models to extend a model's
default querying capabilities and to facilitate common data retrieval tasks.
 Model objects can be found in the ``models`` module.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import BaseUserManager
from django.core.validators import validate_email

if TYPE_CHECKING:  # Protect against circular import
    from .models import AuthUser


class AuthUserManager(BaseUserManager):
    """Custom user model manager

    Regular user accounts are set to an inactive state by default. This is the
    opposite of staff and superuser accounts, which default to being active.
    """

    @staticmethod
    def create_user(username: str, password: str, email: str, **extra_fields) -> AuthUser:
        """Create and save a new user with the given email and password"""

        validate_email(email)

        user_model = get_user_model()
        user = user_model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    @classmethod
    def create_staff_user(cls, username: str, password: str, email: str, **extra_fields) -> AuthUser:
        """Convenience function for creating a new staff user"""

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have ``is_staff`` set to ``True```.')

        return cls.create_user(username, password, email, **extra_fields)

    @classmethod
    def create_superuser(cls, username: str, password: str, email: str, **extra_fields) -> AuthUser:
        """Convenience function for creating a new superuser"""

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have ``is_staff`` set to ``True```.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have ``is_superuser`` set to ``True``.')

        return cls.create_user(username, password, email, **extra_fields)
