"""Tests for the ``AuthUserManager`` class."""

from django.core.exceptions import ValidationError
from django.test import TestCase

from apps.signup.managers import AuthUserManager


class CreateUser(TestCase):
    """Tests for the creation of new users"""

    def test_default_permission_values(self) -> None:
        """Test users are created without admin permissions"""

        new_user = AuthUserManager.create_user(username='test_user', email='test@user.com', password='foo')
        self.assertFalse(new_user.is_staff, 'User is staff')
        self.assertFalse(new_user.is_superuser, 'User is superuser')
        self.assertTrue(new_user.is_active, 'User is not active')

    def test_error_on_invalid_email(self) -> None:
        """Test a ``ValidationError`` is raised when creating a user with an invalid email"""

        with self.assertRaises(ValidationError, msg='No error raised for blank email'):
            AuthUserManager.create_user(email='', username='test_user', password='foo')

        with self.assertRaises(ValidationError, msg='No error raised for non email string'):
            AuthUserManager.create_user(email='asdf', username='test_user', password='foo')


class CreateSuperUser(TestCase):
    """Tests for the creation of new super-users"""

    def test_has_admin_permissions(self) -> None:
        """Test users are created with admin permissions"""

        new_user = AuthUserManager.create_superuser(username='test_user', email='test@user.com', password='foo')
        self.assertTrue(new_user.is_staff)
        self.assertTrue(new_user.is_superuser)
        self.assertTrue(new_user.is_active)

    def test_error_on_invalid_email(self) -> None:
        """Test a ``ValidationError`` is raised when creating a user with an invalid email"""

        with self.assertRaises(ValidationError, msg='No error raised for blank email'):
            AuthUserManager.create_user(email='', username='test_user', password='foo')

        with self.assertRaises(ValidationError, msg='No error raised for non email string'):
            AuthUserManager.create_user(email='asdf', username='test_user', password='foo')

    def test_error_on_invalid_permission_arguments(self) -> None:
        """Test an error is raised when trying to override superuser permissions via kwargs"""

        with self.assertRaises(ValueError, msg='No error raised for is_superuser=False'):
            AuthUserManager.create_superuser(username='test_user', email='super@user.com', password='foo', is_superuser=False)

        with self.assertRaises(ValueError, msg='No error raised for is_staff=False'):
            AuthUserManager.create_superuser(username='test_user', email='super@user.com', password='foo', is_staff=False)
