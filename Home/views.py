from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from Store.models import Product
from .models import Contact


# HOME PAGE
def home(request):
    products = Product.objects.all()
    return render(request, 'Home/home.html', {'products': products})


# CONTACT US VIEW
def contact_us(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        data = Contact()
        data.name = name
        data.email = email
        data.subject = subject
        data.message = message
        data.save()
        messages.success(request, "Thanks for contact us. We will contact you ASAP.")
        return HttpResponseRedirect(reverse("home:contact"))
    else:
        return render(request, 'Home/contact.html')