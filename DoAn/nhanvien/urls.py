from django.urls import path
from . import views

urlpatterns = [
    path("nhanvien/", views.table_nhanvien, name="nhanvien"),
    path('edit_nhanvien/<str:manv>/', views.edit_nhanvien, name='edit_nhanvien'),
    path('delete_nhanvien/<str:manv>/', views.delete_nhanvien, name='delete_nhanvien'),
    path('add_nhanvien/', views.add_nhanvien, name='add_nhanvien')
]