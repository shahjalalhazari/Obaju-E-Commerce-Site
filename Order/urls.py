from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('cart/', views.cart_view, name='cart'),
    path('add/<pk>/', views.add_to_cart, name='add'),
    path('remove/<pk>/', views.remove_from_cart, name='remove'),
]