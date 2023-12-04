from django.contrib import admin

from .models import Category, Products


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = ["name"]
    list_filter = ["name"]
    search_fields = ["name"]


class ProductsAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ["id", "name"]
    list_filter = ["name", "price", "brand"]
    search_fields = ["name", "price", "brand", "category"]


admin.site.register(Products, ProductsAdmin)
admin.site.register(Category, CategoryAdmin)
