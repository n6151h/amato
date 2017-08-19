from rest_framework import serializers

from .models import *

class SeasonSerializer(serializers.ModelSerializer):

    #book = serializers.PrimaryKeyRelatedField(many=True,
    #                        queryset=Book.objects.all())
    #        view_name='opera-score') #,
    #    read_only=True)

    class Meta:
        model = Season
        fields = '__all__'

class ProductionSerializer(serializers.ModelSerializer):

    #book = serializers.HyperlinkedRelatedField(
    #    view_name='opera-score',
    #    read_only=True)

    class Meta:
        model = Production
        fields = '__all__'

class ShowSerializer(serializers.ModelSerializer):

    #book = serializers.HyperlinkedRelatedField(
    #    view_name='opera-score',
    #    read_only=True)

    class Meta:
        model = Show
        fields = '__all__'

class CallSerializer(serializers.ModelSerializer):

    #book = serializers.HyperlinkedRelatedField(
    #    view_name='opera-score',
    #    read_only=True)

    class Meta:
        model = Call
        fields = '__all__'

