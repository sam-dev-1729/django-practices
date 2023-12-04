from django.contrib import admin

from .models import Products


# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ["id", "name"]
    list_filter = ["name", "price", "brand"]
    search_fields = ["name", "price", "brand"]


admin.site.register(Products, ProductsAdmin)
