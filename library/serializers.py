
from rest_framework import serializers

from .models import *

class RoleSerializer(serializers.HyperlinkedModelSerializer):

    #book = serializers.HyperlinkedRelatedField(
    #    view_name='opera-score',
    #    read_only=True)

    class Meta:
        model = Role
        fields = ('name', 'type',
                  'description',  )


class OperaticRoleSerializer(serializers.HyperlinkedModelSerializer):

    #book = serializers.HyperlinkedRelatedField(
    #    view_name='opera-score',
    #    read_only=True)

    class Meta:
        model = OperaticRole
        fields = ('name', 'type',
                  'description', 'voice', 'fach', )


class OperaSerializer(serializers.HyperlinkedModelSerializer):

    roles = OperaticRoleSerializer(many=True)

    class Meta:
        model = Opera
        fields = ('title', 'composer', 'librettist',
                    'synopsis',
                    'roles')
        depth = 1

class BookSerializer(serializers.HyperlinkedModelSerializer):

    roles = RoleSerializer(many=True)

    class Meta:
        model = Book
        fields = ('title', 'author',
                    'synopsis',
                    'roles')
        depth = 1

class ScriptSerializer(serializers.HyperlinkedModelSerializer):

    roles = RoleSerializer(many=True)

    class Meta:
        model = Script
        fields = ('title', 'author'
                    'synopsis',
                    'roles')
        depth = 1

class MusicalSerializer(serializers.HyperlinkedModelSerializer):

    roles = RoleSerializer(many=True)

    class Meta:
        model = Musical
        fields = ('title', 'composer', 'lyricist',
                    'synopsis',
                    'roles')
        depth = 1

class OperaSerializer(serializers.HyperlinkedModelSerializer):

    roles = OperaticRoleSerializer(many=True)

    class Meta:
        model = Opera
        fields = ('title', 'composer', 'librettist',
                    'synopsis',
                    'roles')
        depth = 1

