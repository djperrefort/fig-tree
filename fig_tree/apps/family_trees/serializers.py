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
    'FamilyTreeSerializer',
    'TreePermissionSerializer'
]


class FamilyTreeSerializer(ModelSerializer):
    """Data serializer for the `FamilyTree` database model"""

    class Meta:
        model = FamilyTree
        fields = '__all__'


class TreePermissionSerializer(ModelSerializer):
    """Data serializer for the `TreePermission` database model"""

    class Meta:
        model = TreePermission
        fields = '__all__'
