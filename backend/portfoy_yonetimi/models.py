from django.db import models
from django.core.validators import MinValueValidator # Kullanılmadığı için kaldırılabilir, ama tutarlılık için bıraktım
from decimal import Decimal # Kullanılmadığı için kaldırılabilir, ama tutarlılık için bıraktım

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

    ad_soyad = models.CharField(max_length=100, verbose_name="Ad Soyad")
    telefon = models.CharField(max_length=15, blank=True, null=True, verbose_name="Telefon")
    eposta = models.EmailField(max_length=100, blank=True, null=True, verbose_name="E-posta")
    musteri_turu = models.CharField(max_length=10, choices=TUR_SECENEKLERI, default='ALICI', verbose_name="Müşteri Türü")
    kimlik_numarasi = models.CharField(max_length=20, blank=True, null=True, verbose_name="Kimlik Numarası")
    
    ikametgah_adresi = models.TextField(blank=True, null=True, verbose_name="İkametgah Adresi") 
    
    iban = models.CharField(max_length=34, blank=True, null=True, verbose_name="IBAN")
    kayit_tarihi = models.DateTimeField(auto_now_add=True, verbose_name="Kayıt Tarihi")
    notlar = models.TextField(blank=True, null=True, verbose_name="Notlar")

    class Meta:
        verbose_name = "Müşteri"
        verbose_name_plural = "Müşteriler"

    def __str__(self):
        return f"{self.ad_soyad} ({self.get_musteri_turu_display()})"

# ===============================================
# MÜŞTERİ EVRAK YÖNETİMİ
# ===============================================
class MusteriEvraki(models.Model):
    EVRAK_TURLERI = (
        ('KIRA_SOZLESMESI', 'Kira Sözleşmesi'),
        ('PROTOKOL', 'Protokol'),
        ('SATIS_SOZLESMESI', 'Satış Sözleşmesi'),
        ('SENET', 'Senet'),
    )
    musteri = models.ForeignKey(
        Musteri, 
        on_delete=models.CASCADE, 
        related_name='evraklar',
        verbose_name="Müşteri (Evrak Sahibi)"
    )
    
    evrak_tarihi = models.DateField(
        blank=True, 
        null=True, 
        verbose_name="Evrak Tarihi",
        help_text="Sözleşme veya evrağın düzenlenme tarihi"
    )
    
    dosya = models.FileField(
        upload_to='musteri_evraklari/', 
        verbose_name="Evrak Dosyası",
        help_text="Sözleşme, tapu fotokopisi vb. evrak dosyası"
    )

    evrak_turu = models.CharField(max_length=20, choices=EVRAK_TURLERI, verbose_name="Evrak Türü")

    muhatap = models.ForeignKey(
        Musteri, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='ilgili_oldugu_evraklar',
        verbose_name="Muhatap (İlgili Kişi)"
    )
    
    aciklama = models.CharField(max_length=255, blank=True, null=True, verbose_name="Açıklama")
    yuklenme_tarihi = models.DateTimeField(auto_now_add=True, verbose_name="Yüklenme Tarihi")
    
    def __str__(self):
        return f"{self.musteri.ad_soyad} - {self.aciklama or self.get_evrak_turu_display()}"
        
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
        ('DEVREN_KIRALIK', 'Devren Kiralık'),
        ('SATILDI', 'Satıldı'),
        ('KIRALANDI', 'Kiralandı'),
        ('PASIF', 'Pasif'),
    )

    ESYA_DURUM_SECENEKLERI = (
        ('ESYALI', 'Eşyalı'),
        ('ESYASIZ', 'Eşyasız')
    )

    baslik = models.CharField(max_length=255, verbose_name="Başlık")
    aciklama = models.TextField(verbose_name="Açıklama")
    mülk_turu = models.CharField(max_length=10, choices=TUR_SECENEKLERI, verbose_name="Mülk Türü")
    
    durum = models.CharField(max_length=20, choices=DURUM_SECENEKLERI, default='SATILIK', verbose_name="Durum") 
    esya_durumu = models.CharField(max_length=10, choices= ESYA_DURUM_SECENEKLERI, default='ESYASIZ', verbose_name="Eşya Durumu")
    fiyat = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Fiyat")
    
    brut_m2 = models.IntegerField(blank=True, null=True, verbose_name="Brüt M²")
    net_m2 = models.IntegerField(blank=True, null=True, verbose_name="Net M²")
    
    oda_sayisi = models.CharField(max_length=10, blank=True, null=True, verbose_name="Oda Sayısı")
    bulundugu_kat = models.IntegerField(blank=True, null=True, verbose_name="Bulunduğu Kat")
    bina_kat_sayisi = models.IntegerField(blank=True, null=True, verbose_name="Bina Toplam Kat Sayısı")
    
    adres = models.CharField(max_length=255, verbose_name="Adres Detayı")
    sehir = models.CharField(max_length=50, verbose_name="Şehir")
    ilce = models.CharField(max_length=50, verbose_name="İlçe")
    
    # Mülk sahibi (Satıcı/Kiralayan) ile ilişkilendirme
    sahipleri = models.ManyToManyField(
        Musteri, 
        related_name='sahip_oldugu_mulkler', 
        blank=True, 
        verbose_name="Mülk Sahipleri"
    )
    kayit_tarihi = models.DateTimeField(auto_now_add=True, verbose_name="Kayıt Tarihi")
    guncelleme_tarihi = models.DateTimeField(auto_now=True, verbose_name="Güncelleme Tarihi")

    class Meta:
        verbose_name = "Mülk"
        verbose_name_plural = "Mülkler"

    def __str__(self):
        return f"{self.baslik} ({self.get_durum_display()})"
    

# ===============================================
# FOTOĞRAF MODELİ
# ===============================================
class MulkFotografi(models.Model):
    mulk = models.ForeignKey(Mulk, 
                            on_delete=models.CASCADE, 
                            related_name='fotograflar',
                            verbose_name="İlgili Mülk")
                            
    foto = models.ImageField(upload_to='mulk_fotograflari/', verbose_name="Fotoğraf Dosyası") # Gerçek resim dosyası
    
    aciklama = models.CharField(max_length=255, blank=True, null=True, verbose_name="Açıklama") # Opsiyonel açıklama
    
    varsayilan = models.BooleanField(default=False, verbose_name="Varsayılan Fotoğraf") # Eğer varsa, ilk fotoğrafı belirlemek için
    
    def __str__(self):
        return f"{self.mulk.baslik} - Fotoğraf {self.id}"
    
    class Meta:
        verbose_name = "Mülk Fotoğrafı"
        verbose_name_plural = "Mülk Fotoğrafları"
