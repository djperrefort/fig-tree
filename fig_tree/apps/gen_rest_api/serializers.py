"""
The ``serializers`` module handles serializing/deserializing database models
and query sets. Each serializer class defines which fields are included in the
serialized output and handles the conversion of data types to and from their
serialized representations. Serializers also ensure data integrate by handling
data validation tasks as required by the relevant business domain.
"""

from rest_framework.serializers import ModelSerializer

from . import models


class TreeSerializer(ModelSerializer):
    """Data serializer for the ``Tree`` database model"""

    class Meta:
        model = models.Tree
        fields = '__all__'


class TreePermissionSerializer(ModelSerializer):
    """Data serializer for the ``TreePermission`` database model"""

    class Meta:
        model = models.TreePermission
        fields = '__all__'


class AddressSerializer(ModelSerializer):
    """Data serializer for the ``Address`` database model"""

    class Meta:
        model = models.Address
        fields = '__all__'


class CitationSerializer(ModelSerializer):
    """Data serializer for the ``Citation`` database model"""

    class Meta:
        model = models.Citation
        fields = '__all__'


class EventSerializer(ModelSerializer):
    """Data serializer for the ``Event`` database model"""

    class Meta:
        model = models.Event
        fields = '__all__'


class FamilySerializer(ModelSerializer):
    """Data serializer for the ``Family`` database model"""

    class Meta:
        model = models.Family
        fields = '__all__'


class MediaSerializer(ModelSerializer):
    """Data serializer for the ``Media`` database model"""

    class Meta:
        model = models.Media
        fields = '__all__'


class NameSerializer(ModelSerializer):
    """Data serializer for the ``Name`` database model"""

    class Meta:
        model = models.Name
        fields = '__all__'


class NoteSerializer(ModelSerializer):
    """Data serializer for the ``Note`` database model"""

    class Meta:
        model = models.Note
        fields = '__all__'


class PersonSerializer(ModelSerializer):
    """Data serializer for the ``Person`` database model"""

    class Meta:
        model = models.Person
        fields = '__all__'


class PlaceSerializer(ModelSerializer):
    """Data serializer for the ``Place`` database model"""

    class Meta:
        model = models.Place
        fields = '__all__'


class RepositorySerializer(ModelSerializer):
    """Data serializer for the ``Repository`` database model"""

    class Meta:
        model = models.Repository
        fields = '__all__'


class SourceSerializer(ModelSerializer):
    """Data serializer for the ``Source`` database model"""

    class Meta:
        model = models.Source
        fields = '__all__'


class TagSerializer(ModelSerializer):
    """Data serializer for the ``Tag`` database model"""

    class Meta:
        model = models.Tag
        fields = '__all__'


class URLSerializer(ModelSerializer):
    """Data serializer for the ``URL`` database model"""

    class Meta:
        model = models.URL
        fields = '__all__'
