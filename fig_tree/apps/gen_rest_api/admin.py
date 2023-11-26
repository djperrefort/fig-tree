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
    'gen_rest_api.Address': 'fa fa-address-card',
    'gen_rest_api.Citation': 'fa fa-check-double',
    'gen_rest_api.Event': 'fa fa-calendar-day',
    'gen_rest_api.Family': 'fa fa-users',
    'gen_rest_api.Media': 'fa fa-photo-video',
    'gen_rest_api.Name': 'fa fa-id-badge',
    'gen_rest_api.Person': 'fa fa-user',
    'gen_rest_api.Place': 'fa fa-map-marker-alt',
    'gen_rest_api.Repository': 'fa fa-building',
    'gen_rest_api.Source': 'fa fa-book',
    'gen_rest_api.Tag': 'fa fa-tags',
    'gen_rest_api.URL': 'fa fa-link',
})


class ReadOnlyTreeMixin:
    """Mixin class that adds `tree` field to the list of readonly fields"""

    def get_readonly_fields(self, request, obj=None) -> tuple:
        """Return a tuple of model field names to treat as read-only"""

        fields = super().get_readonly_fields(request)
        if obj:
            fields += ('tree',)

        return fields


class BaseRecordAdmin(ReadOnlyTreeMixin, admin.ModelAdmin):
    """Base class used to build admin interfaces for genealogical record tables"""

    @admin.action
    def set_selected_to_private(self, request, queryset) -> None:
        """Mark selected records as private"""

        queryset.update(private=True)

    @admin.action
    def set_selected_to_public(self, request, queryset) -> None:
        """Mark selected records as public"""

        queryset.update(private=False)

    actions = [set_selected_to_private, set_selected_to_public]
    readonly_fields = ['last_modified']
    list_filter = ['private', 'tree', 'last_modified']
    exclude = ['object_id', 'content_type', 'content_object']


@admin.register(Address)
class AddressAdmin(BaseRecordAdmin):
    """Admin interface for `Address` Records"""

    list_display = ['line1', 'municipality', 'province', 'country', 'lat', 'long', 'private', 'tree']
    search_fields = ['line1', 'line2', 'line3', 'line4', 'municipality', 'province', 'country', 'code', 'lat', 'long']
    fieldsets = [
        ('Family Tree', {'fields': ['tree', 'private']}),
        ('Record Info', {'fields': ['line1', 'line2', 'line3', 'line4', 'municipality', 'province', 'country', 'code', 'lat', 'long', 'date', 'last_modified']}),
    ]


@admin.register(Citation)
class CitationAdmin(BaseRecordAdmin):
    """Admin interface for `Citation` records"""

    list_display = ['source', 'page_or_reference', 'confidence', 'private', 'tree']
    search_fields = ['source', 'page_or_reference', 'tree']
    fieldsets = [
        ('Family Tree', {'fields': ['tree', 'private']}),
        ('Record Info', {'fields': ['page_or_reference', 'confidence', 'source']}),
    ]


@admin.register(Event)
class EventAdmin(BaseRecordAdmin):
    """Admin interface for `Event` records"""

    list_display = ['event_type', 'date', 'date_end', 'place', 'private', 'tree']
    search_fields = ['event_type', 'description']
    fieldsets = [
        ('Family Tree', {'fields': ['tree', 'private']}),
        ('Record Info', {'fields': [
            'event_type',
            'date_type',
            'date',
            'date_end',
            'description',
            'place',
        ]}),
    ]


@admin.register(Family)
class FamilyAdmin(BaseRecordAdmin):
    """Admin interface for `Family` records"""

    list_display = ['parent1', 'parent2', 'children']
    search_fields = ['parent1__primary_name__given_name', 'parent2__primary_name__given_name']
    fieldsets = [
        ('Family Tree', {'fields': ['tree', 'private']}),
        ('Record Info', {'fields': ['parent1', 'parent2', 'children']}),
    ]


@admin.register(Media)
class MediaAdmin(BaseRecordAdmin):
    """Admin interface for `Media` records"""

    list_display = ['description', 'date']
    search_fields = ['description']
    fieldsets = [
        ('Family Tree', {'fields': ['tree', 'private']}),
        ('Record Info', {'fields': ['blob', 'date_type', 'date', 'description']}),
    ]


@admin.register(Name)
class NameAdmin(BaseRecordAdmin):
    """Admin interface for `Name` records"""

    list_display = ['given_name', 'surname', 'prefix', 'suffix']
    search_fields = ['given_name', 'surname', 'prefix', 'suffix']
    fieldsets = [
        ('Family Tree', {'fields': ['tree', 'private']}),
        ('Record Info', {'fields': ['given_name', 'surname', 'prefix', 'suffix']}),
    ]


@admin.register(Person)
class PersonAdmin(BaseRecordAdmin):
    """Admin interface for `Person` records"""

    list_display = ['primary_name', 'sex', 'birth', 'death']
    list_filter = ['private', 'tree', 'last_modified', 'sex']
    search_fields = ['primary_name__given_name', 'primary_name__surname']
    fieldsets = [
        ('Family Tree', {'fields': ['tree', 'private']}),
        ('Record Info', {'fields': [
            'primary_name',
            'alternate_names',
            'nick_names',
            'death',
            'birth',
            'families',
            'parent_families',
        ]}),
    ]


@admin.register(Place)
class PlaceAdmin(BaseRecordAdmin):
    """Admin interface for `Place` records"""

    list_display = ['name', 'place_type', 'enclosed_by']
    search_fields = ['name', 'place_type']
    fieldsets = [
        ('Family Tree', {'fields': ['tree', 'private']}),
        ('Record Info', {'fields': ['name', 'place_type', 'enclosed_by']}),
    ]


@admin.register(Repository)
class RepositoryAdmin(BaseRecordAdmin):
    """Admin interface for `Place` records"""

    list_display = ['type', 'name']
    search_fields = ['type', 'name']
    fieldsets = [
        ('Family Tree', {'fields': ['tree', 'private']}),
        ('Record Info', {'fields': ['type', 'name']}),
    ]


@admin.register(Source)
class SourceAdmin(BaseRecordAdmin):
    """Admin interface for `Place` records"""

    list_display = ['title', 'author', 'pubinfo']
    search_fields = ['title', 'author', 'pubinfo']
    fieldsets = [
        ('Family Tree', {'fields': ['tree', 'private']}),
        ('Record Info', {'fields': ['title', 'author', 'pubinfo']}),
    ]


@admin.register(Tag)
class TagAdmin(BaseRecordAdmin):
    """Admin interface for `Tag` records"""

    list_display = ['name', 'description']
    search_fields = ['name', 'description']
    fieldsets = [
        ('Family Tree', {'fields': ['tree', 'private']}),
        ('Record Info', {'fields': ['name', 'description']}),
    ]


@admin.register(URL)
class URLAdmin(BaseRecordAdmin):
    """Admin interface for `URL` records"""

    list_display = ['href', 'name', 'date']
    search_fields = ['href', 'name']
    fieldsets = [
        ('Family Tree', {'fields': ['tree', 'private']}),
        ('Record Info', {'fields': ['href', 'name', 'date']}),
    ]
