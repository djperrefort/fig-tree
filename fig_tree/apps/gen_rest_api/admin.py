"""
The `admin` module defines custom administrative interfaces used by the
website admin portal. Admin classes are used to extend and enhance the
management of application settings by customizing the appearance, functionality,
and permissions of admin portal interfaces.
"""

from django.contrib import admin
from django.contrib.contenttypes import admin as cadmin

from .models import *


class TreePermissionInline(admin.TabularInline):
    """Inline admin element for family tree user permissions"""

    model = TreePermission
    show_change_link = False
    extra = 1


class CitationInline(cadmin.GenericTabularInline):
    """Inline admin element for source citations"""

    model = Citation
    fk_name = 'citations'
    extra = 1

    def get_readonly_fields(self, request, obj=None):
        return [] if obj is None else ['tree']


class BaseRecordAdmin(admin.ModelAdmin):
    @admin.action
    def set_selected_to_private(self, request, queryset) -> None:
        """Mark selected clusters as enabled"""

        queryset.update(private=True)

    @admin.action
    def set_selected_to_public(self, request, queryset) -> None:
        """Mark selected clusters as disabled"""

        queryset.update(private=False)

    actions = [set_selected_to_private, set_selected_to_public]
    readonly_fields = ['last_modified']
    exclude = ['object_id', 'content_type', 'content_object']

    def get_readonly_fields(self, request, obj=None):
        fields = list(self.readonly_fields)
        if obj:
            fields.extend(['tree'])

        return fields


@admin.register(Tree)
class TreeAdmin(admin.ModelAdmin):
    """Admin interface for `Tree` objects"""

    list_display = ['tree_name']
    inlines = [TreePermissionInline]
    search_fields = ['tree_name']
    ordering = ['tree_name']


@admin.register(Address)
class AddressAdmin(BaseRecordAdmin):
    """Admin interface for `Address` objects"""

    list_display = ['line1', 'municipality', 'country', 'private']
    list_filter = ['private']
    inlines = [CitationInline]


@admin.register(Citation)
class CitationAdmin(BaseRecordAdmin):
    """Admin interface for `Citation` objects"""

    list_display = ['page_or_reference', 'source', 'confidence', 'private']
    list_filter = ['private', 'confidence']
