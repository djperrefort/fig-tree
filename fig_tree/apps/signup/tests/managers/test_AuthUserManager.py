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

    def test_user_is_active(self) -> None:
        """Test new user accounts are marked as active"""

        new_user = AuthUserManager.create_user(username='test_user', email='test@user.com', password='foo')
        self.assertTrue(new_user.is_active, 'User is not active')

    def test_user_data(self) -> None:
        """Test user accounts are created with the correct user information"""

        user_data = dict(username='test_user', email='test@user.com', password='foo')
        new_user = AuthUserManager.create_user(**user_data)
        self.assertEqual(new_user.username, user_data['username'])
        self.assertEqual(new_user.email, user_data['email'])

    def test_error_on_invalid_email(self) -> None:
        """Test a ``ValidationError`` is raised when creating a user with an invalid email"""

        with self.assertRaises(ValidationError, msg='No error raised for blank email'):
            AuthUserManager.create_user(email='', username='test_user', password='foo')

        with self.assertRaises(ValidationError, msg='No error raised for non email string'):
            AuthUserManager.create_user(email='asdf', username='test_user', password='foo')


class CreateStaffUser(TestCase):
    """Tests for the creation of new staff users"""

    def test_user_permissions(self) -> None:
        """Test users are created with admin permissions"""

        new_user = AuthUserManager.create_staff_user(username='test_user', email='test@user.com', password='foo')
        self.assertTrue(new_user.is_staff)
        self.assertFalse(new_user.is_superuser)

    def test_user_is_active(self) -> None:
        """Test new user accounts are marked as active"""

        new_user = AuthUserManager.create_staff_user(username='test_user', email='test@user.com', password='foo')
        self.assertTrue(new_user.is_active, 'User is not active')

    def test_user_data(self) -> None:
        """Test user accounts are created with the correct user information"""

        user_data = dict(username='test_user', email='test@user.com', password='foo')
        new_user = AuthUserManager.create_staff_user(**user_data)
        self.assertEqual(new_user.username, user_data['username'])
        self.assertEqual(new_user.email, user_data['email'])


class CreateSuperUser(TestCase):
    """Tests for the creation of new super-users"""

    def test_user_permissions(self) -> None:
        """Test users are created with admin permissions"""

        new_user = AuthUserManager.create_superuser(username='test_user', email='test@user.com', password='foo')
        self.assertTrue(new_user.is_staff)
        self.assertTrue(new_user.is_superuser)

    def test_user_is_active(self) -> None:
        """Test new user accounts are marked as active"""

        new_user = AuthUserManager.create_superuser(username='test_user', email='test@user.com', password='foo')
        self.assertTrue(new_user.is_active, 'User is not active')

    def test_user_data(self) -> None:
        """Test user accounts are created with the correct user information"""

        user_data = dict(username='test_user', email='test@user.com', password='foo')
        new_user = AuthUserManager.create_superuser(**user_data)
        self.assertEqual(new_user.username, user_data['username'])
        self.assertEqual(new_user.email, user_data['email'])
