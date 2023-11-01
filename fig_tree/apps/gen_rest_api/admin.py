"""
The `admin` module defines custom administrative interfaces used by the
website admin portal. Admin classes are used to extend and enhance the
management of application settings by customizing the appearance, functionality,
and permissions of admin portal interfaces.
"""

from django.contrib import admin

from .models import *


class TreePermissionInline(admin.TabularInline):
    """Inline admin element for family tree user permissions"""

    model = TreePermission
    show_change_link = False
    extra = 0


@admin.register(Tree)
class TreeAdmin(admin.ModelAdmin):
    """Admin interface for family tree objects"""

    list_display = ('tree_name',)
    inlines = [TreePermissionInline]
    search_fields = ['tree_name']
    ordering = ['tree_name']
