from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin, SortableAdminBase, SortableStackedInline
from django.utils.html import format_html

from .models import Place, Image


class ImagesInline(SortableStackedInline):
    model = Image
    fields = ['place', 'img', 'position', 'preview']
    readonly_fields = ['preview']
    ordering = ['position', ]
    extra = 1

    def preview(self, img):
        return format_html(
            '<img src={} height={}>',
            img.img.url,
            200
        )


@admin.register(Image)
class ImagesAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['position', 'place']
    sortable_by = ['position', 'place']


@admin.register(Place)
class PlacesAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImagesInline]
