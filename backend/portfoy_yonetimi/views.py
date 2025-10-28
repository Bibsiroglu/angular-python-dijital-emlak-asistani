# portfoy_yonetimi/views.py

from rest_framework import viewsets
from .models import Musteri, Mulk
from .serializers import MusteriSerializer, MulkSerializer

class MusteriViewSet(viewsets.ModelViewSet):
    """
    Bu ViewSet, Musteri modeli için tüm CRUD işlemlerini otomatik sağlar.
    """
    queryset = Musteri.objects.all().order_by('ad_soyad')
    serializer_class = MusteriSerializer

class MulkViewSet(viewsets.ModelViewSet):
    """
    Bu ViewSet, Mulk modeli için tüm CRUD işlemlerini otomatik sağlar.
    """
    queryset = Mulk.objects.all().order_by('-kayit_tarihi')
    serializer_class = MulkSerializer