from rest_framework import serializers

from .models import *

class CompanySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'