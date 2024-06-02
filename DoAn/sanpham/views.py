from .models import Sanpham
from django.shortcuts import render, get_object_or_404, redirect
from .forms import SanphamForm, SanphamEditForm
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect('/')


def table_sanpham(request):
    query = request.GET.get('q')
    if query:
        if query.startswith('>='):
            try:
                value = float(query[2:])
                ds_sp = Sanpham.objects.filter(gia__gte=value)
            except ValueError:
                ds_sp = Sanpham.objects.none()
        elif query.startswith('>'):
            try:
                value = float(query[1:])
                ds_sp = Sanpham.objects.filter(gia__gt=value)
            except ValueError:
                ds_sp = Sanpham.objects.none()
        elif query.startswith('<='):
            try:
                value = float(query[2:])
                ds_sp = Sanpham.objects.filter(gia__lte=value)
            except ValueError:
                ds_sp = Sanpham.objects.none()
        elif query.startswith('<'):
            try:
                value = float(query[1:])
                ds_sp = Sanpham.objects.filter(gia__lt=value)
            except ValueError:
                ds_sp = Sanpham.objects.none()
        else:
            ds_sp = Sanpham.objects.filter(
                Q(masp__icontains=query) |
                Q(tensp__icontains=query) |
                Q(dvt__icontains=query) |
                Q(nuocsx__icontains=query)
            )
    else:
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

    return render(request, 'table_sanpham.html', {'ds_sp': sp_list, 'query': query})


@login_required(login_url=reverse_lazy('admin:login'))
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


@login_required(login_url=reverse_lazy('admin:login'))
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