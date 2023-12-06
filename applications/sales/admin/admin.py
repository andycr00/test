from django.contrib import admin
from ..models import *


class ClientsAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "document",
        "first_name",
        "last_name",
    ]
    search_fields = ["document"]


class BillsAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "client",
        "company_name",
        "nit",
        "code",
    ]
    search_fields = [
        "company_name",
    ]


class ProductsAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "description",
    ]
    search_fields = [
        "name",
    ]


admin.site.register(Client, ClientsAdmin)
admin.site.register(Bill, BillsAdmin)
admin.site.register(Product, ProductsAdmin)
