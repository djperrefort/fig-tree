"""
The `models` module uses data classes to define and interact with the
application database schema. Each model class reflects the schema for a
distinct database table and provides a high-level API to query and interact
with table data.
"""

from __future__ import annotations

from django.contrib import auth
from django.contrib.contenttypes import fields as cfields
from django.contrib.contenttypes import models as cmodels
from django.db import models
from django.utils.translation import gettext_lazy as _

__all__ = [
    'Tree',
    'TreePermission',
    'Address',
    'Citation',
    'Event',
    'Family',
    'Media',
    'Name',
    'Note',
    'Person',
    'Place',
    'Repository',
    'Source',
    'Tag',
    'URL',
]


# -----------------------------------------------------------------------------
# Models used to organize genealogical records and permissions into trees
# -----------------------------------------------------------------------------

class Tree(models.Model):
    """Database model used to group records together into family trees"""

    tree_name = models.TextField(null=False)


class TreePermission(models.Model):
    """User permissions for family trees"""

    class Meta:
        unique_together = (('tree', 'user',),)

    class Role(models.IntegerChoices):
        """User roles for facilitating RBAC"""

        READ = 10, _('read')
        READ_PRIVATE = 20, _('private')
        WRITE = 30, _('write')
        ADMIN = 40, _('admin')

    tree = models.ForeignKey('Tree', db_index=True, on_delete=models.CASCADE)
    user = models.ForeignKey(auth.get_user_model(), db_index=True, on_delete=models.CASCADE)
    role = models.IntegerField(choices=Role.choices, default='read')


# -----------------------------------------------------------------------------
# Models used to represent individual genealogical record types
# -----------------------------------------------------------------------------

class BaseRecordModel(models.Model):
    """Abstract class for creating DB models with common columns"""

    class Meta:
        abstract = True  # Tell django this model is an abstract base class

    private = models.BooleanField(default=True)
    modified = models.DateTimeField(auto_now=True)
    tree = models.ForeignKey('Tree', db_index=True, on_delete=models.CASCADE)


class Address(BaseRecordModel):
    """The physical location of a `Place`"""

    line1 = models.TextField()
    line2 = models.TextField(null=True)
    long = models.IntegerField(null=True)
    lat = models.IntegerField(null=True)
    municipality = models.TextField(null=True)
    country = models.TextField(null=True)
    code = models.IntegerField(null=True)
    date = models.DateField(null=True)

    citations = cfields.GenericRelation('Citation')


class Citation(BaseRecordModel):
    """Reference object between database objects and `Source` records"""

    class Confidence(models.IntegerChoices):
        """The researcher's confidence level in the accuracy of the cited information"""

        LOW = 0, _('low')
        REGULAR = 1, _('regular')
        HIGH = 2, _('high')

    page_or_ref = models.TextField(null=True)
    confidence = models.IntegerField(choices=Confidence.choices, default=1)

    # Fields required to support generic relationships
    content_type = models.ForeignKey(cmodels.ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = cfields.GenericForeignKey()

    source = models.ForeignKey('Source', on_delete=models.CASCADE, null=True)
    notes = models.ForeignKey('Note', on_delete=models.CASCADE, null=True)


class Event(BaseRecordModel):
    """A single historical event"""

    class DateType(models.IntegerChoices):
        """Date type for the event"""

        REGULAR = 0, _('regular')
        BEFORE = 1, _('before')
        AFTER = 2, _('after')
        ABOUT = 3, _('about')
        RANGE = 4, _('range')
        SPAN = 5, _('span')

    date_type = models.IntegerField(choices=DateType.choices, default='regular')
    event_type = models.TextField()
    year_start = models.IntegerField(null=True)
    month_start = models.IntegerField(null=True)
    day_start = models.IntegerField(null=True)
    year_end = models.IntegerField(null=True)
    month_end = models.IntegerField(null=True)
    day_end = models.IntegerField(null=True)
    description = models.TextField(null=True)

    place = models.OneToOneField('Place', on_delete=models.CASCADE, null=True)
    tags = cfields.GenericRelation('Tag')
    notes = models.ForeignKey('Note', on_delete=models.CASCADE, null=True)
    media = models.ForeignKey('Media', on_delete=models.CASCADE, null=True)
    citations = cfields.GenericRelation('Citation')


class Family(BaseRecordModel):
    """A group of individuals forming a family unit"""

    # Relationships with genealogical meaning
    parent1 = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='family_parent1', null=True)
    parent2 = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='family_parent2', null=True)
    children = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='family_child', null=True)

    # Other relationships
    events = models.ForeignKey('Event', on_delete=models.CASCADE, null=True)
    tags = cfields.GenericRelation('Tag')
    notes = models.ForeignKey('Note', on_delete=models.CASCADE, null=True)
    media = models.ForeignKey('Media', on_delete=models.CASCADE, null=True)
    citations = cfields.GenericRelation('Citation')


class Media(BaseRecordModel):
    """A media object"""

    relative_path = models.FilePathField()
    date = models.DateField(null=True)
    description = models.TextField(null=True)

    tags = cfields.GenericRelation('Tag')
    citations = cfields.GenericRelation('Citation')


class Name(BaseRecordModel):
    """The name of a single individual"""

    given_name = models.TextField(null=True)
    surname = models.TextField(null=True)
    suffix = models.TextField(null=True)
    prefix = models.TextField(null=True)
    citations = cfields.GenericRelation('Citation')


class Note(BaseRecordModel):
    """A text note"""

    text = models.TextField()
    tags = cfields.GenericRelation('Tag')


class Person(BaseRecordModel):
    """A single individual"""

    class Sex(models.IntegerChoices):
        """The individuals biological sex at birth"""

        FEMALE = 0, _('female')
        MALE = 1, _('male')
        Other = 2, _('other')

    sex = models.IntegerField(choices=Sex.choices, null=True)

    # Relationships with genealogical meaning
    primary_name = models.ForeignKey('Name', on_delete=models.CASCADE, related_name='persons_primary', null=True)
    alternate_names = models.ForeignKey('Name', on_delete=models.CASCADE, related_name='persons_alternate', null=True)
    nick_names = models.ForeignKey('Name', on_delete=models.CASCADE, related_name='person_nick', null=True)
    death = models.OneToOneField('Event', on_delete=models.CASCADE, related_name='person_death', null=True)
    birth = models.OneToOneField('Event', on_delete=models.CASCADE, related_name='person_birth', null=True)
    families = models.ForeignKey('Family', on_delete=models.CASCADE, related_name='people', null=True)
    parent_families = models.ForeignKey('Family', on_delete=models.CASCADE, related_name='people_parent', null=True)

    # Generic relationships
    tags = cfields.GenericRelation('Tag')
    events = models.ForeignKey('Event', on_delete=models.CASCADE, null=True)
    notes = models.ForeignKey('Note', on_delete=models.CASCADE, null=True)
    media = models.ForeignKey('Media', on_delete=models.CASCADE, null=True)
    citations = cfields.GenericRelation('Citation')


class Place(BaseRecordModel):
    """A place in the world separate from any physical location"""

    name = models.TextField()
    place_type = models.TextField(null=True)
    enclosed_by = models.IntegerField(null=True)
    latitude = models.CharField(max_length=10, null=True)
    longitude = models.CharField(max_length=10, null=True)
    code = models.IntegerField(null=True)
    date = models.DateField(null=True)

    address = models.ForeignKey('Address', on_delete=models.CASCADE, null=True)
    tags = cfields.GenericRelation('Tag')
    notes = models.ForeignKey('Note', on_delete=models.CASCADE, null=True)
    media = models.ForeignKey('Media', on_delete=models.CASCADE, null=True)
    citations = cfields.GenericRelation('Citation')

    @property
    def encloses(self) -> list[Place]:
        """Return a list of places enclosed by the current place"""

        return self.objects.filter(enclodes_by=self.id).all()


class Repository(BaseRecordModel):
    """A repository that hosts multiple historical sources"""

    type = models.TextField()
    name = models.TextField()

    address_list = models.ForeignKey('Address', on_delete=models.CASCADE, null=True)
    urls = models.ForeignKey('URL', on_delete=models.CASCADE, null=True)
    tags = cfields.GenericRelation('Tag')


class Source(BaseRecordModel):
    """A historical source or piece of reference material"""

    title = models.TextField()
    author = models.TextField(null=True)
    pubinfo = models.TextField(null=True)

    notes = models.ForeignKey('Note', on_delete=models.CASCADE, null=True)
    media = models.ForeignKey('Media', on_delete=models.CASCADE, null=True)
    tags = cfields.GenericRelation('Tag')


class Tag(BaseRecordModel):
    """Data label used to organize data into customizable categories"""

    name = models.TextField()
    modified = models.DateTimeField(auto_now=True)
    description = models.TextField(null=True)

    # Fields required to support generic relationships
    content_type = models.ForeignKey(cmodels.ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = cfields.GenericForeignKey()


class URL(BaseRecordModel):
    """An online resource locator"""

    href = models.TextField()
    name = models.TextField(null=True)
    date = models.DateField(null=True)
