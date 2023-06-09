from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin, SortableAdminBase, SortableStackedInline

from .models import Places, Images


class ImagesInline(SortableStackedInline):
    model = Images
    fields = ['place', 'img', 'preview', 'position']
    readonly_fields = ['preview']
    ordering = ['position', ]
    extra  = 1

    # def preview(self, obj):


@admin.register(Images)
class ImagesAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['place', 'position']
    ordering = ('pk', 'place')
    sortable_by = ['place', 'position']
    readonly_fields = ['preview']


@admin.register(Places)
class PlacesAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImagesInline]
