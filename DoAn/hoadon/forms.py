from django import forms
from .models import Khachhang, Nhanvien, Hoadon
from django.utils import timezone
from django.core.validators import MinValueValidator


class HoadonForm(forms.ModelForm):
    makh = forms.ModelChoiceField(
        queryset=Khachhang.objects.all().order_by('makh'),
        empty_label='None',
        label='Mã Khách Hàng',
        required=False,
    )
    manv = forms.ModelChoiceField(queryset=Nhanvien.objects.all(), empty_label=None, label='Mã Nhân Viên')
    sohd = forms.IntegerField(
        label='Số Hóa Đơn',
        validators=[MinValueValidator(1, 'Số hóa đơn phải lớn hơn 0.')]
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nghd'].initial = timezone.now()
        self.fields['nghd'].widget.attrs['readonly'] = True

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
    makh = forms.ModelChoiceField(
        queryset=Khachhang.objects.all().order_by('makh'),
        empty_label='None',
        label='Mã Khách Hàng',
        required=False,
    )
    sohd = forms.IntegerField(
        label='Số Hóa Đơn',
        validators=[MinValueValidator(1, 'Số hóa đơn phải lớn hơn 0.')]
    )
    manv = forms.ModelChoiceField(queryset=Nhanvien.objects.all(), empty_label=None, label='Mã Nhân Viên')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nghd'].initial = timezone.now()
        self.fields['nghd'].widget.attrs['readonly'] = True
    class Meta:
        model = Hoadon
        fields = '__all__'
        exclude = ['sohd', 'trigia']
        labels = {
            'sohd': 'Số Hóa Đơn',
            'nghd': 'Ngày Hóa Đơn',
            'trigia': 'Trị Giá'
        }
