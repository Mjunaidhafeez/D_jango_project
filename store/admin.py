from django.contrib import admin
from .models.product import Product
from .models.category import Category


# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display = ['product_name', 'product_price', 'product_catgory','product_description']


class AdminCategory(admin.ModelAdmin):
    list_display = ['category_name', 'category_description']

admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)

