"""
The `serializers` module handles serializing/deserializing database models
and query sets. Each serializer class defines which fields are included in the
serialized output and handles the conversion of data types to and from their
serialized representations. Serializers also ensure data integrate by handling
data validation tasks as required by the relevant business domain.
"""

from rest_framework.serializers import ModelSerializer

from .models import *

__all__ = [
    'TreeSerializer',
    'TreePermissionSerializer',
    'AddressSerializer',
    'CitationSerializer',
    'EventSerializer',
    'FamilySerializer',
    'MediaSerializer',
    'NameSerializer',
    'NoteSerializer',
    'PersonSerializer',
    'PlaceSerializer',
    'RepositorySerializer',
    'SourceSerializer',
    'TagSerializer',
    'URLSerializer',
]


# -----------------------------------------------------------------------------
# Serializers for family trees and family tree permissions
# -----------------------------------------------------------------------------

class TreeSerializer(ModelSerializer):
    """Data serializer for the `Tree` database model"""

    class Meta:
        model = Tree
        fields = '__all__'


class TreePermissionSerializer(ModelSerializer):
    """Data serializer for the `TreePermission` database model"""

    class Meta:
        model = TreePermission
        fields = '__all__'


# -----------------------------------------------------------------------------
# Serializers for individual genealogical record types
# -----------------------------------------------------------------------------

class BaseRecordSerializer(ModelSerializer):
    """Base class for serializing individual genealogical record types

    This class assumes the serialized model has a `tree` field and sets the
    field to be writable for new records but read-only for existing records.
    """

    def __init__(self, *args, **kwargs) -> None:
        """Prevent `tree` field from being modified for existing records"""

        super().__init__(*args, **kwargs)
        if self.instance is not None:
            self.fields.get('tree').read_only = True


class AddressSerializer(BaseRecordSerializer):
    """Data serializer for the `Address` database model"""

    class Meta:
        model = Address
        fields = '__all__'


class CitationSerializer(BaseRecordSerializer):
    """Data serializer for the `Citation` database model"""

    class Meta:
        model = Citation
        fields = '__all__'


class EventSerializer(BaseRecordSerializer):
    """Data serializer for the `Event` database model"""

    class Meta:
        model = Event
        fields = '__all__'


class FamilySerializer(BaseRecordSerializer):
    """Data serializer for the `Family` database model"""

    class Meta:
        model = Family
        fields = '__all__'


class MediaSerializer(BaseRecordSerializer):
    """Data serializer for the `Media` database model"""

    class Meta:
        model = Media
        fields = '__all__'


class NameSerializer(BaseRecordSerializer):
    """Data serializer for the `Name` database model"""

    class Meta:
        model = Name
        fields = '__all__'


class NoteSerializer(BaseRecordSerializer):
    """Data serializer for the `Note` database model"""

    class Meta:
        model = Note
        fields = '__all__'


class PersonSerializer(BaseRecordSerializer):
    """Data serializer for the `Person` database model"""

    class Meta:
        model = Person
        fields = '__all__'


class PlaceSerializer(BaseRecordSerializer):
    """Data serializer for the `Place` database model"""

    class Meta:
        model = Place
        fields = '__all__'


class RepositorySerializer(BaseRecordSerializer):
    """Data serializer for the `Repository` database model"""

    class Meta:
        model = Repository
        fields = '__all__'


class SourceSerializer(BaseRecordSerializer):
    """Data serializer for the `Source` database model"""

    class Meta:
        model = Source
        fields = '__all__'


class TagSerializer(BaseRecordSerializer):
    """Data serializer for the `Tag` database model"""

    class Meta:
        model = Tag
        fields = '__all__'


class URLSerializer(BaseRecordSerializer):
    """Data serializer for the `URL` database model"""

    class Meta:
        model = URL
        fields = '__all__'
