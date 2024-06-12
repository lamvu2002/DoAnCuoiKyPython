from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
<<<<<<< Updated upstream
    path("khachhang/", views.KhachhangAPI, name="khachhang"),
    path('khachhang/<str:makh>/', views.KhachhangAPI, name='delete_khachhang'),

    path("nhanvien/", views.NhanvienAPI, name="nhanvien"),
    path('nhanvien/<str:manv>/', views.NhanvienAPI, name='delete_nhanvien'),

    path("sanpham/", views.SanphamAPI, name="sanpham"),
    path('sanpham/<str:masp>/', views.SanphamAPI, name='delete_sanpham'),

    path("hoadon/", views.HoadonAPI, name="hoadon"),
    path('hoadon/<int:sohd>/', views.HoadonAPI, name='delete_hoadon'),

    path("cthd/", views.CthdAPI, name="cthd"),
=======
    path("khachhang/", views.KhachhangGetAPI, name="khachhang"),
    path('khachhang/<str:makh>/', views.KhachhangAPI, name='delete_khachhang'),

    path("nhanvien/", views.NhanvienGetAPI, name="nhanvien"),
    path('nhanvien/<str:manv>/', views.NhanvienAPI, name='delete_nhanvien'),

    path("sanpham/", views.SanphamGetAPI, name="sanpham"),
    path('sanpham/<str:masp>/', views.SanphamAPI, name='delete_sanpham'),

    path("hoadon/", views.HoadonGetAPI, name="hoadon"),
    path('hoadon/<int:sohd>/', views.HoadonAPI, name='delete_hoadon'),

    path("cthd/", views.CthdGetAPI, name="cthd"),
>>>>>>> Stashed changes
    path('cthd/<int:id>/', views.CthdAPI, name='delete_cthd'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
