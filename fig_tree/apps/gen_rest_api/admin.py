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


class ReadOnlyTreeMixin:
    """Mixin class that adds `tree` field to the list of readonly fields"""

    def get_readonly_fields(self, request, obj=None):
        fields = super().get_readonly_fields(request)
        if obj:
            fields += ('tree',)

        return fields


class CitationInline(ReadOnlyTreeMixin, cadmin.GenericTabularInline):
    """Inline admin element for `Citation` records"""

    model = Citation
    fields = ['page_or_reference', 'confidence', 'source']
    fk_name = 'citations'
    extra = 1


class NoteInline(ReadOnlyTreeMixin, cadmin.GenericTabularInline):
    """Inline admin element for `Note` records"""

    model = Note
    fk_name = 'notes'
    extra = 1


class BaseRecordAdmin(ReadOnlyTreeMixin, admin.ModelAdmin):
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


@admin.register(Address)
class AddressAdmin(BaseRecordAdmin):
    """Admin interface for `Address` objects"""

    list_display = ['line1', 'municipality', 'province', 'country', 'lat', 'long', 'private']
    list_filter = ['private']
    inlines = [CitationInline]
    fieldsets = [
        ('Family Tree', {'fields': ['tree', 'private']}),
        ('General', {'fields': ['line1', 'line2', 'line3', 'line4', 'municipality', 'province', 'country', 'code', 'lat', 'long', 'date', 'last_modified']}),
    ]


@admin.register(Event)
class EventAdmin(BaseRecordAdmin):
    list_display = ['event_type', 'date', 'date_end']
    list_filter = ['date_type']
    search_fields = ['event_type', 'description']
    fieldsets = [
        ('Family Tree', {'fields': ['tree', 'private']}),
        ('General', {'fields': [
            'event_type',
            'date_type',
            'date',
            'date_end',
            'description',
            'place',
        ]}),
    ]
    inlines = [CitationInline]


@admin.register(Family)
class FamilyAdmin(BaseRecordAdmin):
    list_display = ['parent1', 'parent2', 'children']
    search_fields = ['parent1__primary_name__given_name', 'parent2__primary_name__given_name']


@admin.register(Media)
class MediaAdmin(BaseRecordAdmin):
    list_display = ['path', 'description']
    search_fields = ['path', 'description']


@admin.register(Name)
class NameAdmin(BaseRecordAdmin):
    list_display = ['given_name', 'surname', 'prefix', 'suffix']
    search_fields = ['given_name', 'surname', 'prefix', 'suffix']


@admin.register(Note)
class NoteAdmin(BaseRecordAdmin):
    list_display = ['content_object', 'text']
    search_fields = ['text']


@admin.register(Person)
class PersonAdmin(BaseRecordAdmin):
    list_display = ['primary_name', 'sex', 'birth', 'death']
    list_filter = ['sex']
    search_fields = ['primary_name__given_name', 'primary_name__surname']


@admin.register(Place)
class PlaceAdmin(BaseRecordAdmin):
    list_display = ['name', 'place_type', 'enclosed_by']
    search_fields = ['name', 'place_type']


@admin.register(Repository)
class RepositoryAdmin(BaseRecordAdmin):
    list_display = ['type', 'name']
    search_fields = ['type', 'name']


@admin.register(Source)
class SourceAdmin(BaseRecordAdmin):
    list_display = ['title', 'author', 'pubinfo']
    search_fields = ['title', 'author', 'pubinfo']


@admin.register(Tag)
class TagAdmin(BaseRecordAdmin):
    list_display = ['name', 'description']
    search_fields = ['name', 'description']


@admin.register(URL)
class URLAdmin(BaseRecordAdmin):
    list_display = ['href', 'name', 'date', 'repository']
    search_fields = ['href', 'name']
