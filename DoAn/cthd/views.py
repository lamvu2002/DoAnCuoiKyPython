from django.urls import reverse

from .models import Cthd
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CthdEditForm, CthdForm
from django.db.models import Q


def table_cthd(request):
    query = request.GET.get('q')
    if query:
        if query.startswith('>='):
            try:
                value = float(query[2:])
                ds_cthd = Cthd.objects.filter(sl__gte=value)
            except ValueError:
                ds_cthd = Cthd.objects.none()
        elif query.startswith('>'):
            try:
                value = float(query[1:])
                ds_cthd = Cthd.objects.filter(sl__gt=value)
            except ValueError:
                ds_cthd = Cthd.objects.none()
        elif query.startswith('<='):
            try:
                value = float(query[2:])
                ds_cthd = Cthd.objects.filter(sl__lte=value)
            except ValueError:
                ds_cthd = Cthd.objects.none()
        elif query.startswith('<'):
            try:
                value = float(query[1:])
                ds_cthd = Cthd.objects.filter(sl__lt=value)
            except ValueError:
                ds_cthd = Cthd.objects.none()
        else:
            ds_cthd = Cthd.objects.filter(
                Q(sohd__sohd__icontains=query) |
                Q(masp__masp__icontains=query) |
                Q(sl__icontains=query)
            )
    else:
        ds_cthd = Cthd.objects.all()

    cthd_list = []
    for cthd in ds_cthd:
        cthd_dict = {
            'sohd': cthd.sohd,
            'masp': cthd.masp,
            'sl': cthd.sl,
            'edit_url': reverse('edit_cthd', args=(cthd.sohd.sohd, cthd.masp.masp))
        }
        cthd_list.append(cthd_dict)

    return render(request, 'table_cthd.html', {'ds_cthd': cthd_list})


def edit_cthd(request, sohd, masp):
    cthd = get_object_or_404(Cthd, sohd=sohd, masp=masp)

    if request.method == 'POST':
        form = CthdEditForm(request.POST, instance=cthd)
        if form.is_valid():
            form.save()
            return redirect('cthd')
    else:
        form = CthdEditForm(instance=cthd)

    return render(request, 'edit_cthd.html', {'form': form})


def delete_cthd(request, sohd, masp):
    cthd = get_object_or_404(Cthd, sohd=sohd, masp=masp)

    if request.method == 'POST':
        cthd.delete()
        return redirect('cthd')

    return render(request, 'delete_cthd.html', {'cthd': cthd})


def add_cthd(request):
    if request.method == 'POST':
        form = CthdForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cthd')
    else:
        form = CthdForm()

    return render(request, 'add_cthd.html', {'form': form})