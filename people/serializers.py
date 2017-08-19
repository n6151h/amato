from rest_framework import serializers

from .models import *

from talent.models import Talent

class PersonSerializer(serializers.ModelSerializer):

    talents = serializers.PrimaryKeyRelatedField(many=True,
                                    read_only=True) #,
                                    #view_name="talent:talent-detail")

    class Meta:
        model = Person
        #exclude = ('talents',)
        fields = '__all__'

class ArtistSerializer(serializers.ModelSerializer):

    talents = serializers.PrimaryKeyRelatedField(many=True,
                                        read_only=True)

    def get_queryset(self):
        import pdb
        pdb.set_trace()

    class Meta:
        model = Artist
        fields = '__all__'



