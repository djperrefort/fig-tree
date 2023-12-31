"""
The `models` module uses data classes to define and interact with the
application database schema. Each model class reflects the schema for a
distinct database table and provides a high-level API to query and interact
with table data.
"""

from __future__ import annotations

from django.contrib.contenttypes import fields as cfields
from django.contrib.contenttypes import models as cmodels
from django.db import models
from django.template import defaultfilters
from django.utils.translation import gettext_lazy as _

from apps.family_trees.models import FamilyTreeModelMixin

__all__ = [
    'BaseRecordModel',
    'Address',
    'Citation',
    'Event',
    'Family',
    'Media',
    'Name',
    'Person',
    'Place',
    'Repository',
    'Source',
    'Tag',
    'URL',
]


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


class BaseRecordModel(FamilyTreeModelMixin, models.Model):
    """Abstract class for creating DB models with common columns"""

    class Meta:
        abstract = True

    last_modified = models.DateTimeField(auto_now=True)


class Address(GenericRelationshipMixin, BaseRecordModel):
    """The physical location of a `Place`"""

    class Meta:
        verbose_name_plural = 'Addresses'

    # Fields
    line1 = models.CharField('Line 1', max_length=255)
    line2 = models.CharField('Line 2', max_length=255, null=True, blank=True)
    line3 = models.CharField('Line 3', max_length=255, null=True, blank=True)
    line4 = models.CharField('Line 4', max_length=255, null=True, blank=True)
    municipality = models.CharField(max_length=255, null=True, blank=True)
    province = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    code = models.CharField(max_length=10, null=True, blank=True)
    lat = models.IntegerField('Latitude', null=True, blank=True)
    long = models.IntegerField('Longitude', null=True, blank=True)
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
    source = models.ForeignKey('Source', on_delete=models.CASCADE)

    def __str__(self) -> str:
        """Return the name of the cited source and supported record"""

        source_name = defaultfilters.truncatechars(self.source.title, 25)
        if self.content_object:
            return f'"{source_name}" citation for "{self.content_object}"'

        return f'"{source_name}" citation'


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
    event_type = models.CharField(max_length=255)
    date_type = models.IntegerField(choices=DateType.choices, default='regular')
    date = models.DateField(null=True, blank=True)
    date_end = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    # Relationships
    place = models.OneToOneField('Place', on_delete=models.CASCADE, null=True, blank=True)
    people = cfields.GenericRelation('Person')
    tags = cfields.GenericRelation('Tag')
    media = cfields.GenericRelation('Media')
    citations = cfields.GenericRelation('Citation')

    def __str__(self) -> None:
        """Return the event type"""

        return defaultfilters.truncatechars(self.event_type, 50)


class Family(BaseRecordModel):
    """A group of individuals forming a family unit"""

    class Meta:
        verbose_name_plural = 'Families'

    # Relationships with familial meaning
    parent1 = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='family_parent1', null=True, blank=True)
    parent2 = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='family_parent2', null=True, blank=True)
    children = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='family_child', null=True, blank=True)

    # Other relationships
    citations = cfields.GenericRelation('Citation')
    media = cfields.GenericRelation('Media')
    tags = cfields.GenericRelation('Tag')

    def __str__(self) -> str:
        """Return the family name using the full names of both parents"""

        parent1 = str(self.parent1) if self.parent1 else 'Unknown'
        parent2 = str(self.parent2) if self.parent2 else 'Unknown'
        return f'Family of "{parent1}" and "{parent2}'


class Media(GenericRelationshipMixin, BaseRecordModel):
    """A media object"""

    class Meta:
        verbose_name_plural = 'Media'

    class DateType(models.IntegerChoices):
        """Date type for the event"""

        REGULAR = 0, _('regular')
        BEFORE = 1, _('before')
        AFTER = 2, _('after')
        ABOUT = 3, _('about')

    blob = models.ImageField()
    date_type = models.IntegerField(choices=DateType.choices, default='regular')
    date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    tags = cfields.GenericRelation('Tag')

    def __str__(self) -> str:
        """Return the media description"""

        return defaultfilters.truncatechars(self.description, 50)


class Name(BaseRecordModel):
    """The name of a single individual"""

    given_name = models.CharField(max_length=255, null=True, blank=True)
    surname = models.CharField(max_length=255, null=True, blank=True)
    suffix = models.CharField(max_length=255, null=True, blank=True)
    prefix = models.CharField(max_length=255, null=True, blank=True)
    citations = cfields.GenericRelation('Citation')

    def __str__(self) -> str:
        """Return the first and last name as a comma seperated string"""

        first = self.given_name or 'Unknown'
        last = self.surname or 'Unknown'
        return f'{last}, {first}'


class Person(BaseRecordModel):
    """A single individual"""

    class Meta:
        verbose_name_plural = 'People'

    class Sex(models.IntegerChoices):
        """The individuals biological sex at birth"""

        FEMALE = 0, _('female')
        MALE = 1, _('male')
        Other = 2, _('other')

    sex = models.IntegerField(choices=Sex.choices, null=True, blank=True)

    # Relationships with genealogical meaning
    primary_name = models.ForeignKey('Name', on_delete=models.CASCADE, related_name='persons_primary', null=True, blank=True)
    alternate_names = models.ForeignKey('Name', on_delete=models.CASCADE, related_name='persons_alternate', null=True, blank=True)
    nick_names = models.ForeignKey('Name', on_delete=models.CASCADE, related_name='person_nick', null=True, blank=True)
    death = models.OneToOneField('Event', on_delete=models.CASCADE, related_name='person_death', null=True, blank=True)
    birth = models.OneToOneField('Event', on_delete=models.CASCADE, related_name='person_birth', null=True, blank=True)
    families = models.ForeignKey('Family', on_delete=models.CASCADE, related_name='people', null=True, blank=True)
    parent_families = models.ForeignKey('Family', on_delete=models.CASCADE, related_name='people_parent', null=True, blank=True)

    # Other relationships
    citations = cfields.GenericRelation('Citation')
    media = cfields.GenericRelation('Media')
    tags = cfields.GenericRelation('Tag')

    def __str__(self) -> str:
        """Return the person's primary name"""

        return str(self.primary_name) if self.primary_name else 'Unknown'


class Place(BaseRecordModel):
    """A place in the world separate from any physical location"""

    name = models.CharField(max_length=255)
    place_type = models.CharField(max_length=255, null=True, blank=True)
    enclosed_by = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    addresses = cfields.GenericRelation('Address')
    citations = cfields.GenericRelation('Citation')
    media = cfields.GenericRelation('Media')
    tags = cfields.GenericRelation('Tag')

    @property
    def encloses(self) -> list[Place]:
        """Return a list of places enclosed by the current place"""

        return self.objects.filter(enclodes_by=self.id).all()

    def __str__(self) -> None:
        """Return the name of the place"""

        return defaultfilters.truncatechars(self.name, 50)


class Repository(BaseRecordModel):
    """A repository that hosts multiple historical sources"""

    class Meta:
        verbose_name_plural = 'Repositories'

    type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    addresses = cfields.GenericRelation('Address')
    tags = cfields.GenericRelation('Tag')

    def __str__(self) -> None:
        """Return the name of the place"""

        return defaultfilters.truncatechars(self.name, 50)


class Source(BaseRecordModel):
    """A historical source or piece of reference material"""

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, null=True, blank=True)
    pubinfo = models.CharField(max_length=500, null=True, blank=True)

    media = cfields.GenericRelation('Media')
    tags = cfields.GenericRelation('Tag')

    def __str__(self) -> str:
        """Return the source title"""

        return defaultfilters.truncatechars(self.title, 50)


class Tag(GenericRelationshipMixin, BaseRecordModel):
    """Data label used to organize data into customizable categories"""

    name = models.CharField(max_length=25)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        """Return the tag name"""

        return str(self.name)


class URL(GenericRelationshipMixin, BaseRecordModel):
    """An online resource locator"""

    href = models.TextField()
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    last_accessed = models.DateField(null=True, blank=True)

    repository = models.ForeignKey('Repository', on_delete=models.CASCADE)

    def __str__(self) -> str:
        """Return the URL name and href"""

        url = defaultfilters.truncatechars(self.href, 50)
        return f'{self.name} ({url})'
