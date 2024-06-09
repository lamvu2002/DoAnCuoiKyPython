from django import forms
from .models import Sanpham
from django.core.validators import MinValueValidator


class SanphamForm(forms.ModelForm):
    DVT_CHOICES = [
        ('CAY', 'CAY'),
        ('HOP', 'HOP'),
        ('CAI', 'CAI'),
        ('QUYEN', 'QUYEN'),
        ('CHUC', 'CHUC'),
    ]
    dvt = forms.ChoiceField(choices=DVT_CHOICES, label='Đơn Vị Tính')
    gia = forms.DecimalField(
        label='Giá',
        validators=[MinValueValidator(501, 'Giá phải lớn hơn 500.')]
    )
    class Meta:
        model = Sanpham
        fields = '__all__'
        labels = {
            'masp': 'Mã Sản Phẩm',
            'tensp': 'Tên Sản Phẩm',
            'nuocsx': 'Nước Sản Xuất',
            'gia': 'Giá',
        }


class SanphamEditForm(forms.ModelForm):
    DVT_CHOICES = [
        ('CAY', 'CAY'),
        ('HOP', 'HOP'),
        ('CAI', 'CAI'),
        ('QUYEN', 'QUYEN'),
        ('CHUC', 'CHUC'),
    ]
    dvt = forms.ChoiceField(choices=DVT_CHOICES, label='Đơn Vị Tính')
    gia = forms.DecimalField(
        label='Giá',
        validators=[MinValueValidator(501, 'Giá phải lớn hơn 500.')]
    )

    class Meta:
        model = Sanpham
        fields = '__all__'
        exclude = ['masp']
        labels = {
            'masp': 'Mã Sản Phẩm',
            'tensp': 'Tên Sản Phẩm',
            'dvt': 'Đơn Vị Tính',
            'nuocsx': 'Nước Sản Xuất',
            'gia': 'Giá',
        }