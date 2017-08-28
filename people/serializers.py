from rest_framework import serializers

from .models import *

from talent.models import Talent
from talent.serializers import *

from util.polymorphic import PolymorphicCTypeField

class ArtistSerializer(serializers.ModelSerializer):

    #talents = serializers.StringRelatedField(many=True, read_only=True)
    #talents = TalentSerializer(read_only=True, many=True)
    talents = serializers.HyperlinkedRelatedField(read_only=True, many=True,
                                                  view_name="api:talent:talent-detail")

    polymorphic_ctype = PolymorphicCTypeField(read_only=True)

    class Meta:
        model = Artist
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        #exclude = ('talents',)
        fields = '__all__'

    def to_representation(self, obj):
        """
        Because Person is Polymorphic
        """
        if isinstance(obj, Artist):
            return ArtistSerializer(obj, context=self.context).to_representation(obj)

        return super(PersonSerializer, self).to_representation(obj)


    def to_internal_value(self, data):
        """
        Because Person is Polymorphic
        """
        if data.get('type') == "Artist":
            self.Meta.model = Artist
            return ArtistSerializer(context=self.context).to_internal_value(data)

        self.Meta.model = Person
        return super(PersonSerializer, self).to_internal_value(data)


