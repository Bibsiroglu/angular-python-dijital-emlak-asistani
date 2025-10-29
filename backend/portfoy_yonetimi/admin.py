from django.contrib import admin
# Gerekli importlar - Sadece '.models' şeklinde göreceli içe aktarma kullanıldı.
from .models import Musteri, Mulk, MulkFotografi, MusteriEvraki 
from django.db.models import Avg, Count
from django.utils.html import format_html
from django.urls import path
from django.shortcuts import render 
from decimal import Decimal

# ------------------------------------------------
# 1. Inline Tanımları (Galeri ve Evraklar)
# ------------------------------------------------

class MulkFotografiInline(admin.TabularInline):
    """
    Mülk detay sayfasında birden fazla fotoğrafın eklenmesini sağlar (Galeri).
    """
    model = MulkFotografi
    extra = 1
    # Dosya yüklemesini direkt olarak listeler, daha düzenli
    fields = ('foto', 'aciklama') 
    # Mülk modelinde 'fotograflar' related_name'ini varsayarak
    fk_name = 'mulk' 

class MusteriEvrakiInline(admin.TabularInline): 
    """
    Müşteri detay sayfasında birden fazla evrakın eklenmesini sağlar.
    """
    model = MusteriEvraki
    extra = 1
    # 'evrak_turu' ve 'muhatap' alanları models.py'de düzeltilmiş olmalıdır
    fields = ('evrak_turu', 'evrak_tarihi', 'muhatap', 'dosya', 'aciklama')
    # Musteri modelinde 'evraklar' related_name'ini varsayarak
    fk_name = 'musteri'
    
# ------------------------------------------------
# 2. Musteri Modeli Admin Tanımı (Filtre Eklendi)
# ------------------------------------------------

class MusteriAdmin(admin.ModelAdmin):
    """
    Müşteri modelini yönetir ve evraklarını inline olarak gösterir.
    """
    list_display = ('ad_soyad', 'telefon', 'eposta', 'get_evrak_sayisi')
    search_fields = ('ad_soyad', 'telefon', 'eposta', 'kimlik_numarasi')
    inlines = [MusteriEvrakiInline] # <-- Evrak arayüzünü ekliyoruz

    # Doğru tuple sintaksı kullanıldı.
    list_filter = ('musteri_turu', 'kayit_tarihi') 

    def get_evrak_sayisi(self, obj):
        return obj.evraklar.count() # Modelinizdeki related_name'e göre ayarlayın
    get_evrak_sayisi.short_description = 'Evrak Sayısı'

# ------------------------------------------------
# 3. Mulk Modeli Admin Tanımı
# ------------------------------------------------

class MulkAdmin(admin.ModelAdmin):
    # Bu metod, her mülkün fotoğraf sayısını list_display'de gösterir
    def get_foto_sayisi(self, obj):
        return obj.fotograflar.count() # Mulk modelinizdeki related_name'e göre ayarlayın
    get_foto_sayisi.short_description = 'Fotoğraf Sayısı'

    def get_sahipleri_listesi(self, obj):
        # Mülkün sahiplerini virgülle ayırarak gösterir (Çoktan Çoğa ilişki olduğu için)
        # models.py'de sahipleri alanı ManyToManyField olarak kabul edilir.
        return ", ".join([s.ad_soyad for s in obj.sahipleri.all()])
    get_sahipleri_listesi.short_description = 'Sahipleri'

    # list_display'e fotoğraf sayısını ve sahipleri ekledik
    list_display = ('baslik', 'mülk_turu', 'fiyat', 'durum', 'sehir', 'get_foto_sayisi', 'get_sahipleri_listesi')
    list_filter = ('mülk_turu', 'durum', 'sehir', 'ilce') # Mulk için filtreler
    search_fields = ('baslik', 'aciklama', 'adres')
    inlines = [MulkFotografiInline] # <-- Galeri arayüzünü ekliyoruz
    
    # filter_horizontal listesi doğru şekilde tanımlandı.
    filter_horizontal = ('sahipleri',) 

    # Alan gruplarını ayırma (isteğe bağlı, okumayı kolaylaştırır)
    fieldsets = (
        ('Mülk Temel Bilgileri', {
            'fields': ('baslik', 'aciklama', 'mülk_turu', 'durum', 'fiyat', 'sahipleri')
        }),
        ('Detaylı Özellikler', {
            'fields': ('brut_m2', 'net_m2', 'oda_sayisi', 'bulundugu_kat', 'bina_kat_sayisi'),
            'classes': ('collapse',), # Bu alanı varsayılan olarak gizler
        }),
        ('Konum Bilgileri', {
            'fields': ('sehir', 'ilce', 'adres'),
        }),
    )
    
    # ------------------------------------------------
    # 4. İstatistiksel Dashboard View (Admin içinde)
    # ------------------------------------------------
    
    def istatistik_dashboard_view(self, request):
        # İstatistik hesaplamaları
        toplam_mulk = Mulk.objects.count()
        ortalama_fiyat_sonuc = Mulk.objects.filter(durum__in=['SATILIK', 'KIRALIK']).aggregate(Avg('fiyat'))['fiyat__avg']
        
        # Mülk türüne göre sayım
        tur_dagilimi = Mulk.objects.values('mülk_turu').annotate(sayi=Count('id')).order_by('-sayi')
        
        # Template'e gönderilecek veriyi hazırla
        context = dict(
            # super metodu ile gelen admin site context'ini korur (sidebar, header vb.)
            self.admin_site.each_context(request),
            toplam_mulk=toplam_mulk,
            # Formatlama kontrolü
            ortalama_fiyat=f"{ortalama_fiyat_sonuc if ortalama_fiyat_sonuc is not None else 0:,.2f} TL",
            tur_dagilimi=tur_dagilimi,
            title="Mülk Yönetimi İstatistik Paneli" # Sayfa başlığını belirler
        )
        
        # Örnek: 'admin/dashboard.html' template'ini render et
        return render(request, "admin/dashboard.html", context)

    # Admin panelindeki URL'leri özelleştirme
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            # Yeni bir URL yolu: /admin/app_adi/mulk/dashboard/
            path('dashboard/', self.admin_site.admin_view(self.istatistik_dashboard_view), name='mulk_dashboard'),
        ]
        return custom_urls + urls

# ------------------------------------------------
# 5. Modelleri Admin'e Kaydetme
# ------------------------------------------------

# Musteri modelini MusteriAdmin ile kaydet
admin.site.register(Musteri, MusteriAdmin) 
# Mulk modelini MulkAdmin ile kaydet
admin.site.register(Mulk, MulkAdmin)

# MulkFotografi ve MusteriEvraki, ilgili Admin sınıfları içinde Inline olarak 
# yönetildiği için ayrı ayrı kaydetmeye gerek yoktur.
