
from django.contrib import admin
from polymorphic.admin import (
    PolymorphicParentModelAdmin,
    PolymorphicChildModelAdmin,
    PolymorphicChildModelFilter
    )

from talent.models import *

# class ModelAChildAdmin(PolymorphicChildModelAdmin):
#     """ Base admin class for all child models """
#     base_model = ModelA

#     # By using these `base_...` attributes instead of the regular ModelAdmin `form` and `fieldsets`,
#     # the additional fields of the child models are automatically added to the admin form.
#     base_form = ...
#     base_fieldsets = (
#         ...
#     )


# @admin.register(ModelB)
# class ModelBAdmin(ModelAChildAdmin):
#     base_model = ModelB
#     # define custom features here


# @admin.register(ModelC)
# class ModelCAdmin(ModelBAdmin):
#     base_model = ModelC
#     show_in_index = True  # makes child model admin visible in main admin site
#     # define custom features here


# @admin.register(ModelA)
# class ModelAParentAdmin(PolymorphicParentModelAdmin):
#     """ The parent model admin """
#     base_model = ModelA
#     child_models = (ModelB, ModelC)
#     list_filter = (PolymorphicChildModelFilter,)  # This is optional.
