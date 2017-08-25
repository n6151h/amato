
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


@admin.register(Dancing)
class DancingAdmin(TalentSubclassAdmin):
    base_model = Dancing
    show_in_index = True


@admin.register(Orchestra)
class OrchestraAdmin(TalentSubclassAdmin):
    base_model = Orchestra
    show_in_index = True


@admin.register(Talent)
class TalentAdmin(PolymorphicParentModelAdmin):
    """*Talent* model admin"""
    base_model = Talent
    child_models = (Singing, Dancing, Orchestra)
    list_filter = (PolymorphicChildModelFilter,)  # This is optional.
