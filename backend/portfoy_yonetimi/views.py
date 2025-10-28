from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Avg, Count, Sum
from decimal import Decimal

# Modeller ve Serializer'lar
from .models import Musteri, Mulk
from .serializers import MusteriSerializer, MulkSerializer

# ------------------------------------------------
# 1. FONKSİYON TABANLI GÖRÜNÜMLER (API_VIEW)
# ------------------------------------------------

@api_view(['GET'])
def mulk_listesi(request):
    """
    Tüm mülklerin listesini çeker ve serileştirir.
    Angular'daki MulkListesiComponent tarafından kullanılır.
    """
    mulkler = Mulk.objects.all().order_by('-kayit_tarihi')
    serializer = MulkSerializer(mulkler, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def istatistik_listesi(request):
    """
    Dashboard için istatistiksel verileri (toplam mülk, ortalama fiyat, dağılım) döndürür.
    """
    toplam_mulk = Mulk.objects.count()
    
    # Ortalama fiyatı hesaplama ve float'a dönüştürme
    ortalama_fiyat_sonuc = Mulk.objects.aggregate(Avg('fiyat'))['fiyat__avg']
    ortalama_fiyat = float(ortalama_fiyat_sonuc) if ortalama_fiyat_sonuc is not None else 0.00
    
    # Durumlara göre sayım (Kiralık, Satılık vb.)
    durum_dagilimi = Mulk.objects.values('durum').annotate(sayi=Count('durum')).order_by()
    
    # Tüm envanterin tahmini toplam değeri
    toplam_deger_sonuc = Mulk.objects.aggregate(Sum('fiyat'))['fiyat__sum']
    toplam_deger = float(toplam_deger_sonuc) if toplam_deger_sonuc is not None else 0.00

    veri = {
        'toplam_mulk': toplam_mulk,
        'ortalama_fiyat': round(ortalama_fiyat, 2),
        'toplam_envanter_degeri': round(toplam_deger, 2),
        'durum_dagilimi': list(durum_dagilimi),
    }
    return Response(veri)


# ------------------------------------------------
# 2. SINIF TABANLI GÖRÜNÜMLER (VIEWSETS - CRUD İÇİN)
# ------------------------------------------------

class MusteriViewSet(viewsets.ModelViewSet):
    """
    Musteri modeli için CRUD işlemlerini sağlar.
    """
    queryset = Musteri.objects.all().order_by('ad_soyad')
    serializer_class = MusteriSerializer

class MulkViewSet(viewsets.ModelViewSet):
    """
    Mulk modeli için CRUD işlemlerini sağlar.
    """
    queryset = Mulk.objects.all().order_by('-kayit_tarihi')
    serializer_class = MulkSerializer