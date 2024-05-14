from django.shortcuts import render
from django.http import HttpResponse
from .models import Khachhang
from django.db import connection

# Create your views here.

def index(request):
    # cursor = connection.cursor()
    # cursor.execute("SELECT * FROM KHACHHANG")
    # ds_kh = cursor.fetchall()
    ds_kh = Khachhang.objects.all()
    output = "</br>".join([kh.hoten for kh in ds_kh])
    # output = "</br>".join([str(row) for row in ds_kh])
    return HttpResponse(output)


def detail(request, makh):
    return HttpResponse("Thong tin chi tiet khach hang %s." % makh)
