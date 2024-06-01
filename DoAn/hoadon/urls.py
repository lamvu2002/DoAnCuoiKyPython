from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.logout_view, name='logout'),
    path("hoadon/", views.table_hoadon, name="hoadon"),
    path('edit_hoadon/<int:sohd>/', views.edit_hoadon, name='edit_hoadon'),
    path('delete_hoadon/<int:sohd>/', views.delete_hoadon, name='delete_hoadon'),
    path('add_hoadon/', views.add_hoadon, name='add_hoadon'),
    path('tinh_tri_gia_hoadon/', views.tinh_tri_gia_hoadon, name='tinh_tri_gia_hoadon'),
]