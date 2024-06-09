from django import forms
from .models import Nhanvien
from django.core.validators import RegexValidator


class NhanvienForm(forms.ModelForm):
    sodt = forms.CharField(
        label='Số Điện Thoại',
        validators=[
            RegexValidator(r'^\d+$', 'Số điện thoại chỉ được chứa các chữ số 0-9.')
        ]
    )

    class Meta:
        model = Nhanvien
        fields = '__all__'
        labels = {
            'manv': 'Mã Nhân Viên',
            'hoten': 'Họ Tên',
            'sodt': 'Số Điện Thoại',
            'ngvl': 'Ngày Vào Làm (yyyy-mm-dd)',
        }


class NhanvienEditForm(forms.ModelForm):
    sodt = forms.CharField(
        label='Số Điện Thoại',
        validators=[
            RegexValidator(r'^\d+$', 'Số điện thoại chỉ được chứa các chữ số 0-9.')
        ]
    )

    class Meta:
        model = Nhanvien
        fields = '__all__'
        exclude = ['manv']
        labels = {
            'manv': 'Mã Nhân Viên',
            'hoten': 'Họ Tên',
            'sodt': 'Số Điện Thoại',
            'ngvl': 'Ngày Vào Làm (yyyy-mm-dd)',
        }