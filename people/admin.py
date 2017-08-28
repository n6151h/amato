from django.contrib import admin

admin.site.site_title = "Your App Title"
admin.site.site_header = "Your App Admin"


from .models import *

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email',)  # talents

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'agent', 'headshot')


admin.site.register(Person, PersonAdmin)
admin.site.register(Artist, ArtistAdmin)
