from django.contrib import admin


from .models import *


class ContactDataInline(admin.StackedInline):
    model = ContactData
    extra = 1

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    inlines = [ContactDataInline,]
    filter_horizontal = ('talents',)
    list_display = ['full_name',]

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    inlines = [ContactDataInline,]
    list_display = ['full_name',]
    filter_horizontal = ('talents',)


@admin.register(RoleLevel)
class RoleLevelAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_talents', 'book', 'level',)
    list_filter = ('book', 'level',)
    fields = ('book', 'name', 'talents', 'level', 'description',)
    filter_horizontal = ('talents',)

    def display_talents(self, obj):
        return ",".join([str(t) for t in obj.talents.all()])

