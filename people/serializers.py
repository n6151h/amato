from rest_framework import serializers

from .models import *

from talent.models import Talent

class PersonSerializer(serializers.ModelSerializer):

    talents = serializers.HyperlinkedRelatedField(many=True,
                    queryset=Talent.objects.all(),
                    view_name="talent:talent-detail")

    class Meta:
        model = Person
        #exclude = ('talents',)
        fields = '__all__'

class ArtistSerializer(serializers.HyperlinkedModelSerializer):

    talents = serializers.HyperlinkedRelatedField(many=True,
                    queryset=Talent.objects.all(),
                    view_name="talent:talent-detail")

    class Meta:
        model = Artist
        fields = '__all__'



