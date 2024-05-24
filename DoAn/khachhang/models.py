
# Create your models here.
from django.db import models


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


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