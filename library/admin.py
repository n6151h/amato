from django.contrib import admin

from .models import (
        Script,
        Musical,
        Opera,
        Role,
        OperaticRole,
    )

class OperaticRoleInline(admin.StackedInline):
    model = OperaticRole
    extra = 1

    fields = ['name', 'description', 'voice', 'fach']

class OperaAdmin(admin.ModelAdmin):
    inlines = [OperaticRoleInline]

    list_display = ['title', 'composer', 'librettist', 'publisher']


class RoleAdmin(admin.StackedInline):
    model = Role
    extra = 1
    fields = ['name', 'description', 'role_type']


class ScriptAdmin(admin.ModelAdmin):
    inlines = [RoleAdmin]

    list_display = ['title', 'author']


class MusicalAdmin(admin.ModelAdmin):
    inlines = [RoleAdmin]

    list_display = ['title', 'composer', 'lyricist']

admin.site.register(Opera, OperaAdmin)
admin.site.register(Script, ScriptAdmin)
admin.site.register(Musical, MusicalAdmin)


