from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Khachhang, Nhanvien, Sanpham, Hoadon, Cthd
from .serializers import KhachhangSerializer, NhanvienSerializer, SanphamSerializer, HoadonSerializer, CthdSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from rest_framework.response import Response
from django.utils import timezone
from django.db.models import Q


@csrf_exempt
@api_view(['GET', 'POST'])
def KhachhangGetAPI(request):
    if request.method == "GET":
        query = request.query_params.get('search', None)
        if query:
            if query.startswith('>='):
                try:
                    value = float(query[2:])
                    khachhangs = Khachhang.objects.filter(doanhso__gte=value)
                except ValueError:
                    khachhangs = Khachhang.objects.none()
            elif query.startswith('>'):
                try:
                    value = float(query[1:])
                    khachhangs = Khachhang.objects.filter(doanhso__gt=value)
                except ValueError:
                    khachhangs = Khachhang.objects.none()
            elif query.startswith('<='):
                try:
                    value = float(query[2:])
                    khachhangs = Khachhang.objects.filter(doanhso__lte=value)
                except ValueError:
                    khachhangs = Khachhang.objects.none()
            elif query.startswith('<'):
                try:
                    value = float(query[1:])
                    khachhangs = Khachhang.objects.filter(doanhso__lt=value)
                except ValueError:
                    khachhangs = Khachhang.objects.none()
            else:
                khachhangs = Khachhang.objects.filter(
                    Q(makh__icontains=query) |
                    Q(hoten__icontains=query) |
                    Q(dchi__icontains=query) |
                    Q(sodt__icontains=query) |
                    Q(ngsinh__icontains=query) |
                    Q(loaikh__icontains=query)|
                    Q(doanhso__icontains=query) |
                    Q(ngdk__icontains=query)
                )
        else:
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

@csrf_exempt
@api_view(['GET', 'POST'])
def NhanvienGetAPI(request):
    if request.method == "GET":
        query = request.query_params.get('search', None)
        nhanviens = Nhanvien.objects.filter(
            Q(manv__icontains=query) |
            Q(hoten__icontains=query) |
            Q(sodt__icontains=query) |
            Q(ngvl__icontains=query)
        )
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

@csrf_exempt
@api_view(['GET', 'POST'])
def SanphamGetAPI(request):
    if request.method == 'GET':
        query = request.query_params.get('search', None)
        if query:
            if query.startswith('>='):
                try:
                    value = float(query[2:])
                    sanphams = Sanpham.objects.filter(gia__gte=value)
                except ValueError:
                    sanphams = Sanpham.objects.none()
            elif query.startswith('>'):
                try:
                    value = float(query[1:])
                    sanphams = Sanpham.objects.filter(gia__gt=value)
                except ValueError:
                    sanphams = Sanpham.objects.none()
            elif query.startswith('<='):
                try:
                    value = float(query[2:])
                    sanphams = Sanpham.objects.filter(gia__lte=value)
                except ValueError:
                    sanphams = Sanpham.objects.none()
            elif query.startswith('<'):
                try:
                    value = float(query[1:])
                    sanphams = Sanpham.objects.filter(gia__lt=value)
                except ValueError:
                    sanphams = Sanpham.objects.none()
            else:
                sanphams = Sanpham.objects.filter(
                    Q(masp__icontains=query) |
                    Q(tensp__icontains=query) |
                    Q(dvt__icontains=query) |
                    Q(nuocsx__icontains=query)
                )
        else:
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

@csrf_exempt
@api_view(['GET', 'POST'])
def HoadonGetAPI(request):
    if request.method == 'GET':
        query = request.query_params.get('search', None)
        if query:
            if query.startswith('>='):
                try:
                    value = float(query[2:])
                    hoadons = Hoadon.objects.filter(trigia__gte=value)
                except ValueError:
                    hoadons = Hoadon.objects.none()
            elif query.startswith('>'):
                try:
                    value = float(query[1:])
                    hoadons = Hoadon.objects.filter(trigia__gt=value)
                except ValueError:
                    hoadons = Hoadon.objects.none()
            elif query.startswith('<='):
                try:
                    value = float(query[2:])
                    hoadons = Hoadon.objects.filter(trigia__lte=value)
                except ValueError:
                    hoadons = Hoadon.objects.none()
            elif query.startswith('<'):
                try:
                    value = float(query[1:])
                    hoadons = Hoadon.objects.filter(trigia__lt=value)
                except ValueError:
                    hoadons = Hoadon.objects.none()
            else:
                hoadons = Hoadon.objects.filter(
                    Q(sohd__icontains=query) |
                    Q(nghd__icontains=query) |
                    Q(makh__makh__icontains=query) |
                    Q(manv__manv__icontains=query) |
                    Q(trigia__icontains=query)
                )
        else:
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
                Hoadon.objects.filter(sohd=hoadon_data['sohd']).update(**hoadon_serializer.validated_data)
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

@csrf_exempt
@api_view(['GET', 'POST'])
def CthdGetAPI(request):
    if request.method == 'GET':
        query = request.query_params.get('search', None)
        if query:
            if query.startswith('>='):
                try:
                    value = float(query[2:])
                    cthds = Cthd.objects.filter(sl__gte=value)
                except ValueError:
                    cthds = Cthd.objects.none()
            elif query.startswith('>'):
                try:
                    value = float(query[1:])
                    cthds = Cthd.objects.filter(sl__gt=value)
                except ValueError:
                    cthds = Cthd.objects.none()
            elif query.startswith('<='):
                try:
                    value = float(query[2:])
                    cthds = Cthd.objects.filter(sl__lte=value)
                except ValueError:
                    cthds = Cthd.objects.none()
            elif query.startswith('<'):
                try:
                    value = float(query[1:])
                    cthds = Cthd.objects.filter(sl__lt=value)
                except ValueError:
                    cthds = Cthd.objects.none()
            else:
                cthds = Cthd.objects.filter(
                    Q(sohd__sohd__icontains=query) |
                    Q(masp__masp__icontains=query) |
                    Q(sl__icontains=query)
                )
        else:
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


@csrf_exempt
@api_view(['PATCH'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def tinh_tri_gia_hoadon(request):
    if request.method == 'PATCH':
        hoadons = Hoadon.objects.all()
        for hoadon in hoadons:
            cthds = Cthd.objects.filter(sohd=hoadon.sohd)

            total_trigia = 0
            for cthd in cthds:
                cthd_trigia = cthd.sl * cthd.masp.gia
                total_trigia += cthd_trigia

            hoadon.trigia = total_trigia
            hoadon_serializer = HoadonSerializer(hoadon, data={'trigia': total_trigia}, partial=True)
            if hoadon_serializer.is_valid():
                Hoadon.objects.filter(sohd=hoadon.sohd).update(**hoadon_serializer.validated_data)
            else:
                return Response(hoadon_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response("Cập nhật giá trị thành công", status=status.HTTP_200_OK)

    return Response("Phương thức không được hỗ trợ", status=status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
@api_view(['PATCH'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def set_loai_khachhang(request):
    if request.method == 'PATCH':
        khachhangs = Khachhang.objects.all()
        for khachhang in khachhangs:
            doanh_so = 0
            hoadons = Hoadon.objects.filter(makh=khachhang.makh)
            for hoadon in hoadons:
                cthds = Cthd.objects.filter(sohd=hoadon.sohd)

                total_trigia = 0
                for cthd in cthds:
                    cthd_trigia = cthd.sl * cthd.masp.gia
                    total_trigia += cthd_trigia

                hoadon.trigia = total_trigia
                doanh_so += total_trigia
                Hoadon.objects.filter(sohd=hoadon.sohd).update(trigia=total_trigia)

            khachhang.doanhso = doanh_so
            khachhang_serializer = KhachhangSerializer(khachhang, data={'doanhso': doanh_so}, partial=True)
            if khachhang_serializer.is_valid():
                khachhang_serializer.save()
            else:
                return Response(khachhang_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            if (khachhang.ngdk <= timezone.datetime(2007, 1, 1, tzinfo=khachhang.ngdk.tzinfo) and khachhang.doanhso >= 10000000) or (
                    khachhang.ngdk > timezone.datetime(2007, 1, 1, tzinfo=khachhang.ngdk.tzinfo) and khachhang.doanhso >= 2000000):
                khachhang.loaikh = 'VIP'
            else:
                khachhang.loaikh = 'THUONG'
            khachhang_serializer = KhachhangSerializer(khachhang, data={'loaikh': khachhang.loaikh}, partial=True)
            if khachhang_serializer.is_valid():
                khachhang_serializer.save()
            else:
                return Response(khachhang_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response("Cập nhật loại khách hàng thành công", status=status.HTTP_200_OK)

    return Response("Phương thức không được hỗ trợ", status=status.HTTP_405_METHOD_NOT_ALLOWED)
