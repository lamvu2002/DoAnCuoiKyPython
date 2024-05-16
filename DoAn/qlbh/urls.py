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
]
