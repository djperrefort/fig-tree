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
from django.template import defaultfilters
from django.utils.translation import gettext_lazy as _

__all__ = [
    'Tree',
    'TreePermission',
    'BaseRecordModel',
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

    class Meta:
        verbose_name = 'Family Tree'

    tree_name = models.CharField('Name', max_length=50)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """Return the name of the family tree"""

        return self.tree_name


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
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """Return the permission level, username, and username and permission """

        return f'{self.role} permissions for {self.user} on {self.tree}'

    def __str__(self) -> str:
        return f'User permissions for {self.user} on {self.tree}'


# -----------------------------------------------------------------------------
# Models used to represent individual genealogical record types
# -----------------------------------------------------------------------------

class BaseRecordModel(models.Model):
    """Abstract class for creating DB models with common columns"""

    class Meta:
        abstract = True

    private = models.BooleanField(default=True)
    last_modified = models.DateTimeField(auto_now=True)
    tree = models.ForeignKey('Tree', db_index=True, on_delete=models.CASCADE)


class GenericRelationshipMixin(models.Model):
    """Mixin class for adding database fields required for generic relationships

    Generic relationships support many-to-one relationships between a single
    left table and N right tables using two columns for foreign keys instead of
    N. One column stores the foreign key while the other references which table
    the foreign key belongs to.
    """

    class Meta:
        abstract = True

    object_id = models.PositiveIntegerField(null=True, blank=True)  # Foreign key
    content_type = models.ForeignKey(cmodels.ContentType, null=True, blank=True, on_delete=models.CASCADE)
    content_object = cfields.GenericForeignKey('content_type', 'object_id')


class Address(GenericRelationshipMixin, BaseRecordModel):
    """The physical location of a `Place`"""

    class Meta:
        verbose_name_plural = 'Addresses'

    # Fields
    line1 = models.CharField('Line 1', max_length=250)
    line2 = models.CharField('Line 2', max_length=250, null=True, blank=True)
    lat = models.IntegerField('Latitude', null=True, blank=True)
    long = models.IntegerField('Longitude', null=True, blank=True)
    municipality = models.CharField(max_length=250, null=True, blank=True)
    country = models.CharField(max_length=250, null=True, blank=True)
    code = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    # Relationships
    citations = cfields.GenericRelation('Citation')

    def __str__(self) -> str:
        """Return the primary address line"""

        return defaultfilters.truncatechars(self.line1, 50)


class Citation(GenericRelationshipMixin, BaseRecordModel):
    """Reference object between database objects and `Source` records"""

    class Confidence(models.IntegerChoices):
        """The researcher's confidence level in the accuracy of the cited information"""

        LOW = 0, _('low')
        REGULAR = 1, _('regular')
        HIGH = 2, _('high')

    # Fields
    page_or_reference = models.CharField(max_length=100, null=True, blank=True)
    confidence = models.IntegerField(choices=Confidence.choices, default=1)

    # Relationships
    notes = cfields.GenericRelation('Note')
    source = models.ForeignKey('Source', on_delete=models.CASCADE, null=True)


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

    # Fields
    date_type = models.IntegerField(choices=DateType.choices, default='regular')
    event_type = models.TextField()
    year_start = models.IntegerField(null=True)
    month_start = models.IntegerField(null=True)
    day_start = models.IntegerField(null=True)
    year_end = models.IntegerField(null=True)
    month_end = models.IntegerField(null=True)
    day_end = models.IntegerField(null=True)
    description = models.TextField(null=True)

    # Relationships
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    place = models.OneToOneField('Place', on_delete=models.CASCADE, null=True)
    tags = cfields.GenericRelation('Tag')
    notes = cfields.GenericRelation('Note')
    media = cfields.GenericRelation('Media')
    citations = cfields.GenericRelation('Citation')


class Family(BaseRecordModel):
    """A group of individuals forming a family unit"""

    # Relationships with familial meaning
    parent1 = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='family_parent1', null=True)
    parent2 = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='family_parent2', null=True)
    children = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='family_child', null=True)

    # Other relationships
    citations = cfields.GenericRelation('Citation')
    media = cfields.GenericRelation('Media')
    notes = cfields.GenericRelation('Note')
    tags = cfields.GenericRelation('Tag')


class Media(GenericRelationshipMixin, BaseRecordModel):
    """A media object"""

    relative_path = models.FilePathField()
    date = models.DateField(null=True)
    description = models.TextField(null=True)

    citations = cfields.GenericRelation('Citation')
    tags = cfields.GenericRelation('Tag')


class Name(BaseRecordModel):
    """The name of a single individual"""

    given_name = models.TextField(null=True)
    surname = models.TextField(null=True)
    suffix = models.TextField(null=True)
    prefix = models.TextField(null=True)
    citations = cfields.GenericRelation('Citation')


class Note(GenericRelationshipMixin, BaseRecordModel):
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

    # Other relationships
    citations = cfields.GenericRelation('Citation')
    media = cfields.GenericRelation('Media')
    notes = cfields.GenericRelation('Note')
    tags = cfields.GenericRelation('Tag')


class Place(BaseRecordModel):
    """A place in the world separate from any physical location"""

    name = models.TextField()
    place_type = models.TextField(null=True)
    enclosed_by = models.IntegerField(null=True)
    latitude = models.CharField(max_length=10, null=True)
    longitude = models.CharField(max_length=10, null=True)
    code = models.IntegerField(null=True)
    date = models.DateField(null=True)

    addresses = cfields.GenericRelation('Address')
    citations = cfields.GenericRelation('Citation')
    media = cfields.GenericRelation('Media')
    notes = cfields.GenericRelation('Note')
    tags = cfields.GenericRelation('Tag')

    @property
    def encloses(self) -> list[Place]:
        """Return a list of places enclosed by the current place"""

        return self.objects.filter(enclodes_by=self.id).all()


class Repository(BaseRecordModel):
    """A repository that hosts multiple historical sources"""

    type = models.TextField()
    name = models.TextField()

    addresses = cfields.GenericRelation('Address')
    tags = cfields.GenericRelation('Tag')


class Source(BaseRecordModel):
    """A historical source or piece of reference material"""

    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250, null=True, blank=True)
    pubinfo = models.CharField(max_length=250, null=True, blank=True)

    media = cfields.GenericRelation('Media')
    notes = cfields.GenericRelation('Note')
    tags = cfields.GenericRelation('Tag')

    def __str__(self) -> str:
        """Return the source title"""

        return defaultfilters.truncatechars(self.title, 50)


class Tag(GenericRelationshipMixin, BaseRecordModel):
    """Data label used to organize data into customizable categories"""

    name = models.TextField()
    description = models.TextField(null=True)


class URL(GenericRelationshipMixin, BaseRecordModel):
    """An online resource locator"""

    href = models.TextField()
    name = models.TextField(null=True)
    date = models.DateField(null=True)

    repository = models.ForeignKey('Repository', on_delete=models.CASCADE)
