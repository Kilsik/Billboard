from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin, SortableAdminBase, SortableStackedInline
from django.utils.html import format_html

from .models import Places, Images


class ImagesInline(SortableStackedInline):
    model = Images
    fields = ['place', 'img', 'position', 'preview']
    readonly_fields = ['preview']
    ordering = ['position', ]
    extra = 1

    def preview(self, obj):
        return format_html(
            '<img src={} height={}>',
            obj.img.url,
            200
        )


@admin.register(Images)
class ImagesAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['place', 'position']
    ordering = ('pk', 'place')
    sortable_by = ['place', 'position']


@admin.register(Places)
class PlacesAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImagesInline]
