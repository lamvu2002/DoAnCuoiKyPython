from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.logout_view, name='logout'),
    path("sanpham/", views.table_sanpham, name="sanpham"),
    path('edit_sanpham/<str:masp>/', views.edit_sanpham, name='edit_sanpham'),
    path('delete_sanpham/<str:masp>/', views.delete_sanpham, name='delete_sanpham'),
    path('add_sanpham/', views.add_sanpham, name='add_sanpham')
]