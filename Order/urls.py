from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('cart/', views.cart_view, name='cart'),
    path('add/<pk>/', views.add_to_cart, name='add'),
    path('remove/<pk>/', views.remove_from_cart, name='remove'),
    path('inc_qty/<int:pk>/', views.inc_qty, name='inc_qty'),
    path('dec_qty/<int:pk>/', views.dec_qty, name='dec_qty'),
    path('orders/', views.orders, name='orders'),
    path('order/<pk>/<orderId>/', views.order, name='order'),
]