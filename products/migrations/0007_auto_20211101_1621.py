# Generated by Django 3.2.8 on 2021-11-01 16:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20211101_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 1, 16, 21, 35, 274381)),
        ),
        migrations.AlterField(
            model_name='test',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 1, 16, 21, 35, 303522)),
        ),
    ]
