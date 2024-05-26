from django import forms
from .models import Khachhang


class KhachhangForm(forms.ModelForm):
    class Meta:
        model = Khachhang
        fields = '__all__'
        exclude = ['loaikh', 'doanhso']
        labels = {
            'makh': 'Mã Khách Hàng',
            'hoten': 'Họ Tên',
            'dchi': 'Địa Chỉ',
            'sodt': 'Số Điện Thoại',
            'ngsinh': 'Ngày Sinh (yyyy-mm-dd)',
            'doanhso': 'Doanh Số',
            'ngdk': 'Ngày Đăng Ký (yyyy-mm-dd)',
        }


class KhachhangEditForm(forms.ModelForm):
    class Meta:
        model = Khachhang
        fields = '__all__'
        exclude = ['loaikh', 'makh', 'doanhso']
        labels = {
            'makh': 'Mã Khách Hàng',
            'hoten': 'Họ Tên',
            'dchi': 'Địa Chỉ',
            'sodt': 'Số Điện Thoại',
            'ngsinh': 'Ngày Sinh (yyyy-mm-dd)',
            'doanhso': 'Doanh Số',
            'ngdk': 'Ngày Đăng Ký (yyyy-mm-dd)',
        }