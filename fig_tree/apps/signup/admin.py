"""
The ``admin`` module defines custom administrative interfaces used by the
website admin portal. Admin classes are used to extend and enhance the
management of application settings by customizing the appearance, functionality,
and permissions of admin portal interfaces.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import *
from .models import *

__all__ = ['AuthenticatedUserAdmin']


class AuthenticatedUserAdmin(UserAdmin):
    """Admin interface for managing user accounts"""

    add_form = UserCreationForm
    form = UserChangeForm
    model = AuthUser

    # Fields shown in the main admin summary page
    list_display = ('username', 'email', 'is_active', 'date_joined')

    # Fields shown when editing a new user
    fieldsets = (
        ('User Data', {'fields': ('username', 'email', 'password')}),
        ('Account Activation', {'fields': ('is_active',)}),
        ('Staff Status', {'fields': ('is_staff', 'is_super_user')}),
    )

    search_fields = ('username', 'email', 'is_active')
    ordering = ('username',)


# Register the Admin classes with the site admin portal
admin.site.register(AuthUser, AuthenticatedUserAdmin)
