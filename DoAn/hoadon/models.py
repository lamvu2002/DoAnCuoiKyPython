from django.db import models


# Create your models here.
class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


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