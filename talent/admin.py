
from django.contrib import admin
from polymorphic.admin import (
    PolymorphicParentModelAdmin,
    PolymorphicChildModelAdmin,
    PolymorphicChildModelFilter
    )

from talent.models import *

class TalentSubclassAdmin(PolymorphicChildModelAdmin):
    """ Base admin class for all child models """
    base_model = Talent

    # By using these `base_...` attributes instead of the regular ModelAdmin `form` and `fieldsets`,
    # the additional fields of the child models are automatically added to the admin form.
    #base_form = ...
    #base_fieldsets = (
    #    ...
    #)


@admin.register(Singing)
class SingingAdmin(TalentSubclassAdmin):
    base_model = Singing
    show_in_index = True

    list_display = ['display_name',]
    exclude = ('category',)
    def display_name(self, obj):

      return "{} ({})".format((obj.voice.name).title(), obj.fach.display_name) \
            if obj.fach.name != '' else (obj.voice.name).title()

    display_name.short_description = 'Vocal Range (and Fach)'


@admin.register(Voice)
class VoiceAdmin(admin.ModelAdmin):
    base_model = Voice
    show_in_index = True

    list_display = ['display_name',]

    def display_name(self, obj):
      return (obj.name).title()

    display_name.short_description = 'Vocal Range / Type'


@admin.register(Fach)
class FachAdmin(admin.ModelAdmin):
    base_model = Fach
    show_in_index = True

    list_display = ['display_or_caps',]

    def display_or_caps(self, obj):
        return obj.display_name if obj.display_name != "" else (obj.name).title()

    display_or_caps.short_description = 'Fach'

@admin.register(Dancing)
class DancingAdmin(TalentSubclassAdmin):
    base_model = Dancing
    show_in_index = True

    exclude = ('category',)

@admin.register(DancingStyle)
class DancingStyleAdmin(admin.ModelAdmin):
    base_model = Instrument
    show_in_index = True

@admin.register(Orchestra)
class OrchestraAdmin(TalentSubclassAdmin):
    base_model = Orchestra
    show_in_index = True

    exclude = ('category',)

@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    base_model = Instrument
    show_in_index = True

@admin.register(Talent)
class InstrumentAdmin(admin.ModelAdmin):
    base_model = Talent
    show_in_index = False

