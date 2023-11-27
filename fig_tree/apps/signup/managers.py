"""
The `managers` module defines custom model managers for encapsulating common
query logic. Managers are attached to database models to extend a model's
default querying capabilities and to facilitate common data retrieval tasks.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from django.contrib import auth
from django.contrib.auth import base_user
from django.core import validators

if TYPE_CHECKING:  # Protect against circular import
    from .models import AuthUser

__all__ = ['AuthUserManager']


class AuthUserManager(auth.base_user.BaseUserManager):
    """Custom user model manager

    Regular user accounts are set to an inactive state by default. This is the
    opposite of staff and superuser accounts, which default to being active.
    """

    @staticmethod
    def create_user(username: str, password: str, email: str, **extra_fields) -> AuthUser:
        """Create a new user with the given email and password"""

        validators.validate_email(email)

        user_model = auth.get_user_model()
        user = user_model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    @classmethod
    def create_staff_user(cls, username: str, password: str, email: str, **extra_fields) -> AuthUser:
        """Create a new staff user with the given email and password"""

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have `is_staff` set to `True`.')

        return cls.create_user(username, password, email, **extra_fields)

    @classmethod
    def create_superuser(cls, username: str, password: str, email: str, **extra_fields) -> AuthUser:
        """Create a new superuser with the given email and password"""

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have `is_staff` set to `True`.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have `is_superuser` set to `True`.')

        return cls.create_user(username, password, email, **extra_fields)
