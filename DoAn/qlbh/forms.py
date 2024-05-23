from django import forms
from .models import Sanpham, Khachhang, Nhanvien, Hoadon, Cthd
from django.utils import timezone


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


class KhachhangForm(forms.ModelForm):
    class Meta:
        model = Khachhang
        fields = '__all__'
        exclude = ['loaikh']
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
        exclude = ['loaikh', 'makh']
        labels = {
            'makh': 'Mã Khách Hàng',
            'hoten': 'Họ Tên',
            'dchi': 'Địa Chỉ',
            'sodt': 'Số Điện Thoại',
            'ngsinh': 'Ngày Sinh (yyyy-mm-dd)',
            'doanhso': 'Doanh Số',
            'ngdk': 'Ngày Đăng Ký (yyyy-mm-dd)',
        }


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


class HoadonForm(forms.ModelForm):
    makh = forms.ModelChoiceField(queryset=Khachhang.objects.all(), empty_label=None, label='Mã Khách Hàng')
    manv = forms.ModelChoiceField(queryset=Nhanvien.objects.all(), empty_label=None, label='Mã Nhân Viên')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nghd'].initial = timezone.now()
        self.fields['trigia'].initial = 0

    class Meta:
        model = Hoadon
        fields = '__all__'
        labels = {
            'sohd': 'Số Hóa Đơn',
            'nghd': 'Ngày Hóa Đơn',
            'trigia': 'Trị Giá'
        }


class HoadonEditForm(forms.ModelForm):
    makh = forms.ModelChoiceField(queryset=Khachhang.objects.all(), empty_label=None, label='Mã Khách Hàng')
    manv = forms.ModelChoiceField(queryset=Nhanvien.objects.all(), empty_label=None, label='Mã Nhân Viên')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nghd'].initial = timezone.now()
        self.fields['trigia'].initial = 0

    class Meta:
        model = Hoadon
        fields = '__all__'
        exclude = ['sohd']
        labels = {
            'sohd': 'Số Hóa Đơn',
            'nghd': 'Ngày Hóa Đơn',
            'trigia': 'Trị Giá'
        }


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

