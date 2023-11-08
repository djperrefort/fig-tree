"""
The `admin` module defines custom administrative interfaces used by the
website admin portal. Admin classes are used to extend and enhance the
management of application settings by customizing the appearance, functionality,
and permissions of admin portal interfaces.
"""

from django.conf import settings
from django.contrib import admin
from django.contrib.contenttypes import admin as cadmin

from .models import *

settings.JAZZMIN_SETTINGS['icons'].update({
    'gen_rest_api.Address': 'fa fa-address-card',
})


class CitationInline(cadmin.GenericTabularInline):
    """Inline admin element for source citations"""

    fields = ['page_or_reference', 'confidence', 'source']
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


@admin.register(Address)
class AddressAdmin(BaseRecordAdmin):
    """Admin interface for `Address` objects"""

    list_display = ['line1', 'municipality', 'province', 'country', 'lat', 'long', 'private']
    list_filter = ['private']
    inlines = [CitationInline]


@admin.register(Citation)
class CitationAdmin(BaseRecordAdmin):
    """Admin interface for `Citation` objects"""

    list_display = ['page_or_reference', 'source', 'confidence', 'private']
    list_filter = ['private', 'confidence']
