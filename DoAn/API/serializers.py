from rest_framework import serializers
from .models import Khachhang, Nhanvien, Sanpham, Hoadon, Cthd


class KhachhangSerializer(serializers.ModelSerializer):
    class Meta:
        model = Khachhang
        fields = '__all__'


class NhanvienSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nhanvien
        fields = '__all__'


class SanphamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sanpham
        fields = '__all__'


class HoadonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hoadon
        fields = '__all__'


class CthdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cthd
        fields = '__all__'
