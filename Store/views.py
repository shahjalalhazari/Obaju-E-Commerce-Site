from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.urls import reverse
from .models import *


# HOME PAGE
def home(request):
    products = Product.objects.all()
    return render(request, 'Store/home.html', {'products': products})


# PRODUCT DETAIL VIEW
def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'Store/detail.html', {'product': product})


# PRODUCT LIST VIEW
def product_list(request, pk):
    sub_category = SubCategory.objects.get(pk=pk)
    products = Product.objects.filter(sub_category=sub_category)
    return render(request, 'Store/product_list.html', {'sub_category': sub_category, 'products': products})


# PRODUCT LIST VIEW
def add_review(request, pk):
    if request.method == "POST":
        product = Product.objects.get(pk=pk)
        data = ProductReview()
        data.product = product
        data.user = request.user
        data.name = request.POST.get('name')
        data.subject = request.POST.get('subject')
        data.rating = request.POST.get('rating')
        data.comment = request.POST.get('comment')
        data.save()
    return HttpResponseRedirect(reverse('store:product_detail', kwargs={'pk': product.pk}))