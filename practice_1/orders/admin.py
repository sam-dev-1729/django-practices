from django.contrib import admin

from .models import Orders


# Register your models here.
class OrdersAdmin(admin.ModelAdmin):
    list_display = ["id", "owner"]
    list_display_links = ["id", "owner"]
    list_filter = ["owner", "date"]
    search_fields = ["owner", "date"]


admin.site.register(Orders, OrdersAdmin)
