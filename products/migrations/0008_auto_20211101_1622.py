# Generated by Django 3.2.8 on 2021-11-01 16:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20211101_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 1, 16, 22, 37, 594101)),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='test',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 1, 16, 22, 37, 622067)),
        ),
    ]
