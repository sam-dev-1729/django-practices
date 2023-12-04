from django.contrib import admin

from .models import Sellers


class SellersAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "phone"]
    list_display_links = ["id", "name"]
    list_filter = ["name", "phone"]
    search_fields = ["name"]


admin.site.register(Sellers, SellersAdmin)
