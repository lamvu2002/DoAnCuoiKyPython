from django.db import models

# Create your models here.


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


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