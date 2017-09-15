from django.contrib import admin


from .models import *

import people.models as pm

from django.contrib.contenttypes.models import ContentType

admin.site.register(Season)
admin.site.register(Production)
admin.site.register(Show)
admin.site.register(CallType)

@admin.register(Call)
class CallAdmin(admin.ModelAdmin):
    list_display = ('dtg', 'production', 'type', 'short_description',)

    filter_horizontal = ('called',)

    fields = ('production', 'type', 'dtg', 'duration', 'location',
           'short_description', 'long_description', 'called',)

    def get_field_queryset(self, db, db_field, request):
        """
        If the ModelAdmin specifies ordering, the queryset should respect that
        ordering.  Otherwise don't specify the queryset, let the field decide
        (returns None in that case).
        """
        if db_field.name == 'called':
            import pdb
            pdb.set_trace()

            role_ct = ContentType.objects.get_for_model(pm.Role)

            return db_field.remote_field.model._default_manager.exclude(polymorphic_ctype=role_ct)

        super().get_field_queryset(db, db_field, request)