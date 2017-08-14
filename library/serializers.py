
from rest_framework import serializers

from .models import Opera, OperaticRole

class OperaSerializer(serializers.Serializer):

    class Meta:
        model = Opera
        fields = ('title', 'composer', 'description',)


class OperaticRoleSerializer(serializers.Serializer):

    class Meta:
        model = OperaticRole
        fields = ('name', 'description', 'voice', 'fach')