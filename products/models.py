from django.db import models
from datetime import datetime
# Create your models here.

class Product(models.Model):

    x = [
        ('phone', 'phone'),
        ('computer','computer')
    ]
    name = models.CharField(max_length=50)
    content = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    active = models.BooleanField(default=True)
    category = models.CharField(max_length=50, null=True, blank=True, choices=x)
    created = models.DateTimeField(default=datetime.now())
    def __str__(self):
        return self.name

    class Meta:
        #verbose_name = 'phone'

        ordering = ['price']


class Test(models.Model):
    date = models.DateField()
    time = models.TimeField(null=True)
    created = models.DateTimeField(default=datetime.now())


class Car(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Charger(models.Model):
    name = models.CharField(max_length=10)
    content = models.TextField()
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    date = models.DateTimeField(default=datetime.now())
    def __str__(self):
        return self.name








