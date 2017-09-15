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

class RoleSerializer(serializers.ModelSerializer):

    #talents = serializers.StringRelatedField(many=True, read_only=True)
    #talents = TalentSerializer(read_only=True, many=True)
    talents = serializers.HyperlinkedRelatedField(read_only=True, many=True,
                                                  view_name="api:talent:talent-detail")

    polymorphic_ctype = PolymorphicCTypeField(read_only=True)

    class Meta:
        model = Artist
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

        return super(PersonSerializer, self).to_representation(obj)


#     def to_internal_value(self, data):
#         """
#         Because Person is Polymorphic
#         """
#         if data.get('type') == "Artist":
#             self.Meta.model = Artist
#             return ArtistSerializer(context=self.context).to_internal_value(data)

#         self.Meta.model = Person
#         return super(PersonSerializer, self).to_internal_value(data)


# # -----[ Roles and role subtypes (e.g. OperaticRole) ]

# class OperaticRoleSerializer(serializers.ModelSerializer):

#     url = serializers.HyperlinkedIdentityField(
#                     view_name='api:library:operaticrole-detail')

#     #book = serializers.PrimaryKeyRelatedField(
#     #                queryset=Opera.objects.all())
#     book = serializers.HyperlinkedRelatedField(
#                     queryset=Opera.objects.all(),
#                     view_name='api:library:opera-detail')

#     #role_type = serializers.ChoiceField(choices=RoleTypeEnum)

#     polymorphic_ctype = PolymorphicCTypeField(read_only=True)

#     class Meta:
#         model = OperaticRole
#         fields = '__all__'

#     def create(self, validated_data):
#         role = OperaticRole.objects.create(**validated_data)
#         return role

#     def to_representation(self, obj):
#         '''
#         For whatever reason, when we get here, *obj* is a *Role*
#         instance rather than an *OperaticRole* instance.  Even more
#         odd is the fact that there is a *operaticrole* attribute
#         of *obj* that points to what we really want.  WTF?

#         In the end, I wound up not using this at all and just making
#         the *roles* field in *OperaSerializer* a *HyperlinkedRelatedField*.
#         '''
#         return super(OperaticRoleSerializer, self).to_representation(obj)


# class RoleTypeField(serializers.ChoiceField):


#     def to_internal_value(self, data):
#         import pdb
#         pdb.set_trace()

#         xx = getattr(RoleTypeEnum, data.replace('-', '_'))

#         return xx


# class RoleSerializer(serializers.ModelSerializer):

#     url = serializers.HyperlinkedIdentityField(view_name='api:library:role-detail')
#     book = serializers.HyperlinkedRelatedField(view_name='api:library:book-detail',
#                                                queryset=Opera.objects.all())

#     #role_type = serializers.ChoiceField(choices=RoleTypeEnum)
#     role_type = RoleTypeField(choices=RoleTypeEnum)

#     class Meta:
#         model = Role
#         fields = '__all__'

#     def to_representation(self, obj):
#         """
#         Because Role is Polymorphic
#         """

#         import pdb
#         pdb.set_trace()

#         if isinstance(obj, OperaticRole):
#             return OperaticRoleSerializer(obj, context=self.context).to_representation(obj)

#         #return super(RoleSerializer, self).to_representation(obj)
#         return str(obj.name)


#     def to_internal_value(self, data):
#         """
#         Because Role is Polymorphic
#         """

#         import pdb
#         pdb.set_trace()

#         if data.get('type') == "OperaticRole":
#             self.Meta.model = OperaticRole
#             return OperaticRoleSerializer(context=self.context).to_internal_value(data)

#         self.Meta.model = Role
#         return super(RoleSerializer, self).to_internal_value(data)


