
from rest_framework import serializers

from .models import *

from .forms import *


class OperaticRoleSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
                    view_name='api:library:operaticrole-detail')

    #book = serializers.PrimaryKeyRelatedField(
    #                queryset=Opera.objects.all())
    book = serializers.HyperlinkedRelatedField(
                    queryset=Opera.objects.all(),
                    view_name='api:library:opera-detail')

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
        import pdb
        return super(OperaticRoleSerializer, self).to_representation(obj)


class RoleSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='api:library:role-detail')
    book = serializers.HyperlinkedRelatedField(view_name='api:library:book-detail', queryset=Opera.objects.all())

    class Meta:
        model = Role
        fields = '__all__'

    def to_representation(self, obj):
        """
        Because Role is Polymorphic
        """
        if isinstance(obj, OperaticRole):
            return OperaticRoleSerializer(obj, context=self.context).to_representation(obj)

        return super(RoleSerializer, self).to_representation(obj)


    def to_internal_value(self, data):
        """
        Because Role is Polymorphic
        """
        if data.get('type') == "OperaticRole":
            self.Meta.model = OperaticRole
            return OperaticRoleSerializer(context=self.context).to_internal_value(data)

        self.Meta.model = Role
        return super(RoleSerializer, self).to_internal_value(data)


class ScriptSerializer(serializers.ModelSerializer):

    roles = RoleSerializer(many=True, read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='api:library:script-detail')

    class Meta:
        model = Script
        fields = '__all__'
        extra_kwargs = {'url': {'view_name': 'api:library:script-detail'}}
        depth = 1

class MusicalSerializer(serializers.ModelSerializer):

    roles = RoleSerializer(many=True, read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='api:library:musical-detail')

    class Meta:
        model = Musical
        fields = '__all__'
        depth = 1

class OperaSerializer(serializers.ModelSerializer):

    roles = serializers.HyperlinkedRelatedField(read_only=True,
                view_name="api:library:operaticrole-detail", many=True)

    url = serializers.HyperlinkedIdentityField(
                view_name='api:library:opera-detail')

    def get_queryset(self, request):
        import pdb
        pdb.set_trace()

        return OperaticRole.objects.all()

    class Meta:
        model = Opera
        fields = '__all__'

    # def create(self, validated_data):
    #     roles_data = validated_data.pop('roles')
    #     opera = Opera.objects.create(**validated_data)
    #     for role_data in roles_data:
    #         Opera.objects.create(album=opera, **roles_data)
    #     return opera


    # def update(self, instance, validated_data):
    #     # Update the book instance
    #     instance.title = validated_data['title']
    #     instance.save()

    #     # Delete any pages not included in the request
    #     role_ids = [item['opera_id'] for item in validated_data['roles']]
    #     for role in instance.roles:
    #         if role.id not in role_ids:
    #             role.delete()

    #     # Create or update page instances that are in the request
    #     for item in validated_data['roles']:
    #         role = OperaticRole(**item)
    #         role.save()

    #     return instance

    def to_representation(self, obj):
         return super(OperaSerializer, self).to_representation(obj)


class BookSerializer(serializers.ModelSerializer):

    roles = serializers.PrimaryKeyRelatedField(many=True, queryset=Role.objects.all())
    url = serializers.HyperlinkedIdentityField(view_name='api:library:book-detail')

    class Meta:
        model = Book
        fields = '__all__'

    def to_representation(self, obj):
        """
        Because Book is Polymorphic
        """
        if isinstance(obj, Script):
            return ScriptSerializer(obj, context=self.context).to_representation(obj)
        elif isinstance(obj, Musical):
            return MusicalSerializer(obj, context=self.context).to_representation(obj)
        elif isinstance(obj, Opera):
            return OperaSerializer(obj, context=self.context).to_representation(obj)

        return super(BookSerializer, self).to_representation(obj)


    def to_internal_value(self, data):
        """
        Because book is Polymorphic
        """
        if data.get('type') == "Script":
            self.Meta.model = Script
            return ScriptSerializer(context=self.context).to_internal_value(data)
        elif data.get('type') == "Musical":
            self.Meta.model = Musical
            return MusicalSerializer(context=self.context).to_internal_value(data)
        elif data.get('type') == "Opera":
            self.Meta.model = Opera
            return OperaSerializer(context=self.context).to_internal_value(data)

        self.Meta.model = Book
        return super(BookSerializer, self).to_internal_value(data)
