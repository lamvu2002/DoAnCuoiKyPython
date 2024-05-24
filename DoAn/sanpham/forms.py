from django import forms
from .models import Sanpham


class SanphamForm(forms.ModelForm):
    class Meta:
        model = Sanpham
        fields = '__all__'
        labels = {
            'masp': 'Mã Sản Phẩm',
            'tensp': 'Tên Sản Phẩm',
            'dvt': 'Đơn Vị Tính',
            'nuocsx': 'Nước Sản Xuất',
            'gia': 'Giá',
        }


class SanphamEditForm(forms.ModelForm):
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