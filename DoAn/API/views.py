from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Khachhang, Nhanvien, Sanpham, Hoadon, Cthd
from .serializers import KhachhangSerializer, NhanvienSerializer, SanphamSerializer, HoadonSerializer, CthdSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def KhachhangGetAPI(request):
    if request.method == "GET":
        khachhangs = Khachhang.objects.all()
        khachhang_serializer = KhachhangSerializer(khachhangs, many=True)
        return Response(khachhang_serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        khachhang_data = JSONParser().parse(request)
        khachhang_serializer = KhachhangSerializer(data=khachhang_data)
        if khachhang_serializer.is_valid():
            khachhang_serializer.save()
            return Response("Thêm thành công", status=status.HTTP_201_CREATED)
        return Response("Thêm thất bại", status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['PUT', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def KhachhangAPI(request, makh=""):
    if request.method == 'PUT':
        khachhang_data = JSONParser().parse(request)
        khachhang = Khachhang.objects.get(makh=khachhang_data['makh'])
        khachhang_serializer = KhachhangSerializer(khachhang, data=khachhang_data)
        if khachhang_serializer.is_valid():
            khachhang_serializer.save()
            return Response("Cập nhật thành công", status=status.HTTP_200_OK)
        return Response("Cập nhật thất bại", status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        try:
            khachhang = Khachhang.objects.get(makh=makh)
            khachhang.delete()
            return Response("Xóa thành công", status=status.HTTP_204_NO_CONTENT)
        except Khachhang.DoesNotExist:
            return Response("Khách hàng không tồn tại", status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def NhanvienGetAPI(request):
    if request.method == "GET":
        nhanviens = Nhanvien.objects.all()
        nhanvien_serializer = NhanvienSerializer(nhanviens, many=True)
        return Response(nhanvien_serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        nhanvien_data = JSONParser().parse(request)
        nhanvien_serializer = NhanvienSerializer(data=nhanvien_data)
        if nhanvien_serializer.is_valid():
            nhanvien_serializer.save()
            return Response("Thêm thành công", status=status.HTTP_201_CREATED)
        return Response("Thêm thất bại", status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['PUT', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def NhanvienAPI(request, manv=""):
    if request.method == 'PUT':
        nhanvien_data = JSONParser().parse(request)
        try:
            nhanvien = Nhanvien.objects.get(manv=nhanvien_data['manv'])
            nhanvien_serializer = NhanvienSerializer(nhanvien, data=nhanvien_data)
            if nhanvien_serializer.is_valid():
                nhanvien_serializer.save()
                return Response("Cập nhật thành công", status=status.HTTP_200_OK)
            return Response("Cập nhật thất bại", status=status.HTTP_400_BAD_REQUEST)
        except Nhanvien.DoesNotExist:
            return Response("Nhân viên không tồn tại", status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        try:
            nhanvien = Nhanvien.objects.get(manv=manv)
            nhanvien.delete()
            return Response("Xóa thành công", status=status.HTTP_204_NO_CONTENT)
        except Nhanvien.DoesNotExist:
            return Response("Nhân viên không tồn tại", status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def SanphamGetAPI(request):
    if request.method == 'GET':
        sanphams = Sanpham.objects.all()
        sanpham_serializer = SanphamSerializer(sanphams, many=True)
        return Response(sanpham_serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        sanpham_data = JSONParser().parse(request)
        sanpham_serializer = SanphamSerializer(data=sanpham_data)
        if sanpham_serializer.is_valid():
            sanpham_serializer.save()
            return Response("Thêm thành công", status=status.HTTP_201_CREATED)
        return Response("Thêm thất bại", status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['PUT', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def SanphamAPI(request, masp=""):
    if request.method == 'PUT':
        sanpham_data = JSONParser().parse(request)
        try:
            sanpham = Sanpham.objects.get(masp=sanpham_data['masp'])
            sanpham_serializer = SanphamSerializer(sanpham, data=sanpham_data)
            if sanpham_serializer.is_valid():
                sanpham_serializer.save()
                return Response("Cập nhật thành công", status=status.HTTP_200_OK)
            return Response("Cập nhật thất bại", status=status.HTTP_400_BAD_REQUEST)
        except Sanpham.DoesNotExist:
            return Response("Sản phẩm không tồn tại", status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        try:
            sanpham = Sanpham.objects.get(masp=masp)
            sanpham.delete()
            return Response("Xóa thành công", status=status.HTTP_204_NO_CONTENT)
        except Sanpham.DoesNotExist:
            return Response("Sản phẩm không tồn tại", status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def HoadonGetAPI(request):
    if request.method == 'GET':
        hoadons = Hoadon.objects.all()
        hoadon_serializer = HoadonSerializer(hoadons, many=True)
        return Response(hoadon_serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        hoadon_data = JSONParser().parse(request)
        hoadon_serializer = HoadonSerializer(data=hoadon_data)
        if hoadon_serializer.is_valid():
            hoadon_serializer.save()
            return Response("Thêm thành công", status=status.HTTP_201_CREATED)
        return Response("Thêm thất bại", status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['PUT', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def HoadonAPI(request, sohd=0):
    if request.method == 'PUT':
        hoadon_data = JSONParser().parse(request)
        try:
            hoadon = Hoadon.objects.get(sohd=hoadon_data['sohd'])
            hoadon_serializer = HoadonSerializer(hoadon, data=hoadon_data)
            if hoadon_serializer.is_valid():
                hoadon_serializer.save()
                return Response("Cập nhật thành công", status=status.HTTP_200_OK)
            return Response("Cập nhật thất bại", status=status.HTTP_400_BAD_REQUEST)
        except Hoadon.DoesNotExist:
            return Response("Hóa đơn không tồn tại", status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        try:
            hoadon = Hoadon.objects.get(sohd=sohd)
            hoadon.delete()
            return Response("Xóa thành công", status=status.HTTP_204_NO_CONTENT)
        except Hoadon.DoesNotExist:
            return Response("Hóa đơn không tồn tại", status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def CthdGetAPI(request):
    if request.method == 'GET':
        cthds = Cthd.objects.all()
        cthd_serializer = CthdSerializer(cthds, many=True)
        return Response(cthd_serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        cthd_data = JSONParser().parse(request)
        cthd_serializer = CthdSerializer(data=cthd_data)
        if cthd_serializer.is_valid():
            cthd_serializer.save()
            return Response("Thêm thành công", status=status.HTTP_201_CREATED)
        return Response("Thêm thất bại", status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['PUT', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def CthdAPI(request, id=0):
    if request.method == 'PUT':
        cthd_data = JSONParser().parse(request)
        try:
            cthd = Cthd.objects.get(id=cthd_data['id'])
            cthd_serializer = CthdSerializer(cthd, data=cthd_data)
            if cthd_serializer.is_valid():
                cthd_serializer.save()
                return Response("Cập nhật thành công", status=status.HTTP_200_OK)
            return Response("Cập nhật thất bại", status=status.HTTP_400_BAD_REQUEST)
        except Cthd.DoesNotExist:
            return Response("Chi tiết hóa đơn không tồn tại", status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        try:
            cthd = Cthd.objects.get(id=id)
            cthd.delete()
            return Response("Xóa thành công", status=status.HTTP_204_NO_CONTENT)
        except Cthd.DoesNotExist:
            return Response("Chi tiết hóa đơn không tồn tại", status=status.HTTP_404_NOT_FOUND)
