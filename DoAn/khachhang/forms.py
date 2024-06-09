from django import forms
from .models import Khachhang
from django.utils import timezone
from django.core.validators import RegexValidator


class KhachhangForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ngdk'].initial = timezone.now()
        self.fields['ngdk'].widget.attrs['readonly'] = True
        self.fields['loaikh'].initial = "CHUA XEP LOAI"
        self.fields['loaikh'].widget.attrs['readonly'] = True
        self.fields['doanhso'].initial = 0
        self.fields['doanhso'].widget.attrs['readonly'] = True

    sodt = forms.CharField(
        label='Số Điện Thoại',
        validators=[
            RegexValidator(r'^\d+$', 'Số điện thoại chỉ được chứa các chữ số 0-9.')
        ]
    )

    class Meta:
        model = Khachhang
        fields = '__all__'

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

    sodt = forms.CharField(
        label='Số Điện Thoại',
        validators=[
            RegexValidator(r'^\d+$', 'Số điện thoại chỉ được chứa các chữ số 0-9.')
        ]
    )

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