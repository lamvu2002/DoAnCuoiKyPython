from django import forms
from .models import Nhanvien


class NhanvienForm(forms.ModelForm):
    class Meta:
        model = Nhanvien
        fields = '__all__'
        labels = {
            'manv': 'Mã Nhân Viên',
            'hoten': 'Họ Tên',
            'sodt': 'Số Điện Thoại',
            'ngvl': 'Ngày Vào Làm (yyyy/mm/dd)',
        }


class NhanvienEditForm(forms.ModelForm):
    class Meta:
        model = Nhanvien
        fields = '__all__'
        exclude = ['manv']
        labels = {
            'manv': 'Mã Nhân Viên',
            'hoten': 'Họ Tên',
            'sodt': 'Số Điện Thoại',
            'ngvl': 'Ngày Vào Làm (yyyy/mm/dd)',
        }