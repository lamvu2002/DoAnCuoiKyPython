from django.db import models


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Khachhang(BaseModel):
    makh = models.CharField(db_column='MAKH', primary_key=True, max_length=4,
                            db_collation='Vietnamese_CI_AS')
    hoten = models.CharField(db_column='HOTEN', max_length=40,
                             db_collation='Vietnamese_CI_AS')
    dchi = models.CharField(db_column='DCHI', max_length=50, db_collation='Vietnamese_CI_AS', blank=False,
                            null=False)
    sodt = models.CharField(db_column='SODT', max_length=20,
                            db_collation='Vietnamese_CI_AS')
    ngsinh = models.DateTimeField(db_column='NGSINH', blank=False, null=False)
    doanhso = models.DecimalField(db_column='DOANHSO', max_digits=19, decimal_places=4, blank=False,
                                  null=False)
    ngdk = models.DateTimeField(db_column='NGDK', blank=False, null=False)
    loaikh = models.CharField(db_column='LOAIKH', max_length=20, db_collation='Vietnamese_CI_AS', blank=False,
                              null=False)

    def __str__(self):
        return f"Mã Khách Hàng: {self.makh}, Họ Tên: {self.hoten}, Địa Chỉ: {self.dchi}, Số Điện Thoại: {self.sodt}\
        , Ngày Sinh: {self.ngsinh}, Doanh Số: {self.doanhso}, Ngày Đăng Ký: {self.ngdk}, Loại Khách Hàng: {self.loaikh}"

    class Meta:
        managed = False
        db_table = 'KHACHHANG'


class Hoadon(BaseModel):
    sohd = models.IntegerField(db_column='SOHD', primary_key=True)
    nghd = models.DateTimeField(db_column='NGHD', blank=False, null=False)
    makh = models.ForeignKey('Khachhang', models.DO_NOTHING, db_column='MAKH', blank=False,
                             null=False)
    manv = models.ForeignKey('Nhanvien', models.DO_NOTHING, db_column='MANV', blank=False,
                             null=False)
    trigia = models.DecimalField(db_column='TRIGIA', max_digits=19, decimal_places=4, blank=False,
                                 null=False)

    class Meta:
        managed = False
        db_table = 'HOADON'


class Nhanvien(BaseModel):
    manv = models.CharField(db_column='MANV', primary_key=True, max_length=4,
                            db_collation='Vietnamese_CI_AS')
    hoten = models.CharField(db_column='HOTEN', max_length=40,
                             db_collation='Vietnamese_CI_AS')
    sodt = models.CharField(db_column='SODT', max_length=20,
                            db_collation='Vietnamese_CI_AS')
    ngvl = models.DateTimeField(db_column='NGVL', blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'NHANVIEN'


class Sanpham(BaseModel):
    masp = models.CharField(db_column='MASP', primary_key=True, max_length=4,
                            db_collation='Vietnamese_CI_AS')
    tensp = models.CharField(db_column='TENSP', max_length=40, db_collation='Vietnamese_CI_AS', blank=False,
                             null=False)
    dvt = models.CharField(db_column='DVT', max_length=20, db_collation='Vietnamese_CI_AS', blank=False,
                           null=False)
    nuocsx = models.CharField(db_column='NUOCSX', max_length=40, db_collation='Vietnamese_CI_AS', blank=False,
                              null=False)
    gia = models.DecimalField(db_column='GIA', max_digits=19, decimal_places=4, blank=False,
                              null=False)

    class Meta:
        managed = False
        db_table = 'SANPHAM'


class Cthd(BaseModel):
    sohd = models.ForeignKey('Hoadon', models.DO_NOTHING, db_column='SOHD')
    masp = models.ForeignKey('Sanpham', models.DO_NOTHING, db_column='MASP')
    sl = models.IntegerField(db_column='SL', blank=False, null=False)


    class Meta:
        managed = False
        db_table = 'CTHD'
        unique_together = (('sohd', 'masp'),)
