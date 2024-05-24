from .models import Sanpham
from django.shortcuts import render, get_object_or_404, redirect
from .forms import SanphamForm, SanphamEditForm


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
        form = SanphamEditForm(request.POST, instance=sanpham)
        if form.is_valid():
            form.save()
            return redirect('sanpham')
    else:
        form = SanphamEditForm(instance=sanpham)

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