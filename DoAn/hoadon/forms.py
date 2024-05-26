from django import forms
from .models import Khachhang, Nhanvien, Hoadon
from django.utils import timezone


class HoadonForm(forms.ModelForm):
    makh = forms.ModelChoiceField(
        queryset=Khachhang.objects.all().order_by('makh'),
        empty_label='None',
        label='Mã Khách Hàng',
        required=False,
    )
    manv = forms.ModelChoiceField(queryset=Nhanvien.objects.all(), empty_label=None, label='Mã Nhân Viên')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nghd'].initial = timezone.now()
        self.fields['trigia'].initial = 0

    class Meta:
        model = Hoadon
        fields = '__all__'
        exclude = ['trigia']
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
        exclude = ['sohd', 'trigia']
        labels = {
            'sohd': 'Số Hóa Đơn',
            'nghd': 'Ngày Hóa Đơn',
            'trigia': 'Trị Giá'
        }
