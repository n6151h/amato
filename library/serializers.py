
from rest_framework import serializers

from .models import *

from .forms import *

class RoleSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='library:role-detail')
    book = serializers.HyperlinkedRelatedField(view_name='library:book-detail', queryset=Opera.objects.all())

    class Meta:
        model = Role
        fields = '__all__'


class OperaticRoleSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(
                    view_name='library:operaticrole-detail')
    book = serializers.PrimaryKeyRelatedField(
                    queryset=Opera.objects.all())

    class Meta:
        model = OperaticRole
        fields = '__all__'

    def create(self, validated_data):
        role = OperaticRole.objects.create(**validated_data)
        return role

    def to_representation(self, obj):
        '''
        For whatever reason, when we get here, *obj* is a *Role*
        instance rather than an *OperaticRole* instance.  Even more
        odd is the fact that there is a *operaticrole* attribute
        of *obj* that points to what we really want.  WTF?

        In the end, I wound up not using this at all and just making
        the *roles* field in *OperaSerializer* a *HyperlinkedRelatedField*.
        '''
        cobj = obj.operaticrole
        return super(OperaticRoleSerializer, self).to_representation(obj)


class BookSerializer(serializers.HyperlinkedModelSerializer):

    roles = serializers.PrimaryKeyRelatedField(many=True, queryset=Role.objects.all())
    url = serializers.HyperlinkedIdentityField(view_name='library:book-detail')

    class Meta:
        model = Book
        fields = '__all__'

class ScriptSerializer(serializers.HyperlinkedModelSerializer):

    roles = RoleSerializer(many=True, read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='library:script-detail')

    class Meta:
        model = Script
        fields = '__all__'
        extra_kwargs = {'url': {'view_name': 'library:script-detail'}}
        depth = 1

class MusicalSerializer(serializers.HyperlinkedModelSerializer):

    roles = RoleSerializer(many=True, read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='library:musical-detail')

    class Meta:
        model = Musical
        fields = '__all__'
        depth = 1

class OperaSerializer(serializers.HyperlinkedModelSerializer):

    roles = serializers.HyperlinkedRelatedField(queryset=OperaticRole.objects.all(),
                view_name="library:operaticrole-detail", many=True)
    url = serializers.HyperlinkedIdentityField(
                view_name='library:opera-detail')

    class Meta:
        model = Opera
        fields = '__all__'

    def create(self, validated_data):
        roles_data = validated_data.pop('roles')
        opera = Opera.objects.create(**validated_data)
        for role_data in roles_data:
            Opera.objects.create(album=opera, **roles_data)
        return opera


    def update(self, instance, validated_data):
        # Update the book instance
        instance.title = validated_data['title']
        instance.save()

        # Delete any pages not included in the request
        role_ids = [item['opera_id'] for item in validated_data['roles']]
        for role in instance.roles:
            if role.id not in role_ids:
                role.delete()

        # Create or update page instances that are in the request
        for item in validated_data['roles']:
            role = OperaticRole(**item)
            role.save()

        return instance

    def to_representation(self, obj):
        return super(OperaSerializer, self).to_representation(obj)

