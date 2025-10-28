from rest_framework import serializers
from .models import MulkFotografi, Musteri, Mulk

class MulkFotografiSerializer(serializers.ModelSerializer):
    class Meta:
        model = MulkFotografi
        fields = ('foto', 'aciklama') # 'foto' burada fotoğrafın URL'sini verecek

class MusteriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musteri
        fields = '__all__' # Tüm alanları dahil et

class MulkSerializer(serializers.ModelSerializer):
    fotograflar = MulkFotografiSerializer(many=True, read_only=True)
    class Meta:
        model = Mulk
        fields = ('id', 'baslik', 'durum', 'fiyat', 'sehir', 'ilce', 'brut_m2', 'net_m2', 'oda_sayisi', 'fotograflar')

