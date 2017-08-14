
from rest_framework import serializers

from .models import Opera, OperaticRole

class OperaticRoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = OperaticRole
        fields = ('id', 'name', 'description', 'voice', 'fach',)


class OperaSerializer(serializers.ModelSerializer):

    #roles = serializers.HyperlinkedRelatedField(
    #    view_name='operatic-role',
    #    lookup_field='book',
    #    many=True,
    #    read_only=True)

    class Meta:
        model = Opera
        fields = ('id', 'title', 'composer', 'synopsis', 'roles')
        depth = 1
