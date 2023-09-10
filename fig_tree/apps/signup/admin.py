"""
The ``admin`` module defines custom administrative interfaces used by the
website admin portal. Admin classes are used to extend and enhance the
management of application settings by customizing the appearance, functionality,
and permissions of admin portal interfaces.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import AuthUser


class AuthenticatedUserAdmin(UserAdmin):
    """Admin interface for managing user accounts"""

    add_form = UserCreationForm
    form = UserChangeForm
    model = AuthUser

    # Fields shown in the main admin summary page
    list_display = ('username', 'email')

    # Fields shown when editing a new user
    fieldsets = (
        ('User Data', {'fields': list_display}),
        ('Staff Status', {'fields': ('is_staff', 'is_super_user')}),
    )

    search_fields = ('username', 'email')
    ordering = ('username',)


# Register the Admin classes with the site admin portal
admin.site.register(AuthUser, AuthenticatedUserAdmin)
