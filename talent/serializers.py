from rest_framework import serializers

from .models import *


class TalentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Talent
        fields = '__all__'

class SingingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Singing
        fields = '__all__'


class DancingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dancing
        fields = '__all__'


