from rest_framework import serializers

from .models import *

from talent.models import Talent
from talent.serializers import *

from util.polymorphic import PolymorphicCTypeField

class ContactDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactData
        fields = "__all__"


class ArtistSerializer(serializers.ModelSerializer):

    #talents = serializers.StringRelatedField(many=True, read_only=True)
    #talents = TalentSerializer(read_only=True, many=True)
    talents = serializers.HyperlinkedRelatedField(read_only=True, many=True,
                                                  view_name="api:talent:talent-detail")

    polymorphic_ctype = PolymorphicCTypeField(read_only=True)

    contacts = ContactDataSerializer(many=True, read_only=True)

    url = serializers.HyperlinkedIdentityField(read_only=True,
                                               view_name="api:people:artist-detail")

    class Meta:
        model = Artist
        fields = '__all__'


class StaffSerializer(serializers.ModelSerializer):

    #talents = serializers.StringRelatedField(many=True, read_only=True)
    #talents = TalentSerializer(read_only=True, many=True)
    talents = serializers.HyperlinkedRelatedField(read_only=True, many=True,
                                                  view_name="api:talent:talent-detail")

    polymorphic_ctype = PolymorphicCTypeField(read_only=True)

    class Meta:
        model = Staff
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):

    #talents = serializers.HyperlinkedRelatedField(read_only=True, many=True,
    #                                              view_name="api:talent:talent-detail")
    talents = TalentSerializer(many=True, read_only=True)

    url = serializers.HyperlinkedIdentityField(view_name="api:people:role-detail",
                                               read_only=True)

    polymorphic_ctype = PolymorphicCTypeField(read_only=True)

    class Meta:
        model = Role
        fields = '__all__'



class PersonSerializer(serializers.ModelSerializer):

    talents = serializers.HyperlinkedRelatedField(read_only=True, many=True,
                                                  view_name="api:talent:talent-detail")
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

        elif isinstance(obj, Staff):
            return StaffSerizlizer(obj, context=self.context).to_representation(obj)

        elif isinstance(obj, Role):
            return RoleSerializer(obj, context=self.context).to_representation(obj)

        return super(PersonSerializer, self).to_representation(obj)


