from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("khachhang/", views.KhachhangGetAPI, name="khachhang_api"),
    path('khachhang/<str:makh>/', views.KhachhangAPI, name='delete_khachhang_api'),

    path("nhanvien/", views.NhanvienGetAPI, name="nhanvien_api"),
    path('nhanvien/<str:manv>/', views.NhanvienAPI, name='delete_nhanvien_api'),

    path("sanpham/", views.SanphamGetAPI, name="sanpham_api"),
    path('sanpham/<str:masp>/', views.SanphamAPI, name='delete_sanpham_api'),

    path("hoadon/", views.HoadonGetAPI, name="hoadon_api"),
    path('hoadon/<int:sohd>/', views.HoadonAPI, name='delete_hoadon_api'),

    path("cthd/", views.CthdGetAPI, name="cthd_api"),
    path('cthd/<int:id>/', views.CthdAPI, name='delete_cthd_api'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path("tinh-tri-gia-hd/", views.tinh_tri_gia_hoadon, name="tinh-tg-hd"),
    path("set_loai_khachhang/", views.set_loai_khachhang, name="set_loai_khachhang"),

]
