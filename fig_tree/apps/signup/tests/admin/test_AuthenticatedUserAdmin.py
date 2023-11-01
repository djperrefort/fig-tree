"""Tests for the `AuthenticatedUserAdmin` class."""

from django.contrib import admin
from django.test import TestCase

from apps.signup.models import AuthUser


class AdminRegistration(TestCase):
    """Test the registration of admin models"""

    def test_is_registered(self):
        """Test the user model class has a registered admin class"""

        self.assertTrue(admin.site.is_registered(AuthUser))
