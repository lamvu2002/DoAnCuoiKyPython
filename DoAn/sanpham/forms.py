from django import forms
from .models import Sanpham


from django import forms
from .models import Sanpham


class SanphamForm(forms.ModelForm):
    DVT_CHOICES = [
        ('cay', 'cay'),
        ('hop', 'hop'),
        ('cai', 'cai'),
        ('quyen', 'quyen'),
        ('chuc', 'chuc'),
    ]
    dvt = forms.ChoiceField(choices=DVT_CHOICES, label='Đơn Vị Tính')

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
        ('cay', 'cay'),
        ('hop', 'hop'),
        ('cai', 'cai'),
        ('quyen', 'quyen'),
        ('chuc', 'chuc'),
    ]
    dvt = forms.ChoiceField(choices=DVT_CHOICES, label='Đơn Vị Tính')

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