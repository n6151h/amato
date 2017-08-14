from django.contrib import admin

from .models import Opera, OperaticRole

class OperaticRoleInline(admin.StackedInline):
    model = OperaticRole
    extra = 1

    fields = ['name', 'description', 'voice', 'fach']

class OperaAdmin(admin.ModelAdmin):
    inlines = [OperaticRoleInline]

    list_display = ['title', 'composer', 'librettist', 'publisher']

admin.site.register(Opera, OperaAdmin)

