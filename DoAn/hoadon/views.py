from .models import Hoadon
from django.shortcuts import render, get_object_or_404, redirect
from .forms import HoadonForm, HoadonEditForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


def table_hoadon(request):
    ds_hd = Hoadon.objects.all()
    hd_list = []
    for hd in ds_hd:
        hd_dict = {
            'sohd': hd.sohd,
            'nghd': hd.nghd,
            'makh': hd.makh,
            'manv': hd.manv,
            'trigia': hd.trigia,
        }
        hd_list.append(hd_dict)

    return render(request, 'table_hoadon.html', {'ds_hd': hd_list})


def edit_hoadon(request, sohd):
    hoadon = get_object_or_404(Hoadon, sohd=sohd)

    if request.method == 'POST':
        form = HoadonEditForm(request.POST, instance=hoadon)
        if form.is_valid():
            #form.save()
            Hoadon.objects.filter(sohd=sohd).update(**form.cleaned_data)
            return redirect('hoadon')
    else:
        form = HoadonEditForm(instance=hoadon)

    return render(request, 'edit_hoadon.html', {'form': form})


def delete_hoadon(request, sohd):
    hoadon = get_object_or_404(Hoadon, sohd=sohd)

    if request.method == 'POST':
        hoadon.delete()
        return redirect('hoadon')

    return render(request, 'delete_hoadon.html', {'hoadon': hoadon})


def add_hoadon(request):
    if request.method == 'POST':
        form = HoadonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hoadon')
    else:
        form = HoadonForm()

    return render(request, 'add_hoadon.html', {'form': form})