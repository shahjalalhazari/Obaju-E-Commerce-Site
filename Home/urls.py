from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us/', views.about_us, name='about'),
    path('contact-us/', views.contact_us, name='contact'),
    path('faq/', views.faq, name='faq'),
]