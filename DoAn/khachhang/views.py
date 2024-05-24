from django.urls import reverse

from .models import Khachhang
from django.shortcuts import render, get_object_or_404, redirect
from .forms import KhachhangForm, KhachhangEditForm
from django.utils import timezone


def table_khachhang(request):
    ds_kh = Khachhang.objects.all()
    kh_list = []
    for kh in ds_kh:
        kh_dict = {
            'makh': kh.makh,
            'hoten': kh.hoten,
            'dchi': kh.dchi,
            'sodt': kh.sodt,
            'ngsinh': kh.ngsinh,
            'doanhso': kh.doanhso,
            'ngdk': kh.ngdk,
            'loaikh': kh.loaikh,
        }
        kh_list.append(kh_dict)

    return render(request, 'table_khachhang.html', {'ds_kh': kh_list})


def edit_khachhang(request, makh):
    khachhang = get_object_or_404(Khachhang, makh=makh)

    if request.method == 'POST':
        form = KhachhangEditForm(request.POST, instance=khachhang)
        if form.is_valid():
            form.save()
            return redirect('khachhang')
    else:
        form = KhachhangEditForm(instance=khachhang)

    return render(request, 'edit_khachhang.html', {'form': form})


def delete_khachhang(request, makh):
    khachhang = get_object_or_404(Khachhang, makh=makh)

    if request.method == 'POST':
        khachhang.delete()
        return redirect('khachhang')

    return render(request, 'delete_khachhang.html', {'khachhang': khachhang})


def add_khachhang(request):
    if request.method == 'POST':
        form = KhachhangForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('khachhang')
    else:
        form = KhachhangForm()

    return render(request, 'add_khachhang.html', {'form': form})


def set_loai_khachhang(request):
    if request.method == 'POST':
        khachhangs = Khachhang.objects.all()
        for khachhang in khachhangs:
            if (khachhang.ngdk < timezone.datetime(2007, 1, 1,
                                                   tzinfo=khachhang.ngdk.tzinfo) and khachhang.doanhso >= 10000000) or (
                    khachhang.ngdk > timezone.datetime(2007, 1, 1,
                                                       tzinfo=khachhang.ngdk.tzinfo) and khachhang.doanhso >= 2000000):
                khachhang.loaikh = 'Vip'
                khachhang.save()
            else:
                khachhang.loaikh = 'Regular'
                khachhang.save()

        return redirect('khachhang')

    return render(request, 'set_loai_khachhang.html')