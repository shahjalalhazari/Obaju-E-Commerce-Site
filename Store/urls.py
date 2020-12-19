from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('product/<pk>/', views.product_detail, name='product_detail'),
    path('product-list/<pk>/', views.product_list, name='product_list'),
    path('category-list/<pk>/', views.category_list, name='category_list'),
    path('sub-category-list/<pk>/', views.sub_cat_list, name='sub_cat_list'),
    path('add_review/<pk>/', views.add_review, name='add_review'),
]