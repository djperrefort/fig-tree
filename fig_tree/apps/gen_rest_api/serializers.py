"""
The ``serializers`` module defines classes for serializing/deserializing
database models and query sets. Each serializer class defines which fields are
included in the serialized output and handles the conversion of data types to
and from their serialized representations. Serializers also ensure data
integrate by handling data validation tasks as required by the relevant
business domain.
"""

from rest_framework import serializers

from . import models


class AddressSerializer(serializers.ModelSerializer):
    """Data serializer for the ``Address`` database model"""

    class Meta:
        model = models.Address
        fields = '__all__'
        depth = 1


class CitationSerializer(serializers.ModelSerializer):
    """Data serializer for the ``Citation`` database model"""

    class Meta:
        model = models.Citation
        fields = '__all__'
        depth = 1


class EventSerializer(serializers.ModelSerializer):
    """Data serializer for the ``Event`` database model"""

    class Meta:
        model = models.Event
        fields = '__all__'
        depth = 1


class FamilySerializer(serializers.ModelSerializer):
    """Data serializer for the ``Family`` database model"""

    class Meta:
        model = models.Family
        fields = '__all__'
        depth = 1


class MediaSerializer(serializers.ModelSerializer):
    """Data serializer for the ``Media`` database model"""

    class Meta:
        model = models.Media
        fields = '__all__'
        depth = 1


class NameSerializer(serializers.ModelSerializer):
    """Data serializer for the ``Name`` database model"""

    class Meta:
        model = models.Name
        fields = '__all__'
        depth = 1


class NoteSerializer(serializers.ModelSerializer):
    """Data serializer for the ``Note`` database model"""

    class Meta:
        model = models.Note
        fields = '__all__'
        depth = 1


class PersonSerializer(serializers.ModelSerializer):
    """Data serializer for the ``Person`` database model"""

    class Meta:
        model = models.Person
        fields = '__all__'
        depth = 1


class PlaceSerializer(serializers.ModelSerializer):
    """Data serializer for the ``Place`` database model"""

    class Meta:
        model = models.Place
        fields = '__all__'
        depth = 1


class RepositorySerializer(serializers.ModelSerializer):
    """Data serializer for the ``Repository`` database model"""

    class Meta:
        model = models.Repository
        fields = '__all__'
        depth = 1


class SourceSerializer(serializers.ModelSerializer):
    """Data serializer for the ``Source`` database model"""

    class Meta:
        model = models.Source
        fields = '__all__'
        depth = 1


class TagSerializer(serializers.ModelSerializer):
    """Data serializer for the ``Tag`` database model"""

    class Meta:
        model = models.Tag
        fields = '__all__'
        depth = 1


class URLSerializer(serializers.ModelSerializer):
    """Data serializer for the ``URL`` database model"""

    class Meta:
        model = models.URL
        fields = '__all__'
        depth = 1
