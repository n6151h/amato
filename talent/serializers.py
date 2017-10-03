from rest_framework import serializers

from .models import *

from util.polymorphic import PolymorphicCTypeField

class SingingSerializer(serializers.ModelSerializer):

    polymorphic_ctype = PolymorphicCTypeField(read_only=True)
    voice = serializers.StringRelatedField()
    fach = serializers.StringRelatedField()

    class Meta:
        model = Singing
        fields = '__all__'


class DancingSerializer(serializers.ModelSerializer):

    polymorphic_ctype = PolymorphicCTypeField(read_only=True)
    style = serializers.StringRelatedField()

    class Meta:
        model = Dancing
        fields = '__all__'

class OrchestraSerializer(serializers.ModelSerializer):

    polymorphic_ctype = PolymorphicCTypeField(read_only=True)
    instrument = serializers.StringRelatedField()

    class Meta:
        model = Dancing
        fields = '__all__'

class ActingSerializer(serializers.ModelSerializer):

    polymorphic_ctype = PolymorphicCTypeField(read_only=True)
    instrument = serializers.StringRelatedField()

    class Meta:
        model = Dancing
        fields = '__all__'


class TalentSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(read_only=True,
                                               view_name="api:talent:talent-detail")

    class Meta:
        model = Talent
        fields = '__all__'

    def to_representation(self, obj):
        """
        Because Talent is Polymorphic
        """
        if isinstance(obj, Singing):
            return SingingSerializer(obj, context=self.context).to_representation(obj)

        elif isinstance(obj, Dancing):
            return DancingSerializer(obj, context=self.context).to_representation(obj)

        elif isinstance(obj, Acting):
            return ActingSerializer(obj, context=self.context).to_representation(obj)

        elif isinstance(obj, Orchestra):
            return OrchestraSerializer(obj, context=self.context).to_representation(obj)

        return super(TalentSerializer, self).to_representation(obj)


    def to_internal_value(self, data):
        """
        Because Talent is Polymorphic
        """
        if data.get('type') == "Singing":
            self.Meta.model = Singing
            return SingingSerializer(context=self.context).to_internal_value(data)

        elif data.get('type') == "Dancing":
            self.Meta.model = Dancing
            return DancingSerializer(context=self.context).to_internal_value(data)

        elif data.get('type') == "Acting":
            self.Meta.model = Acting
            return ActingSerializer(context=self.context).to_internal_value(data)

        elif data.get('type') == "Orchestra":
            self.Meta.model = Orchestra
            return OrchestraSerializer(context=self.context).to_internal_value(data)

        self.Meta.model = Talent
        return super(TalentSerializer, self).to_internal_value(data)
