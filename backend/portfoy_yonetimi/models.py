# backend/portfoy_yonetimi/models.py

from django.db import models

# MÜŞTERİ YÖNETİMİ
class Musteri(models.Model):
    # Tür seçenekleri
    TUR_SECENEKLERI = (
        ('ALICI', 'Alıcı'),
        ('SATICI', 'Satıcı'),
        ('KIRACI', 'Kiracı'),
        ('KIRALAYAN', 'Kiralayan'),
        ('YATIRIMCI', 'Yatırımcı'),
    )

    ad_soyad = models.CharField(max_length=100)
    telefon = models.CharField(max_length=15, unique=True)
    eposta = models.EmailField(max_length=100, blank=True, null=True)
    musteri_turu = models.CharField(max_length=10, choices=TUR_SECENEKLERI, default='ALICI')
    kayit_tarihi = models.DateTimeField(auto_now_add=True)
    notlar = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.ad_soyad} ({self.musteri_turu})"


# PORTFÖY YÖNETİMİ (Mülkler)
class Mulk(models.Model):
    # Tür seçenekleri
    TUR_SECENEKLERI = (
        ('KONUT', 'Konut'),
        ('ISYERI', 'İşyeri'),
        ('ARSA', 'Arsa'),
        ('PROJE', 'Proje'),
    )
    # Durum seçenekleri
    DURUM_SECENEKLERI = (
        ('SATILIK', 'Satılık'),
        ('KIRALIK', 'Kiralık'),
        ('SATILDI', 'Satıldı'),
        ('KIRALANDI', 'Kiralandı'),
        ('PASIF', 'Pasif'),
    )

    baslik = models.CharField(max_length=255)
    aciklama = models.TextField()
    mülk_turu = models.CharField(max_length=10, choices=TUR_SECENEKLERI)
    durum = models.CharField(max_length=10, choices=DURUM_SECENEKLERI, default='SATILIK')
    
    fiyat = models.DecimalField(max_digits=15, decimal_places=2)
    brut_m2 = models.IntegerField(blank=True, null=True)
    net_m2 = models.IntegerField(blank=True, null=True)
    oda_sayisi = models.CharField(max_length=10, blank=True, null=True)
    
    adres = models.CharField(max_length=255)
    sehir = models.CharField(max_length=50)
    ilce = models.CharField(max_length=50)
    
    # Mülk sahibi (Satıcı/Kiralayan) ile ilişkilendirme
    sahip = models.ForeignKey(Musteri, on_delete=models.SET_NULL, null=True, blank=True, related_name='sahip_oldugu_mulkler')
    
    kayit_tarihi = models.DateTimeField(auto_now_add=True)
    guncelleme_tarihi = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.baslik} ({self.get_durum_display()})"
    # backend/core/settings.py
