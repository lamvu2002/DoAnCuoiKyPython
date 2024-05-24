from .models import Nhanvien
from django.shortcuts import render, get_object_or_404, redirect
from .forms import NhanvienForm, NhanvienEditForm


# Create your views here.

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
        form = NhanvienEditForm(request.POST, instance=nhanvien)
        if form.is_valid():
            form.save()
            return redirect('nhanvien')
    else:
        form = NhanvienEditForm(instance=nhanvien)

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