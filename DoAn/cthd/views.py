from django.urls import reverse

from .models import Cthd
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CthdEditForm, CthdForm


# Create your views here.

def table_cthd(request):
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