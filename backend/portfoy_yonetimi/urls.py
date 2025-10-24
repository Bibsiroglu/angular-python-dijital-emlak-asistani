# backend/portfoy_yonetimi/urls.py

from rest_framework.routers import DefaultRouter
from .views import MulkViewSet, MusteriViewSet

router = DefaultRouter()

# R'nin hemen yanındaki tırnak işaretinin içindeki 'mulkler' kelimesini kontrol edin.
router.register(r'mulkler', MulkViewSet) 
router.register(r'musteriler', MusteriViewSet)

urlpatterns = router.urls