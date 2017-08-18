from django.contrib import admin


from .models import *

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email',)  # talents

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'agent', 'headshot')


admin.site.register(Person, PersonAdmin)
admin.site.register(Artist, ArtistAdmin)
