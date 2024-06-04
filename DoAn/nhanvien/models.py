from django.db import models


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Nhanvien(BaseModel):
    manv = models.CharField(db_column='MANV', primary_key=True, max_length=4,
                            db_collation='Vietnamese_CI_AS')
    hoten = models.CharField(db_column='HOTEN', max_length=40,
                             db_collation='Vietnamese_CI_AS')
    sodt = models.CharField(db_column='SODT', max_length=20,
                            db_collation='Vietnamese_CI_AS')
    ngvl = models.DateTimeField(db_column='NGVL', blank=False, null=False)

    def __str__(self):
        return f"Mã Nhân Viên: {self.manv}, Họ Tên: {self.hoten}, Số Điện Thoại: {self.sodt}, Ngày Vào Làm: {self.ngvl}"

    class Meta:
        managed = False
        db_table = 'NHANVIEN'