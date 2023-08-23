"""Application forms for data input and validation.

The ``forms`` module defines form classes used to define the structure, input
fields, and validation rules for various data input forms. Server and client
side form validation is handled by application views found in the ``views``
module.
"""

from django.contrib.auth import forms
from django.forms import fields as form_fields

from .models import AuthUser

_user_fields = ('username', 'email', 'first_name', 'last_name')
_user_field_classes = {
    'username': forms.UsernameField,
    'email': form_fields.EmailField,
    'first_name': form_fields.CharField,
    'last_name': form_fields.CharField
}


class UserCreationForm(forms.UserCreationForm):
    """Form for creating a new user account"""

    class Meta(forms.UserCreationForm.Meta):
        model = AuthUser
        fields = _user_fields
        field_classes = _user_field_classes


class UserChangeForm(forms.UserChangeForm):
    """Form for modifying existing user data"""

    class Meta:
        model = AuthUser
        fields = _user_fields
        field_classes = _user_field_classes
