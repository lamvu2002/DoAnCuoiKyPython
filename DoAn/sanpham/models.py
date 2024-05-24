from django.db import models


# Create your models here.
class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


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
