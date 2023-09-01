"""Tests for the ``UserChangeForm`` class."""

from django.test import TestCase

from apps.signup.forms import UserChangeForm
from apps.signup.models import AuthUser


class FormFields(TestCase):
    """Test which fields are marked as required"""

    required_fields = ('username', 'email')
    form = UserChangeForm()

    def test_required_fields(self) -> None:
        """Test required fields are marked as required"""

        for field_name, field in self.form.fields.items():
            if field_name in self.required_fields:
                self.assertTrue(field.required, f'Field {field_name} is should be required.')

            else:
                self.assertFalse(field.required, f'Field {field_name} is should not be required.')


class UsesCustomAuthUser(TestCase):
    """Test the form uses the custom user database model"""

    def runTest(self) -> None:
        """Execute the test"""

        self.assertIs(UserChangeForm().Meta.model, AuthUser)
