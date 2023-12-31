"""
The `forms` module defines form classes used to define the structure, input
fields, and validation rules for various data input forms. Server and client
side form validation is handled by application views found in the `views`
module.
"""

from django.contrib.auth import forms
from django.forms import fields as form_fields

from .models import *

__all__ = ['UserCreationForm', 'UserChangeForm']

EXISTING_USERNAME_ERROR = "An account with this username already exists."
EXISTING_EMAIL_ERROR = "An account with this email address already exists."


class UserCreationForm(forms.UserCreationForm):
    """Form for creating a new user account"""

    class Meta(forms.UserCreationForm.Meta):
        model = AuthUser
        fields = ('username', 'email')
        field_classes = {
            'username': forms.UsernameField,
            'email': form_fields.EmailField
        }
        error_messages = {
            "username": {"unique": EXISTING_USERNAME_ERROR},
            "email": {"unique": EXISTING_EMAIL_ERROR},
        }


class UserChangeForm(forms.UserChangeForm):
    """Form for modifying existing user data"""

    class Meta:
        model = AuthUser
        fields = ('username', 'email')
        field_classes = {
            'username': forms.UsernameField,
            'email': form_fields.EmailField
        }
        error_messages = {
            "username": {"unique": EXISTING_USERNAME_ERROR},
            "email": {"unique": EXISTING_EMAIL_ERROR},
        }
