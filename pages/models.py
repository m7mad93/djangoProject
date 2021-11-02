from django.db import models
from datetime import datetime
# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=100)
    #content = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    #created = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name