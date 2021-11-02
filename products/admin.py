from django.contrib import admin
from .models import Product, Test, Car , Charger
# Register your models here.
admin.site.register(Product)
admin.site.register(Test)
admin.site.register(Car)
admin.site.register(Charger)