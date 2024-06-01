from django import forms
from django.core.validators import MinValueValidator

from .models import Sanpham, Hoadon, Cthd


class CthdForm(forms.ModelForm):
    sohd = forms.ModelChoiceField(queryset=Hoadon.objects.all(), empty_label=None, label='Số Hóa Đơn')
    masp = forms.ModelChoiceField(queryset=Sanpham.objects.all(), empty_label=None, label='Mã Sản Phẩm')
    sl = forms.IntegerField(validators=[MinValueValidator(1)], label='Số Lượng')

    class Meta:
        model = Cthd
        fields = '__all__'
        labels = {
            'sohd': 'Số Hóa Đơn',
            'masp': 'Mã Sản Phẩm',
            'sl': 'Số Lượng'
        }


class CthdEditForm(forms.ModelForm):
    masp = forms.ModelChoiceField(queryset=Sanpham.objects.all(), empty_label=None, label='Mã Sản Phẩm')
    sl = forms.IntegerField(validators=[MinValueValidator(1)], label='Số Lượng')

    class Meta:
        model = Cthd
        fields = '__all__'
        labels = {
            'sohd': 'Số Hóa Đơn',
            'masp': 'Mã Sản Phẩm',
            'sl': 'Số Lượng'
        }

