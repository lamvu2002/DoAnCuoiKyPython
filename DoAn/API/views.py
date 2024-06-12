from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import Khachhang, Nhanvien, Sanpham, Hoadon, Cthd
from .serializers import KhachhangSerializer, NhanvienSerializer, SanphamSerializer, HoadonSerializer, CthdSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.


<<<<<<< Updated upstream
@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def KhachhangAPI(request, makh=""):
    if request.method == 'GET':
        khachhangs = Khachhang.objects.all()
        khachhang_serializer = KhachhangSerializer(khachhangs, many=True)
        return JsonResponse(khachhang_serializer.data, safe=False)
    elif request.method == "POST":
=======
@api_view(['GET'])
def KhachhangGetAPI(request):
    khachhangs = Khachhang.objects.all()
    khachhang_serializer = KhachhangSerializer(khachhangs, many=True)
    return JsonResponse(khachhang_serializer.data, safe=False)

@csrf_exempt
@api_view(['POST', 'PUT', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def KhachhangAPI(request, makh=""):
    if request.method == "POST":
>>>>>>> Stashed changes
        khachhang_data = JSONParser().parse(request)
        khachhang_serializer = KhachhangSerializer(data=khachhang_data)
        if khachhang_serializer.is_valid():
            khachhang_serializer.save()
            return JsonResponse("Thêm thành công", safe=False)
        return JsonResponse("Thêm thất bại", safe=False)
    elif request.method == 'PUT':
        khachhang_data = JSONParser().parse(request)
        khachhang = Khachhang.objects.get(makh=khachhang_data['makh'])
        khachhang_serializer = KhachhangSerializer(khachhang, data=khachhang_data)
        if khachhang_serializer.is_valid():
            khachhang_serializer.save()
            return JsonResponse("Cập nhật thành công", safe=False)
        return JsonResponse("Cập nhật thất bại", safe=False)
    elif request.method == 'DELETE':
        khachhang = Khachhang.objects.get(makh=makh)
        khachhang.delete()
        return JsonResponse("Xóa thành công", safe=False)


<<<<<<< Updated upstream
@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def NhanvienAPI(request, manv=""):
    if request.method == 'GET':
        nhanviens = Nhanvien.objects.all()
        nhanvien_serializer = NhanvienSerializer(nhanviens, many=True)
        return JsonResponse(nhanvien_serializer.data, safe=False)
    elif request.method == "POST":
=======
@api_view(['GET'])
def NhanvienGetAPI(request):
    nhanviens = Nhanvien.objects.all()
    nhanvien_serializer = NhanvienSerializer(nhanviens, many=True)
    return JsonResponse(nhanvien_serializer.data, safe=False)


@csrf_exempt
@api_view(['POST', 'PUT', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def NhanvienAPI(request, manv=""):
    if request.method == "POST":
>>>>>>> Stashed changes
        nhanvien_data = JSONParser().parse(request)
        nhanvien_serializer = NhanvienSerializer(data=nhanvien_data)
        if nhanvien_serializer.is_valid():
            nhanvien_serializer.save()
            return JsonResponse("Thêm thành công", safe=False)
        return JsonResponse("Thêm thất bại", safe=False)
    elif request.method == 'PUT':
        nhanvien_data = JSONParser().parse(request)
        nhanvien = Nhanvien.objects.get(manv=nhanvien_data['manv'])
        nhanvien_serializer = NhanvienSerializer(nhanvien, data=nhanvien_data)
        if nhanvien_serializer.is_valid():
            nhanvien_serializer.save()
            return JsonResponse("Cập nhật thành công", safe=False)
        return JsonResponse("Cập nhật thất bại", safe=False)
    elif request.method == 'DELETE':
        nhanvien = Nhanvien.objects.get(manv=manv)
        nhanvien.delete()
        return JsonResponse("Xóa thành công", safe=False)


<<<<<<< Updated upstream
@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
=======
@api_view(['GET'])
def SanphamGetAPI(request):
    if request.method == 'GET':
        sanphams = Sanpham.objects.all()
        sanpham_serializer = SanphamSerializer(sanphams, many=True)
        return JsonResponse(sanpham_serializer.data, safe=False)


@csrf_exempt
@api_view(['POST', 'PUT', 'DELETE'])
>>>>>>> Stashed changes
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def SanphamAPI(request, masp=""):
    if request.method == 'GET':
        sanphams = Sanpham.objects.all()
        sanpham_serializer = SanphamSerializer(sanphams, many=True)
        return JsonResponse(sanpham_serializer.data, safe=False)
    elif request.method == "POST":
        sanpham_data = JSONParser().parse(request)
        sanpham_serializer = SanphamSerializer(data=sanpham_data)
        if sanpham_serializer.is_valid():
            sanpham_serializer.save()
            return JsonResponse("Thêm thành công", safe=False)
        return JsonResponse("Thêm thất bại", safe=False)
    elif request.method == 'PUT':
        sanpham_data = JSONParser().parse(request)
        sanpham = Sanpham.objects.get(masp=sanpham_data['masp'])
        sanpham_serializer = SanphamSerializer(sanpham, data=sanpham_data)
        if sanpham_serializer.is_valid():
            sanpham_serializer.save()
            return JsonResponse("Cập nhật thành công", safe=False)
        return JsonResponse("Cập nhật thất bại", safe=False)
    elif request.method == 'DELETE':
        sanpham = Sanpham.objects.get(masp=masp)
        sanpham.delete()
        return JsonResponse("Xóa thành công", safe=False)


<<<<<<< Updated upstream
@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def HoadonAPI(request, sohd=0):
=======
@api_view(['GET'])
def HoadonGetAPI(request):
>>>>>>> Stashed changes
    if request.method == 'GET':
        hoadons = Hoadon.objects.all()
        hoadon_serializer = HoadonSerializer(hoadons, many=True)
        return JsonResponse(hoadon_serializer.data, safe=False)
<<<<<<< Updated upstream
    elif request.method == "POST":
=======


@csrf_exempt
@api_view(['POST', 'PUT', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def HoadonAPI(request, sohd=0):
    if request.method == "POST":
>>>>>>> Stashed changes
        hoadon_data = JSONParser().parse(request)
        hoadon_serializer = HoadonSerializer(data=hoadon_data)
        if hoadon_serializer.is_valid():
            hoadon_serializer.save()
            return JsonResponse("Thêm thành công", safe=False)
        return JsonResponse("Thêm thất bại", safe=False)
    elif request.method == 'PUT':
        hoadon_data = JSONParser().parse(request)
        hoadon = Hoadon.objects.get(sohd=hoadon_data['sohd'])
        hoadon_serializer = HoadonSerializer(hoadon, data=hoadon_data)
        if hoadon_serializer.is_valid():
            hoadon_serializer.save()
            return JsonResponse("Cập nhật thành công", safe=False)
        return JsonResponse("Cập nhật thất bại", safe=False)
    elif request.method == 'DELETE':
        hoadon = Hoadon.objects.get(sohd=sohd)
        hoadon.delete()
        return JsonResponse("Xóa thành công", safe=False)


<<<<<<< Updated upstream
@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def CthdAPI(request, id=0):
=======
@api_view(['GET'])
def CthdGetAPI(request):
>>>>>>> Stashed changes
    if request.method == 'GET':
        cthds = Cthd.objects.all()
        cthd_serializer = CthdSerializer(cthds, many=True)
        return JsonResponse(cthd_serializer.data, safe=False)
<<<<<<< Updated upstream
    elif request.method == "POST":
=======


@csrf_exempt
@api_view(['POST', 'PUT', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def CthdAPI(request, id=0):
    if request.method == "POST":
>>>>>>> Stashed changes
        cthd_data = JSONParser().parse(request)
        cthd_serializer = CthdSerializer(data=cthd_data)
        if cthd_serializer.is_valid():
            cthd_serializer.save()
            return JsonResponse("Thêm thành công", safe=False)
        return JsonResponse("Thêm thất bại", safe=False)
    elif request.method == 'PUT':
        cthd_data = JSONParser().parse(request)
        cthd = Cthd.objects.get(id=cthd_data['id'])
        cthd_serializer = CthdSerializer(cthd, data=cthd_data)
        if cthd_serializer.is_valid():
            cthd_serializer.save()
            return JsonResponse("Cập nhật thành công", safe=False)
        return JsonResponse("Cập nhật thất bại", safe=False)
    elif request.method == 'DELETE':
        cthd = Cthd.objects.get(id=id)
        cthd.delete()
        return JsonResponse("Xóa thành công", safe=False)