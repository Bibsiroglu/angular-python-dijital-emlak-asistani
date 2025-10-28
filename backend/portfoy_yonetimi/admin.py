from django.contrib import admin
from .models import Musteri, Mulk, MulkFotografi
from django.db.models import Avg, Count
from django.utils.html import format_html
from django.urls import path
from django.shortcuts import render
from decimal import Decimal

# ------------------------------------------------
# 1. MulkFotografi için Inline Tanımı (Galeri)
# ------------------------------------------------

class MulkFotografiInline(admin.TabularInline):
    """
    Mülk detay sayfasında birden fazla fotoğrafın eklenmesini sağlar.
    """
    model = MulkFotografi
    extra = 1
    # Dosya yüklemesini direkt olarak listeler, daha düzenli
    fields = ('foto', 'aciklama') 
    
# ------------------------------------------------
# 2. Mulk Modeli Admin Tanımı
# ------------------------------------------------

class MulkAdmin(admin.ModelAdmin):
    # Bu metod, her mülkün fotoğraf sayısını list_display'de gösterir
    def get_foto_sayisi(self, obj):
        return obj.fotograflar.count()
    get_foto_sayisi.short_description = 'Fotoğraf Sayısı'

    # list_display'e fotoğraf sayısını ve diğer önemli alanları ekledik
    list_display = ('baslik', 'mülk_turu', 'fiyat', 'durum', 'sehir', 'get_foto_sayisi')
    
    list_filter = ('mülk_turu', 'durum', 'sehir')
    search_fields = ('baslik', 'aciklama')
    inlines = [MulkFotografiInline] # <-- Galeri arayüzünü ekliyoruz
    
    # ------------------------------------------------
    # 3. İstatistiksel Dashboard View (Admin içinde)
    # ------------------------------------------------
    
    def istatistik_dashboard_view(self, request):
        # Admin modelinin içinden istatistikleri hesaplama
        toplam_mulk = Mulk.objects.count()
        ortalama_fiyat_sonuc = Mulk.objects.aggregate(Avg('fiyat'))['fiyat__avg']
        
        context = dict(
           # super metodu ile gelen context'i korur
           self.admin_site.each_context(request),
           toplam_mulk=toplam_mulk,
           ortalama_fiyat=f"{ortalama_fiyat_sonuc or 0:,.2f} TL"
        )
        
        # Eğer bu dosyanızda özel bir template kullanmak isterseniz
        # render(request, "admin/dashboard.html", context) kullanabilirsiniz.
        # Şimdilik mülk listesini döndürelim ve istatistikleri konsolda tutalım.
        return super().changelist_view(request, extra_context=context)

    # Admin panelindeki URL'leri özelleştirme
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            # Yeni bir URL yolu: /admin/portfoy_yonetimi/mulk/dashboard/
            path('dashboard/', self.admin_site.admin_view(self.istatistik_dashboard_view), name='mulk_dashboard'),
        ]
        return custom_urls + urls

# ------------------------------------------------
# 4. Modelleri Admin'e Kaydetme
# ------------------------------------------------

admin.site.register(Musteri)
admin.site.register(Mulk, MulkAdmin)

# MulkFotografi artık MulkAdmin içinde Inline olarak yönetildiği için ayrı kaydetmeye gerek yoktur.