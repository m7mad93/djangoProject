# Generated by Django 3.2.8 on 2021-11-01 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]