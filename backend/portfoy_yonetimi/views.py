# backend/portfoy_yonetimi/views.py

from rest_framework import viewsets
from .models import Mulk, Musteri
from .serializers import MulkSerializer, MusteriSerializer # Serializers dosyasının da mevcut ve doğru olduğundan emin olun

# --- MulkViewSet (Sizdeki eksik olan kısım) ---
class MulkViewSet(viewsets.ModelViewSet):
    # Tüm mülkleri en yeniye göre sıralar
    queryset = Mulk.objects.all().order_by('-kayit_tarihi')
    serializer_class = MulkSerializer

# --- MusteriViewSet ---
class MusteriViewSet(viewsets.ModelViewSet):
    # Tüm müşterileri isme göre sıralar
    queryset = Musteri.objects.all().order_by('ad_soyad')
    serializer_class = MusteriSerializer