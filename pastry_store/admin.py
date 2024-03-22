from django.contrib import admin
from .models import Products,ItemsDelivery
# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('product_name','quantity','total')
    list_filter = ['category']
    # search_fields = ['category']
admin.site.register(Products, ProductsAdmin)
admin.site.register(ItemsDelivery)