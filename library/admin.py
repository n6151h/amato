from django.contrib import admin

from enumchoicefield.admin import EnumListFilter

from .models import (
        Script,
        Musical,
        Opera,
    )

@admin.register(Opera)
class OperaAdmin(admin.ModelAdmin):
    inlines = []

    list_display = ['title', 'composer', 'librettist', 'publisher']


@admin.register(Script)
class ScriptAdmin(admin.ModelAdmin):
    inlines = []

    list_display = ['title', 'author']


@admin.register(Musical)
class MusicalAdmin(admin.ModelAdmin):
    inlines = []

    list_display = ['title', 'composer', 'lyricist']



