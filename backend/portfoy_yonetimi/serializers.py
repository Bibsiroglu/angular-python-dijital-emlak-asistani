# backend/portfoy_yonetimi/serializers.py

from rest_framework import serializers
from .models import Mulk, Musteri

class MusteriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musteri
        fields = '__all__'

class MulkSerializer(serializers.ModelSerializer):
    # Bu, Mulk modelindeki 'sahip' alanı için gerekli
    # read_only=True: GET isteklerinde tam Musteri objesini verir
    sahip = MusteriSerializer(read_only=True) 
    
    # write_only=True: POST/PUT isteklerinde sadece sahip ID'sini alır
    sahip_id = serializers.PrimaryKeyRelatedField(queryset=Musteri.objects.all(), source='sahip', write_only=True, required=False)

    class Meta:
        model = Mulk
        fields = '__all__'
        # Mulk'un kendisi POST/PUT yaparken sadece ID üzerinden işlem yapmalı
        read_only_fields = ('sahip',)
        