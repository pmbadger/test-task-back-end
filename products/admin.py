from django.contrib import admin
from .models import Product, SelectedProduct


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(SelectedProduct)
class SelectedProductAdmin(admin.ModelAdmin):
    list_filter = ["user", "product"]
