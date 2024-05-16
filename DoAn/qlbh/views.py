from django.shortcuts import render
from .models import Khachhang, Sanpham, Nhanvien
from django.shortcuts import render, get_object_or_404, redirect
from .forms import SanphamForm, KhachhangForm, NhanvienForm
from django.utils import timezone


# Create your views here.

def index(request):
    return render(request, 'index.html')


def table_sanpham(request):
    ds_sp = Sanpham.objects.all()
    sp_list = []
    for sp in ds_sp:
        sp_dict = {
            'masp': sp.masp,
            'tensp': sp.tensp,
            'dvt': sp.dvt,
            'nuocsx': sp.nuocsx,
            'gia': sp.gia,
        }
        sp_list.append(sp_dict)

    return render(request, 'table_sanpham.html', {'ds_sp': sp_list})


def edit_sanpham(request, masp):
    sanpham = get_object_or_404(Sanpham, masp=masp)

    if request.method == 'POST':
        form = SanphamForm(request.POST, instance=sanpham)
        if form.is_valid():
            form.save()
            return redirect('sanpham')
    else:
        form = SanphamForm(instance=sanpham)

    return render(request, 'edit_sanpham.html', {'form': form})


def delete_sanpham(request, masp):
    sanpham = get_object_or_404(Sanpham, masp=masp)

    if request.method == 'POST':
        sanpham.delete()
        return redirect('sanpham')

    return render(request, 'delete_sanpham.html', {'sanpham': sanpham})


def add_sanpham(request):
    if request.method == 'POST':
        form = SanphamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sanpham')
    else:
        form = SanphamForm()

    return render(request, 'add_sanpham.html', {'form': form})


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
        form = KhachhangForm(request.POST, instance=khachhang)
        if form.is_valid():
            form.save()
            return redirect('khachhang')
    else:
        form = KhachhangForm(instance=khachhang)

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


def table_nhanvien(request):
    ds_nv = Nhanvien.objects.all()
    nv_list = []
    for nv in ds_nv:
        nv_dict = {
            'manv': nv.manv,
            'hoten': nv.hoten,
            'sodt': nv.sodt,
            'ngvl': nv.ngvl,
        }
        nv_list.append(nv_dict)

    return render(request, 'table_nhanvien.html', {'ds_nv': nv_list})


def edit_nhanvien(request, manv):
    nhanvien = get_object_or_404(Nhanvien, manv=manv)

    if request.method == 'POST':
        form = NhanvienForm(request.POST, instance=nhanvien)
        if form.is_valid():
            form.save()
            return redirect('nhanvien')
    else:
        form = NhanvienForm(instance=nhanvien)

    return render(request, 'edit_nhanvien.html', {'form': form})


def delete_nhanvien(request, manv):
    nhanvien = get_object_or_404(Nhanvien, manv=manv)

    if request.method == 'POST':
        nhanvien.delete()
        return redirect('nhanvien')

    return render(request, 'delete_nhanvien.html', {'nhanvien': nhanvien})


def add_nhanvien(request):
    if request.method == 'POST':
        form = NhanvienForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nhanvien')
    else:
        form = NhanvienForm()

    return render(request, 'add_nhanvien.html', {'form': form})
