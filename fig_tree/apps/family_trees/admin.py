"""
The `admin` module defines custom administrative interfaces used by the
website admin portal. Admin classes are used to extend and enhance the
management of application settings by customizing the appearance, functionality,
and permissions of admin portal interfaces.
"""

from django.conf import settings
from django.contrib import admin

from .models import *

settings.JAZZMIN_SETTINGS['icons'].update({
    'family_trees.FamilyTree': 'fab fa-pagelines',
})

settings.JAZZMIN_SETTINGS["changeform_format_overrides"].update({
    'family_trees.FamilyTree': 'single',
})


class TreePermissionInline(admin.TabularInline):
    """Inline admin element for family tree user permissions"""

    model = TreePermission
    show_change_link = False
    extra = 0


@admin.register(FamilyTree)
class TreeAdmin(admin.ModelAdmin):
    """Admin interface for `FamilyTree` objects"""

    list_display = ['tree_name', 'last_modified']
    inlines = [TreePermissionInline]
    search_fields = ['tree_name']
    ordering = ['tree_name']
