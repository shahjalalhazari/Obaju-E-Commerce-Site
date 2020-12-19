from django.shortcuts import render
from Store.models import Product


# HOME PAGE
def home(request):
    products = Product.objects.all()
    return render(request, 'Store/home.html', {'products': products})