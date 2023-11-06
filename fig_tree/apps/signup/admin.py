"""
The `admin` module defines custom administrative interfaces used by the
website admin portal. Admin classes are used to extend and enhance the
management of application settings by customizing the appearance, functionality,
and permissions of admin portal interfaces.
"""

from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import *
from .models import *

__all__ = ['AuthUserAdmin']

admin.site.unregister(Group)
settings.JAZZMIN_SETTINGS['icons'].update({
    'signup.AuthUser': 'fa fa-user',
})


@admin.register(AuthUser)
class AuthUserAdmin(UserAdmin):
    """Admin interface for managing user accounts"""

    add_form = UserCreationForm
    form = UserChangeForm

    @admin.action
    def activate_selected_users(self, request, queryset) -> None:
        """Mark selected users as active"""

        queryset.update(is_active=True)

    @admin.action
    def deactivate_selected_users(self, request, queryset) -> None:
        """Mark selected users as inactive"""

        queryset.update(is_active=False)

    actions = [activate_selected_users, deactivate_selected_users]
    list_display = ['username', 'email', 'is_active', 'date_joined']
    search_fields = ['username', 'email', 'is_active']
    list_filter = ['is_active', 'date_joined']
    ordering = ['username']

    readonly_fields = ['date_joined']
    fieldsets = [
        ('User Data', {'fields': ('username', 'email', 'date_joined', 'is_active', 'password')}),
        ('Staff Status', {'fields': ('is_staff', 'is_super_user')}),
    ]
