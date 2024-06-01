from .models import Hoadon, Cthd
from django.shortcuts import render, get_object_or_404, redirect
from .forms import HoadonForm, HoadonEditForm
from django.db.models import Q
from django.utils.timezone import localtime
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect('/')


def table_hoadon(request):
    query = request.GET.get('q')
    if query:
        if query.startswith('>='):
            try:
                value = float(query[2:])
                ds_hd = Hoadon.objects.filter(trigia__gte=value)
            except ValueError:
                ds_hd = Hoadon.objects.none()
        elif query.startswith('>'):
            try:
                value = float(query[1:])
                ds_hd = Hoadon.objects.filter(trigia__gt=value)
            except ValueError:
                ds_hd = Hoadon.objects.none()
        elif query.startswith('<='):
            try:
                value = float(query[2:])
                ds_hd = Hoadon.objects.filter(trigia__lte=value)
            except ValueError:
                ds_hd = Hoadon.objects.none()
        elif query.startswith('<'):
            try:
                value = float(query[1:])
                ds_hd = Hoadon.objects.filter(trigia__lt=value)
            except ValueError:
                ds_hd = Hoadon.objects.none()
        else:
            ds_hd = Hoadon.objects.filter(
                Q(sohd__icontains=query) |
                Q(nghd__icontains=query) |
                Q(makh__makh__icontains=query) |
                Q(manv__manv__icontains=query) |
                Q(trigia__icontains=query)
            )
    else:
        ds_hd = Hoadon.objects.all()
    hd_list = []
    for hd in ds_hd:
        local_nghd = localtime(hd.nghd)
        hd_dict = {
            'sohd': hd.sohd,
            'nghd': local_nghd.strftime("%d/%m/%Y, %H:%M:%S"),
            'makh': hd.makh,
            'manv': hd.manv,
            'trigia': hd.trigia,
        }
        hd_list.append(hd_dict)

    return render(request, 'table_hoadon.html', {'ds_hd': hd_list})


@login_required(login_url=reverse_lazy('admin:login'))
def edit_hoadon(request, sohd):
    hoadon = get_object_or_404(Hoadon, sohd=sohd)

    if request.method == 'POST':
        form = HoadonEditForm(request.POST, instance=hoadon)
        if form.is_valid():
            Hoadon.objects.filter(sohd=sohd).update(**form.cleaned_data)
            return redirect('hoadon')
    else:
        form = HoadonEditForm(instance=hoadon)

    return render(request, 'edit_hoadon.html', {'form': form})


@login_required(login_url=reverse_lazy('admin:login'))
def delete_hoadon(request, sohd):
    hoadon = get_object_or_404(Hoadon, sohd=sohd)

    if request.method == 'POST':
        hoadon.delete()
        return redirect('hoadon')

    return render(request, 'delete_hoadon.html', {'hoadon': hoadon})


@login_required(login_url=reverse_lazy('admin:login'))
def add_hoadon(request):
    if request.method == 'POST':
        form = HoadonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hoadon')
    else:
        form = HoadonForm()

    return render(request, 'add_hoadon.html', {'form': form})


@login_required(login_url=reverse_lazy('admin:login'))
def tinh_tri_gia_hoadon(request):
    if request.method == 'POST':
        hoadons = Hoadon.objects.all()
        for hoadon in hoadons:

            cthds = Cthd.objects.filter(sohd=hoadon.sohd)

            total_trigia = 0
            for cthd in cthds:
                cthd_trigia = cthd.sl * cthd.masp.gia
                total_trigia += cthd_trigia

            hoadon.trigia = total_trigia
            Hoadon.objects.filter(sohd=hoadon.sohd).update(trigia=total_trigia)

        return redirect('hoadon')

    return render(request, 'tinh_tri_gia_hoadon.html')