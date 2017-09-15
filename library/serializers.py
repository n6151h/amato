
from rest_framework import serializers

from urllib.parse import urlparse

from .models import *

from .forms import *

from util.polymorphic import PolymorphicCTypeField



# -----[ Books and Book subtypees (e.g. scripts, opera scores, ...) ]


class ScriptSerializer(serializers.ModelSerializer):

    #roles = RoleSerializer(many=True, read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='api:library:script-detail')

    polymorphic_ctype = PolymorphicCTypeField(read_only=True)

    class Meta:
        model = Script
        fields = '__all__'
        extra_kwargs = {'url': {'view_name': 'api:library:script-detail'}}
        depth = 1

class MusicalSerializer(serializers.ModelSerializer):

    #roles = RoleSerializer(many=True, read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='api:library:musical-detail')

    polymorphic_ctype = PolymorphicCTypeField(read_only=True)

    class Meta:
        model = Musical
        fields = '__all__'
        depth = 1

class OperaSerializer(serializers.ModelSerializer):

    #roles = serializers.HyperlinkedRelatedField(read_only=True,
    #            view_name="api:library:operaticrole-detail", many=True)

    url = serializers.HyperlinkedIdentityField(
                view_name='api:library:opera-detail')

    polymorphic_ctype = PolymorphicCTypeField(read_only=True)

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

    #def to_representation(self, obj):
    #     return super(OperaSerializer, self).to_representation(obj)


class BookSerializer(serializers.ModelSerializer):

    roles = serializers.HyperlinkedRelatedField(many=True, read_only=True,
                                                view_name="api:people:role-detail")
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
