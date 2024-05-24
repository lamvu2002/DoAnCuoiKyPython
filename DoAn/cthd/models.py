from django.db import models


# Create your models here.
class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Cthd(BaseModel):
    sohd = models.OneToOneField('Hoadon', models.DO_NOTHING, db_column='SOHD', primary_key=True)
    masp = models.ForeignKey('Sanpham', models.DO_NOTHING, db_column='MASP')
    sl = models.IntegerField(db_column='SL', blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'CTHD'
        unique_together = (('sohd', 'masp'),)


class Hoadon(BaseModel):
    sohd = models.IntegerField(db_column='SOHD', primary_key=True)  # Field name made lowercase.
    nghd = models.DateTimeField(db_column='NGHD', blank=True, null=True)  # Field name made lowercase.
    makh = models.ForeignKey('Khachhang', models.DO_NOTHING, db_column='MAKH', blank=True,
                             null=True)  # Field name made lowercase.
    manv = models.ForeignKey('Nhanvien', models.DO_NOTHING, db_column='MANV', blank=True,
                             null=True)  # Field name made lowercase.
    trigia = models.DecimalField(db_column='TRIGIA', max_digits=19, decimal_places=4, blank=True,
                                 null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HOADON'


class Sanpham(BaseModel):
    masp = models.CharField(db_column='MASP', primary_key=True, max_length=4,
                            db_collation='Vietnamese_CI_AS')  # Field name made lowercase.
    tensp = models.CharField(db_column='TENSP', max_length=40, db_collation='Vietnamese_CI_AS', blank=True,
                             null=True)  # Field name made lowercase.
    dvt = models.CharField(db_column='DVT', max_length=20, db_collation='Vietnamese_CI_AS', blank=True,
                           null=True)  # Field name made lowercase.
    nuocsx = models.CharField(db_column='NUOCSX', max_length=40, db_collation='Vietnamese_CI_AS', blank=True,
                              null=True)  # Field name made lowercase.
    gia = models.DecimalField(db_column='GIA', max_digits=19, decimal_places=4, blank=True,
                              null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SANPHAM'

class Khachhang(BaseModel):
    makh = models.CharField(db_column='MAKH', primary_key=True, max_length=4,
                            db_collation='Vietnamese_CI_AS')  # Field name made lowercase.
    hoten = models.CharField(db_column='HOTEN', max_length=40,
                             db_collation='Vietnamese_CI_AS')  # Field name made lowercase.
    dchi = models.CharField(db_column='DCHI', max_length=50, db_collation='Vietnamese_CI_AS', blank=True,
                            null=True)  # Field name made lowercase.
    sodt = models.CharField(db_column='SODT', max_length=20,
                            db_collation='Vietnamese_CI_AS')  # Field name made lowercase.
    ngsinh = models.DateTimeField(db_column='NGSINH', blank=True, null=True)  # Field name made lowercase.
    doanhso = models.DecimalField(db_column='DOANHSO', max_digits=19, decimal_places=4, blank=True,
                                  null=True)  # Field name made lowercase.
    ngdk = models.DateTimeField(db_column='NGDK', blank=True, null=True)  # Field name made lowercase.
    loaikh = models.CharField(db_column='LOAIKH', max_length=20, db_collation='Vietnamese_CI_AS', blank=True,
                              null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KHACHHANG'


class Nhanvien(BaseModel):
    manv = models.CharField(db_column='MANV', primary_key=True, max_length=4,
                            db_collation='Vietnamese_CI_AS')  # Field name made lowercase.
    hoten = models.CharField(db_column='HOTEN', max_length=40,
                             db_collation='Vietnamese_CI_AS')  # Field name made lowercase.
    sodt = models.CharField(db_column='SODT', max_length=20,
                            db_collation='Vietnamese_CI_AS')  # Field name made lowercase.
    ngvl = models.DateTimeField(db_column='NGVL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NHANVIEN'