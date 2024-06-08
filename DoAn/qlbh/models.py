from django.db import models


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Cthd(BaseModel):
    sohd = models.ForeignKey('Hoadon', models.DO_NOTHING, db_column='SOHD')
    masp = models.ForeignKey('Sanpham', models.DO_NOTHING, db_column='MASP')
    sl = models.IntegerField(db_column='SL', blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'CTHD'
        unique_together = (('sohd', 'masp'),)


class Hoadon(BaseModel):
    sohd = models.IntegerField(db_column='SOHD', primary_key=True)
    nghd = models.DateTimeField(db_column='NGHD', blank=False, null=False)
    makh = models.ForeignKey('Khachhang', models.DO_NOTHING, db_column='MAKH', blank=True,
                             null=True)
    manv = models.ForeignKey('Nhanvien', models.DO_NOTHING, db_column='MANV', blank=False,
                             null=False)
    trigia = models.DecimalField(db_column='TRIGIA', max_digits=19, decimal_places=4, blank=False,
                                 null=False)

    class Meta:
        managed = False
        db_table = 'HOADON'


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

    class Meta:
        managed = False
        db_table = 'KHACHHANG'


class Khachhang1(BaseModel):
    makh = models.CharField(db_column='MAKH', max_length=4,
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

    class Meta:
        managed = False
        db_table = 'KHACHHANG1'


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


class Sanpham1(BaseModel):
    masp = models.CharField(db_column='MASP', max_length=4,
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
        db_table = 'SANPHAM1'


class AuthGroup(BaseModel):
    name = models.CharField(unique=True, max_length=150, db_collation='Vietnamese_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(BaseModel):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(BaseModel):
    name = models.CharField(max_length=255, db_collation='Vietnamese_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='Vietnamese_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(BaseModel):
    password = models.CharField(max_length=128, db_collation='Vietnamese_CI_AS')
    last_login = models.DateTimeField(blank=False, null=False)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='Vietnamese_CI_AS')
    first_name = models.CharField(max_length=150, db_collation='Vietnamese_CI_AS')
    last_name = models.CharField(max_length=150, db_collation='Vietnamese_CI_AS')
    email = models.CharField(max_length=254, db_collation='Vietnamese_CI_AS')
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(BaseModel):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(BaseModel):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(BaseModel):
    action_time = models.DateTimeField()
    object_id = models.TextField(db_collation='Vietnamese_CI_AS', blank=False, null=False)
    object_repr = models.CharField(max_length=200, db_collation='Vietnamese_CI_AS')
    action_flag = models.SmallIntegerField()
    change_message = models.TextField(db_collation='Vietnamese_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=False, null=False)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(BaseModel):
    app_label = models.CharField(max_length=100, db_collation='Vietnamese_CI_AS')
    model = models.CharField(max_length=100, db_collation='Vietnamese_CI_AS')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(BaseModel):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='Vietnamese_CI_AS')
    name = models.CharField(max_length=255, db_collation='Vietnamese_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(BaseModel):
    session_key = models.CharField(primary_key=True, max_length=40, db_collation='Vietnamese_CI_AS')
    session_data = models.TextField(db_collation='Vietnamese_CI_AS')
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class QlbhCthd(BaseModel):
    id = models.BigAutoField(primary_key=True)
    sl = models.IntegerField()
    sohd = models.ForeignKey('QlbhHoadon', models.DO_NOTHING)
    masp = models.ForeignKey('QlbhSanpham', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'qlbh_cthd'


class QlbhHoadon(BaseModel):
    sohd = models.IntegerField(primary_key=True)
    nghd = models.DateTimeField()
    trigia = models.DecimalField(max_digits=19, decimal_places=2)
    makh = models.ForeignKey('QlbhKhachhang', models.DO_NOTHING)
    manv = models.ForeignKey('QlbhNhanvien', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'qlbh_hoadon'


class QlbhKhachhang(BaseModel):
    makh = models.CharField(primary_key=True, max_length=4, db_collation='Vietnamese_CI_AS')
    hoten = models.CharField(max_length=40, db_collation='Vietnamese_CI_AS')
    dchi = models.CharField(max_length=50, db_collation='Vietnamese_CI_AS', blank=False, null=False)
    sodt = models.CharField(max_length=20, db_collation='Vietnamese_CI_AS')
    ngsinh = models.DateTimeField(blank=False, null=False)
    doanhso = models.DecimalField(max_digits=19, decimal_places=2, blank=False, null=False)
    ngdk = models.DateTimeField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'qlbh_khachhang'


class QlbhNhanvien(BaseModel):
    manv = models.CharField(primary_key=True, max_length=4, db_collation='Vietnamese_CI_AS')
    hoten = models.CharField(max_length=40, db_collation='Vietnamese_CI_AS')
    sodt = models.CharField(max_length=20, db_collation='Vietnamese_CI_AS')
    ngvl = models.DateTimeField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'qlbh_nhanvien'


class QlbhSanpham(BaseModel):
    masp = models.CharField(primary_key=True, max_length=4, db_collation='Vietnamese_CI_AS')
    tensp = models.CharField(max_length=40, db_collation='Vietnamese_CI_AS')
    dvt = models.CharField(max_length=20, db_collation='Vietnamese_CI_AS')
    nuocsx = models.CharField(max_length=40, db_collation='Vietnamese_CI_AS')
    gia = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'qlbh_sanpham'
