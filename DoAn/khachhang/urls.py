from django.urls import path
from . import views

urlpatterns = [
    path("khachhang/", views.table_khachhang, name="khachhang"),
    path('edit_khachhang/<str:makh>/', views.edit_khachhang, name='edit_khachhang'),
    path('delete_khachhang/<str:makh>/', views.delete_khachhang, name='delete_khachhang'),
    path('add_khachhang/', views.add_khachhang, name='add_khachhang'),
    path('set_loai_khachhang/', views.set_loai_khachhang, name='set_loai_khachhang'),

]