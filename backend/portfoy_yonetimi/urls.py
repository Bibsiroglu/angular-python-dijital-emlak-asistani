from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MusteriViewSet, MulkViewSet

# DefaultRouter, ViewSet'ler için gerekli olan tüm URL yollarını otomatik oluşturur.
router = DefaultRouter()

# Uç noktaları router'a kaydetme
# Bu, http://127.0.0.1:8000/api/musteriler/ ve /api/mulkler/ yollarını oluşturur.
router.register(r'musteriler', MusteriViewSet)
router.register(r'mulkler', MulkViewSet) 

# Eğer Django projenizin ana urls.py'sinde 'api/' yolu tanımlanmışsa
urlpatterns = [
    path('', include(router.urls)),
]
# Eğer projenizin ana urls.py'sinde uygulamanız doğrudan takılıysa, urlpatterns = router.urls