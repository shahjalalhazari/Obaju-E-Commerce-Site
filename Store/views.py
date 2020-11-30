from django.shortcuts import render
from .models import *


# HOME PAGE
def home(request):
    products = Product.objects.all()
    return render(request, 'Store/home.html', {'products': products})


# PRODUCT DETAIL VIEW
def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'Store/detail.html', {'product': product})


def product_list(request, pk):
    sub_category = SubCategory.objects.get(pk=pk)
    products = Product.objects.filter(sub_category=sub_category)
    return render(request, 'Store/product_list.html', {'sub_category': sub_category, 'products': products})