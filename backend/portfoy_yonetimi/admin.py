from django.contrib import admin
from .models import Musteri, Mulk, MulkFotografi, MusteriEvraki 
from django.db.models import Avg, Count
from django.utils.html import format_html
# Gerekli olan reverse fonksiyonu buraya import edildi.
from django.urls import path, reverse 
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
    fk_name = 'mulk' 

class MusteriEvrakiInline(admin.TabularInline): 
    """
    Müşteri detay sayfasında birden fazla evrakın eklenmesini sağlar.
    """
    model = MusteriEvraki
    extra = 1
    fields = ('evrak_turu', 'evrak_tarihi', 'muhatap', 'dosya', 'aciklama')
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
    inlines = [MusteriEvrakiInline]

    list_filter = ('musteri_turu', 'kayit_tarihi') 

    def get_evrak_sayisi(self, obj):
        # Modelinizdeki related_name: 'evraklar'
        return obj.evraklar.count() 
    get_evrak_sayisi.short_description = 'Evrak Sayısı'

# ------------------------------------------------
# 3. Mulk Modeli Admin Tanımı
# ------------------------------------------------

class MulkAdmin(admin.ModelAdmin):
    
    # Bu metod, her mülkün fotoğraf sayısını list_display'de gösterir
    def get_foto_sayisi(self, obj):
        # Modelinizdeki related_name: 'fotograflar'
        return obj.fotograflar.count()
    get_foto_sayisi.short_description = 'Fotoğraf Sayısı'

    # Buraya yerleştirilen, tıklanabilir sahipleri gösteren metod
    def get_sahipleri_listesi(self, obj):
        """
        Mülkün sahiplerini tıklanabilir linkler halinde gösterir.
        """
        sahip_linkleri = []
        for sahip in obj.sahipleri.all():
            # Musteri modelinin detay URL'sini oluştur
            # URL formatı: 'admin:appname_modelname_change'
            url = reverse('admin:portfoy_yonetimi_musteri_change', args=[sahip.pk])
            # HTML formatında linki oluştur
            sahip_linkleri.append(format_html('<a href="{}">{}</a>', url, sahip.ad_soyad))
        
        return format_html(", ".join(sahip_linkleri))
        
    get_sahipleri_listesi.short_description = 'Sahipleri'
    # Bu özelliği eklemek ZORUNLUDUR, aksi halde HTML güvenli olarak işlenmez
    get_sahipleri_listesi.allow_tags = True
    # Sıralama için admin alanını ayarla
    get_sahipleri_listesi.admin_order_field = 'sahipleri' 

    def get_konut_tipi_display(self, obj):
       if obj.mülk_turu == 'KONUT':
            return obj.get_konut_tipi_display()
       return '-'
    get_konut_tipi_display.short_description = 'Konut Tipi'

    def get_isyeri_tipi_display(self, obj):
       if obj.mülk_turu == 'ISYERI':
            return obj.get_isyeri_tipi_display()
       return '-'
    get_isyeri_tipi_display.short_description = 'İsyeri Tipi'

    list_display = ('baslik', 'mülk_turu','get_konut_tipi_display','get_isyeri_tipi_display', 'fiyat', 'durum', 'sehir', 'get_foto_sayisi', 'get_sahipleri_listesi')
    list_filter = ('mülk_turu', 'durum', 'sehir', 'ilce')
    search_fields = ('baslik', 'aciklama', 'adres')
    inlines = [MulkFotografiInline]
    
    filter_horizontal = ('sahipleri',) 

    # Alan gruplarını ayırma (tasinmaz_id çıkarıldı)
    fieldsets = (
        ('Mülk Temel Bilgileri', {
            'fields': ('baslik', 'aciklama', 'mülk_turu', 'konut_tipi', 'isyeri_tipi', 'durum', 'fiyat', 'sahipleri')
        }),
        ('Detaylı Özellikler', {
            'fields': ('brut_m2', 'net_m2', 'oda_sayisi', 'bulundugu_kat', 'bina_kat_sayisi'),
            'classes': ('collapse',),
        }),
        ('Konum Bilgileri', {
            'fields': ('sehir', 'ilce', 'adres'),
        }),
    )

    class Media:
        """
        Django Admin'e bu form yüklenirken toggle_konut_tipi.js dosyasını yüklemesini söyler.
        """
        js = (
            'portfoy_yonetimi/js/toggle_konut_tipi.js', 
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
            self.admin_site.each_context(request),
            toplam_mulk=toplam_mulk,
            # Fiyatı TL olarak formatla
            ortalama_fiyat=f"{ortalama_fiyat_sonuc if ortalama_fiyat_sonuc is not None else 0:,.2f} TL",
            tur_dagilimi=tur_dagilimi,
            title="Mülk Yönetimi İstatistik Paneli"
        )
        
        # Admin dashboard'u için varsayılan bir template adını kullanır.
        return render(request, "admin/dashboard.html", context)

    # Admin panelindeki URL'leri özelleştirme
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('dashboard/', self.admin_site.admin_view(self.istatistik_dashboard_view), name='mulk_dashboard'),
        ]
        return custom_urls + urls

# ------------------------------------------------
# 5. Modelleri Admin'e Kaydetme
# ------------------------------------------------

admin.site.register(Musteri, MusteriAdmin) 
admin.site.register(Mulk, MulkAdmin)
