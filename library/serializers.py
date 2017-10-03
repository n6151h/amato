
from rest_framework import serializers

from urllib.parse import urlparse

from .models import *

from .forms import *

from people.serializers import RoleSerializer

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



class BookSerializer(serializers.ModelSerializer):

    #role_set = serializers.HyperlinkedRelatedField(many=True, read_only=True,
    #                                            view_name="api:people:role-detail")

    role_set = RoleSerializer(many=True, read_only=True)

    url = serializers.HyperlinkedIdentityField(view_name='api:library:book-detail')

    class Meta:
        model = Book
        fields = '__all__'

