from rest_framework import serializers
from enumchoicefield import ChoiceEnum, EnumChoiceField

from .models import *

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

    class Meta:
        model = Call
        fields = '__all__'

    type = EnumChoiceField(enum_class=CallTypes)