from django.contrib import admin

from .models import Places, Images


class ImagesInline(admin.TabularInline):
    model = Images


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ["pk", "place"]
    ordering = ('pk',)

@admin.register(Places)
class PlacesAdmin(admin.ModelAdmin):
    inlines = [ImagesInline]
