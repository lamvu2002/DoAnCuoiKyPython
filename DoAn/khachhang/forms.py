from django import forms
from .models import Khachhang
from django.utils import timezone


class KhachhangForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ngdk'].initial = timezone.now()
        self.fields['ngdk'].widget.attrs['readonly'] = True
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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ngdk'].initial = timezone.now()
        self.fields['ngdk'].widget.attrs['readonly'] = True


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