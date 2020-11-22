from django.contrib import admin
from .models import ForWhom, Category, SubCategory, Product


admin.site.register(ForWhom)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)