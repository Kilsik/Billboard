from django.contrib import admin
# from django.utils.safestring import mark_safe

from .models import Places, Images


class ImagesInline(admin.TabularInline):
    model = Images
    fields = ['place', 'img', 'preview', 'position']
    readonly_fields = ['preview']

    # def preview(self, obj):


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['place', 'position']
    ordering = ('pk', 'place')
    sortable_by = ['place', 'position']
    readonly_fields = ['preview']


@admin.register(Places)
class PlacesAdmin(admin.ModelAdmin):
    inlines = [ImagesInline]
