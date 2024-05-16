from django import forms
from .models import Sanpham, Khachhang, Nhanvien


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
