from django.contrib import admin


from .models import *

class InstrumentalistAdmin(admin.ModelAdmin):
    list_display = ('name', 'instrument', 'phone', 'email')

class SingerAdmin(admin.ModelAdmin):
    list_display = ('name', 'voice', 'phone', 'email')

class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'area', 'phone', 'email')

admin.site.register(Instrumentalist, InstrumentalistAdmin)
admin.site.register(Singer, SingerAdmin)
admin.site.register(Staff, StaffAdmin)
