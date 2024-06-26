# Generated by Django 5.0.6 on 2024-06-08 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoadon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cthd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sl', models.IntegerField(db_column='SL')),
            ],
            options={
                'db_table': 'CTHD',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sanpham',
            fields=[
                ('masp', models.CharField(db_collation='Vietnamese_CI_AS', db_column='MASP', max_length=4, primary_key=True, serialize=False)),
                ('tensp', models.CharField(db_collation='Vietnamese_CI_AS', db_column='TENSP', max_length=40)),
                ('dvt', models.CharField(db_collation='Vietnamese_CI_AS', db_column='DVT', max_length=20)),
                ('nuocsx', models.CharField(db_collation='Vietnamese_CI_AS', db_column='NUOCSX', max_length=40)),
                ('gia', models.DecimalField(db_column='GIA', decimal_places=4, max_digits=19)),
            ],
            options={
                'db_table': 'SANPHAM',
                'managed': False,
            },
        ),
    ]
