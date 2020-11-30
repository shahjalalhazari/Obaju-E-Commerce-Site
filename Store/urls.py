from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<pk>/', views.product_detail, name='product_detail'),
    path('product-list/<pk>/', views.product_list, name='product_list'),
]