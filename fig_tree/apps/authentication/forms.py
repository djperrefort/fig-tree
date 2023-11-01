"""
The ``forms`` module defines form classes used to define the structure, input
fields, and validation rules for various data input forms. Server and client
side form validation is handled by application views found in the ``views``
module.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm as AuthForm

__all__ = ['AuthenticationForm']

class AuthenticationForm(AuthForm):
    """Extends the built-in form for authenticating users"""

    remember_me = forms.BooleanField(required=False)
