from .models import Khachhang, Hoadon, Cthd
from django.shortcuts import render, get_object_or_404, redirect
from .forms import KhachhangForm, KhachhangEditForm
from django.utils import timezone
from django.db.models import Q
from django.utils.timezone import localtime
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect('/')


def table_khachhang(request):
    query = request.GET.get('q')
    if query:
        if query.startswith('>='):
            try:
                value = float(query[2:])
                ds_kh = Khachhang.objects.filter(doanhso__gte=value)
            except ValueError:
                ds_kh = Khachhang.objects.none()
        elif query.startswith('>'):
            try:
                value = float(query[1:])
                ds_kh = Khachhang.objects.filter(doanhso__gt=value)
            except ValueError:
                ds_kh = Khachhang.objects.none()
        elif query.startswith('<='):
            try:
                value = float(query[2:])
                ds_kh = Khachhang.objects.filter(doanhso__lte=value)
            except ValueError:
                ds_kh = Khachhang.objects.none()
        elif query.startswith('<'):
            try:
                value = float(query[1:])
                ds_kh = Khachhang.objects.filter(doanhso__lt=value)
            except ValueError:
                ds_kh = Khachhang.objects.none()
        else:
            ds_kh = Khachhang.objects.filter(
                Q(makh__icontains=query) |
                Q(hoten__icontains=query) |
                Q(dchi__icontains=query) |
                Q(sodt__icontains=query) |
                Q(loaikh__icontains=query)
            )
    else:
        ds_kh = Khachhang.objects.all()

    kh_list = []
    for kh in ds_kh:
        local_ngsinh = localtime(kh.ngsinh)
        local_ngdk = localtime(kh.ngdk)
        kh_dict = {
            'makh': kh.makh,
            'hoten': kh.hoten,
            'dchi': kh.dchi,
            'sodt': kh.sodt,
            'ngsinh': local_ngsinh.strftime("%d/%m/%Y, %H:%M:%S"),
            'doanhso': kh.doanhso,
            'ngdk': local_ngdk.strftime("%d/%m/%Y, %H:%M:%S"),
            'loaikh': kh.loaikh,
        }
        kh_list.append(kh_dict)

    return render(request, 'table_khachhang.html', {'ds_kh': kh_list, 'query': query})


@login_required(login_url=reverse_lazy('admin:login'))
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


@login_required(login_url=reverse_lazy('admin:login'))
def delete_khachhang(request, makh):
    khachhang = get_object_or_404(Khachhang, makh=makh)

    if request.method == 'POST':
        khachhang.delete()
        return redirect('khachhang')

    return render(request, 'delete_khachhang.html', {'khachhang': khachhang})


@login_required(login_url=reverse_lazy('admin:login'))
def add_khachhang(request):
    if request.method == 'POST':
        form = KhachhangForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('khachhang')
    else:
        form = KhachhangForm()

    return render(request, 'add_khachhang.html', {'form': form})


@login_required(login_url=reverse_lazy('admin:login'))
def set_loai_khachhang(request):
    if request.method == 'POST':
        khachhangs = Khachhang.objects.all()
        
        for khachhang in khachhangs:
            doanh_so = 0
            hoadons = Hoadon.objects.filter(makh=khachhang.makh)
            for hoadon in hoadons:
                cthds = Cthd.objects.filter(sohd=hoadon.sohd)

                total_trigia = 0
                for cthd in cthds:
                    cthd_trigia = cthd.sl * cthd.masp.gia
                    total_trigia += cthd_trigia

                hoadon.trigia = total_trigia
                doanh_so += total_trigia
                Hoadon.objects.filter(sohd=hoadon.sohd).update(trigia=total_trigia)

            khachhang.doanhso = doanh_so
            khachhang.save()

            if (khachhang.ngdk < timezone.datetime(2007, 1, 1,
                                                   tzinfo=khachhang.ngdk.tzinfo) and khachhang.doanhso >= 10000000) or (
                    khachhang.ngdk > timezone.datetime(2007, 1, 1,
                                                       tzinfo=khachhang.ngdk.tzinfo) and khachhang.doanhso >= 2000000):
                khachhang.loaikh = 'VIP'
                khachhang.save()
            else:
                khachhang.loaikh = 'THUONG'
                khachhang.save()

        return redirect('khachhang')

    return render(request, 'set_loai_khachhang.html')