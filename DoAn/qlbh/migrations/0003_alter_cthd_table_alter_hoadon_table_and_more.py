# Generated by Django 5.0.6 on 2024-05-22 02:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qlbh', '0002_authgroup_authgrouppermissions_authpermission_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='cthd',
            table='CTHD',
        ),
        migrations.AlterModelTable(
            name='hoadon',
            table='HOADON',
        ),
        migrations.AlterModelTable(
            name='khachhang',
            table='KHACHHANG',
        ),
        migrations.AlterModelTable(
            name='nhanvien',
            table='NHANVIEN',
        ),
        migrations.AlterModelTable(
            name='sanpham',
            table='SANPHAM',
        ),
    ]