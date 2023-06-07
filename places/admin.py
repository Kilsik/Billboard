from django.contrib import admin

from .models import Places, Images


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ["pk", "place"]
    ordering = ('pk',)

admin.site.register(Places)
# admin.site.register(Images)