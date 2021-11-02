from django.shortcuts import render
from . models import Product, Test, Car, Charger

# Create your views here.

def product(request):
    return render(request, 'products/product.html')
def products(request):
    return render(request, 'products/products.html', {'pro':Product.objects.all()})
def tests(request):
    return render(request, 'products/products.html', {'te':Test.objects.all()})
def cars(request):
    return render(request, 'products/products.html', {'ca':Car.objects.all()})
def chargers(request):
    return render(request, 'products/products.html', {'carg':Charger.objects.all()})