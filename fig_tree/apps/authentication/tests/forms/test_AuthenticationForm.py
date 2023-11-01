"""Tests for the `AuthenticationForm` class"""

from django.test import TestCase

from apps.authentication.forms import AuthenticationForm


class RememberMeField(TestCase):
    """Test the `remember_me` field"""

    def test_not_required(self) -> None:
        """Test the field is not required"""

        form = AuthenticationForm()
        self.assertFalse(form.fields['remember_me'].required)
