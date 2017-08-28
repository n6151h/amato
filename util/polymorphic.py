
'''
Extras for use with Django Polymorphic package
'''

from rest_framework import serializers

class PolymorphicCTypeField(serializers.RelatedField):

    def to_representation(self, value):
        return str(value)

    def display_value(self, instance):
        import pdb
        pdb.set_trace()
        return '"class": "%s"' % instance.polymorphic_ctype