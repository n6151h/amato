from rest_framework import serializers

from .models import *

class SingerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Singer
        fields = '__all__'
        extra_kwargs = {'url': {'view_name': 'people:singer-detail'}}

class InstrumentalistSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Instrumentalist
        fields = '__all__'

class DancerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Dancer
        fields = '__all__'

class StaffSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Staff
        fields = '__all__'

