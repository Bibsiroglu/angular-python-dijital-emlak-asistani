# backend/portfoy_yonetimi/admin.py

from django.contrib import admin
from .models import Mulk, Musteri

# İsteğe bağlı: Admin panelinde daha güzel listeleme için
class MulkAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'mülk_turu', 'durum', 'fiyat', 'sehir', 'guncelleme_tarihi')
    list_filter = ('mülk_turu', 'durum', 'sehir')
    search_fields = ('baslik', 'adres', 'aciklama')

class MusteriAdmin(admin.ModelAdmin):
    list_display = ('ad_soyad', 'musteri_turu', 'telefon', 'kayit_tarihi')
    list_filter = ('musteri_turu',)
    search_fields = ('ad_soyad', 'telefon', 'eposta')


admin.site.register(Mulk, MulkAdmin)
admin.site.register(Musteri, MusteriAdmin)