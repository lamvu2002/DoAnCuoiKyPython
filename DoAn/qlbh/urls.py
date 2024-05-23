from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sanpham/", views.table_sanpham, name="sanpham"),
    path('edit_sanpham/<str:masp>/', views.edit_sanpham, name='edit_sanpham'),
    path('delete_sanpham/<str:masp>/', views.delete_sanpham, name='delete_sanpham'),
    path('add_sanpham/', views.add_sanpham, name='add_sanpham'),

    path("khachhang/", views.table_khachhang, name="khachhang"),
    path('edit_khachhang/<str:makh>/', views.edit_khachhang, name='edit_khachhang'),
    path('delete_khachhang/<str:makh>/', views.delete_khachhang, name='delete_khachhang'),
    path('add_khachhang/', views.add_khachhang, name='add_khachhang'),
    path('set_loai_khachhang/', views.set_loai_khachhang, name='set_loai_khachhang'),

    path("nhanvien/", views.table_nhanvien, name="nhanvien"),
    path('edit_nhanvien/<str:manv>/', views.edit_nhanvien, name='edit_nhanvien'),
    path('delete_nhanvien/<str:manv>/', views.delete_nhanvien, name='delete_nhanvien'),
    path('add_nhanvien/', views.add_nhanvien, name='add_nhanvien'),

    path("hoadon/", views.table_hoadon, name="hoadon"),
    path('edit_hoadon/<int:sohd>/', views.edit_hoadon, name='edit_hoadon'),
    path('delete_hoadon/<int:sohd>/', views.delete_hoadon, name='delete_hoadon'),
    path('add_hoadon/', views.add_hoadon, name='add_hoadon'),

    path("cthd/", views.table_cthd, name="cthd"),
    path('edit_cthd/<int:sohd>/<str:masp>/', views.edit_cthd, name='edit_cthd'),
    path('delete_cthd/<int:sohd>/<str:masp>/', views.delete_cthd, name='delete_cthd'),
    path('add_cthd/', views.add_cthd, name='add_cthd'),
]
