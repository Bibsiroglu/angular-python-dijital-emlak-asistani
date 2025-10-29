# backend/portfoy_yonetimi/models.py

from django.db import models

# ===============================================
# MÜŞTERİ YÖNETİMİ
# ===============================================
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
    kimlik_numarasi = models.CharField(max_length=20, blank=True, null=True)
    ikametgah_adresi = models.TextField(max_length=255, blank=True, null=True)
    iban = models.CharField(max_length=34, blank=True, null=True)
    kayit_tarihi = models.DateTimeField(auto_now_add=True)
    notlar = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.ad_soyad} ({self.musteri_turu})"

# ===============================================
# MÜŞTERİ EVRAK YÖNETİMİ (Yeni Model)
# ===============================================
class MusteriEvraki(models.Model):
    EVRAK_TURLERI = (
        ('KIRA SOZLESMESI', 'Kira Sözleşmesi'),
        ('PROTOKOL', 'Protokol'),
        ('SATIS SOZLESMESI', 'Satış Sözleşmesi'),
        ('SENET', 'Senet'),
    )
    musteri = models.ForeignKey(
        Musteri, 
        on_delete=models.CASCADE, 
        related_name='evraklar'
    )
    
    # Evrağın düzenlenme/geçerlilik tarihi
    evrak_tarihi = models.DateField(
        blank=True, 
        null=True, 
        verbose_name="Evrak Tarihi",
        help_text="Sözleşme veya evrağın düzenlenme tarihi"
    )
    
    # Gerçek dosya yükleme alanı (PDF, JPG vb.)
    dosya = models.FileField(
        upload_to='musteri_evraklari/', 
        verbose_name="Evrak Dosyası",
        help_text="Sözleşme, tapu fotokopisi vb. evrak dosyası"
    )

    # Evrak türü (Opsiyonel, ama faydalı olabilir)
    evrak_turu = models.CharField(max_length=20, choices=EVRAK_TURLERI)

    muhatap = models.ForeignKey(Musteri, on_delete=models.SET_NULL, null=True, blank=True, related_name='muhatap')
    
    aciklama = models.CharField(max_length=255, blank=True, null=True)
    yuklenme_tarihi = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.musteri.ad_soyad} - {self.aciklama or 'Evrak'}"
        
    class Meta:
        verbose_name = "Müşteri Evrağı"
        verbose_name_plural = "Müşteri Evrakları"
# ===============================================
# PORTFÖY YÖNETİMİ (Mülkler)
# ===============================================
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
    bulundugu_kat = models.IntegerField(blank=True, null=True, verbose_name="Bulunduğu Kat")
    bina_kat_sayisi = models.IntegerField(blank=True, null=True, verbose_name="Bina Toplam Kat Sayısı")
    
    adres = models.CharField(max_length=255)
    sehir = models.CharField(max_length=50)
    ilce = models.CharField(max_length=50)
    
    # Mülk sahibi (Satıcı/Kiralayan) ile ilişkilendirme
    sahipleri = models.ManyToManyField(
        Musteri, 
        related_name='sahip_oldugu_mulkler', 
        blank=True, 
        verbose_name="Mülk Sahipleri"
    )
    kayit_tarihi = models.DateTimeField(auto_now_add=True)
    guncelleme_tarihi = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.baslik} ({self.get_durum_display()})"
    

# ===============================================
# 3. YENİ FOTOĞRAF MODELİ (Mulk sınıfının dışında!)
# ===============================================
class MulkFotografi(models.Model):
    mulk = models.ForeignKey(Mulk, 
                             on_delete=models.CASCADE, 
                             related_name='fotograflar') # Bu fotoğrafların hangi mülke ait olduğunu belirtir.
                             
    foto = models.ImageField(upload_to='mulk_fotograflari/') # Gerçek resim dosyası
    
    aciklama = models.CharField(max_length=255, blank=True, null=True) # Opsiyonel açıklama
    
    varsayilan = models.BooleanField(default=False) # Eğer varsa, ilk fotoğrafı belirlemek için
    
    def __str__(self):
        return f"{self.mulk.baslik} - Fotoğraf {self.id}"
    
    class Meta:
        verbose_name_plural = "Mülk Fotoğrafları"