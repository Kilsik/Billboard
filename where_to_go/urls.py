from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from places import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_billboards),
    path('places/<int:placeid>', views.show_place_detail, name='show-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
