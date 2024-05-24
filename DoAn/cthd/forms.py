from django import forms
from .models import Sanpham, Hoadon, Cthd


class CthdForm(forms.ModelForm):
    sohd = forms.ModelChoiceField(queryset=Hoadon.objects.all(), empty_label=None, label='Số Hóa Đơn')
    masp = forms.ModelChoiceField(queryset=Sanpham.objects.all(), empty_label=None, label='Mã Sản Phẩm')

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

    class Meta:
        model = Cthd
        fields = '__all__'
        exclude = ['sohd']
        labels = {
            'masp': 'Mã Sản Phẩm',
            'sl': 'Số Lượng'
        }

