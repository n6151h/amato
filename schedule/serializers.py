from rest_framework import serializers

from .models import *

import people.serializers as ps

class SeasonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Season
        fields = '__all__'

class ProductionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Production
        fields = '__all__'

class ShowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Show
        fields = '__all__'

class CallSerializer(serializers.ModelSerializer):

    called = ps.PersonSerializer(many=True, read_only=True)

    class Meta:
        model = Call
        fields = '__all__'


class CastMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = CastMember
        fields = '__all__'

