from rest_framework import serializers
from .models import Musteri, Mulk

class MusteriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musteri
        fields = '__all__' # Tüm alanları dahil et

class MulkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mulk
        fields = '__all__' # Tüm alanları dahil et