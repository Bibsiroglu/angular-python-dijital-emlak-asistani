from django.contrib import admin
from .models import Musteri, Mulk, MulkFotografi # Yeni modeli import edin

# 1. Galeri için arayüz (Inline) tanımlıyoruz
class MulkFotografiInline(admin.TabularInline): # TabularInline, daha kompakt bir görünüm sağlar
    model = MulkFotografi
    extra = 1 # Varsayılan olarak bir boş alan göster

# 2. Mulk modelini bu galeri arayüzü ile kaydediyoruz
class MulkAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'mülk_turu', 'fiyat', 'durum')
    list_filter = ('mülk_turu', 'durum', 'sehir')
    search_fields = ('baslik', 'aciklama')
    inlines = [MulkFotografiInline] # <-- Galeri arayüzünü buraya ekliyoruz

# 3. Müşteri modelini de admin'e kaydediyoruz
admin.site.register(Musteri)
admin.site.register(Mulk, MulkAdmin) # Mulk modelini yeni admin sınıfı ile kaydedin

# MulkFotografi modelini ayriyetten kaydetmeye gerek yok, Mulk üzerinden yönetilecek.