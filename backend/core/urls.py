from django.contrib import admin
from django.urls import path, include
# GEREKLİ IMPORTLAR
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('portfoy_yonetimi.urls')), 
]

# SADECE GELİŞTİRME ORTAMI İÇİN GEÇERLİ AYARLAR
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)